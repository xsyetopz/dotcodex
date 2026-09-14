#I feel like I'm throwing tokens away every time I interrupt a subagent [Visit](https://www.reddit.com/r/codex/comments/1weuvol/i_feel_like_im_throwing_tokens_away_every_time_i/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [babamba_324](https://www.reddit.com/user/babamba_324/)
### **Vote:** 3
---
I'm trying to build a little bootstrap tool for my own projects with Codex. It's a bit like a harness, and it saves the agents' messages and progress to a database as they work.
I have a main agent that gives tasks to subagents. Sometimes it sends one off to do something, then realizes it forgot to include important information. But the subagent is already working by then. So the main agent interrupts it and gives it updated instructions.
That part really bothers me. If the work it already did gets thrown away, it feels like I burned those tokens for nothing.
I'm thinking of making the main agent wait once it gives out a task. Let the subagent finish, get the result, then give it the missing info and ask it to fix whatever needs fixing. Basically, work with what it already did rather than stop it halfway through.
But I'm not sure that's any better. If I already know the instructions are wrong, letting it keep going could waste even more tokens.
How do you handle this? I keep going back and forth on whether waiting is actually a good idea.
---
## Comments 14

- by [unknown](#) **&#x21C5; 3**
  <br/> I create files of tasks (Task-001.md, Task-002.md) and ask the orchestrator to spawn subagents to do each task. If there are dependent tasks (Can't do 4 until 3 is done), I create a file that I hand to the orchestrator with a dependency graph.

- by [unknown](#) **&#x21C5; 1**
  <br/> Honest question: how often those tasks are independent?

Asking this because my first harness version had agents to build tasks but parallel agents spawned like 1 out of 50 times, in coding that's obvious, the vast majority of tasks are clearly dependent from the previous task. Moreover, being agents with limited context (the context passed by orchestrator), the only tangible difference in output was low quality code.

Not a criticism but really curious what's your experience because by now, based on my exp and some research paper, I really wonder how people can benefit from such implementation, apart from clear indipendent tasks -for example searching on the web or the codebase itself -  just to name one thing that benefits from multiple agents.

- by [unknown](#) **&#x21C5; 2**
  <br/> It's not common, but a project is just finished had 126 independent parts, orchestrator was told "spawn Luna medium sub agents to perform these independent tasks (R-01.md through R-43.md and T-01.md through T-83.md). Create a document (Failed.md) and note any tasks that failed and why."

It spawned 3 sub agents and gave them 4 tasks at a time. Each task contained a description of the goal, list of files to create/ modify, any interface they needed, a list of acceptance criteria, and test data with expected results.

These were all heavy math modules, and required 5 sessions to complete (5 hour limit :/). Testing showed an error in one module, the order of two operations were backward. The unit tests still passed, integration testing showed the error.

For other things I'll have UI tasks,  DB tasks, etc.

- by [unknown](#) **&#x21C5; 1**
  <br/> I see, probably your use cases are a bit different than mine i.e. math modules which are definitely more independent than a single Enterprise application.

As a software engineer I find it impractical and prone to low quality for production grade application, where also supervision and understanding is paramount.

That Saida, apart from parallel subagents yeah, the implementation part is similar and common to most harnesses : plan/task files with detailed steps and evidences of what has been done and what failed.

- by [unknown](#) **&#x21C5; 2**
  <br/> I use subagents for trivial read-only tasks, unless speed is prioritised.

- by [unknown](#) **&#x21C5; 2**
  <br/> Interrupting is the right move when the missing information invalidates the task, but don't treat interruption as a restart. Persist each subagent's latest checkpoint—assumptions, files touched, partial conclusions, and unresolved questions—then send the correction as a delta against that checkpoint. For small omissions, queue a follow-up and let the current step finish. For scope-changing mistakes, stop immediately. A useful rule is to compare expected remaining waste: if continuing would produce output you can still reuse, wait; if it will commit to the wrong architecture or data model, interrupt. The real optimization is resumability, not avoiding every interrupted token.

- by [unknown](#) **&#x21C5; 1**
  <br/> I really like the idea, and it honestly sounds like an ideal way to do it. I just don’t think I have the time or the ability to build all of that properly right now. Even with Astra, I feel like getting the whole thing working perfectly would be pretty difficult.

- by [unknown](#) **&#x21C5; 2**
  <br/> If the subagent already went sideways, cutting early wastes less than letting it finish the wrong plan. I stop at the first wrong step, then restart with a tighter brief.

- by [unknown](#) **&#x21C5; 2**
  <br/> Have it wait to assign a subagent until it has a bounded task with all information present.

- by [unknown](#) **&#x21C5; 1**
  <br/> Yeah, that's what I'd like to do too.

I already have a checkpoint where the main agent has to make the full plan first and show it to me before doing anything. If I tell it to continue, it starts working from that plan.

The problem is that even with that, new problems still show up while the work is actually being done.

I don't think a person or an AI can know every little detail in advance and perfectly plan everything all the way to the end. That sounds a bit philosophical, but I think it's just something you see in practice. You start doing the work, and eventually something comes up that wasn't obvious at the planning stage.

So even if the plan itself was good, sooner or later I still get cases where the orchestrator forgets some important context and sends a subagent off with incomplete instructions.

I could keep adding more checks and rules to handle every case, but then the bootstrap starts getting bigger and more complicated than I want it to be.

And this might sound a little irresponsible, but the simplest solution I can think of right now is just keeping the initial task I give the orchestrator really small. If it makes a mistake, then even if some tokens get wasted, the loss is still relatively small.

I'm also thinking about saving the failed work instead of completely throwing it away. I could store the bad instruction from the orchestrator together with whatever response or code the subagent produced from it.

Then maybe later I could run a local LLM + RAG system over that data. Some of it could possibly become training data for another local model, or I could just make it searchable so that if I need to build something similar later, the old code can still be useful as a reference.

Obviously that doesn't actually give me the tokens back, but at least the failed work wouldn't be completely wasted.

- by [unknown](#) **&#x21C5; 2**
  <br/> Claude has this by default, although I think it's a bug, where most times if the team lead sends a message to a teammate while the teammate is working, the teammate essentially ignores it until it's done their work. This seems to happen because the teammate doesn't check their inbox while they're working. Only when they stop.

I find this extremely irritating cause you'll have the team lead request a change of direction only to realize the teammate ignored it for hours and now has gone so far down the wrong path it'll take few more hours to refactor. That's an even bigger waste of tokens

I say interrupt proactively. Save time and tokens

- by [unknown](#) **&#x21C5; 2**
  <br/> Claude does that too? Sounds like Codex and Claude handle subagents in a pretty similar way then.

Anyway, the idea of burning hours worth of work and tokens is honestly terrifying. Yeah, that’s definitely something I’d want to prevent.

- by [unknown](#) **&#x21C5; 2**
  <br/> I made sure this does not happen. Let the sub agent finish and please keep its work.
