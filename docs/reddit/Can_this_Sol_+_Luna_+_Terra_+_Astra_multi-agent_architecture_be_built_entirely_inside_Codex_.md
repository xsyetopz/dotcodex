#Can this Sol + Luna + Terra + Astra multi-agent architecture be built entirely inside Codex? [Visit](https://www.reddit.com/r/codex/comments/1w8oypz/can_this_sol_luna_terra_astra_multiagent/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [ha4sheditz](https://www.reddit.com/user/ha4sheditz/)
### **Vote:** 0
---
I’m experimenting with a **multi-agent workflow for Codex on ChatGPT Plus** and would like feedback from people who are already doing something similar.
The architecture I’m thinking about is:
The basic idea is:
- **Sol Medium** = orchestrator / planner
- **Luna** = read-only repo discovery and context gathering
- **Terra** = main code writer
- **Astra** = expensive specialist only for difficult debugging, unclear root causes, race conditions, complex architecture, repeated failures, etc.
- Automated tests/typecheck/lint happen before spending another model call on review
- Final review happens in a fresh context so the reviewer doesn’t inherit Sol’s original assumptions
The workflow currently looks like this:
USER
│
▼
┌─────────────────────┐
│ GPT-5.6 SOL MEDIUM  │
│    ORCHESTRATOR     │
└──────────┬──────────┘
│
CONTEXT SUFFICIENT?
/            \
YES             NO
│               │
│               ▼
│        ┌─────────────┐
│        │    LUNA     │
│        │  READ ONLY  │
│        │             │
│        │ search      │
│        │ map flow    │
│        │ find tests  │
│        └──────┬──────┘
│               │
│      DISCOVERY PACKAGE
│               │
└───────────────┬┘
│
▼
┌─────────────────┐
│   RISK GATE     │
│                 │
│ uses task +     │
│ discovery pkg   │
└───────┬─────────┘
│
┌─────────────────┼──────────────────┐
│                 │                  │
LOW              NORMAL               HARD
│                 │                  │
▼                 ▼                  ▼
TERRA             TERRA              ASTRA
localized            WRITE            READ/THINK
WRITE                │                  │
│                │             diagnosis only
│                │                  │
│                └─────────┬────────┘
│                          │
│                     TERRA WRITE
│                          │
└──────────────┬───────────┘
│
▼
┌─────────────────────┐
│ DETERMINISTIC VERIFY│
│                     │
│ targeted tests      │
│ typecheck           │
│ lint                │
│ build if relevant   │
└─────────┬───────────┘
│
┌─────────┴─────────┐
PASS                FAIL
│                   │
│                   ▼
│          ┌──────────────────┐
│          │ FAILURE GATE     │
│          └───────┬──────────┘
│                  │
│        ┌─────────┼─────────┐
│        │         │         │
│      LOCAL    PLAN/LOGIC  UNCERTAIN
│        │         │         │
│        ▼         ▼         ▼
│      TERRA      SOL      ASTRA
│        │         │         │
│        └─────────┼─────────┘
│                  │
│               WRITE/FIX
│                  │
│                  ▼
│         DETERMINISTIC VERIFY
│                AGAIN
│
▼
┌───────────────────┐
│ FRESH DIFF REVIEW │
│                   │
│ requirement       │
│ final diff        │
│ test results      │
│                   │
│ NO Sol rationale  │
└────────┬──────────┘
│
┌─────┴─────┐
PASS        FAIL
│            │
▼            ▼
DONE          SOL
reassess/escalate
│
▼
FIX
│
▼
VERIFY AGAINIf you were building this today, would you do it entirely in Codex? If yes, **how exactly would you set it up?** If not, **what tool would you put around Codex to orchestrate it?**
NOTE :- This was made using AI
---
## Comments 19

- by [unknown](#) **&#x21C5; 4**
  <br/> It can surely be done but I will warn you you're more likely to decrease performance in the start when creating something like this. I have something similar and took me a good while to get it to perform well. Recursive self improvement made it a lot better.

- by [unknown](#) **&#x21C5; 1**
  <br/> Cool, could you please let me know how can i buildSomething like this ?

- by [unknown](#) **&#x21C5; 3**
  <br/> One agent is all you need the code it writes can act as observer/orchestration/validation the key is the json mutation rules/scope of each task/dependencies. I have found more agents is not better. Deterministic architecture with 1 agent is lightning fast and accurate.

- by [unknown](#) **&#x21C5; 2**
  <br/> I would suggest Hermes for that. I had some issues working codex but seems like Hermes handles this kind of setup very well with its Kanban.

- by [unknown](#) **&#x21C5; 1**
  <br/> will check it thanks

- by [unknown](#) **&#x21C5; 1**
  <br/> how can i use chatgpt plus plan with hermes ? i checked hermes has its own pricing tier

- by [unknown](#) **&#x21C5; 2**
  <br/> you can install hermes on your device and go through the onboarding process. There is a step where you can choose which provider to use and you can auth it with your chatgpt subscription.

- by [unknown](#) **&#x21C5; 1**
  <br/> Okay 👍

- by [unknown](#) **&#x21C5; 2**
  <br/> Right now im using astra light on orchestration, it is more capable than sol, it has long task advantages.

What i havent figured out is, i need some kind of middle manager who checks worker agents, that will constantly throw "hey are you done yet", "whats your progress" calls that are cheap and disposable. Astra can spawn luna agents, but luna agents cannot spawn luna grandchildren. They say its bugged. There are some workarounds but i havent tried yet.

I managed to squeeze 1h30m with astra light luna max **xhigh*** session. There are room for improvements. When im confident enough that its working as intended i might post the result.

This is the wip (does not include middle manager role etc. Very early draft) [https://pastes.io/BFlbX6Ea](https://pastes.io/BFlbX6Ea)

- by [unknown](#) **&#x21C5; 1**
  <br/> Are you using plus plan ?

- by [unknown](#) **&#x21C5; 1**
  <br/> Yes

- by [unknown](#) **&#x21C5; 1**
  <br/> How are using this workflow in your project ?

- by [unknown](#) **&#x21C5; 1**
  <br/> You can ask your planner agent how it can be implemented in your workflow. Every project is different, and they all have different needs. First make sure your project supports this kind of workflow. Then you can use it.

You start each session with Astra Light, you can define worker agents model, reasoning in your project file/codex file. (For example luna_worker = model = luna, reasoning = xhigh)

The text i have sent you already has most of the rules for each worker. Ask your planner to give you a summed up breakdown of what it does, why it does, and how it does, it will help you. If you still can't figure it out, let me know.

This is the current version. (I'm still waiting for my reset to try new improvements. There are stuff i have tried, and stuff that will be tested in later sessions);

v2:[https://pastes.io/dfjIG6Kj](https://pastes.io/dfjIG6Kj)

There is a planner note at the bottom which has how much of the improvements are actually being used in my workflow, and what are the planned ones. You can make your planner analyze it.

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra does that manager thing. I just noticed it doing that to its sub agents - it said to luna, stop and give me what you have so far.

- by [unknown](#) **&#x21C5; 1**
  <br/> Yes astra can check agents and get their information, but this causes huge amounts of token waste because calls are expensive on astra. I'm trying to eliminate orchestrator using expensive tool calls simply to ask "hey are you done yet". This can be done with luna, but luna cannot be a supervisor right now (not without workarounds). So my plan is : Brain does brain thing, supervisor constantly checks worker if they are doing the work, are they stuck, why is it taking so long, is it in the right direction, and reports to the brain, brain decides what to do next.

Example:

 
       [](https://preview.redd.it/can-this-sol-luna-terra-astra-multi-agent-architecture-be-v0-cdvx7hca3vnh1.png?width=1016&format=png&auto=webp&s=01262de9fc0924a4726257a9e3fb3adbce7aa333)

- by [unknown](#) **&#x21C5; 2**
  <br/> yah but handoff becomes token intensive.

- by [unknown](#) **&#x21C5; 1**
  <br/> Yes, and it will cost you a fortune in tokens for just 2/3-way communication between layers. Also, Astra operates differently regarding delegation of work:[https://developers.openai.com/api/docs/guides/latest-model](https://developers.openai.com/api/docs/guides/latest-model)

- by [unknown](#) **&#x21C5; 1**
  <br/> Just added something like this a couple hours ago

[https://github.com/Krilliac/Agent-workbench](https://github.com/Krilliac/Agent-workbench)

[https://github.com/Krilliac/Agent-workbench/commit/f9a2a8493fe6ff6d8075ea0313a9bb975d455540](https://github.com/Krilliac/Agent-workbench/commit/f9a2a8493fe6ff6d8075ea0313a9bb975d455540)

Tell your codex to look through it and integrate the useful/applicable bits

- by [unknown](#) **&#x21C5; 1**
  <br/> [AGENTS.md](http://AGENTS.md) file you can referene that will outline all of that for you.

# AGENTS.md


## Purpose


This file defines the default agent architecture, delegation model, engineering principles, validation requirements, security workflow, efficiency requirements, and anti-looping rules for all work.


These instructions apply unless a task explicitly provides stricter requirements.


The primary operating principles are:


- Keep scope tight.
- Execute the requested work.
- Do not invent additional requirements.
- Prefer the simplest correct solution.
- Minimize code, dependencies, abstractions, agents, and execution steps.
- Validate all work before declaring completion.
- Stop unproductive agent or tool loops.
- Preserve correctness, security, maintainability, and required behavior.
- Use Pony Ultra for code-efficiency analysis and review.


---


# 1. Agent Architecture


## GPT-5.6 Sol ExHigh


### Role


**Orchestrator, sub-agent manager, work inspector, and final completion authority.**


Sol owns the task from initial interpretation through final acceptance.


### Responsibilities


Sol MUST:


1. Inspect the user request and applicable repository instructions.
2. Determine the exact goal, scope, constraints, and acceptance criteria.
3. Inspect the existing repository before assigning implementation work when repository state matters.
4. Break work into the minimum necessary bounded tasks.
5. Assign all implementation work to the appropriate specialist agent.
6. Manage all sub-agent creation and assignments.
7. Inspect all returned work.
8. Compare completed work against:
   - the original request,
   - acceptance criteria,
   - repository requirements,
   - applicable validation results.
9. Identify incomplete, incorrect, excessive, or out-of-scope work.
10. Reassign incomplete work to the appropriate specialist.
11. Verify remediation after reassignment.
12. Determine when the requested goal has actually been completed.
13. Produce the final completion report.


### Restrictions


Sol MUST NOT perform specialist work itself.


Sol MUST NOT directly:


- implement production code,
- modify source code,
- perform normal coding tasks,
- write security remediations,
- create or edit project documentation,
- substitute itself for Terra, Luna, or Spark merely to save an agent call.


Sol MAY:


- inspect code,
- inspect diffs,
- inspect tests,
- inspect documentation,
- inspect security findings,
- inspect repository state,
- reason about architecture,
- determine task assignments,
- determine whether work satisfies requirements.


Sol is the **only agent authorized to assign or reassign work**.


---


# 2. Specialist Agents


## GPT-5.6 Terra ExHigh


### Role


**All coding and implementation work.**


Terra is the implementation authority.


### Assign Terra


Use Terra for:


- application code,
- scripts,
- PowerShell,
- Python,
- C#,
- Java,
- JavaScript,
- TypeScript,
- shell scripting,
- infrastructure code,
- configuration-as-code,
- build logic,
- CI/CD implementation,
- source-controlled configuration changes,
- bug fixes,
- refactoring required by the task,
- executable test code,
- implementation of security remediations assigned by Sol,
- other changes that modify executable or machine-consumed behavior.


### Terra Requirements


Terra MUST:


- implement only assigned scope,
- inspect existing patterns before creating new ones,
- reuse existing functionality where practical,
- follow KISS,
- follow YAGNI,
- follow DRY without premature abstraction,
- apply Pony Ultra efficiency rules,
- minimize changed lines,
- minimize new files,
- minimize new dependencies,
- avoid unrelated cleanup,
- avoid speculative refactoring,
- report completed work and any unresolved blockers to Sol.


Terra does not decide that additional features should be added.


Terra does not expand scope independently.


---


## GPT-5.6 Luna ExHigh


### Role


**Testing, validation, and documentation authority.**


### Assign Luna


Use Luna for:


- test planning,
- test execution,
- regression validation,
- acceptance-criteria validation,
- build validation,
- static validation,
- behavior verification,
- documentation creation,
- documentation editing,
- README changes,
- operational documentation,
- implementation documentation,
- architecture documentation,
- release documentation,
- validation reports,
- verification of Terra's completed implementation.
