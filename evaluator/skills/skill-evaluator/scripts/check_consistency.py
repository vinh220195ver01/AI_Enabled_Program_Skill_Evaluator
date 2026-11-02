#!/usr/bin/env python3
"""
Consistency checker for skill-evaluator's own bundle.

This exists because the same class of bug has recurred repeatedly across this
framework's self-audits: a "the metrics registry has two entries" line left
stale after a third entry was added, a rule citation ("scientific-method.md
#3") pointing at a rule number that no longer exists after renumbering, a
stale "Mindset/Navigation/Philosophy/Process/Tool" enum missing a pattern
added later, a dangling reference to a file that got renamed or removed. Each
instance was individually patched only after a human or a blind grader
happened to notice it. This is a linter for exactly that failure class -- it
cannot verify that an "Enforced by:" claim is *true* (that still needs a
human/grader reading the actual behavior), only that what it points at (a
file, a rule number, a required field) still exists and hasn't drifted.

Known limitation: the rule-citation check is line-based and skips any line
that mentions both `references/scientific-method.md` and `agents/grader.md`
in the same line (ambiguous which numbers belong to which file) -- rare in
practice, but a real gap in this v1 checker, not silently pretended away.

Known NOT-caught classes (found by having an independent grader try to break
this script against this framework's own documented incident history):
semantic/self-referential drift like a pre-written verdict leaking into a
rubric file, a workflow-step ordering contradiction, a stale caveat whose
factual premise no longer holds, or a report template whose fields have
drifted from the JSON schema it's meant to render. None of these are lexical
or structural in a way a regex/JSON-shape check can see -- they need a human
or a grader actually reading the content, the same way "Enforced by:" claims
still need a human to verify they're *true*, not just that their citation
target exists.

Usage:
    python scripts/check_consistency.py
Exit code 0 if clean, 1 if any check found a problem (all problems printed,
not just the first).
"""
import json
import re
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent

# Files that legitimately don't exist in THIS bundle because they belong to
# skill-creator, a separate sibling skill this one integrates with when
# present (see references/skill-creator-integration.md) -- not a dangling
# reference, a documented external dependency. Verified by hand against that
# file's "Reuse from skill-creator" table before adding each one here; don't
# add to this list without the same check, or it becomes a way to silence
# real drift instead of filtering known-good noise.
KNOWN_EXTERNAL_SKILL_CREATOR_FILES = {
    "agents/analyzer.md",
    "scripts/aggregate_benchmark.py",
    "scripts/run_loop.py",
    "scripts/package_skill.py",
}


def all_md_files():
    return sorted(SKILL_ROOT.glob("**/*.md"))


def all_source_files():
    """.md and .py files, excluding this script itself -- its own docstring
    quotes example drift patterns (e.g. "scientific-method.md #3") that would
    otherwise be indistinguishable from real citations to a line-based scan."""
    this_file = Path(__file__).resolve()
    files = list(SKILL_ROOT.glob("**/*.md")) + list(SKILL_ROOT.glob("**/*.py"))
    return sorted(f for f in files if f.resolve() != this_file)


def read(path):
    return path.read_text(encoding="utf-8")


_FENCE = re.compile(r"```.*?```", re.DOTALL)


def strip_code_fences(text):
    """Rubric files (agents/input-layer-judge.md especially) contain fenced
    ```markdown examples with illustrative, fictional paths like
    `scripts/create-doc.py` -- these are teaching examples, not real
    cross-references, and must not be checked as if they were.

    Replaces fence content with blank lines (same newline count) rather than
    deleting it outright, so line numbers reported for matches elsewhere in
    the file stay accurate against the original text.
    """
    return _FENCE.sub(lambda m: "\n" * m.group(0).count("\n"), text)


def check_file_references(problems):
    """Every backtick-quoted agents/references/scripts path should exist on disk,
    unless it's a documented skill-creator external, inside a fenced example, or
    inside a Markdown table row -- course-standard docs like skill-standard.md use
    table rows for illustrative "good vs bad" examples with fictional paths
    (e.g. `references/business-rules.md`), the same teaching-example pattern
    strip_code_fences() already excludes for fenced blocks."""
    pattern = re.compile(r"`((?:agents|references|scripts)/[\w.-]+\.(?:md|py|json))`")
    for md in all_md_files():
        text = strip_code_fences(read(md))
        for m in pattern.finditer(text):
            rel = m.group(1)
            if rel in KNOWN_EXTERNAL_SKILL_CREATOR_FILES:
                continue
            line_start = text.rfind("\n", 0, m.start()) + 1
            before = text[line_start:m.start()]
            if before.lstrip().startswith("|") or re.search(r"\((?:vd|e\.g\.)\b[^)]*$", before, re.IGNORECASE):
                continue  # markdown table row, or an inline "(vd ...)"/"(e.g. ...)" example not yet closed
            if not (SKILL_ROOT / rel).exists():
                line = text.count("\n", 0, m.start()) + 1
                problems.append(
                    f"{md.relative_to(SKILL_ROOT)}:{line}: references `{rel}`, which does not exist"
                )


def _numbered_headers(text, header_pattern):
    return set(int(n) for n in re.findall(header_pattern, text, re.MULTILINE))


_CITATION_NUMBER = re.compile(r"#(\d+)|\brule\s+(\d+)\b", re.IGNORECASE)


def check_rule_citations(problems):
    """Both citation styles actually used across the bundle -- `#N` (e.g. `agents/grader.md` #4)
    and prose "rule N" (e.g. "per references/scientific-method.md rule 4") -- must point at a
    rule number that actually exists in the target file right now. Scans .py files too: rule
    citations also show up in scripts/aggregate_layered.py's comments, not just markdown.

    A file citing its OWN rules (e.g. scientific-method.md saying "per rule 6 below" inside
    scientific-method.md itself) never repeats its own filename -- treat any "#N"/"rule N" in
    such a file as a self-citation unconditionally, don't require the filename to be present
    on that line the way an external citation needs it."""
    sci_path = SKILL_ROOT / "references" / "scientific-method.md"
    sci_numbers = _numbered_headers(read(sci_path), r"^## (\d+)\.")

    grader_path = SKILL_ROOT / "agents" / "grader.md"
    grader_numbers = _numbered_headers(read(grader_path), r"^(\d+)\.\s+\*\*")

    for src in all_source_files():
        text = read(src)
        is_sci_self = src.resolve() == sci_path.resolve()
        is_grader_self = src.resolve() == grader_path.resolve()
        for lineno, line in enumerate(text.splitlines(), start=1):
            mentions_sci = is_sci_self or "scientific-method.md" in line
            mentions_grader = is_grader_self or "agents/grader.md" in line
            if mentions_sci and mentions_grader:
                continue  # ambiguous which numbers belong to which file -- skip, see docstring
            if not mentions_sci and not mentions_grader:
                continue
            valid = sci_numbers if mentions_sci else grader_numbers
            target_file = "references/scientific-method.md" if mentions_sci else "agents/grader.md"
            for m in _CITATION_NUMBER.finditer(line):
                num = int(m.group(1) or m.group(2))
                if num not in valid:
                    problems.append(
                        f"{src.relative_to(SKILL_ROOT)}:{lineno}: cites `{target_file}` rule {num}, "
                        f"but that file's current rule numbers are {sorted(valid)}"
                    )


def check_metrics_registry(problems):
    registry_path = SKILL_ROOT / "references" / "metrics_registry.json"
    data = json.loads(read(registry_path))
    required = {"name", "axis", "applies_to_layers", "scorer_type", "scorer_ref", "description"}
    valid_scorer_types = {"assertion", "rubric", "derived"}
    for entry in data.get("metrics", []):
        name = entry.get("name", "<unnamed>")
        missing = required - entry.keys()
        if missing:
            problems.append(f"metrics_registry.json: entry '{name}' missing field(s): {sorted(missing)}")
        if "axis" in entry and not isinstance(entry["axis"], list):
            problems.append(f"metrics_registry.json: entry '{name}' has non-list `axis` (must be an array, even for one axis)")
        if "applies_to_layers" in entry and not isinstance(entry["applies_to_layers"], list):
            problems.append(f"metrics_registry.json: entry '{name}' has non-list `applies_to_layers`")
        if entry.get("scorer_type") not in valid_scorer_types:
            problems.append(
                f"metrics_registry.json: entry '{name}' has invalid scorer_type "
                f"'{entry.get('scorer_type')}' (must be one of {sorted(valid_scorer_types)})"
            )


def check_d7_pattern_enum(problems):
    """The old 5-pattern enum without Framework shouldn't appear anywhere unqualified."""
    stale = "Mindset/Navigation/Philosophy/Process/Tool"
    for md in all_md_files():
        text = read(md)
        for m in re.finditer(re.escape(stale), text):
            tail = text[m.end():m.end() + len("/Framework")]
            if tail != "/Framework":
                line = text.count("\n", 0, m.start()) + 1
                problems.append(
                    f"{md.relative_to(SKILL_ROOT)}:{line}: stale 5-pattern enum found "
                    f"without /Framework appended"
                )


def check_eval_design_checks_count(problems):
    """Nothing should describe the eval-design checks as "two" or a "pair" --
    there are three (Instruction Clarity, Test Prompt Realism, Description Accuracy)."""
    pattern = re.compile(r"\b(two|pair)\b[^.\n]{0,60}eval[- ]design", re.IGNORECASE)
    for md in all_md_files():
        text = read(md)
        for m in pattern.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            problems.append(
                f"{md.relative_to(SKILL_ROOT)}:{line}: describes eval-design checks as "
                f"two/a pair, but there are three"
            )


def main():
    problems = []
    check_file_references(problems)
    check_rule_citations(problems)
    check_metrics_registry(problems)
    check_d7_pattern_enum(problems)
    check_eval_design_checks_count(problems)

    if not problems:
        print("check_consistency: all checks passed, no known drift pattern found.")
        return 0

    print(f"check_consistency: {len(problems)} problem(s) found:\n")
    for p in problems:
        print(f"  - {p}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
