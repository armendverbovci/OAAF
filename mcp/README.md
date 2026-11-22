# OAAF MCP server

This is a small [Model Context Protocol](https://modelcontextprotocol.io) server that gives AI assistants the Operational AI Assurance Framework (OAAF) as tools. With it, an assistant can rate the capabilities of an AI system, list the requirements that apply, and apply the OAAF v1.0 decision rules in the same way every time, rather than estimating them.

It runs locally over stdio, needs only Python 3.8 or later, and installs nothing. It doesn't send data anywhere.

## Tools

| Tool | What it does |
|---|---|
| `oaaf_overview` | Summarises OAAF: its principles, control states, tiers and decision rules |
| `oaaf_rate_capability` | Applies the two-question test to one capability (High, Medium or Low) |
| `oaaf_applicable_requirements` | Lists the requirements that apply at Tier 1, 2 or 3, optionally for one domain |
| `oaaf_get_requirement` | Looks up one requirement by ID, for example `P4-06` |
| `oaaf_decide` | Applies the decision rules to a full assessment and returns a decision for each capability |

## Set-up

1. Clone or download this repository.
2. Add the server to your MCP client's configuration. For Claude Desktop, and for other clients that use the same format:

```json
{
  "mcpServers": {
    "oaaf": {
      "command": "python3",
      "args": ["/full/path/to/OAAF/mcp/oaaf_mcp_server.py"]
    }
  }
}
```

3. Restart the client. Then ask it something like "Use OAAF to assess our customer email agent", or "Which OAAF requirements apply to a Tier 2 system?"

The server loads `oaaf.json` and the decision script from the same repository, so the server, the online tool and the assistant skill all apply the same rules.

## Licence

CC BY 4.0. If you use OAAF, please credit it: Verbovci, A. (2026). *Operational AI Assurance Framework (OAAF), Version 1.0.* Zenodo. https://doi.org/10.5281/zenodo.24352952
