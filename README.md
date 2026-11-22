# Operational AI Assurance Framework (OAAF)

**OAAF is a free, sector-neutral method for deciding, on evidence, whether a deployed AI system or AI agent should keep operating, be restricted, or be stopped. It is adapted from aviation safety management.**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24352952.svg)](https://doi.org/10.5281/zenodo.24352952)

Version 1.0, November 2026 · Author: Armend Verbovci · Licence: [CC BY 4.0](LICENSE) (free to use and adapt, including commercially, with credit)

| Read | Use | Automate |
|---|---|---|
| [Full framework (web)](FRAMEWORK.md) | **[Online assessment tool](tool/)** | [AI assistant skill](skills/oaaf-assessment/SKILL.md) |
| [Framework (PDF)](downloads/OAAF_v1.0.pdf) | [Assessment workbook (Excel)](downloads/OAAF_v1.0_Assessment_Workbook.xlsx) | [MCP server for AI assistants](mcp/) |
| [Introduction to OAAF (article)](blog/introducing-oaaf.md) | [Quick start for simple systems](#quick-start-one-afternoon) | [Machine-readable rules (oaaf.json)](oaaf.json) |
| [Frequently asked questions](FAQ.md) | [Worked examples](FRAMEWORK.md#annex-b-worked-examples) | [Decision script](skills/oaaf-assessment/scripts/oaaf_decide.py) |

**Help test OAAF:** take the [Two-Assessor Challenge](challenge/). Assess a synthetic AI agent case on your own and see whether you reach the same decision as other people.

## The problem

Most AI assurance effort goes into the period before a system goes live: evaluations, benchmarks, red-teaming and policy sign-off. Far less addresses the question an operator faces every day once it is running: **should this system keep running, in this form, right now?** Who can stop it, when would they, how would anyone notice it had degraded, and what happens after a model provider quietly updates the model?

Safety-critical industries answered these questions decades ago. OAAF brings that operating discipline to AI in any sector.

## When to use OAAF

- An AI system or agent is about to go live and someone has to sign off that it is ready.
- A system is live and nobody has defined when it should be restricted or switched off.
- A model provider has changed or updated the model behind a live system.
- Something has gone wrong and a capability needs to be stopped, investigated and returned to service.
- You need a practical basis for post-market monitoring or deployer monitoring under the EU AI Act.

It is designed for owners and operators of AI systems, heads of AI governance, risk, compliance and internal audit, independent assessors, and regulators. No AI engineering or aviation background is needed.

## How it works, in one page

1. **Define the system as it is actually operated**, including people, data, tools and permissions, not just the model.
2. **List what the system can cause to happen** (its capabilities) and rate each with two questions:
   - Must a human positively accept this output before it takes effect?
   - If it is wrong, would the harm be irreversible before detection, or above the organisation's materiality threshold?

   No acceptance and serious consequence = **High**. Acceptance and minor consequence = **Low**. Anything else = **Medium**.
3. **Set the Consequence Tier.** Tier 1 systems need 8 requirements, Tier 2 need 25, Tier 3 need all 36. Any High capability means at least Tier 2.
4. **Define five control states** for each capability: S0 Normal, S1 Degraded, S2 Restricted, S3 Contained, S4 Unacceptable, covering both the model and the service around it.
5. **Assess the requirements** in seven domains: accountability and authority, hazards and risk, operational boundaries, continuous assurance, occurrence and learning, change assurance, and human and AI operation.
6. **Apply fixed decision rules.** Findings are rated Routine, Significant or Critical by rule, not judgement. Each capability is then **Ready**, **Ready with Conditions** or **Not Ready**. There is no percentage score: one missing stop mechanism is never averaged away.

Two ideas set OAAF apart:

- **Negative-space assurance.** The riskiest path is often the one nobody looks at: the transaction auto-approved, the case not escalated, the job quietly deprioritised. OAAF requires that path to be monitored.
- **Boundary assurance.** Real gaps tend to sit between teams (model risk and IT, change management and vendor management, internal change control and an external model provider). OAAF asks questions that cross those seams.

## Quick start (one afternoon)

For a low-consequence system, complete these eight items on one page:

1. Name an accountable owner (P1-01).
2. Write down foreseeable misuse and failure modes (P2-01).
3. Write down when you would restrict or stop the system (P3-01).
4. Name who reviews performance and how often (P4-01).
5. Give users a way to report problems (P5-01).
6. Record the current configuration: model, version, prompts, tools, data (P6-01).
7. Note the likely effect of each change before release (P6-02).
8. List the people who act on the output (P7-01).

If any capability turns out to be High, use the full assessment instead.

## Using OAAF with an AI assistant

The [`skills/oaaf-assessment`](skills/oaaf-assessment/) folder is an open-format agent skill. Add it to an AI assistant that supports skills (for example Claude, by uploading the zipped folder from [downloads](downloads/)) and ask it to "run an OAAF assessment" on your system. The assistant guides you through the questions, then applies the decision rules with a small script so that the same answers always give the same decision.

Assistants that support the Model Context Protocol can use the [OAAF MCP server](mcp/), which has tools for rating capabilities, listing requirements and applying the decision rules. It uses only the Python standard library.

Developers and governance tools can load [`oaaf.json`](oaaf.json), which contains all 36 requirements, tiers, control states, evidence rules and decision rules in structured form.

## How OAAF relates to other frameworks

OAAF does not replace ISO/IEC 42001, the NIST AI Risk Management Framework or the EU AI Act. It sits underneath them, turning their requirements into an operating regime for one deployed system. Annex D of the framework maps each domain to the relevant clauses and articles. Section 2.6 compares OAAF with other 2026 work on deployment and agent assurance.

## Status and limitations

Version 1.0 is a published method for use and comment. The worked examples are synthetic, and the decision rules have been checked by design rather than by independent assessors on a real system. Section 9 of the framework sets out the limitations in full. Results from real use, especially two people assessing the same system independently, are the most useful feedback. You can [report real use](https://github.com/armendverbovci/OAAF/issues/new?template=real-use-report.yml) or take the [Two-Assessor Challenge](challenge/).

## Cite

Verbovci, A. (2026). *Operational AI Assurance Framework (OAAF), Version 1.0.* Zenodo. https://doi.org/10.5281/zenodo.24352952

See also [CITATION.cff](CITATION.cff).

## Contact

Comments, corrections and results from real use: armendverbovci@gmail.com, or open an issue in this repository.

*Developed independently, in a personal capacity, from public standards and published literature. It does not represent the views of any employer, client or regulator.*
