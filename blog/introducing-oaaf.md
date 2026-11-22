---
title: "Should this AI system still be running? Introducing OAAF"
description: "A long introduction to the Operational AI Assurance Framework: why pre-deployment testing is not enough, the two-question test, control states, the 36 requirements, the decision rules and three worked examples."
---

# Should this AI system still be running?

**Introducing the Operational AI Assurance Framework (OAAF)**

*Armend Verbovci, November 2026*

Ask an organisation how it decided its AI system was fit to go live, and you'll usually get a confident answer. There were evaluations, benchmarks, red-teaming, an impact assessment, perhaps a committee sign-off. Real work went into it.

Then ask a different question: how do you know, today, that the system should still be running in its current form? And if it shouldn't, who would decide that, how quickly could they act, and what would happen next?

The answers get much thinner. Often there isn't one.

That gap is what the Operational AI Assurance Framework, or OAAF, is built to fill. It's a free, open method for deciding, on evidence, whether a deployed AI system or AI agent should keep operating, be restricted, or be stopped, and for keeping that decision current as the system, its data and its suppliers change. Version 1.0 is published under a Creative Commons licence, so anyone can use it, adapt it and build on it, commercially or not, as long as they credit the source.

This post explains what OAAF is, why I built it, how it works from start to finish, and where its weaknesses are. It's long because the framework is meant to be used rather than admired, and you can't use something you only half understand. If you only want the short version: OAAF takes the way safety-critical industries run high-consequence systems day to day and applies it to AI, in any sector, with depth that scales to how much harm the system could actually do.

## The question nobody owns after go-live

Most of the effort in AI assurance goes into the period before a system is switched on. That makes sense. It's when the system is newest, when the most people are paying attention, and when the approval gate gives everyone a clear deadline.

But a deployed AI system isn't a finished product sitting on a shelf. It runs every day, in conditions that keep moving. And the question an operator faces once it's live is simple to state and hard to answer: should this system keep running, in this form, right now?

The US National Institute of Standards and Technology published its first report on monitoring deployed AI in March 2026. Its conclusion was blunt: best practice for monitoring, validated methods and even shared terminology are all still at an early stage. In other words, the field hasn't yet settled how to do the thing that matters most once a system is in service.

I don't think that's because nobody cares. It's because the in-service question falls between functions. Data scientists own the model. IT owns the infrastructure. Risk owns the risk register. The business owns the outcome. Each of them holds part of the answer, and nobody holds the whole of it.

## Why testing before launch isn't enough

Pre-deployment evaluation is necessary. OAAF doesn't argue against it. But it isn't sufficient, for four reasons that come up again and again.

**The model is not the system.** When an AI system causes harm, the cause is rarely the model on its own. It's the combination of the model with its prompts, data, tools, integrations, the people who use it and the process it sits in. You can evaluate a model thoroughly and still know very little about whether the system around it is safe to run.

**Systems change after approval.** Prompts get edited. Knowledge sources get updated. And third-party model providers change how their models behave, sometimes without telling anyone. The system that was approved six months ago may not be the system running today, even if nobody in your organisation touched it.

**Oversight goes where it can see.** Human review tends to focus on what the AI flags. If a fraud model holds a suspicious transaction, an analyst looks at it. If it approves a transaction automatically, nobody looks at all. The cases a system quietly lets through often get no review whatsoever, and those are frequently the cases that matter most.

**Nobody has defined "degraded".** Most organisations can switch a system off. Far fewer have agreed in advance when they would switch it off, who would make that call, and what happens to the work the system was doing. When something goes wrong, those decisions get made under pressure, by whoever happens to be in the room.

Regulation is heading the same way. The EU AI Act requires providers of high-risk systems to run post-market monitoring and report serious incidents, requires those systems to be designed for effective human oversight, and requires deployers to monitor how they operate. Under the Digital Omnibus on AI, which came into force in July 2026, the high-risk obligations now apply from December 2027 for one group of systems and August 2028 for another. That gives organisations a window to build a proper operating regime rather than bolt one on in a hurry.

## Where the idea came from

I spent more than twenty years in aviation, ten of them as an air traffic controller, and more than a decade leading safety, quality and compliance work for air navigation service providers. When I started looking at how AI systems are governed once they're live, I kept recognising the problem. Aviation met it a long time ago.

Aviation doesn't certify an aircraft or an air traffic system and then walk away. It runs a continuous operating regime. There are named people with real authority. There are defined degraded modes, so everyone knows in advance what "not quite right" looks like and what to do about it. There's occurrence reporting, so problems get recorded before they become accidents. There's investigation, controlled change, and a formal return to service after something has gone wrong.

The formal name for this is a Safety Management System, set out internationally in ICAO Annex 19 and the ICAO Safety Management Manual. Its core logic is that a system which worked in testing is not, on that evidence alone, acceptable to operate. Acceptability has to be maintained, every day, by people who know what they're looking for and have the power to act.

OAAF borrows that logic. It doesn't borrow the vocabulary, and you don't need to know anything about aviation to use it. I deliberately left behind the parts that don't transfer: certification by a single authority before operation, prescriptive rules for specific technologies, and aviation's jargon. AI systems change too often, and are used in too many sectors, for those to work.

## What OAAF is, and what it isn't

It helps to be clear about scope from the start.

OAAF is a method for running and assessing one deployed AI-enabled system. It's designed to be usable by a governance, risk, safety or operations lead who doesn't have an AI engineering background. It's sector-neutral, so it applies equally to a customer service chatbot and to an agent supporting critical infrastructure. And it's proportionate: the depth of assessment scales with the consequences of the system getting things wrong.

OAAF is not an organisation-wide AI management system. That's what ISO/IEC 42001 is for. It's not a model evaluation or testing method. It's not a certification scheme, and using it doesn't amount to a claim of legal compliance. And it's not a maturity model or a scoring system. That last point is deliberate, and I'll come back to why.

It's aimed at four groups of people:

- owners and operators of deployed AI systems, including agents, who need to know whether they're actually in control;
- heads of AI governance, risk, compliance or internal audit, who need an operational test underneath their policy framework;
- independent assessors, who need a method that two people can apply to the same system and reach the same answer;
- regulators and sector bodies looking for a practical example of in-service AI assurance.

## The nine principles

Everything in OAAF follows from nine principles. They're short, and most of them will sound obvious once stated, but each one closes off a common mistake.

**1. System of operation.** Assurance applies to the AI-enabled system as it's actually deployed and run: the model, data, software, tools, interfaces, people, processes and environment. Assuring the model alone doesn't tell you that running the system is acceptable.

**2. Context dependency.** Risk depends on context, not on capability. The same model can be harmless answering staff questions about holiday policy and highly consequential approving payments.

**3. Proportionality.** Rigour scales with consequence. Applying the same depth to every system isn't thoroughness. It's a design fault, because it either buries low-risk systems in paperwork or spreads attention too thinly across high-risk ones.

**4. Continuous, not one-off.** Assurance is maintained for the life of the system through a mix of continuous, periodic and event-triggered activity. That doesn't mean watching every parameter every second. It means knowing what you're watching, why, and what would make you act.

**5. Assurance is not performance.** Good performance figures are not the same thing as evidence that you'd notice if performance got worse. A dashboard full of green numbers tells you how the system did on the things you measured. It doesn't tell you what you're not measuring.

**6. Acceptable, not absolute.** The aim is acceptable operation within a defined context and risk tolerance. OAAF never claims a system is "safe" in some absolute sense, and nor should anyone else.

**7. Independence in proportion to risk.** The more harm a system can do, the more its assessment should involve someone other than the team that built or runs it.

**8. Accountability requires authority.** A named owner who can't actually restrict or stop the system is a control deficiency, not a control. Putting someone's name on a form isn't the same as giving them power.

**9. Negative-space assurance.** Assurance has to cover what the system doesn't flag, escalate or surface. The path where AI output becomes action with nobody looking is usually the least examined and the most consequential.

That ninth principle is, I think, the most important idea in the framework, and it runs through everything that follows.

## Step one: working out what you're actually assessing

Before any assessment, OAAF asks you to scope the system properly. This decides how much of the framework applies. It takes four steps and the result fits on a single page, which the framework calls a System Card.

### Define the system as it's really operated

Write down, in plain language, the system's purpose and intended outcome; who uses it, who operates it and who's affected by what it produces; the AI components (which models, from which providers, at which versions) and the non-AI components; the data and knowledge sources, tools and integrations, and the permissions the system holds in other systems; how human oversight is arranged; and the assumptions and known limitations.

You also set a **materiality threshold**. This is the level of financial, operational or other consequence above which your organisation treats an error as material. It's your organisation's call, not the assessor's. If you don't set one, OAAF applies a default: any consequence that moves money, commits the organisation to a third party, or communicates externally on its behalf counts as material. That default matters. It stops an organisation from dodging scrutiny simply by never defining what "serious" means.

### List what the system can do

OAAF assesses **capabilities**, not models. A capability is something the system can cause to happen: approve a transaction, send a reply, reorder a queue, raise an order, recommend a diagnosis, flag a case for review.

This is one of the framework's most practical moves. A single model often supports several capabilities with very different consequences. A customer service agent might draft replies for a human to send, which is low risk, and also issue refunds on its own, which is not. Treating the whole system as one thing forces you to either over-control the harmless part or under-control the dangerous part. Splitting it by capability lets you treat each part on its merits.

For AI agents, each class of tool action counts as a capability.

### Rate each capability with two questions

This is where OAAF gets specific. Each capability gets rated High, Medium or Low using just two questions.

**Question one: human acceptance.** Must a human actively accept this specific output before it takes effect?

Only a positive act counts here: an approval, a release, a click to send. A human being *able* to see the output doesn't count. Sampling a proportion of outputs doesn't count. Being able to step in afterwards doesn't count. The test is whether this particular output waits for a person to say yes.

**Question two: consequence.** If the output is wrong, would the resulting harm either be irreversible before it would normally be detected, or exceed the materiality threshold?

Reversible here has a strict meaning. It means the organisation can fully restore the previous state by itself, without needing a third party's cooperation, before harm actually happens. And crucially, you judge the reversibility of the *consequence*, not of the action. Reordering a work queue can be undone in seconds. The two-hour delay it caused can't.

Put the two answers together and you get the rating:

- No human acceptance, and serious consequence: **High**.
- No human acceptance, but consequence not serious: **Medium**.
- Human acceptance, and serious consequence: **Medium**.
- Human acceptance, and consequence not serious: **Low**.

That's all. Capability Criticality is used in exactly two places: setting the minimum tier for the system and rating findings. The framework is explicit that it shouldn't be stretched into a second tier system. Its job is narrow and it does that job.

Why so simple? Because in testing, the biggest source of disagreement between assessors wasn't the evidence. It was how they rated the capability in the first place. A looser question, such as "does output become action without human review?", lets one assessor say "supervisors review the queue" and another say "nobody approves individual changes". Both are reasonable readings. The two-question test removes that wiggle room. Visibility isn't acceptance. Reversibility is about the outcome, not the button.

### Set the Consequence Tier

The Consequence Tier decides which of OAAF's requirements apply. There are three tiers, judged on three factors:

- **Worst credible harm.** Tier 1 is minor financial or reputational harm. Tier 2 covers operational disruption, material financial loss, or harm to individuals that can be recovered from. Tier 3 is severe or irreversible harm to people, critical services or the organisation.
- **Reversibility.** Easily reversed at Tier 1, reversible with effort at Tier 2, difficult or impossible to reverse at Tier 3.
- **Autonomy.** Easily overridden at Tier 1, meaningful autonomy with a human in the loop at Tier 2, and limited or no practical window to override at Tier 3.

The highest applicable factor wins. And there's one hard rule linking the two scales: a system with any High capability is at least Tier 2.

The tier is a scoping device, not a grade. A Tier 1 system isn't an immature system. It's a system that can't do much harm, so it doesn't need much process.

How much applies? A Tier 1 system needs 8 of OAAF's 36 requirements. Tier 2 needs 25. Tier 3 needs all 36.

### Record the regulatory overlay separately

Legal or sector classification, such as EU AI Act high-risk status or financial, medical or aviation regulation, is recorded on its own line. It adds obligations whatever the tier, but it doesn't set the tier. That's intentional. A system can be Tier 2 by consequence and carry heavy regulatory obligations, or the other way round. Mixing the two together muddies both. Earlier drafts did mix them, and separating them was one of the first fixes I made.

### Draw the decision paths

Finally, for every Medium or High capability, you draw its **Operational Decision Path**:

Input, then AI processing, then AI decision, then *either* human acceptance *or no human acceptance*, then system action, then external consequence.

The "no human acceptance" branch must always be drawn, even if your answer is "this never happens". This sounds like a small formality. It isn't. Drawing that branch is what exposes negative space. In one of the worked examples I'll describe below, every layer of governance in a well-run bank pointed at the branch a human eventually saw. None pointed at the branch where the decision was final. You only notice that when you're made to draw both.

## Operational control states: agreeing in advance what "not right" looks like

One of the clearest lessons from aviation is that you decide what degraded looks like before you're in it. OAAF does this with five operational control states.

- **S0 Normal.** Operating within validated conditions. Standard monitoring. The operating team runs it.
- **S1 Degraded.** Conditions or the assurance margin have deteriorated, but things are still within tolerance. Monitoring and sampling increase. The operating team decides, with the owner informed.
- **S2 Restricted.** Operation is allowed only with added controls, typically by inserting a human acceptance step on the affected capabilities or reducing limits. The accountable owner decides.
- **S3 Contained.** The capability is constrained, isolated or switched to a fallback process, with a controlled recovery. The accountable owner decides, with management informed.
- **S4 Unacceptable.** Carrying on would exceed accepted risk. The affected capability stops. The accountable owner, or anyone else with stop authority, can make that call.

The important thing about these states is that they describe what controls must be in place, not how well the model is scoring. A system can post excellent metrics while in a poor operational state, and the reverse. A fraud model might be scoring beautifully on the transactions it sees while the monitoring that would catch a problem has quietly stopped working.

OAAF requires states to be defined for two things, not one. **Model condition** covers quality, drift and unexpected behaviour. **Service condition** covers availability, latency, stale or missing data, monitoring outages and failures in things the system depends on. For each capability, you have to record what happens when the AI simply isn't available. Does the process fail safe, stopping or holding until the AI comes back, or does it fail open, carrying on without it? Plenty of organisations have never answered that question for systems they rely on every day.

States apply per capability. One capability can be Restricted while others carry on normally. And any capability leaving S3 or S4 has to go through a defined return-to-service process. You don't just switch it back on and hope.

## The 36 requirements

OAAF's requirements sit in seven domains. Each requirement is tagged with the tier from which it applies, and then applies at every tier above. Some are marked as **control-critical**. These are the requirements an organisation needs in order to detect a problem and stop it, and they carry extra weight when it comes to making decisions.

Every requirement was written to pass one test: what specific evidence would make an assessor say yes rather than no? If I couldn't answer that, the requirement was rewritten or removed. Several early requirements failed that test and didn't survive.

I won't list all 36 here, since they're in the full document, but here's what each domain covers and the requirements that matter most.

### P1: Accountability and authority

This domain is about who's in charge and whether they can actually act. It starts with a named individual as accountable owner of the deployed system, which applies to every system, even Tier 1. Higher tiers add documented responsibilities for technical, risk and business roles, an escalation path to senior management, and at Tier 3 a statement setting out what suppliers, model providers and deployers are each responsible for.

The key requirement is P1-05, which is control-critical. It has two halves. The owner must hold documented authority to *initiate* restriction or stopping of any capability. And a mechanism must exist to *execute* that within a response time set for each capability, and it must have been exercised within the review period.

That split exists because of a real problem found in testing. In many organisations, the business owner of an AI system can decide it should stop, but actually stopping it needs IT, a change board, or a vendor. If the stop takes 48 hours to execute on a system that moves money every second, the owner's "authority" is largely theoretical. P1-05 tests both halves separately, and the execution half fails if it's slower than the capability's consequences can tolerate.

### P2: Context, hazards and risk

This covers what could go wrong. At Tier 1 it's just a list of foreseeable misuse and credible failure modes. From Tier 2 it becomes structured hazard identification across model, data, integration, infrastructure, human factors and external dependencies, plus risk assessment using a documented method. At Tier 3 the risk record must be reviewed at least every 12 months, after every material change, and after every significant occurrence.

One detail matters a lot here. Hazard identification must include hazards whose controls are owned by other functions. If the infrastructure team owns resilience, the infrastructure outage hazard still has to appear in this system's hazard log, with the owning function and the interface recorded. I'll explain why under the Boundary Rule below.

### P3: Operational boundaries

This is where the control states come to life. At Tier 1, you document the conditions that would make you restrict or stop the system. From Tier 2, you define the control states for both model and service condition, set measurable triggers for moving between states, and limit the system's technical permissions to what it's declared to do. At Tier 3 you also define who has authority over each transition and log every transition with its rationale.

That permissions requirement, P3-06, was added late, because of AI agents. Agents often run under broad service accounts, which means they can technically do far more than anyone intended. Anything a system can do but hasn't declared has never been rated, so it's never been assessed. P3-06 requires those extra permissions to be removed, or declared and assessed.

### P4: Continuous assurance

This domain covers monitoring. Every system needs operational performance monitored and reviewed by a named person at a defined interval. From Tier 2, safety-relevant indicators must be separated from general performance indicators, and given targets and trigger levels linked to the state transitions in P3.

The requirement I'd point any reader to first is P4-06. For each High capability, monitoring must cover the path where output became action with no human acceptance. That can be done by sampling, outcome tracking or independent checks. It's negative-space assurance turned into something an assessor can test.

At Tier 3, OAAF also asks for **assurance coverage** to be reported using hazard-signal mapping. For each identified hazard, you record whether there's an operational signal that would detect it before harm: fully, partially, or not at all. It's reported as three counts rather than a percentage, which avoids false precision. I'm open about this being an interim method, and I'll come back to its limits.

### P5: Occurrence and learning

Every system needs a channel for reporting problems with its output, and the people who use it need to know how. From Tier 2, occurrences get classified, and anything at the level of a deviation or worse gets investigated with corrective action recorded. At Tier 3, there's a defined return-to-service process for capabilities coming back from S3 or S4, and lessons from occurrences must feed back into the risk record and the change process.

The classification scheme draws directly on aviation occurrence reporting. It runs from an observation (a potentially relevant anomaly), through an unsafe condition (a safety barrier is missing or degraded but nothing has gone wrong yet, for example monitoring has silently stopped), a deviation (the system operated outside expected behaviour), a near miss (no harm, but there could have been), an incident (harm occurred), up to a serious incident. The "unsafe condition" category is particularly useful for AI. Many of the most dangerous moments are when nothing has gone wrong yet, but the thing that would tell you has stopped working.

### P6: Change assurance

Every system needs a configuration baseline good enough to reconstruct the system that produced any given output: the model and version, prompts and instructions, tools and the permissions they used, data and knowledge sources, persistent memory or context stores, and thresholds. And every change needs its operational significance assessed before release, judged by its potential effect on behaviour, boundaries, controls or risk, not by how big it looks technically.

That last point matters. A one-line prompt edit can change an AI system's behaviour more than a major software release. Change management that judges changes by lines of code will miss the changes that matter.

From Tier 2, changes are classified by impact level, from administrative through to changes affecting safety controls. And P6-05 requires external dependencies that can materially change behaviour, such as model providers and third-party data feeds, to be covered by change detection, version pinning, supplier notification, or evidenced compensating monitoring. At Tier 3, behavioural changes and above must be reassessed against the risk record before release.

### P7: Human and AI operation

The final domain covers the people around the system. Every system needs the human roles that receive, accept or act on its output identified. From Tier 2, the risks of both over-reliance and under-reliance must be assessed for each role, and escalation authority and criteria documented. At Tier 3, competency requirements must be current for everyone with authority to intervene, and the framework asks you to assess whether oversight itself is degrading, through workload, alert overload, complacency, or incentives that discourage people from challenging the system.

That last item is easy to underrate. If analysts are measured on how many cases they clear per hour, they have every incentive to accept the AI's recommendation and move on. The oversight exists on paper and fades in practice.

### What isn't a separate domain

Cybersecurity, including prompt injection and manipulation, data integrity, privacy and resilience aren't given their own domains. They show up where they bite: as hazards in P2, as service conditions in P3, and as dependencies in P6. Organisations that already have security and privacy controls should record them as evidenced controls, not duplicate them.

## The decision rules: why OAAF has no score

This is the part of OAAF I'm most confident about, because it fixed a real failure.

Without decision rules, the end of an assessment is an informed impression of a compliance table. Two competent assessors can look at the same table and reach opposite conclusions. In testing, that's exactly what happened. So OAAF turns findings into decisions by rule.

### Assessment values

Each applicable requirement gets one of four values. **Compliant** means the control is defined, in use, and there's a record of it working within the review period (at Tier 1, defined and in use is enough). **Partially Compliant** means it's defined but incomplete, inconsistently applied, or has no record of operation. **Not Demonstrated** means the evidence isn't enough to establish that the control is defined and in use. Note that this doesn't mean the control doesn't exist, only that it hasn't been shown. **Not Applicable** means the requirement is above the system's tier.

The review period is 12 months, or the time since the last material change, whichever is shorter.

### Three evidence rules

**Rule 1: evidenced, not assumed.** A control owned by another function only counts if it's evidenced against *this* system. That means a named owner, a record the assessor has actually seen, and a demonstrated link to this system's decision path. "IT will have a disaster recovery plan" is an assumption. "Vendor management covers that supplier" is an assumption. An assumed control is Not Demonstrated. It can be noted as a candidate compensating control while the evidence is gathered.

**Rule 2: absence of harm is not evidence.** A clean incident record doesn't downgrade a risk nobody has assessed. And it isn't evidence that controls work if the monitoring that would have detected the harm is missing, or nobody knows what it covers. "Nothing has gone wrong" is only meaningful if you'd have known.

**Rule 3: the Boundary Rule.** Any hazard that could affect a capability's decision path must be recorded in this system's hazard identification, even when its control belongs to another function. The record names the owning function and the interface. Recording a hazard isn't a claim to own its control. But a hazard owned somewhere else and recorded nowhere is invisible, and invisible hazards are the ones that catch organisations out.

### Finding criticality, derived rather than judged

Every Partially Compliant or Not Demonstrated result becomes a finding, and its seriousness is worked out by rule:

- A control-critical requirement affecting a High capability: **Critical**.
- A control-critical requirement affecting a Medium capability: **Significant**.
- Any other requirement affecting a High or Medium capability: **Significant**.
- Anything affecting only Low capabilities: **Routine**.

A finding that isn't specific to one capability, such as having no accountable owner at all, takes the rating of the highest capability it affects. An assessor can raise a finding by one level, with written reasons, but can never lower one. There are three levels only. No fourth level, and no numeric score.

### Decisions per capability

Each capability then gets one of three outcomes:

- **Not Ready** if there's any open Critical finding affecting it.
- **Ready with Conditions** if there are Significant findings but no open Critical one. Each condition gets an owner and a date.
- **Ready** if there are only Routine findings, or none.

A Critical finding can only be cleared in two ways. Either there's an evidenced compensating control, meeting Rule 1, or there's a documented, time-limited risk acceptance signed by someone who holds the authority to stop that capability. In the second case the capability becomes Ready with Conditions, with the acceptance listed as one of the conditions.

Neither good intentions to fix things nor a large number of Compliant results elsewhere clears a Critical finding.

That's why there's no percentage score. One missing stop mechanism should never be averaged away by thirty satisfied requirements elsewhere. A score of 90% sounds reassuring. It means nothing if the missing 10% is the ability to stop the system that moves money.

If a capability that's already running is found Not Ready, it should move to S2 Restricted, if a human acceptance step or reduced limits can be added, or to S3 Contained, until the finding is cleared.

### Why per capability matters

Making decisions per capability might look like a technical detail. In practice it's what makes organisations willing to act. "Restrict the auto-approval path, carry on with the review path" is a proportionate decision that a business can actually take. "Stop everything" usually gets argued down to "stop nothing". Giving people a middle option makes it far more likely they'll do something.

### When to assess

A full assessment is needed before first operation and at least every 12 months. Changes classed as behavioural or higher trigger reassessment of the affected capabilities, as does any return to service from S3 or S4. A proposal to retire a system, or evidence that a capability no longer does its job, triggers a retirement decision.

And OAAF runs as a loop, not a gate: define, assess, bound, monitor, detect, intervene, report, investigate, correct, verify, then return, restrict or retire, learn, and back to define.

## Three worked examples

The framework includes three worked examples. All are synthetic, designed to stress different parts of the method rather than drawn from real organisations. Here's what each one showed.

### InboxAgent: an ungoverned enterprise agent

An agent reads incoming customer emails, pulls account and order data, drafts replies, and can issue refunds and reschedule deliveries without human review. Ambiguous cases go to a human queue. It runs on an external foundation model that the provider updates without notice. Monitoring covers uptime and latency only. There's no AI risk record, changes go through normal software release with no behavioural review, and no materiality threshold has been set.

Scoping gives three capabilities. Issuing refunds or rescheduling without review is High: no human acceptance, and because no threshold was set, financial actions count as material by default. Drafting a reply for a human to send is Low. Routing ambiguous cases to the human queue is Medium. The system is Tier 2.

The findings are what you'd expect from a system nobody has really governed. There's no designated owner, just an engineering lead who's the owner by default. The assessor raised that finding to Critical because nobody could say who owned the agent. There are no triggers for restricting refunds. Refunds issued without review are never sampled. The provider's model version isn't recorded, and its silent updates are neither detected nor pinned. And the agent's account can also edit customer records, a capability nobody declared.

The decision: the refund capability is Not Ready and moves to S2, with human acceptance inserted, until triggers and negative-space sampling exist. Drafting replies is Ready with Conditions.

The lesson is that uptime monitoring isn't operational assurance. The sharpest single finding was the invisible provider update: a live, unassessed change to a system that moves money.

### SentryModel: a well-governed fraud system

This example was designed to test something harder. A bank scores every transaction for fraud. Above a threshold, transactions are held for a trained analyst. Below it, they're approved automatically, and no human ever sees them. The bank has a certified AI management system, a model risk function, independent validation, a change board and quarterly committee reporting. On paper, it's doing everything right.

Auto-approval below the threshold is High: no human acceptance, and fraud losses can't be recovered before they're detected. Holding and flagging is Medium, because an analyst decides, but a wrongly released hold still moves money. The system is Tier 3.

The bank was Compliant on 25 of the 36 requirements. It does most of this well. But every remaining finding sat at a **seam between functions**.

The owner could initiate a stop, but executing it needed a change board quorum that took 48 hours or more. Infrastructure outage hazards were left to IT and recorded nowhere. Control states were well defined for model quality, but there was no state or trigger for the scoring service going down, so nobody had decided whether the bank fails open or fails closed if the fraud model is unavailable. All review effort went on held transactions, and auto-approved transactions weren't sampled at all. Third-party device and identity data feeds were managed as general vendors, outside AI change control. And analyst throughput targets created an unassessed incentive to accept the model's score.

The decision: auto-approval is Not Ready and moves to S2, with a lower auto-approval limit and outcome sampling added, until fail-safe behaviour and negative-space monitoring are in place. Hold and flag is Ready with Conditions.

This is the example I'd most want people to remember. A mature management system can still leave the most consequential path, the one where no human looks, almost unexamined. Governance effort follows visibility. OAAF's questions are designed to follow consequence instead.

### Field Operations Agent: an ambiguous capability

The third example tested the hardest open question from earlier drafts: would two assessors rate an ambiguous capability the same way?

A water utility uses an AI agent to support maintenance of its distribution network. It reads sensor alerts and work orders, drafts the weekly maintenance schedule for a supervisor to approve, raises purchase orders for spare parts under 2,000 euros, and continuously reorders the field crews' job queue. Supervisors can see the queue and override it, but don't approve individual changes. Emergency bursts go to a separate control room. The agent uses a third-party model through an API, keeps persistent notes between sessions, and runs under a shared service account. The materiality threshold is 2,000 euros.

Drafting the schedule is Low, since a supervisor approves it. Purchase orders are Medium: no human acceptance, but they're under the threshold and suppliers allow cancellation within 24 hours, checked daily.

The queue is the interesting one. Is there human acceptance? No. Supervisors can see and override the queue, but that's visibility, not positive acceptance. Is the consequence serious? Yes. Reordering is reversible in seconds, but a delayed repair isn't. A leak pushed down the list keeps leaking. So queue reordering is High.

Under the older wording, one assessor could easily have said "supervisors review the queue, so it's Medium" and another "nobody approves anything, so it's High". The two-question test removes that ambiguity.

The findings: the shared service account can also close work orders and edit asset records, neither of which was declared. There's no check on jobs the agent pushed down the queue. Triggers exist for model errors but not for stale sensor data. The agent's persistent notes aren't in the configuration baseline, so past decisions can't be reconstructed. Supervisors have stopped checking the queue order since the agent arrived. And the model version is pinned, but nobody tracks when the provider plans to retire it.

The decision: queue reordering is Not Ready and moves to S2, with a supervisor accepting any change that moves a job down by more than a day, until permissions are reduced and deprioritised jobs are sampled. Purchase orders are Ready with Conditions. Schedule drafting is Ready.

This example also changed the framework. Two elements were added because of it: P3-06, limiting permissions to declared capabilities, and including persistent memory and tool permissions in the configuration baseline.

## Testing whether two assessors agree

A framework that gives different answers depending on who applies it isn't much use. So during development, I assessed the SentryModel case from two deliberately different viewpoints, a strict assessor and a pragmatic one, working from identical evidence.

Under the earlier draft, which had no decision rules, they reached opposite conclusions. The strict view said Not Ready. The pragmatic view said Ready with Conditions.

The reasons were specific. "Authority to stop" was ambiguous, since the owner could initiate a stop that took 48 hours to execute. It was unclear whether hazards owned by other teams belonged in the system's hazard log. Assumed controls ("IT probably has a recovery plan") were treated as evidence. The absence of harm was used to downgrade a risk: automation bias was rated low because nothing had gone wrong yet. And severity was left to judgement, so the same gap was Critical to one assessor and Significant to the other.

Each cause got a fix: the split in P1-05, the Boundary Rule, the evidence rules, and derived criticality. Re-running the contested items under version 1.0, both viewpoints converged on the same findings, the same criticality and the same decision for each capability.

The one remaining dependency was that both assessors had to rate capability criticality the same way to begin with. The two-question test was written to close that gap, and then checked against the ambiguous queue capability in the utility example.

I want to be honest about what this is. It's a design check, done by one author taking two viewpoints. It isn't a trial with independent assessors. That's the next test the framework needs.

## AI agents

Agents don't need a separate framework. They fit the same structure, with a few points of emphasis.

Each class of tool action is a capability and gets its own two-question test. Permissions matter most: agents often run with broad service credentials, so they can do far more than their declared capabilities, and anything undeclared has never been rated. Persistent memory and context stores are part of the configuration baseline, because they change the agent's behaviour without any code or prompt change. And an agent's choices *not* to act, the items it skips, deprioritises or defers, are negative space. When the capability is High, those choices need monitoring too.

That last point is easy to miss. We tend to think about agent risk in terms of what an agent does. Often the bigger risk is what it quietly decides not to do.

## Getting started

### Tier 1 in an afternoon

If your system is low-consequence, OAAF asks for eight things, and in practice that's one afternoon and one page:

1. Complete the System Card: purpose, owner, capabilities, materiality threshold.
2. Run the two-question test on each capability. If any comes out High, you're at least Tier 2, so stop and do a full assessment.
3. List foreseeable misuse and failure modes.
4. Write down when you would restrict or stop the system.
5. Name who reviews performance, and how often.
6. Set up a way for users to report problems.
7. Record the current configuration and start a change log noting the likely effect of each change.
8. List the people who act on the system's output.

If that sounds too basic to be worth doing, try it on a system you already run. Many organisations can't complete point four.

### A full assessment

For Tier 2 and 3, the sequence is: scope the system and agree the tier and criticality with the accountable owner before you collect any evidence; draw the decision paths for Medium and High capabilities, including the no-acceptance branch; collect evidence against each applicable requirement, preferring records of the control actually operating over documents describing it; record findings, applying the three evidence rules; derive criticality; decide per capability; set the control state of anything found Not Ready; and agree conditions, owners and dates, and schedule the next trigger.

### Who should assess

At Tier 1, the operating team can assess its own system. At Tier 2, someone outside the team that runs the system should review the assessment. At Tier 3, it should be carried out by someone independent of both the build and the operating teams, whether internal or external.

### If you already have a management system

Organisations with ISO/IEC 42001, a model risk framework or a working change board will find much of OAAF already in place. Assess what you have against the requirements using Rule 1, and concentrate on the control-critical requirements, negative-space monitoring (P4-06) and external dependency change (P6-05). That's where mature organisations most often have gaps, as the SentryModel example shows.

## How OAAF fits with ISO, NIST and the EU AI Act

OAAF doesn't replace any of these. It sits underneath them, turning their requirements into an operating regime for a single deployed system.

ISO/IEC 42001 sets the management system for AI at organisation level. ISO/IEC 23894 covers AI risk management, ISO/IEC 42005 covers impact assessment, and ISO/IEC TS 8200 addresses controllability. OAAF assumes these may exist and provides the system-level regime beneath them.

The NIST AI Risk Management Framework defines outcomes across four functions: Govern, Map, Measure and Manage. OAAF offers one concrete way to carry out Measure and Manage once a system is live.

For the EU AI Act, OAAF's domains connect to the articles on risk management, human oversight, record-keeping, accuracy and robustness, deployer obligations, post-market monitoring and serious incident reporting. The full document includes an indicative mapping. To be clear, meeting an OAAF requirement doesn't by itself establish conformity with any standard or compliance with any law.

Several 2026 publications cover ground close to OAAF, and they're worth reading alongside it: work on operational deployment assurance, on operationalising agentic AI use cases, on evaluating enterprise agents across control dimensions, on whether agent systems keep enough evidence to answer questions about specific decisions, and on how aviation safety management should treat AI. Ideas such as operating envelopes, escalation states and evidence requirements appear in several of them.

OAAF's contribution isn't any single one of those concepts. It's the combination: an operating regime that runs for the whole life of the system, including occurrence learning, change from external providers and return to service; explicit attention to negative space and the seams between functions; sector neutrality; and decision rules designed so that two assessors reach the same conclusion from the same evidence.

## Limitations, stated plainly

OAAF is version 1.0, and it has weaknesses. I'd rather you knew them now than found them later.

**Reproducibility is designed for, not yet proven.** The decision rules converged two viewpoints in a design check. That's not a field trial. The next test needed is independent assessors applying OAAF to the same real system. Some judgement also remains: whether an organisation's materiality threshold is reasonable (the assessor records it but doesn't replace it), where tier boundaries fall for systems near a threshold, and the line between Partially Compliant and Compliant when records are weak.

**Assurance coverage is measured crudely.** Hazard-signal mapping only counts hazards someone has identified. It says nothing about hazards nobody has thought of. That's why it's reported as three counts rather than a percentage.

**The worked examples are synthetic.** They were designed to stress the framework. Real use will find problems they didn't.

**Some things have deliberately not been built.** There's no maturity model, because no decision in the worked examples needed one. There's no certification scheme, which would first need evidence that independent assessors agree. There's no numeric score. And there's no software tooling beyond templates, a workbook and a rules file.

There's also a rule for future versions, which I've applied to every change since the first draft: new components will only be added when a worked case or real use shows the existing framework can't reach a reliable decision without them, and each addition will cite the finding that justifies it. Frameworks tend to grow by accumulation until nobody can use them. I'd like OAAF to grow only by necessity.

## What's in the release

Alongside the [framework document](../FRAMEWORK.md), the release includes:

- an [online assessment tool](../tool/) that runs in your browser, rates capabilities, shows which requirements apply and produces a decision per capability;
- an [assessment workbook](../downloads/OAAF_v1.0_Assessment_Workbook.xlsx) with the same rules built in, plus templates for the System Card, capability register, findings register and decision record;
- a [machine-readable rules file](../oaaf.json) for tools;
- an open-format [AI assistant skill](../skills/oaaf-assessment/SKILL.md) and an [MCP server](../mcp/), so AI assistants can guide a user through an assessment and apply the decision rules.

Yes, there's something a little recursive about using AI to help assess AI. I think it's also practical: the decision rules are deterministic, which is exactly the kind of thing a tool should apply consistently.

## How you can help

What OAAF needs most is real use. If you apply it to a system, I'd like to hear what happened: where it worked, where it was unclear, where two of your people disagreed, and where it missed something that mattered. You can [report it here](https://github.com/armendverbovci/OAAF/issues/new?template=real-use-report.yml).

The most valuable result anyone could share is two independent assessors applying it to the same system and comparing their answers. To make that easy, I've set up the [Two-Assessor Challenge](../challenge/): a synthetic AI agent case, about 20 minutes of reading, that you assess on your own and submit. Every result goes into version 1.1.

Comments and corrections are welcome by email at armend.verbovci@gmail.com. Later versions will be published under the same record.

If you use or build on OAAF, please cite it as:

Verbovci, A. (2026). *Operational AI Assurance Framework (OAAF), Version 1.0.* Zenodo. https://doi.org/10.5281/zenodo.24352952

## A closing thought

Aviation didn't become safe because aircraft got good at passing tests. It became safe because the industry accepted that passing a test is where the work starts, not where it ends, and built a way of operating around that idea: people with real authority, agreed limits, honest reporting, and the discipline to stop, investigate and come back carefully.

AI is now meeting the same questions. Who's accountable? How would we know if something was wrong? And what happens next?

OAAF is my attempt to give organisations a practical way to answer them for the systems they're already running. It's small on purpose, it's free, and it's open to challenge. If it helps one organisation notice the path where nobody was looking before that path causes harm, it will have done its job.

---

*OAAF is offered as a practical method. Applying it does not establish compliance with any law or standard, and it does not replace sector regulation, legal advice or a competent safety assessment. It was developed independently, in a personal capacity, from public standards and published literature. All worked examples are synthetic.*
