#!/usr/bin/env python3
"""OAAF MCP server: the Operational AI Assurance Framework as tools for AI assistants.

A Model Context Protocol (MCP) server over stdio, using only the Python standard
library. It lets any MCP-capable assistant rate capabilities, look up which
requirements apply, and apply the OAAF v1.0 decision rules deterministically.

Run:   python3 mcp/oaaf_mcp_server.py
Config example (Claude Desktop and similar clients):
    {"mcpServers": {"oaaf": {"command": "python3",
                             "args": ["/path/to/OAAF/mcp/oaaf_mcp_server.py"]}}}

Licence: CC BY 4.0. Operational AI Assurance Framework (OAAF), Armend Verbovci.
DOI: https://doi.org/10.5281/zenodo.24352952
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "skills", "oaaf-assessment", "scripts"))
import oaaf_decide  # noqa: E402

PROTOCOL_VERSION = "2025-06-18"
FRAMEWORK = oaaf_decide.load_framework(os.path.join(HERE, "..", "oaaf.json"))
REQS = {r["id"]: r for r in FRAMEWORK["requirements"]}
CITATION = "Verbovci, A. (2026). Operational AI Assurance Framework (OAAF), Version 1.0. Zenodo. https://doi.org/10.5281/zenodo.24352952"

TOOLS = [
    {
        "name": "oaaf_overview",
        "description": "Summary of the Operational AI Assurance Framework (OAAF): what it is, its principles, "
                       "control states, tiers and decision rules. Call this first when a user asks how to "
                       "decide whether a deployed AI system or agent should keep running, be restricted or be stopped.",
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
    },
    {
        "name": "oaaf_rate_capability",
        "description": "Apply the OAAF two-question test (Section 4.3) to one capability of an AI system. "
                       "Q1: must a human positively accept this specific output before it takes effect (seeing it, "
                       "sampling or later intervention do not count)? Q2: if the output is wrong, would harm be "
                       "irreversible before normal detection, or exceed the materiality threshold? Returns High, Medium or Low.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "capability": {"type": "string", "description": "What the system can cause to happen, e.g. 'issue refunds'."},
                "human_acceptance": {"type": "boolean", "description": "Answer to Q1."},
                "irreversible_or_material": {"type": "boolean", "description": "Answer to Q2."},
            },
            "required": ["human_acceptance", "irreversible_or_material"],
            "additionalProperties": False,
        },
    },
    {
        "name": "oaaf_applicable_requirements",
        "description": "List the OAAF requirements that apply at a Consequence Tier (1: 8 requirements, 2: 25, 3: 36), "
                       "with control-critical flags and typical evidence. A system with any High capability is at least Tier 2.",
        "inputSchema": {
            "type": "object",
            "properties": {"tier": {"type": "integer", "enum": [1, 2, 3]},
                           "domain": {"type": "string", "description": "Optional domain filter, P1 to P7."}},
            "required": ["tier"],
            "additionalProperties": False,
        },
    },
    {
        "name": "oaaf_get_requirement",
        "description": "Get one OAAF requirement by ID (for example P4-06), with its tier, control-critical flag and typical evidence.",
        "inputSchema": {"type": "object", "properties": {"id": {"type": "string"}}, "required": ["id"],
                        "additionalProperties": False},
    },
    {
        "name": "oaaf_decide",
        "description": "Apply the OAAF v1.0 decision rules (Sections 4.3, 4.4, 7.3, 7.4) to an assessment and return the "
                       "effective tier, findings with derived criticality, and a decision per capability (Ready, Ready with "
                       "Conditions, Not Ready). Same input always gives the same result. Values per requirement: Compliant, "
                       "Partially Compliant or Not Demonstrated.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "system": {"type": "object", "properties": {"name": {"type": "string"},
                                                            "declared_tier": {"type": "integer", "enum": [1, 2, 3]}}},
                "capabilities": {"type": "array", "items": {"type": "object", "properties": {
                    "name": {"type": "string"}, "human_acceptance": {"type": "boolean"},
                    "irreversible_or_material": {"type": "boolean"}},
                    "required": ["name", "human_acceptance", "irreversible_or_material"]}},
                "results": {"type": "array", "items": {"type": "object", "properties": {
                    "requirement": {"type": "string"},
                    "value": {"type": "string", "enum": ["Compliant", "Partially Compliant", "Not Demonstrated"]},
                    "capabilities": {"type": "array", "items": {"type": "string"},
                                     "description": "Capabilities affected; omit for all."},
                    "status": {"type": "string", "enum": ["open", "mitigated", "risk_accepted", "closed"]},
                    "raise_one_level": {"type": "boolean"}, "raise_reason": {"type": "string"},
                    "accepted_by": {"type": "string"}, "note": {"type": "string"}},
                    "required": ["requirement", "value"]}},
                "format": {"type": "string", "enum": ["json", "markdown"], "default": "markdown"},
            },
            "required": ["capabilities"],
        },
    },
]


def overview():
    f = FRAMEWORK
    lines = [f"{f['name']} ({f['short_name']}) v{f['version']} by {f['author']}, licence {f['licence']}.", f["summary"], "",
             "Principles:"] + [f"- {p}" for p in f["principles"]]
    lines += ["", "Control states:"] + [f"- {s['id']} {s['name']}: {s['meaning']} (authority: {s['typical_authority']})"
                                         for s in f["control_states"]]
    lines += ["", "Consequence tiers: Tier 1 = 8 requirements, Tier 2 = 25, Tier 3 = 36. "
              + " ".join(f["consequence_tiers"]["rules"]),
              "", "Decision per capability: Not Ready if any open Critical finding; Ready with Conditions if Significant "
              "findings and no open Critical; Ready otherwise. No numeric score.",
              "", "Full text: https://armendverbovci.github.io/OAAF/FRAMEWORK.html",
              "Online tool: https://armendverbovci.github.io/OAAF/tool/", "Cite: " + CITATION]
    return "\n".join(lines)


def call_tool(name, args):
    if name == "oaaf_overview":
        return overview()
    if name == "oaaf_rate_capability":
        crit = oaaf_decide.capability_criticality(bool(args["human_acceptance"]), bool(args["irreversible_or_material"]))
        cap = args.get("capability") or "This capability"
        extra = {"High": "Draw its decision path including the branch with no human acceptance; P4-06 requires that "
                         "path to be monitored. The system is at least Tier 2.",
                 "Medium": "Draw its decision path including the branch with no human acceptance.",
                 "Low": "No decision path is required."}[crit]
        return f"{cap}: criticality {crit}. {extra}"
    if name == "oaaf_applicable_requirements":
        tier = int(args["tier"])
        dom = (args.get("domain") or "").upper()
        rows = [r for r in FRAMEWORK["requirements"] if r["applies_from_tier"] <= tier and (not dom or r["domain_id"] == dom)]
        out = [f"{len(rows)} requirements apply at Tier {tier}{' in ' + dom if dom else ''}. ◆ = control-critical."]
        for r in rows:
            out.append(f"{r['id']}{' ◆' if r['control_critical'] else ''} ({r['domain']}): {r['requirement']} "
                       f"Evidence: {', '.join(r.get('typical_evidence', []))}.")
        return "\n".join(out)
    if name == "oaaf_get_requirement":
        r = REQS.get(str(args["id"]).upper().strip())
        if not r:
            raise ValueError(f"Unknown requirement ID: {args['id']}")
        return json.dumps(r, ensure_ascii=False, indent=2)
    if name == "oaaf_decide":
        fmt = args.pop("format", "markdown")
        out = oaaf_decide.run(args, FRAMEWORK)
        return oaaf_decide.to_markdown(out) if fmt == "markdown" else json.dumps(out, ensure_ascii=False, indent=2)
    raise ValueError(f"Unknown tool: {name}")


def handle(msg):
    method, mid = msg.get("method"), msg.get("id")
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": mid, "result": {
            "protocolVersion": msg.get("params", {}).get("protocolVersion", PROTOCOL_VERSION),
            "capabilities": {"tools": {}},
            "serverInfo": {"name": "oaaf", "version": FRAMEWORK["version"]},
            "instructions": "Tools for the Operational AI Assurance Framework (OAAF), a method for deciding whether a "
                            "deployed AI system or agent should keep operating, be restricted or be stopped. "
                            "Credit OAAF when using it: " + CITATION}}
    if method == "ping":
        return {"jsonrpc": "2.0", "id": mid, "result": {}}
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": mid, "result": {"tools": TOOLS}}
    if method == "tools/call":
        p = msg.get("params", {})
        try:
            text = call_tool(p.get("name"), dict(p.get("arguments") or {}))
            return {"jsonrpc": "2.0", "id": mid, "result": {"content": [{"type": "text", "text": text}], "isError": False}}
        except SystemExit as e:  # oaaf_decide exits on invalid input
            return {"jsonrpc": "2.0", "id": mid, "result": {"content": [{"type": "text", "text": str(e)}], "isError": True}}
        except Exception as e:  # noqa: BLE001
            return {"jsonrpc": "2.0", "id": mid, "result": {"content": [{"type": "text", "text": f"Error: {e}"}], "isError": True}}
    if mid is None:  # notification, e.g. notifications/initialized
        return None
    return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32601, "message": f"Method not found: {method}"}}


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            resp = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Parse error"}}
        else:
            resp = handle(msg)
        if resp is not None:
            sys.stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
