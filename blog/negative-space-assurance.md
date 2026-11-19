---
title: "Negative-space assurance: the AI decisions nobody reviews"
description: "Most oversight of AI systems follows what the system flags. The riskiest path is often the one it quietly lets through. A short essay on negative-space assurance, and how to check for it in an afternoon."
---

# Negative-space assurance: the AI decisions nobody reviews

*Armend Verbovci, November 2026*

Picture a bank that is doing AI governance properly. It has a certified AI management system, a model risk team, independent validation, a change board and quarterly reports to a board committee. Its fraud model scores every transaction. When a transaction looks suspicious, it is held, and a trained analyst looks at it before any money moves.

Now ask a simple question. What happens to the transactions the model *doesn't* find suspicious?

They're approved automatically, and nobody ever looks at them. Not the analysts, whose whole job is the held transactions. Not the model risk team, which validates the model's accuracy on the cases it's shown. Not the committee, which sees the fraud losses that other controls later catch.

That is negative space. It's the part of an AI system's work where output becomes action and no human is looking. In many systems it's where most of the decisions are made, and also where the least attention goes.

## Oversight follows visibility

It isn't carelessness. It's how attention works.

When an AI system flags something, it creates a task. Tasks have owners, queues, targets and dashboards. Organisations are very good at managing tasks, so the flagged path gets reviewed, measured and audited.

The unflagged path creates nothing. A transaction that's approved automatically doesn't land in anyone's queue. A customer email the agent decides not to escalate doesn't appear anywhere. A maintenance job the scheduling agent quietly moves down the list doesn't set off an alert. Each of these is a decision with consequences, but none of them is visible as a decision.

So "human oversight" often turns out to mean human oversight of the cases the AI picked out for humans. When the AI is wrong in the other direction, by letting something through, ranking it lower or staying silent, the oversight never gets involved.

## Why it matters more than it seems

There are three reasons this blind spot is more dangerous than it looks.

**The volumes are lopsided.** In most deployed systems, the automatic path handles far more decisions than the reviewed one. A fraud model might hold one transaction in a thousand. A triage agent might escalate one email in twenty. If you only check the reviewed path, you're checking a small, unrepresentative slice of what the system does.

**The errors are silent.** A wrongly flagged case gets corrected, because someone looks at it. A wrongly passed case usually doesn't. Its harm turns up later, somewhere else, if it turns up at all: as a fraud loss traced weeks afterwards, a complaint, a repair that came too late. By then nobody connects it to the AI's decision.

**Good figures hide it.** The model's performance metrics usually come from labelled data or from cases people reviewed. If nobody ever reviews the automatic approvals, any errors in them never become data. The dashboard stays green because it's measuring the part of the system that's being watched. A clean incident record means very little if nothing was in place to notice an incident.

## A useful habit: draw both branches

The most practical fix I know is also the simplest. For every capability that matters, draw the path from input to real-world consequence, and draw both branches:

> Input → AI processing → AI decision → **human acceptance** *or* **no human acceptance** → system action → external consequence

Draw the "no human acceptance" branch even if you think the answer is "that never happens". Forcing yourself to draw it is the point. In the bank example, every layer of governance pointed at the first branch. When the second branch is drawn on the same page, the gap is obvious.

Agents add a twist. An agent's choices *not* to act are negative space as well: the items it skips, defers or deprioritises. A scheduling agent that pushes a water leak down a repair queue hasn't taken any visible action. It has simply reordered a list. But a repair that gets delayed can't be undone, even though the reordering could be.

## Visibility is not acceptance

One trap needs naming. People often say a path is overseen because a human *could* see it: the queue is visible, the transactions are on a report, a supervisor can always override. That isn't oversight of the decision. It's the theoretical possibility of noticing.

The test I use is strict. A human has accepted an output only if they took a positive action on that specific output before it took effect: an approval, a release, a click to send. Being able to see it doesn't count. Sampling some outputs doesn't count. Being able to step in afterwards doesn't count. Under that test, a lot of systems described as "human in the loop" turn out to have no human in the loop at all for most of what they do.

## How to check your own system in an afternoon

You don't need a programme to find out whether you have a negative-space problem. Pick one AI system and work through these five questions.

1. **What can it cause to happen?** List the actions, not the model: approve, send, reorder, raise, decline, skip.
2. **For each action, does a person positively accept each output before it takes effect?** Visibility, sampling and override don't count.
3. **Where the answer is no, would an error be irreversible before you'd normally notice it, or above the level your organisation treats as material?** Judge the consequence, not the action.
4. **For every action where both answers point to risk, what checks the decisions nobody reviewed?** Look for random sampling of automatic outcomes, outcome tracking, or an independent check, and for records showing it actually happened.
5. **If that check stopped tomorrow, how long would it take anyone to notice?**

If question four gets a blank look, you've found your negative space. If question five gets a long answer, you've found a second problem: the check exists, but nothing makes sure it keeps running. In one worked case I built, a fraud team's post-payment sampling had quietly been skipped for three months of the year because of workload, and nothing flagged it.

## What good looks like

The controls themselves aren't exotic. They are:

- **random sampling of the automatic path**, sized to the volume and consequence, with records kept;
- **outcome tracking**, following automatically approved cases forward to see what actually happened to them;
- **independent checks**, where a separate process or team tests a sample of decisions against ground truth;
- **trigger levels**, so that what sampling finds can actually move the system into a restricted state, rather than just appearing in a report;
- **a stop that works**, so that when the automatic path needs restricting, someone has the authority and the means to do it within a time that fits the risk.

None of this is new to safety-critical industries. Aviation has spent decades learning that the dangerous moments are often the quiet ones, where a barrier has quietly failed and nothing has gone wrong *yet*. AI systems now make high volumes of quiet decisions, and the same lesson applies.

## Where this comes from

Negative-space assurance is one of the nine principles of the [Operational AI Assurance Framework (OAAF)](../), a free, open method for deciding whether a deployed AI system or agent should keep operating, be restricted, or be stopped. In OAAF, the two-question test above sets each capability's criticality. For every High capability, requirement P4-06 asks for monitoring of the path where output became action with no human acceptance.

If you'd like to try it on a system, the [online assessment tool](../tool/) runs in your browser. The [introduction to OAAF](introducing-oaaf.md) explains the whole framework. And if you want to test your judgement against other people's, the [Two-Assessor Challenge](../challenge/) gives you a synthetic AI agent case that's full of negative space.

*OAAF v1.0 by Armend Verbovci, CC BY 4.0. [DOI 10.5281/zenodo.24352952](https://doi.org/10.5281/zenodo.24352952).*
