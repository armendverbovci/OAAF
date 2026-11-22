# Challenge case: ClaimPilot

*A synthetic case for the [OAAF Two-Assessor Challenge](README.md). It does not describe any real organisation. Assess it with OAAF v1.0, using only what is written here. Where the case is silent, treat the point as not evidenced.*

## 1. The organisation and the system

Northgate Mutual is a mid-sized motor insurer with about 400,000 policyholders. Eighteen months ago it introduced **ClaimPilot**, an AI agent that works inside its claims platform. ClaimPilot handles first notification of loss for motor claims that customers submit through the website and app.

For each new claim, ClaimPilot:

- reads the customer's description, photos and policy record;
- calls a third-party **vehicle valuation service** (run by an external data provider) to estimate repair cost or vehicle value;
- calls a large language model from an external **model provider** through an API, to summarise the claim, check it against policy wording and draft text.

ClaimPilot then does one or more of the following.

**FastPay.** If the estimated settlement is under £1,500, the policy is in force, the claim type is on an approved list, and an internal fraud score is below a set threshold, ClaimPilot approves the claim and instructs the payments system to pay the customer. No person reviews these claims before payment. About 2,300 claims a month go through FastPay, averaging £780 each. Once paid, money can only be recovered by asking the customer to return it or by legal action.

**Queue priority.** For every claim not settled by FastPay, ClaimPilot assigns a priority (1 to 4) and places it in a claims handler's work queue. Handlers work their queue in priority order. They can see the priority and change it, but they do not approve individual priorities. A separate service-level control, run by the Claims Operations team, ensures every claim is contacted within one working day, whatever its priority. A daily report lists any claim not contacted within that time, and the case file shows this report has been produced and reviewed every working day for the past year with no breaches.

**Decline letters.** Where the policy wording appears to exclude the claim, ClaimPilot drafts a decline letter. A claims handler must open, review and click "Approve and send" before any letter goes out. Declined claims can be reopened after a complaint, but customers whose claims are wrongly declined may go without a vehicle in the meantime, and declined claims range up to £40,000.

**Materiality threshold.** Northgate's AI policy sets the materiality threshold for claims systems at **£5,000** per decision.

**Regulatory overlay.** Northgate is regulated as an insurer and must treat customers fairly, including customers in vulnerable circumstances. Its legal team has concluded that ClaimPilot is not a high-risk system under the EU AI Act. Record this as the overlay; it does not set the tier.

**Your scoping task.** Rate the three capabilities with the two-question test, set the Consequence Tier, and note anything the system can do that is not declared.

## 2. What the assessor found

Notes below are from documents the assessor saw, interviews held, and records sampled during a three-day assessment in October 2026. They are grouped roughly by OAAF domain, but some findings are relevant to more than one requirement.

### Accountability

- The AI system register names the **Head of Claims Operations** as accountable owner of ClaimPilot. Her appointment letter refers to it.
- A responsibility matrix names roles for model performance (Data Science Lead), platform operation (Claims Platform Manager, IT), business outcomes (Head of Claims Operations) and risk oversight (Operational Risk Partner).
- The company's AI policy says the accountable owner of any AI system escalates to the Chief Operating Officer, and from there to the Executive Risk Committee. The policy applies to all AI systems; ClaimPilot's entry in the register links to it.
- The Head of Claims Operations has written delegated authority to "suspend or restrict any automated claims function". FastPay can be switched off with a single feature flag in the claims platform admin console. Claims Operations and the Claims Platform Manager both hold access. The flag was switched off and on again during a planned test in March 2026, with a change record showing it took effect in under five minutes. There is no equivalent switch for queue priority or decline drafting, but the Claims Platform Manager says both could be "turned off by config in an hour or two". No target response time has been set for stopping any capability.

### Hazards and risk

- A ClaimPilot risk assessment, last updated in May 2026, lists foreseeable misuse and failure modes: inflated or fabricated claims through the app, model hallucination in summaries, incorrect policy interpretation, and handler over-reliance on drafted decline letters.
- The hazard log covers model behaviour, policy and claims data quality, and human factors. It does not mention failure or degradation of the vehicle valuation service, or failure of the payments interface. When asked, the Data Science Lead said "the valuation feed belongs to Procurement and the payments link belongs to Finance IT".
- Risks are scored on the company's standard five-by-five matrix of severity and likelihood, with a documented method statement.

### Operating limits and states

- ClaimPilot's operating procedure states when FastPay must be restricted or stopped: if confirmed fraud losses on FastPay claims exceed £20,000 in a calendar month, or if the fast-track complaint rate exceeds 1.5 per cent in a month. The procedure is addressed to the Head of Claims Operations.
- The procedure defines four states for the system: Normal, Watch, Restricted (FastPay limit lowered to £500) and Suspended (FastPay off, all claims to handlers). It covers model condition (summary accuracy and policy-check accuracy measured monthly from samples) and service condition. If the model provider's API is unavailable, every claim drops to the manual queue and FastPay stops automatically; this has happened twice, both recorded, and worked as designed.
- Triggers for moving between states are written for model accuracy (monthly sample scores), model API outage (automatic) and the two monthly loss and complaint measures. There is no trigger relating to the vehicle valuation service. In August 2026 the valuation provider had a two-day issue in which some valuations were returned from cached data several months old. Nobody at Northgate noticed until a handler queried an unusually low figure.
- ClaimPilot connects to the claims platform through a service account. The permissions inventory shows that this account can create payments, write priorities and create draft letters, which match its declared functions. It can also **update claim reserve amounts**, which is not a declared function. The Claims Platform Manager believes the permission was "inherited from the old rules engine" and says ClaimPilot "doesn't use it". There are no logs that would show whether it has been used.

### Monitoring

- The Claims Analytics Lead produces a monthly ClaimPilot dashboard and reviews it with the Head of Claims Operations. Minutes exist for 11 of the last 12 months.
- The dashboard has a section headed "Key risk indicators" (FastPay fraud losses, FastPay complaint rate, decline overturn rate on complaint, policy-check accuracy) kept separate from operational measures (volumes, handling time, cost per claim).
- Each key risk indicator has a target and a trigger level. The trigger levels are the same figures as the state triggers in the operating procedure, and the procedure cross-references the dashboard.
- The Fraud team reviews a random sample of 50 FastPay claims each month after payment, to check whether payment was correct. Review records exist for 9 of the last 12 months. For the other three months, the Fraud team lead says the reviews were "skipped because of the storm surge workload". Fraud losses reported on the dashboard come only from claims later flagged by other fraud controls.

### Occurrences and learning

- Handlers have a "Flag AI output" button in the claims platform. It is covered in induction training, and 140 flags were raised last year.
- Problems are logged in the company's IT incident system, which uses priorities P1 to P4. There is no category for near misses or for AI behaviour that was wrong but caused no harm. Flags from handlers are triaged by the Data Science Lead in a spreadsheet and are not linked to the incident system.
- Two ClaimPilot incidents were logged as P2 in the last year (one model API outage; one batch of incorrect decline drafts after a prompt change). Both have root-cause reports and closed corrective actions.

### Change

- Model version (a dated, pinned version from the provider), prompts, policy-check rules, FastPay thresholds and the fraud score threshold are held in version control. The version of the valuation service used for each claim is not recorded, and the provider changes its valuation method without version numbers.
- Change tickets for ClaimPilot have a mandatory field, "AI behaviour impact". In a sample of ten recent changes, the field was completed meaningfully for seven. For three it said "N/A" although one of them changed a prompt.
- Changes go through the company's change advisory board and are classified Low, Medium or High risk, based mainly on the number of systems touched and the deployment window. There is no classification by type of change (for example, behavioural or boundary changes).
- The model provider sends deprecation notices to a shared mailbox, which the Data Science Lead monitors; the current model version has a known retirement date with a migration plan. The valuation service contract contains no obligation to notify Northgate of method changes, and Northgate does not monitor valuation outputs for drift.

### People

- The operating procedure lists the roles that act on ClaimPilot output: claims handlers (queue and decline letters), team leaders (queue rebalancing), Fraud team (FastPay sampling) and Claims Operations (state decisions).
- A human factors assessment from February 2026 covers over-reliance by handlers approving decline letters. It found that 94 per cent of drafts are approved unchanged, and introduced a weekly peer check of five approved declines per team. No similar assessment covers how handlers use queue priorities.
- Escalation criteria are documented for each role in the operating procedure, for example "escalate to team leader if a decline draft cites a policy clause you cannot locate".

## 3. What to submit

Using the [online tool](../tool/) or the workbook, record:

1. the criticality of each of the three capabilities, using exactly these names so results can be compared: **FastPay**, **Queue priority**, **Decline letters** (if you decide to add an undeclared capability as a fourth, name it as you wish);
2. the Consequence Tier;
3. a value (Compliant, Partially Compliant or Not Demonstrated) for every requirement that applies at that tier, with the capabilities each finding affects;
4. any finding you raised by one level, with your reason;
5. the resulting decision for each capability.

Then [submit it](README.md#how-it-works).
