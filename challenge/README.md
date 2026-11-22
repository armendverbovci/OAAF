# The OAAF Two-Assessor Challenge

**Can two people, working separately from the same evidence, reach the same decision about an AI system? Help find out.**

OAAF's decision rules were designed so that two competent assessors reach the same conclusion from the same evidence. So far that has only been checked by design, by one author taking two viewpoints (Annex C and Section 9.1 of the [framework](../FRAMEWORK.md)). That is the framework's biggest open weakness. This challenge is how to test it properly, in public.

## How it works

1. **Read the case.** [ClaimPilot](case-claimpilot.md) is a synthetic AI agent used by a motor insurer. The case file contains everything an assessor found: documents seen, interviews and records. It takes about 20 minutes to read.
2. **Assess it on your own.** Use the [online assessment tool](../tool/) or the [assessment workbook](../downloads/OAAF_v1.0_Assessment_Workbook.xlsx). Rate each capability, set the tier, record a value for every applicable requirement, and let the rules produce the decision. Do not discuss it with anyone else who is taking part until you have submitted.
3. **Submit your result.** Download your assessment as JSON from the tool and [open a submission issue](https://github.com/armendverbovci/OAAF/issues/new?template=challenge-submission.yml), or email it to armendverbovci@gmail.com. Tell us briefly about your background and which items you found hardest to call.
4. **See how you compare.** Results are compared with a [published script](compare.py) and summarised on this page, anonymised unless you ask to be named. Assessments from pairs who work in the same organisation but assess separately are especially welcome.

No AI engineering or aviation background is needed. A risk, audit, compliance, operations or engineering background is enough.

## What is measured

For every pair of submissions:

- agreement on **capability criticality** (High, Medium, Low);
- agreement on the **Consequence Tier**;
- agreement on the **value** given to each applicable requirement;
- agreement on the **criticality of each finding**;
- agreement on the **decision for each capability** (Ready, Ready with Conditions, Not Ready).

The last one matters most. The framework accepts that assessors will sometimes disagree on details. What it claims is that the rules absorb those differences so that the decision comes out the same.

## Why take part

- You get hands-on practice with a structured method for in-service AI assurance, using a realistic agent case.
- Every result goes into the evidence behind the next version. Where the rules fail to bring assessors together, they will be changed, and the change will cite the results that justified it (Section 9.5).
- Contributors who wish to be named will be credited in OAAF version 1.1.

## Results so far

No submissions yet. This page will be updated as results arrive.

| Round | Submissions | Capability criticality agreement | Decision agreement | Notes |
|---|---|---|---|---|
| 1 | 0 | – | – | Open |

## Rules

- Work alone, from the case file only. Where the case does not tell you something, treat it as not evidenced (Rule 1, Section 7.2).
- Do not look at other people's submissions in the issue tracker before you submit your own.
- The author's own reference assessment will be published only after round 1 closes, so it does not anchor anyone.

*OAAF v1.0 by Armend Verbovci, CC BY 4.0. [DOI 10.5281/zenodo.24352952](https://doi.org/10.5281/zenodo.24352952). The case is entirely synthetic and does not describe any real organisation.*
