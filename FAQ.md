# OAAF: frequently asked questions

Short answers about the [Operational AI Assurance Framework (OAAF)](README.md). Section numbers refer to the [full framework](FRAMEWORK.md).

## What is OAAF?

A free, sector-neutral method for deciding, on evidence, whether a deployed AI system or AI agent should keep operating, be restricted, or be stopped. It adapts the safety management practices used in aviation to AI systems in any sector.

## How do I decide whether an AI system is ready to go live?

Define the system as it will actually be operated, list what it can cause to happen, rate each capability with OAAF's two-question test, and assess the requirements that apply to its Consequence Tier. Fixed rules then give each capability one of three outcomes: Ready, Ready with Conditions, or Not Ready (Sections 4 and 7).

## How do I monitor an AI system after deployment?

Define control states (Normal, Degraded, Restricted, Contained, Unacceptable) with measurable triggers between them, separate safety-relevant indicators from general performance figures, and, for any capability that acts without human acceptance, monitor that unreviewed path directly through sampling or outcome tracking (Sections 5 and 6, domains P3 and P4).

## When should an AI system be switched off or restricted?

When conditions you defined in advance are met. OAAF requires those conditions to be written down (P3-01), turned into measurable triggers (P3-03), linked to named decision authority (P3-04), and backed by a mechanism that can actually execute a stop within a set response time (P1-05). Restriction is usually better than a full stop: OAAF decisions apply per capability, so you can restrict one function and keep the rest running.

## How do I assure an AI agent?

Treat each class of tool action as a separate capability and rate each one. Make sure the agent's technical permissions match its declared capabilities (P3-06), include its persistent memory and tool permissions in the configuration baseline (P6-01), and monitor what it chooses not to do, such as items skipped or deprioritised (P4-06). Section 8.4 and worked example B3 cover agents.

## What should we do when the model provider updates the model?

Treat it as a change to your system. OAAF requires external dependencies that can change behaviour to be covered by change detection, version pinning, supplier notification or evidenced compensating monitoring (P6-05), and behavioural changes to be assessed before release (P6-02 to P6-04).

## What is negative-space assurance?

Assurance of what the system does without anyone looking: outputs that became action with no human acceptance, and choices not to flag, escalate or act. Human review tends to follow what the AI flags, so the unreviewed path is often the least examined and most consequential (Principle 9, P4-06).

## What is boundary assurance?

Checking the interfaces between teams, where controls are most often assumed rather than evidenced: for example model risk and IT operations, or change management and vendor management. OAAF requires hazards to be recorded even when another team owns the control, and only counts another team's control if it is evidenced against this system (Section 7.2).

## Does OAAF help with the EU AI Act?

It provides a practical structure for the monitoring that the Act expects: post-market monitoring by providers (Article 72), serious incident reporting (Article 73), human oversight (Article 14) and deployer monitoring (Article 26). Following Regulation (EU) 2026/1744, high-risk obligations apply from 2 December 2027 for Annex III systems and 2 August 2028 for Annex I systems. Using OAAF does not by itself establish legal compliance (Annex D).

## How does OAAF relate to ISO/IEC 42001 and the NIST AI RMF?

ISO/IEC 42001 sets an organisation-wide AI management system, and the NIST AI RMF defines outcomes across Govern, Map, Measure and Manage. OAAF sits underneath both as the operating regime for one deployed system, and is one concrete way to carry out Measure and Manage once a system is in service (Section 2.6, Annex D).

## Is OAAF only for aviation or safety-critical systems?

No. It is sector-neutral and proportionate. A low-consequence system, such as an internal assistant, needs only 8 of the 36 requirements and can be covered in an afternoon. The worked examples include customer service, banking fraud scoring and utility maintenance.

## Why is there no score?

Because averaging hides the failures that matter. A system that meets thirty requirements but has no working way to stop it is not 90% ready. OAAF rates each finding by rule and decides per capability (Section 7.3).

## How do two assessors reach the same answer?

Criticality is derived from a table, not judged. Three evidence rules remove the most common sources of disagreement: assumed controls, "nothing has gone wrong" reasoning, and hazards owned by other teams. Annex C shows the rules applied to a case where two viewpoints had previously disagreed. This has been checked by design, not yet by independent assessors on a real system.

## How long does an assessment take?

A Tier 1 quick start takes about an afternoon. A full Tier 2 or Tier 3 assessment depends on the system and the quality of existing records, typically days rather than weeks for a single system.

## Can I use OAAF commercially, adapt it or build tools on it?

Yes. It is licensed under CC BY 4.0: you can use, copy, adapt and build on it, including commercially, provided you credit the author.

## Can an AI assistant run an OAAF assessment?

Yes. The repository includes an open-format agent skill (`skills/oaaf-assessment`) that guides a user through the assessment and applies the decision rules with a script, and a machine-readable file (`oaaf.json`) for tools.

## Who developed OAAF?

Armend Verbovci, an air navigation services professional with more than twenty years in aviation, including ten years as an air traffic controller and more than a decade leading safety, quality and compliance functions. It was developed independently, in a personal capacity.

## Is there a tool for running an OAAF assessment?

Yes. The [online assessment tool](tool/) runs in your browser and sends nothing anywhere. It rates capabilities with the two-question test, shows the requirements that apply, and gives each capability a decision. There's also an [Excel workbook](downloads/OAAF_v1.0_Assessment_Workbook.xlsx), an [AI assistant skill](skills/oaaf-assessment/SKILL.md) and an [MCP server](mcp/) for assistants. All of them apply the same rules.

## How can I help improve OAAF?

Take the [Two-Assessor Challenge](challenge/), which tests whether independent assessors reach the same decision. Or [report what happened](https://github.com/armendverbovci/OAAF/issues/new?template=real-use-report.yml) when you used OAAF on a real system. Changes in later versions will cite the results that justified them.
