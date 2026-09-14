#Astra's plans got too heavy during development, so we worked out some planning rules [Visit](https://www.reddit.com/r/OpenaiCodex/comments/1w967sn/astras_plans_got_too_heavy_during_development_so/)
### **Subreddit:** [r/OpenaiCodex](https://www.reddit.com/r/OpenaiCodex)
### **Author:** [TheBanq](https://www.reddit.com/user/TheBanq/)
### **Vote:** 32
---
After some long and intense development sessions, on several projects basically non-stop since release (including long planning sessions, usually 4 rounds with fresh context), I've got some learnings.
FYI: After 10h+ Sessions and a few major milestones, I asked Astra for a review of the plan, after it had implemented large parts of it.
What could be better, how was the plan written etc. – I then let it discuss improvements with the last agent, that had been working on it, to work out some points for future plan writing.
The main point as always is, the development is too heavy, too much testing, even though I really tried to trim down on it during many revision rounds of the specs + plan.
Here's the ruleset, I personally will build a skill from this, you can use the information however you like.
(Planned with Astra xHigh, implemented with Astra High)
The following is the last response after discussion over it for a while:
AGENT:
**We have agreed on a shared version.** The agent in “Siteplane Plan Check” explicitly confirmed it; there are no unresolved substantive disagreements. No files or existing plans were changed during the discussion.
Our shared principle is:
This gives us **eight core rules**:
- **Describe the outcome and completion criteria clearly.** The plan specifies observable behavior, scope, and relevant boundaries. It must be clear when the task has been sufficiently completed. Required product behavior is distinguished from suggested implementation methods.
- **Match the depth of planning to the risk.** Small changes get short plans. Large pieces of work are divided into independently verifiable outcomes. A functional batch, an acceptance milestone, and a chat session do not have to be the same size.
- **Choose the least expensive check that provides reliable evidence.** Development checks, targeted boundary checks, and overall acceptance are available levels of verification. Not every task needs all three. Uncertain integration assumptions are checked early; the delivered scope receives an appropriate, connected acceptance check.
- **Justify every additional expensive check.** It must cover a relevant risk that cheaper existing checks do not adequately address. Existing tests and tools take priority. New testing infrastructure is treated as a separate cost and needs a concrete benefit.
- **Repeat verification based on the actual impact of changes.** Previous evidence remains valid for the version it tested. Whether it applies to a changed version is assessed against changes to code, dependencies, builds, configuration, and environment. Affected boundaries are checked again; unclear effects require broader checking. A short explanation is normally sufficient.
- **Diagnose failures before repeating expensive runs.** Distinguish product bugs, test harness bugs, infrastructure problems, and missing access. Another long run needs a reason to expect success. Recurring failures lead to targeted investigation. Within the assignment, the agent improves its approach autonomously; it must not silently reduce agreed outcomes or security requirements.
- **Keep evidence concise and store it durably.** Existing reports plus a short record linking the tested version, check, result, and limits of the evidence are normally sufficient. Additional artifacts are saved only when they help. This should not turn into a separate evidence-management platform.
- **Reviews must simplify the plan and have a stopping point.** Reviews resolve concrete uncertainties, contradictions, and relevant gaps in verification. They also remove duplication and outdated requirements. Settled decisions are reopened only when there is new information. Newly discovered, real security issues can still be examined at any time.
**We explicitly included several important qualifications:**
- A deliberately failing baseline is not a general requirement for every new feature. A targeted regression test is usually useful for bug fixes; explicitly agreed requirements for a failing baseline remain binding.
- File names and change size do not determine risk. An operational installation guide can change product behavior even though it is “just documentation.”
- An assertion that was never reached, or was too weak, does not provide valid evidence. After correcting it, the affected behavior must actually be checked.
- Functional acceptance and success-rate measurement are separate activities. When measuring success rates, successful retries must not replace the original failed attempts.
- There is no universal test-to-code ratio, blanket time limit for a batch, or automatic requirement to run complete test matrices.
**This is how the skill should be structured:**
Proposed name: `efficient-implementation-plans`.
Initially, **one short** [`SKILL.md`](http://SKILL.md) is sufficient, containing its scope, the core rules, a flexible workflow, and three final questions:
- Is it clear when the implementation is finished?
- Does every expensive requirement provide a distinct benefit?
- Can the implementing agent choose an equivalent, less expensive approach?
The skill applies when creating, reviewing, or revising implementation plans. Discussions remain discussions. Relevant rules for reruns and diagnosis must then appear in the respective plan itself, so the implementing agent can find them there.
For the initial quality check, a few thought-through examples are sufficient: a small copy change, operational instructions, a package release, concurrent saves, a permissions change, and success-rate measurement. No additional scripts or testing infrastructure are initially planned for this.
**The agreement therefore covers both better verification strategies and limits on the planning process itself.** That combination is intended to prevent each additional review from making the plan heavier.
---
## Comments 12

- by [unknown](#) **&#x21C5; 3**
  <br/> Few questions

How does it know the risk and how is risk defined?

How does it know to chose the least expensive check and how is expense calculated? How does it measure an expensive run?

How do you define the stopping point. What satisfies it?

- by [unknown](#) **&#x21C5; 1**
  <br/> Not the author, but I have had to answer these three for my own plan template, and the only answers that survived contact were mechanical.

Risk: the plan names the invariants for the area it touches, auth paths, migrations, money, anything with a rollback cost. A step that touches one is high risk, everything else is not. It is a list, not a judgement call.

Cheapest sufficient proof: one line of budget at the top of the plan, for example "smoke only unless a listed invariant is touched". eddzsh said the same thing above and is right that a rule with no number attached gets ignored.

Stopping point: the plan carries a Non-Goals section, and a review is finished when there is no open question that sits inside the scope and outside the Non-Goals. Reviews grow forever because nothing says what the change is not for.

If you paste the scope of one plan in a paragraph I'll draft the Non-Goals and invariants block for it here.

- by [unknown](#) **&#x21C5; 0**
  <br/> This is all heavily discussed in the creation of the Specs and Implementation plan.

Note I spend probably 5-10 nonstop hours working on the specs, discussion, cutting stuff, thinking about stuff, correcting things etc. – Since I really want those to be as clean as possible, without over engineering and without forgetting stuff.

Then I build the implement plan from this, to satisfy those specs.

- by [unknown](#) **&#x21C5; 2**
  <br/> Thanks, i tightened it up a bit and added it to my global AGENTS.md.

I had similar instructions to the effect that the amount of testing has to correlate to the degree of criticality of the function in question.

- by [unknown](#) **&#x21C5; 2**
  <br/> Check my other reply, I would recommend making it into a skill, since not every session will need to build implementation plans

- by [unknown](#) **&#x21C5; 2**
  <br/> The rule that usually fails in practice is "justify every expensive check" with no number attached. I put a one-line budget at the top of the plan (smoke only, unless auth or payments change) and Astra stops inventing a second test harness mid-session.

- by [unknown](#) **&#x21C5; 2**
  <br/> Hot take: most of the tests LLMs write are slop. I tell it to not write tests unless I specifically ask for them.

- by [unknown](#) **&#x21C5; 3**
  <br/> I started doing that in the past couple of months as well

- by [unknown](#) **&#x21C5; 2**
  <br/> Holy wall of text!

- by [unknown](#) **&#x21C5; 1**
  <br/> effient-implementation-plans skill:

---

name: efficient-implementation-plans

description: Write, review, or revise software implementation plans with bounded scope, risk-based verification, and explicit rerun rules. Use for implementation planning and reviews of planning or testing overhead, not ordinary coding without a planning request.

---

# Efficient Implementation Plans

Make the requested outcome reliably achievable with proportionate product, planning, and verification effort. Every additional requirement, abstraction, test, or supporting system needs a concrete benefit for the current goal.

## Scope and authority

Match the requested action: discussion, review, drafting, or editing. Discussion and review alone do not authorize file changes, skill installation, implementation, or changes to project rules. Follow existing project contracts; this skill does not authorize silently dropping agreed gates. Propose changes to binding outcomes, scope, or safety requirements for the user's decision. Make routine implementation and verification choices autonomously within the authorized scope.

## Core rules

  1. **Define an observable finish.** State the delivered behavior, scope, relevant dependencies, and sufficient acceptance criteria. Separate binding outcomes and safety boundaries from suggested implementation details. Do not turn “robust” or “production-ready” into an unbounded list of hypothetical requirements. Prefer the simplest design that fully meets the current goal.
  2. **Scale detail to risk.** A small change needs a small plan. Split substantial work into independently verifiable outcomes with clear dependencies. Product batches, acceptance milestones, and chat sessions may have different boundaries; preserve explicit user constraints. Avoid speculative abstractions, universal task forms, and repeating every planning field for every small step.
  3. **Choose the cheapest sufficient proof.** Development checks, targeted boundary checks, and coherent end-to-end acceptance are available layers, not three mandatory steps for every task. Select them by actual failure risk. Check uncertain integration assumptions early. Use real browsers, services, or execution environments where simulations cannot establish the required behavior. A prepared fixture proves only its declared boundary, not the fresh entry path it bypasses. Prefer a focused regression for bug fixes; a costly red baseline for a new feature requires a concrete purpose or explicit contract.
  4. **Justify expensive tests and new infrastructure.** Ask what plausible incorrect implementation the proposed test would catch that cheaper existing checks would miss. Choose variants for distinct risks and interactions, not an automatic Cartesian product of platforms, providers, and scenarios. Reuse existing tests and tools. Make substantial new harness work visible as its own cost; do not hide a new testing system under “add tests.”
  5. **Rerun according to impact.** A result remains evidence for its tested artifact; assess its applicability to the delivered state using relevant source, dependencies, packaging, build, configuration, and environment changes. Renew affected proofs and explain reuse briefly. Investigate uncertain impact and broaden verification where needed. New package bytes require relevant checks of the actual deliverable, not automatically every previous live test. A reporter or selector change preserves unrelated evidence only if entry, fixtures, assertions, and success detection remain valid. Unreached or previously inadequate assertions remain unproven. Final evidence must collectively cover the delivered state.
  6. **Diagnose before expensive repetition.** Classify failures as product, harness, infrastructure/external service, or access problems from the first failure. Another expensive run needs a concrete hypothesis, relevant correction, or changed prerequisite. A transient failure may justify a bounded retry. Repeated causes require investigation at the smallest reproducible boundary. Reassess the strategy when new infrastructure or repeated full runs add effort without new confidence. Improve the method autonomously and communicate material deviations; do not introduce automatic work stoppages or permission loops.
  7. **Keep evidence durable and small.** Prefer existing reports with a short association of tested state, command/check, result, and material limits. Record failure category and cleanup when relevant; retain screenshots or logs only when useful. Store important evidence durably from the first run instead of reconstructing temporary output later. Do not create a separate evidence platform or comprehensive dependency ledger. Distinguish functional acceptance after a fix from reliability measurement: preserve an agreed corpus, sample, failures, and retries when measuring success rates. Successful retries do not replace original measurements.
  8. **Make reviews subtractive and finishable.** Resolve actionable ambiguities, contradictions, and relevant coverage gaps; remove redundant obligations and obsolete assumptions. A new mandatory requirement needs a current goal or concrete risk. Reopen settled decisions only with new information, including real new security findings. Stop reviewing when implementation-relevant decisions and acceptance are clear. Do not launch repeated whole-plan audits or additional reviewers without a specific unresolved question.

## Working approach

- Read the relevant request, existing contracts, and targeted implementation context. Avoid broad audits without a question they need to answer.

- Identify the smallest complete outcome, consequential risks, and independently verifiable steps. Assign only the necessary checks. For costly checks, include the important reuse, rerun, and diagnosis conditions in the plan itself so the implementing agent can follow them without loading this skill.

- Inspect actual effects rather than filenames or line counts. Editorial text normally needs no product run; executable documentation or agent instructions can change behavior. A one-line authorization change can affect many actors and require broad checks.

- Remove duplicate requirements and proofs. Return the discussion, findings, draft, or edits in the user's requested form. State material assumptions or unresolved decisions without inventing a new approval process.

Before finishing, ask:

- Is it clear when the implementation is sufficiently complete?

- Does every expensive obligation provide distinct value?

- Can the implementer choose an equally reliable, cheaper method within the agreed contract?

Do not impose universal test-to-product line ratios, batch time limits, red baselines, full test matrices, or prescribed document lengths. Use unexpected effort as a signal to reassess decisions, not as a reason to weaken required outcomes.

- by [unknown](#) **&#x21C5; 1**
  <br/> Not to shit on your plans, I can see you've put effort into that but you're treating an LLM like it has judgement.

It doesn't. So it compensates for the planning not having solid directives by running shitloads of tests.

It needs something solid to utilise & you will get better results.

Something like the following, treat it as a descending ladder will give you much less churn and keep the LLM more focused.

Behaviours & systems you want. (Check to make sure that pre-existing systems don't already exist, codebases can really surprise you, even your own from a few months ago)

Contracts & invariants of those systems.

Implementation plan.

Check the Implementation plan against the reality of the codebase.

The really big one that I see very few people talk about and they really should: split up the Implementation plan by authority boundaries.

Important step for avoiding over engineering. Plan a testing regimen here. I found that with 5.6 it would never run the whole system and come up with some half broken shit that's been so thoroughly tested and protected that you can't change anything or the whole project blows up. I haven't used astra as of yet, but I'd expect more of the same. Recursive reasoning doesn't change the RL training regimen.

Then finally implement in stages. Because the plan has been split by authority boundaries it should be dramatically easier to see which stages have done what & the LLM should have a much better idea of where to go & what to test.

N.b. because of the RL training that openai utilises, it WILL overengineer the shit out of your plans if you don't specify what you want.

As soon as I see that it's hashed something, that's a red flag for me like "alright stop implementation, first, reread this stage of planning & tell me what has been missed".

I find this system to be pretty effective. Unfortunately I haven't found a way to automate it effectively because it makes thinking at the wrong abstraction pretty obvious. And boy howdy, do llm's so very often "think" aka pattern match at the wrong abstraction level on the regular.

Good luck out there :)

- by [unknown](#) **&#x21C5; 0**
  <br/> I created implementation plans for each slice of an implementation as I usually would for any other model, and provided my usual workflow prompt to Astra before going to bed so it could use most of my remaining before my weekly reset.

When I woke up, Astra had used 1/3rd of my weekly Pro x5 quota AFTER the reset and had not even made it through half of the FIRST implementation slice. It decided to ignore my planned workflow units and split each slice into 100 tiny steps applying the full workflow intended for each slice to every tiny step.

My workflow and prompts are specifically designed to guard against Sol's insane over-engineering, but this thing has taken over-engineering of workflows to a whole new level.
