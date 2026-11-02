#!/usr/bin/env python3
"""
Turns a profile's criteria (profiles/<name>/criteria.json) plus ONE assessment's answer key
(--baseline PATH, different for every exam) into the pre-registered evals/eval_plan.json
(SKILL.md Step 1).

Two scoring models are supported:

`weighted-pass-fail` (manual-qa v0.4+, auto-qa): criteria are lists of conditions, scored by
criterion_rules.py (course default: mode "proportional", pass at >= 80% of conditions met,
partial credit below that) and rolled up per competency by group points (5 per group) and
group weights. The plan records the resolved criteria, scoring settings, competencies and
gates. --baseline is optional; --sub-category is required when a criterion has sub-category
conditions.

`deduction` (the old v0.3 points model -- not to be confused with the `pass_rule` mode also
once named "deduction", renamed to "proportional" on 2026-10-23, see work-log.md): every
criterion is `deduction` type -- it has
max_points and penalty_per_error; its score is max_points minus penalty x errors,
floored at 0. Criteria belong to groups; the total is the sum of all criteria
and the assessment passes at or above `pass_threshold`.

What it checks before writing anything:
  - no value still starts with "TODO" (an unfilled skeleton is never pre-registered)
  - criterion ids are unique, each belongs to a declared group
  - each group's criteria add up to the group's max_points
  - pass_threshold <= total of all max_points
  - baseline: unique ids, bug severities inside severity_scale, thresholds present

The profile is read with profile_loader.load_profile, which resolves shared criteria
fragments (`$ref` in groups, e.g. profiles/_shared/skill-standard.json). It records sha256
of criteria.json, of every shared fragment and of the answer key in the plan, so a later
edit to any of them after grading started is detectable.

Usage:
    python scripts/build_plan_from_profile.py profiles/manual-qa \
        --skill-name trainee-01 --hypothesis "..." --out evals/eval_plan.json

--baseline is required. The answer key belongs to one assessment and lives next to its
exam, not in the profile folder; profiles/<name>/baseline.template.json shows its shape.
"""
import argparse
import hashlib
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

from criterion_rules import conditions_for, rule_for
from profile_loader import ProfileError, load_profile

REQUIRED_THRESHOLDS = {"ambiguity_found_pct", "ambiguity_with_tr_pct", "bug_found_pct"}


def walk_todos(node, path=""):
    if isinstance(node, str) and node.strip().upper().startswith("TODO"):
        yield path
    elif isinstance(node, dict):
        for k, v in node.items():
            yield from walk_todos(v, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk_todos(v, f"{path}[{i}]")


def dup_ids(items, label):
    seen, out = set(), []
    for it in items:
        if it.get("id") in seen:
            out.append(f"{label}: duplicate id {it.get('id')}")
        seen.add(it.get("id"))
    return out


def validate(criteria, baseline):
    problems = []
    model = criteria.get("scoring_model", "deduction")
    if model != "deduction":
        return [f"criteria.json: scoring_model {model!r} is not supported yet; this script only builds "
                f"plans for the 'deduction' points model ({criteria.get('status', 'no status given')})"]
    for label, doc in (("criteria.json", criteria), ("baseline.json", baseline)):
        problems += [f"{label}: unfilled TODO at {p}" for p in walk_todos(doc)]

    groups = {g["id"]: g for g in criteria.get("groups", [])}
    problems += dup_ids(criteria.get("groups", []), "criteria.json groups")
    problems += dup_ids(criteria.get("criteria", []), "criteria.json criteria")
    if not criteria.get("criteria"):
        problems.append("criteria.json: no criteria")

    sums = {gid: 0 for gid in groups}
    for c in criteria.get("criteria", []):
        cid = c.get("id")
        if c.get("type") != "deduction":
            problems.append(f"criteria.json: {cid} type must be 'deduction'")
        if c.get("group") not in groups:
            problems.append(f"criteria.json: {cid} group {c.get('group')!r} is not declared in groups")
            continue
        for f in ("max_points", "penalty_per_error"):
            if not isinstance(c.get(f), (int, float)) or c[f] <= 0:
                problems.append(f"criteria.json: {cid} needs a positive numeric {f}")
        if not c.get("details"):
            problems.append(f"criteria.json: {cid} needs `details` (the grader reads it)")
        sums[c["group"]] += c.get("max_points") or 0
        for adv in c.get("advisory", []):
            if adv.get("decision") != "human" or not adv.get("id"):
                problems.append(f"criteria.json: {cid} advisory entries need an id and decision 'human'")
    for gid, g in groups.items():
        if sums[gid] != g.get("max_points"):
            problems.append(f"criteria.json: group {gid} criteria add up to {sums[gid]}, group max_points is {g.get('max_points')}")
    total = sum(g.get("max_points", 0) for g in groups.values())
    if not isinstance(criteria.get("pass_threshold"), (int, float)) or not 0 < criteria["pass_threshold"] <= total:
        problems.append(f"criteria.json: pass_threshold must be between 1 and the total {total}")
    ov = criteria.get("l0_override")
    if ov and (ov.get("mode") != "replace" or ov.get("group") not in groups or not ov.get("reason")):
        problems.append("criteria.json: l0_override needs mode 'replace', a declared group, and a reason")

    na = baseline.get("not_assessed", [])
    crit_ids = {c.get("id") for c in criteria.get("criteria", [])}
    na_ids = {x.get("criterion") for x in na}
    for x in na:
        if x.get("criterion") not in crit_ids:
            problems.append(f"baseline.json: not_assessed names unknown criterion {x.get('criterion')!r}")
        if not x.get("reason"):
            problems.append(f"baseline.json: not_assessed {x.get('criterion')} needs a reason")
    if na_ids >= crit_ids:
        problems.append("baseline.json: not_assessed removes every criterion")
    # a list is only required when an assessed criterion needs it
    needed = {"acceptance_criteria", "ambiguities", "edge_cases"}
    for c in criteria.get("criteria", []):
        if c.get("id") not in na_ids:
            needed |= set(c.get("needs", []))
    for key in ("acceptance_criteria", "ambiguities", "edge_cases", "bugs"):
        problems += dup_ids(baseline.get(key, []), f"baseline.json {key}")
        if key in needed and not baseline.get(key):
            problems.append(f"baseline.json: {key} is empty (needed by an assessed criterion; list the criterion under not_assessed if the exam does not cover it)")
    scale = baseline.get("severity_scale", [])
    if not scale:
        problems.append("baseline.json: severity_scale is empty")
    for b in baseline.get("bugs", []):
        if b.get("severity") not in scale:
            problems.append(f"baseline.json: {b.get('id')} severity {b.get('severity')!r} not in severity_scale")
    missing = REQUIRED_THRESHOLDS - set(baseline.get("thresholds", {}))
    if missing:
        problems.append(f"baseline.json: thresholds missing {sorted(missing)}")
    return problems


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_weighted(profile, sub_category):
    problems = [f"criteria.json: unfilled TODO at {p}" for p in walk_todos(profile)]
    groups = {g["id"]: g for g in profile.get("groups", [])}
    problems += dup_ids(profile.get("groups", []), "criteria.json groups")
    problems += dup_ids(profile.get("criteria", []), "criteria.json criteria")
    scoring = profile.get("scoring", {})
    for key in ("group_points", "pass_threshold"):
        if not isinstance(scoring.get(key), (int, float)) or scoring[key] <= 0:
            problems.append(f"scoring.{key} must be a positive number (got {scoring.get(key)!r})")
    if isinstance(scoring.get("group_points"), (int, float)) and isinstance(scoring.get("pass_threshold"), (int, float)) \
            and scoring["pass_threshold"] > scoring["group_points"]:
        problems.append("scoring.pass_threshold is above group_points: nobody could pass")
    if abs(sum(g.get("weight", 0) for g in groups.values()) - 1) > 1e-9:
        problems.append("group weights must add up to 1")
    if not profile.get("competencies"):
        problems.append("profile lists no `competencies`; the report scores per competency (auto-qa still needs them: AU-10)")
    for c in profile.get("criteria", []):
        if c.get("group") not in groups:
            problems.append(f"{c.get('id')}: group {c.get('group')!r} is not declared")
            continue
        rule, _ = rule_for(profile, c)
        try:
            if not conditions_for(c, rule, sub_category):
                problems.append(f"{c['id']}: no conditions to count")
        except ValueError as e:
            problems.append(str(e))
    for gid in groups:
        if not any(c.get("group") == gid for c in profile.get("criteria", [])):
            problems.append(f"group {gid} has no criteria")
    return problems


def build_weighted(args, profile, sources):
    baseline = None
    if args.baseline:
        baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
        if baseline.get("profile") != args.profile_dir.name:
            print(f"build_plan_from_profile: baseline.json profile is {baseline.get('profile')!r}, expected "
                  f"{args.profile_dir.name!r}, nothing written")
            return 1
    if args.competencies:
        wanted = [c.strip() for c in args.competencies.split(",") if c.strip()]
        unknown = [c for c in wanted if c not in profile.get("competencies", [])]
        if unknown:
            print(f"build_plan_from_profile: --competencies {unknown} not in the profile's competencies "
                  f"{profile.get('competencies')}, nothing written")
            return 1
        # This exam covers only some competencies: keep them (profile order), the rest are not assessed.
        profile = {**profile, "competencies": [c for c in profile["competencies"] if c in wanted]}
    problems = validate_weighted(profile, args.sub_category)
    if problems:
        print(f"build_plan_from_profile: {len(problems)} problem(s), nothing written:\n")
        for p in problems:
            print(f"  - {p}")
        return 1
    scoring = profile["scoring"]
    criteria = []
    for c in profile["criteria"]:
        rule, origin = rule_for(profile, c)
        criteria.append({**c, "effective_rule": rule, "rule_origin": origin,
                         "conditions": conditions_for(c, rule, args.sub_category)})
    plan = {
        "skill_name": args.skill_name,
        "skill_version": args.skill_version,
        "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "hypothesis": args.hypothesis,
        "scope": {
            "layers": ["L0", "L1"] + (["L2", "L3"] if args.has_refinement else []),
            "has_refinement_step": args.has_refinement,
            "refinement_mechanism": "trainee-submitted refined version" if args.has_refinement else None,
            "primary_axes": ["correctness"],
            "n_repeats": 1,
            "assessment": {
                "scoring_model": "weighted-pass-fail",
                "profile": args.profile_dir.name,
                "criteria_version": profile.get("version"),
                "criteria_sha256": sha256(args.profile_dir / "criteria.json"),
                "shared_sources": sources[1:],
                "baseline_sha256": sha256(args.baseline) if baseline else None,
                "baseline_version": baseline.get("version") if baseline else None,
                "sub_category": args.sub_category,
                "competencies": profile["competencies"],
                "competency_catalog": profile.get("competency_catalog", []),
                "skill_to_competency": scoring.get("skill_to_competency"),
                "scoring": {k: scoring[k] for k in ("group_points", "pass_threshold", "group_score")},
                "groups": profile["groups"],
                "gates": profile.get("gates", []),
                "criteria": criteria,
            },
        },
        "baseline": {"type": "assessment_baseline",
                     "reference": f"{args.baseline} assessment {baseline.get('assessment_id')} v{baseline.get('version')}"
                     if baseline else "none"},
        "evals": [{
            "id": 1,
            "name": baseline.get("assessment_id", args.skill_name) if baseline else args.skill_name,
            "prompt": f"See requirement source: {baseline['requirement_source']}" if baseline else "See the exam brief",
            "files": [baseline["requirement_source"]] if baseline and baseline.get("requirement_source") else [],
            "assertions": [{"id": c["id"], "text": f"{c['name']}: {c['description']}", "pre_registered": True}
                           for c in profile["criteria"]],
            "exploratory_assertions": [],
        }],
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8")
    gate_open = [g["id"] for g in profile.get("gates", []) if not g.get("pass_when_all")]
    print(f"Wrote {args.out}: {len(criteria)} criteria, {len(profile['competencies'])} competencies, "
          f"{scoring['group_points']} points per group, pass at {scoring['pass_threshold']}")
    if gate_open:
        print(f"  gate {gate_open} has no conditions yet: its verdict will come from a person")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("profile_dir", type=Path)
    ap.add_argument("--skill-name", required=True)
    ap.add_argument("--skill-version", default="final")
    ap.add_argument("--hypothesis", required=True)
    ap.add_argument("--has-refinement", action="store_true",
                    help="trainee submitted a refined version (real L2)")
    ap.add_argument("--baseline", type=Path, help="this assessment's answer key (baseline.json); required for the "
                    "deduction model, optional for weighted-pass-fail")
    ap.add_argument("--competencies", help="comma-separated competency ids this exam covers (weighted-pass-fail "
                    "only); default: every competency of the profile")
    ap.add_argument("--sub-category", help="sub-category being assessed (criteria with sub-category conditions)")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    cpath = args.profile_dir / "criteria.json"
    bpath = args.baseline
    try:
        criteria, sources = load_profile(args.profile_dir)
    except ProfileError as e:
        print(f"build_plan_from_profile: {len(e.problems)} problem(s), nothing written:\n")
        for p in e.problems:
            print(f"  - {p}")
        return 1
    if criteria.get("scoring_model") == "weighted-pass-fail":
        return build_weighted(args, criteria, sources)
    if bpath is None:
        ap.error("--baseline is required for the deduction model")
    baseline = json.loads(bpath.read_text(encoding="utf-8"))

    problems = validate(criteria, baseline)
    if baseline.get("profile") != args.profile_dir.name:
        problems.append(f"baseline.json: profile is {baseline.get('profile')!r}, expected {args.profile_dir.name!r}")
    if problems:
        print(f"build_plan_from_profile: {len(problems)} problem(s), nothing written:\n")
        for p in problems:
            print(f"  - {p}")
        return 1

    na_ids = {x["criterion"] for x in baseline.get("not_assessed", [])}
    full_total = sum(g["max_points"] for g in criteria["groups"])
    assessed = [c for c in criteria["criteria"] if c["id"] not in na_ids]
    groups = [{**g, "max_points": sum(c["max_points"] for c in assessed if c["group"] == g["id"])} for g in criteria["groups"]]
    assessed_total = sum(g["max_points"] for g in groups)
    # Assumption, flagged in the report: when criteria are not assessed, the pass line keeps the
    # same proportion of the points that remain (rounded up).
    threshold = math.ceil(criteria["pass_threshold"] * assessed_total / full_total) if na_ids else criteria["pass_threshold"]

    layers = ["L0", "L1"] + (["L2", "L3"] if args.has_refinement else [])
    plan = {
        "skill_name": args.skill_name,
        "skill_version": args.skill_version,
        "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "hypothesis": args.hypothesis,
        "scope": {
            "layers": layers,
            "has_refinement_step": args.has_refinement,
            "refinement_mechanism": "trainee-submitted refined version" if args.has_refinement else None,
            "primary_axes": ["correctness"],
            "n_repeats": 1,
            "assessment": {
                "profile": args.profile_dir.name,
                "criteria_version": criteria.get("version"),
                "baseline_version": baseline.get("version"),
                "criteria_sha256": sha256(cpath),
                "shared_sources": sources[1:],
                "baseline_sha256": sha256(bpath),
                "pass_threshold": threshold,
                "pass_threshold_original": criteria["pass_threshold"],
                "full_total": full_total,
                "not_assessed": baseline.get("not_assessed", []),
                "groups": groups,
                "l0_override": criteria.get("l0_override"),
                "criteria": assessed,
            },
        },
        "baseline": {
            "type": "assessment_baseline",
            "reference": f"{args.baseline} assessment "
                         f"{baseline['assessment_id']} v{baseline.get('version')}",
        },
        "evals": [{
            "id": 1,
            "name": baseline["assessment_id"],
            "prompt": f"See requirement source: {baseline['requirement_source']}",
            "files": [baseline["requirement_source"]],
            "assertions": [
                {"id": c["id"], "text": f"{c['name']}: {c['pass_when']}", "pre_registered": True}
                for c in assessed
            ],
            "exploratory_assertions": [],
        }],
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {args.out}: {len(assessed)} criteria, {assessed_total} points, pass at {threshold}")
    if na_ids:
        print(f"  not assessed: {sorted(na_ids)}; pass line scaled from {criteria['pass_threshold']}/{full_total} to {threshold}/{assessed_total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
