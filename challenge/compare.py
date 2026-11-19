#!/usr/bin/env python3
"""Compare independent OAAF assessments of the same case.

Usage:
    python3 compare.py submission1.json submission2.json [more.json ...] [--markdown]

Each file is an assessment in the format produced by the OAAF online tool
(see skills/oaaf-assessment/assets/example_assessment.json). The decision rules
are applied to each submission with the reference script, and every pair of
submissions is compared on capability criticality, Consequence Tier,
requirement values, finding criticality and the decision per capability.

Only the standard library is used. Licence: CC BY 4.0. OAAF, Armend Verbovci.
"""
import argparse
import itertools
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "skills", "oaaf-assessment", "scripts"))
import oaaf_decide  # noqa: E402

CASE_CAPABILITIES = ["FastPay", "Queue priority", "Decline letters"]


def norm(name):
    return " ".join(name.lower().split())


def evaluate(path, framework):
    with open(path, encoding="utf-8") as f:
        a = json.load(f)
    out = oaaf_decide.run(a, framework)
    caps = {norm(c["name"]): c["criticality"] for c in out["capabilities"]}
    decisions = {norm(d["capability"]): d["outcome"] for d in out["decisions"]}
    values = {r["requirement"]: r["value"] for r in a.get("results", [])}
    findings = {}
    for f in out["findings"]:
        findings[(f["requirement"], norm(f["capability"]))] = f["criticality"]
    extra = [c["name"] for c in out["capabilities"] if norm(c["name"]) not in {norm(x) for x in CASE_CAPABILITIES}]
    return {"file": os.path.basename(path), "tier": out["effective_tier"], "caps": caps,
            "decisions": decisions, "values": values, "findings": findings, "extra": extra,
            "applicable": set(oaaf_decide_applicable(framework, out["effective_tier"]))}


def oaaf_decide_applicable(framework, tier):
    return [r["id"] for r in framework["requirements"] if r["applies_from_tier"] <= tier]


def ratio(same, total):
    return f"{same}/{total}" if total else "n/a"


def compare(x, y):
    keys = [norm(c) for c in CASE_CAPABILITIES]
    cap_same = sum(1 for k in keys if x["caps"].get(k) and x["caps"].get(k) == y["caps"].get(k))
    dec_same = sum(1 for k in keys if x["decisions"].get(k) and x["decisions"].get(k) == y["decisions"].get(k))
    common = sorted(x["applicable"] & y["applicable"])
    val_same = sum(1 for r in common if x["values"].get(r) and x["values"].get(r) == y["values"].get(r))
    val_diff = [r for r in common if x["values"].get(r) != y["values"].get(r)]
    fkeys = set(x["findings"]) | set(y["findings"])
    fkeys = {k for k in fkeys if k[1] in keys}
    f_same = sum(1 for k in fkeys if x["findings"].get(k) == y["findings"].get(k))
    return {"pair": f"{x['file']} vs {y['file']}",
            "tier_agrees": x["tier"] == y["tier"],
            "capability_criticality": ratio(cap_same, len(keys)),
            "requirement_values": ratio(val_same, len(common)),
            "values_differing": val_diff,
            "finding_criticality": ratio(f_same, len(fkeys)),
            "decisions": ratio(dec_same, len(keys))}


def main():
    ap = argparse.ArgumentParser(description="Compare independent OAAF assessments.")
    ap.add_argument("files", nargs="+")
    ap.add_argument("--framework", default=None)
    ap.add_argument("--markdown", action="store_true")
    a = ap.parse_args()
    if len(a.files) < 2:
        sys.exit("Give at least two assessments to compare.")
    framework = oaaf_decide.load_framework(a.framework)
    subs = [evaluate(p, framework) for p in a.files]
    pairs = [compare(x, y) for x, y in itertools.combinations(subs, 2)]
    if not a.markdown:
        print(json.dumps({"submissions": [{"file": s["file"], "tier": s["tier"], "capabilities": s["caps"],
                                            "decisions": s["decisions"], "extra_capabilities": s["extra"]} for s in subs],
                          "pairs": pairs}, indent=2, ensure_ascii=False))
        return
    print("## Submissions\n")
    print("| File | Tier | " + " | ".join(CASE_CAPABILITIES) + " |")
    print("|---|---|" + "---|" * len(CASE_CAPABILITIES))
    for s in subs:
        cells = [f"{s['caps'].get(norm(c), '–')}: {s['decisions'].get(norm(c), '–')}" for c in CASE_CAPABILITIES]
        print(f"| {s['file']} | {s['tier']} | " + " | ".join(cells) + " |")
    print("\n## Pairwise agreement\n")
    print("| Pair | Tier | Capability criticality | Requirement values | Finding criticality | Decisions | Values that differ |")
    print("|---|---|---|---|---|---|---|")
    for p in pairs:
        print(f"| {p['pair']} | {'Same' if p['tier_agrees'] else 'Differs'} | {p['capability_criticality']} | "
              f"{p['requirement_values']} | {p['finding_criticality']} | {p['decisions']} | {', '.join(p['values_differing']) or 'none'} |")


if __name__ == "__main__":
    main()
