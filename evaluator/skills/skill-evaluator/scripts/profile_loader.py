#!/usr/bin/env python3
"""
Loads a profile's criteria.json and resolves the shared files it references, so anything
used by several profiles is edited in one place. Two kinds of shared file live in
profiles/_shared/:

1. Criteria fragments, pulled in with a `$ref` entry in `groups` (path relative to the
   profile folder). A fragment holds exactly one group and its criteria:

    "groups": [{"$ref": "../_shared/skill-standard.json"}, {"id": "B", ...}]

    {"fragment": "<name>", "version": "...",
     "group": {"id": "A", ...}, "criteria": [{"id": "A1", "group": "A", ...}]}

   Resolving replaces the `$ref` entry with the fragment's group (tagged with
   `shared_from` and `shared_version`) and adds the fragment's criteria to `criteria`,
   ordered by group.

2. Course-wide settings, pulled in with a top-level `extends` list. The file's `settings`
   become top-level keys of the resolved profile (e.g. the default `pass_rule`), and
   `settings_from` records which file each one came from:

    "extends": ["../_shared/course-rules.json"]

    {"shared": "<name>", "version": "...", "settings": {"pass_rule": {...}}}

It refuses, with every problem listed, when:
  - a shared file is missing, or lacks its required keys
  - a fragment criterion belongs to another group than the fragment's
  - something defined in a shared file is also defined in the profile: a fragment's
    group or criterion id, or a setting key. There is no local override at that level;
    a change goes into the shared file, for every profile. (A single criterion or group
    may still carry its own `pass_rule`, see criterion_rules.py.)
  - a `pass_rule` anywhere in the resolved profile is invalid (criterion_rules.check_rules)
  - the profile's `competencies` name an id that is not in the course `competency_catalog`

Usage (prints a summary per profile; --out writes the resolved profile, one profile only):
    python scripts/profile_loader.py profiles/manual-qa profiles/auto-qa
    python scripts/profile_loader.py profiles/manual-qa --out resolved.json
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

from criterion_rules import check_rules


class ProfileError(Exception):
    def __init__(self, problems):
        super().__init__("\n".join(problems))
        self.problems = problems


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def check_competencies(profile):
    """A profile's `competencies` must be unique ids from the course `competency_catalog`."""
    if "competencies" not in profile:
        return []
    catalog = {c.get("id") for c in profile.get("competency_catalog", [])}
    listed = profile["competencies"]
    problems = [f"competencies: {c!r} is not in the course competency_catalog" for c in listed if c not in catalog]
    if len(set(listed)) != len(listed):
        problems.append("competencies: duplicate ids")
    if not listed:
        problems.append("competencies: empty list")
    return problems


def check_plan_fresh(asm, profile_dir):
    """Compare a pre-registered eval_plan.json's recorded sha256 (asm = plan["scope"]["assessment"])
    against the profile's files as they are now. Returns a list of mismatches (empty = still fresh).

    A stale plan (profile edited after the plan was built, e.g. a pass_rule mode renamed) freezes
    an `effective_rule` that no longer matches criterion_rules.py's current MODES, and crashes deep
    inside evaluate() with a confusing KeyError instead of this clear message -- call this before
    merging judge results or rendering a report, not after.
    """
    profile_dir = Path(profile_dir)
    cpath = profile_dir / "criteria.json"
    if not cpath.is_file():
        return [f"{cpath}: profile no longer exists"]
    problems = []
    current = sha256(cpath)
    recorded = asm.get("criteria_sha256")
    if recorded and current != recorded:
        problems.append(f"{cpath}: edited since this plan was built (sha256 {recorded[:12]}... -> {current[:12]}...); "
                         f"rebuild the plan with build_plan_from_profile.py")
    for src in asm.get("shared_sources", []):
        p = Path(src["path"])
        if not p.is_file():
            problems.append(f"{p}: no longer exists (recorded in the plan's shared_sources)")
        elif sha256(p) != src.get("sha256"):
            problems.append(f"{p}: edited since this plan was built (sha256 differs); "
                             f"rebuild the plan with build_plan_from_profile.py")
    return problems


def load_profile(profile_dir):
    """Return (resolved_criteria, sources).

    sources lists every file the result was built from, criteria.json first:
    [{"path": str, "sha256": str, "version": str|None}], so a plan can detect later edits
    to shared files as well as to the profile itself.
    """
    profile_dir = Path(profile_dir)
    cpath = profile_dir / "criteria.json"
    profile = _read_json(cpath)
    sources = [{"path": cpath.as_posix(), "sha256": sha256(cpath), "version": profile.get("version")}]
    problems = []

    settings, settings_from = {}, {}
    for ref in profile.get("extends", []):
        spath = (profile_dir / ref).resolve()
        if not spath.is_file():
            problems.append(f"criteria.json: extends {ref} not found ({spath})")
            continue
        shared = _read_json(spath)
        missing = [k for k in ("shared", "version", "settings") if not shared.get(k)]
        if missing:
            problems.append(f"{ref}: missing {missing}")
            continue
        for key, value in shared["settings"].items():
            if key in profile:
                problems.append(f"{ref}: setting {key!r} is also defined in criteria.json; edit the shared file instead")
            elif key in settings:
                problems.append(f"{ref}: setting {key!r} is already set by another extends file")
            else:
                settings[key] = value
                settings_from[key] = f"_shared/{spath.name}"
        sources.append({"path": spath.as_posix(), "sha256": sha256(spath), "version": shared["version"]})

    local_group_ids = {g.get("id") for g in profile.get("groups", []) if "$ref" not in g}
    local_criterion_ids = {c.get("id") for c in profile.get("criteria", [])}
    groups, shared_criteria = [], []
    for entry in profile.get("groups", []):
        if "$ref" not in entry:
            groups.append(entry)
            continue
        fpath = (profile_dir / entry["$ref"]).resolve()
        label = entry["$ref"]
        if not fpath.is_file():
            problems.append(f"criteria.json: $ref {label} not found ({fpath})")
            continue
        frag = _read_json(fpath)
        missing = [k for k in ("fragment", "version", "group", "criteria") if not frag.get(k)]
        if missing:
            problems.append(f"{label}: missing {missing}")
            continue
        gid = frag["group"].get("id")
        if gid in local_group_ids:
            problems.append(f"{label}: group {gid} is also defined in criteria.json; edit the fragment instead")
        for c in frag["criteria"]:
            if c.get("group") != gid:
                problems.append(f"{label}: {c.get('id')} belongs to group {c.get('group')!r}, fragment group is {gid!r}")
            if c.get("id") in local_criterion_ids:
                problems.append(f"{label}: {c.get('id')} is also defined in criteria.json; edit the fragment instead")
        groups.append({**frag["group"], "shared_from": f"_shared/{fpath.name}", "shared_version": frag["version"]})
        shared_criteria += frag["criteria"]
        sources.append({"path": fpath.as_posix(), "sha256": sha256(fpath), "version": frag["version"]})

    if problems:
        raise ProfileError(problems)
    order = {g.get("id"): i for i, g in enumerate(groups)}
    criteria = sorted(shared_criteria + profile.get("criteria", []), key=lambda c: order.get(c.get("group"), len(order)))
    resolved = {**profile, **settings, "groups": groups, "criteria": criteria}
    if settings_from:
        resolved["settings_from"] = settings_from
    problems = check_rules(resolved) + check_competencies(resolved)
    if problems:
        raise ProfileError(problems)
    return resolved, sources


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("profile_dirs", type=Path, nargs="+")
    ap.add_argument("--out", type=Path, help="write the resolved profile (one profile only)")
    args = ap.parse_args()
    if args.out and len(args.profile_dirs) != 1:
        ap.error("--out needs exactly one profile")

    failed = 0
    for d in args.profile_dirs:
        try:
            resolved, sources = load_profile(d)
        except ProfileError as e:
            failed += 1
            print(f"{d}: {len(e.problems)} problem(s)")
            for p in e.problems:
                print(f"  - {p}")
            continue
        print(f"{d}: {len(resolved['groups'])} groups, {len(resolved['criteria'])} criteria")
        for g in resolved["groups"]:
            ids = [c["id"] for c in resolved["criteria"] if c.get("group") == g.get("id")]
            shared = f"  (shared: {g['shared_from']} v{g['shared_version']})" if "shared_from" in g else ""
            print(f"  {g.get('id')} {g.get('name')}: {', '.join(ids)}{shared}")
        if args.out:
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(json.dumps(resolved, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"Wrote {args.out}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
