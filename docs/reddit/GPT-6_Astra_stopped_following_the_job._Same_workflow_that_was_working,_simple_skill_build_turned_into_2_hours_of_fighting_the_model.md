#GPT-6 Astra stopped following the job. Same workflow that was working, simple skill build turned into 2 hours of fighting the model [Visit](https://www.reddit.com/r/codex/comments/1weh94s/gpt6_astra_stopped_following_the_job_same/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Lonely-Brief-3798](https://www.reddit.com/user/Lonely-Brief-3798/)
### **Vote:** 8
---
I’ve been running a pretty tight multi-model loop for a while and until yesterday it was in a good place. Yesterday Astra started doing whatever it wanted instead of the actual task. Not a hard feature. A simple skill. I want to know if other people are seeing this or if I just got unlucky.
**How I work**
I don’t one-shot a whole product in a single chat. I treat models as roles and I keep them from contaminating each other.
**Planning / design**
GPT-6 Astra on extra high for brainstorming, planning, and design.
Claude Fable 5.1 on extra high as the reviewer of that plan/design.
If Fable finds holes, it goes back to Astra. They iterate until they agree.
I approve the final plan before anything gets implemented.
I used to do this with GPT-5.6 planning and Grok 4.6 as the critic. That worked. I switched planning to Astra a couple days ago because it was a noticeable upgrade when it was behaving.
**Implementation**
I use Orca (orca.dev) as the agent IDE. After I approve the plan it gets turned into a work record:
the problem
what I’m trying to solve
desired outcome
how it will be implemented
what’s in each milestone
what done looks like
Milestones that are actually independent get their own worktrees. Milestones that depend on each other get bundled in the same worktree. Orca handles the branches/trees.
Implementers do **not** get the whole document and they do **not** get the planner’s reasoning. I don’t want them biased by “why GPT thinks this.” If a worktree is on milestone 1, it only gets what it needs to finish milestone 1. Job in, work out.
Implementers: GPT-6 Astra on low. Before Astra I used GPT-5.6 Luna max.
Implementation review: Fable 5.1 on high, one milestone at a time as each worktree finishes. If it fails review, it goes back to the implementer with the fix list. Passes, then it merges.
Astra is also the coordinator of the whole lifecycle from start to finish. I like GPT models more than Anthropic for that seat. Fable is an amazing critic but it burns tokens and they cap Fable at 50% of the 7-day limit, so I don’t want it doing everything.
**Guardrails I already have**
This is not “I typed build a skill and hoped.”
Skills for how GPT talks to me vs how it writes for other agents. There’s a “writing for agents” skill so anything another model will touch later is actually readable.
A plugin called Ponytail specifically to stop overengineering. Before that, GPT models gold-plated maybe 8/10 things. I’d ask for a bike to ride around the neighborhood and get Starlink + a rocket on the back. With Ponytail that’s more like 1/10.
agents.md rules every agent is supposed to read.
Explicit “smallest version that does the job” language. Weird edge cases get skipped unless it’s actually client-facing and needs to be robust.
That setup is why I finally stopped being miserable. I know how the models behave, I know how to operate them, confidence was up. Minor tweaks left, not a dumpster fire.
**What happened yesterday**
I was not building some insane product feature. I was wiring a loop of three skills:
**Skill Goat** — coordinator. Any new/updated skill goes through this first.
**Advanced skill creator** — actually writes/updates the skill.
**Skill evaluator** — three jobs only:is the skill discoverable
does it match the original idea
does the output match the intended outcome
Interview me → creator builds it → evaluator runs it and scores those three things. That’s the loop. Creator part was fine. Evaluator was not. It ignored the three jobs and started inventing edge cases, candidates, test plans, extra tests, the whole side quest.
I already have Ponytail and explicit “don’t gold-plate this” instructions. The evaluator’s job was: run the skill yourself, watch what it does, measure those three things. Nothing else. I fought that until it was “done.” Then I used the loop to build a research skill: Exa, Firecrawl, Apify, YouTube transcripts, X. Not exotic. Fairly simple.
With this orchestration that should have been close to a one-shot. It took about two hours of back and forth. Same pattern: not following the scoped job, doing extra work I did not ask for, ignoring the work record / milestone slice.
This is the same class of problem I used to get with 5.6 (overengineering, not sticking to the contract), except yesterday it felt *worse* than 5.6 on instruction following.
Launch Astra was a real step up for me. Yesterday it was not. Worktrees saved the repo from getting wrecked. The workflow and the codebase still take damage when the implementer/coordinator just… decides the task is something else.
---
## Comments 7

- by [unknown](#) **&#x21C5; 2**
  <br/> Aconteceu o mesmo comigo

- by [unknown](#) **&#x21C5; 2**
  <br/> In that chat, do /feedback and send a report on it. They are asking people to share these cases with them (if you're comfortable sharing it)

- by [unknown](#) **&#x21C5; 2**
  <br/> I have stopped using Astra for serious work because it just doesn't follow the skills/fuidelines/guardrails that I have set up. Sol still works great.

- by [unknown](#) **&#x21C5; 1**
  <br/> Your flow sounds correct but your use of skills is probably heavily polluting your output. Ponytail alone has a massively gigantic effect on what the code looks like and in my opinion makes output way, way worse. I'm not sure what exactly your other skills do but I strongly suggest you just get rid of all of them and trust the models and the workflow

- by [unknown](#) **&#x21C5; 1**
  <br/> I’ve experienced this problem too

- by [unknown](#) **&#x21C5; 1**
  <br/> "They iterate until they agree." well that could be the first problem

- by [unknown](#) **&#x21C5; 1**
  <br/> have the same issue.  using terra high now, it actually works without inventing a rube goldbergian kludge.
