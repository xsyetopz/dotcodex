#Astra VS Astra + Luna Agents [Visit](https://www.reddit.com/r/codex/comments/1wcr5c1/astra_vs_astra_luna_agents/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [ThePDFProfessor](https://www.reddit.com/user/ThePDFProfessor/)
### **Vote:** 10
---
Over the last few days, I’ve been developing a tool that helps with a few things, and one of the areas I’ve been testing heavily is **agents**.
The problemAstra is extremely token-efficient, which makes **Astra Low surprisingly 'cheap'** when working alone.
But when Astra is used as an orchestrator managing other agents, that efficiency starts getting lost for two main reasons:
- **Cheaper models like Luna tend to write more than necessary.** Even if Astra Low doesn’t fully re-read every implementation, it still has to process a significant amount of agent output to review and coordinate the work.
- **Communication between the orchestrator and agents is still inefficient.** Agents often carry much more context than they actually need.
I’m currently working on reducing that context overhead. If anyone has ideas or has experimented with this, I’d be interested in hearing how you approached it.
The result is that, in most of my tests, **Astra ends up consuming significantly more tokens when using agents than when completing the same task alone.**
Test setupA few important details:
- I built my **own agent-management system**, specifically designed to reduce input-token and cached-input-token usage.
- The **Advisor** shown in the results is part of my internal system, so it can mostly be ignored when comparing Astra alone vs. Astra + workers.
The test taskThe benchmark was not a synthetic coding problem.
I took an existing repository:
- written in a different programming language,
- originally built for macOS,
and asked the system to implement the same functionality inside one of my existing Windows projects.
I chose this because it exercises most of the things an agentic coding system would actually need to do in a real-world task:
**Research → analyze → understand an unfamiliar codebase → implement → handle UI/UX → follow project-specific instructions → match existing patterns and architecture.**
So far, my results suggest that **agents are not automatically more efficient just because the worker models are cheaper**.
In some cases, the coordination and context overhead can make the total run substantially more expensive than simply letting Astra handle the task itself.
I’ll keep testing this with more tasks and different agent configurations.
---
## Comments 15

- by [unknown](#) **&#x21C5; 3**
  <br/> Now I know why so many people complain about usage disappearing, while I just run Astra Xhigh and dont worry about it...lol

- by [unknown](#) **&#x21C5; 14**
  <br/> Don't let cheap models write code. Even supervised by a higher model. It'll just be a lot of babysitting, reviewing, back-and-forth corrections. Lots of usage waste.

What you should use the cheap models for is *context gathering*. Your goal should be, in as **few turns as possible**, to get as much **relevant data** into Astra's context window as is needed to understand the solution space.

Then, with that data, just let Astra (high/xhigh) churn through intense reasoning and develop its solution. Write it out to an implementation plan / design document. Don't actually have Astra write the code, that takes many tool calls and many turns and will nuke your usage.

Once the plan is written. Pass it to an actual capable model who won't fuck it all up. Sol (medium/high) is a reasonable choice, *they* can use Luna for their own context gathering / orientation, but they need to be the one to write the actual code so they can flex and adapt when surprises turn up.

Once everything is finished, then you can do an adversarial review pass with the original plan author (Astra, they have all the right context). This part is only needed if you are paranoid about quality/correctness (you should be).

- by [unknown](#) **&#x21C5; 2**
  <br/> Yep, I think this is a much better approach too.

I mainly did this test because I wanted to try the subagent/orchestrator approach and measure the overhead in practice.

What you're proposing feels more like a structured workflow: use cheaper models to gather only the relevant context, have Astra turn that into a strong plan/design doc, and then pass that document to the implementation model instead of carrying all the previous context and back-and-forth with it.

That should reduce a lot of unnecessary context usage while also avoiding the babysitting problem of having cheap models write the code.

This is the approach I'm currently testing.

Expect results, once my usage resets,HAHAHAHA.

- by [unknown](#) **&#x21C5; 2**
  <br/> this solution would be so much more efficient if openai had looked into issue of losing cache context of parent to worker:  [https://github.com/openai/codex/issues/24704](https://github.com/openai/codex/issues/24704)

- by [unknown](#) **&#x21C5; 0**
  <br/> Yeah currently is a lot of problems with agents and context and delegation and tool calls.......

[https://github.com/openai/codex/blob/main/codex-rs/core/src/tools/handlers/multi_agents_v2/spawn.rs?utm_source=chatgpt.com](https://github.com/openai/codex/blob/main/codex-rs/core/src/tools/handlers/multi_agents_v2/spawn.rs?utm_source=chatgpt.com)

HAHAHAHAHAHHA

- by [unknown](#) **&#x21C5; 1**
  <br/> In my Astra plan session prompt, I usually say something along the lines of “In your plan, identify how you will use cheaper subagents for the appropriate task; you will use fresh GPT-6 Astra (Low) for judgment and any mid-project reviews - your session is Astra High; your plan will launch fresh Luna/XHigh and Sol/medium workers for the bounded execution as necessary.”

So far that has been working for me really well, although I’m sure there are ways to optimize / drive more efficiency.

- by [unknown](#) **&#x21C5; 0**
  <br/> I disagree. Luna's amazing at coding if you give it actual direction and no ambiguity.

If you're on a higher plan and don't need to rely on lunamaxxing to not be locked out of 5h periods, do whatever, but I've yet to have it fuck up in a way counter to what it was instructed to do.

If your Astra planing is chunking general tasks into smaller, but not completely defined problems, you might have issues. But I've had no problems with a prompting style that makes it clear *exactly* what it needs to do.

- by [unknown](#) **&#x21C5; 3**
  <br/> I’ve done a lot more tests, but this was the most significant one.

And about Astra Low vs Astra XHigh: yeah, it’s actually true HAHAHAHA.

For difficult tasks, Astra XHigh often uses significantly fewer tokens per completed task than Astra Low because it needs fewer iterations.

For easier tasks, Astra Low is still cheaper and usually more than enough.

So my current rule is basically:

**Difficult task → Astra XHigh****Easy task → Astra Low**

- by [unknown](#) **&#x21C5; 1**
  <br/> Or just plan with Astra low, then switch to Sol low (new context window) to execute.

- by [unknown](#) **&#x21C5; -1**
  <br/> Luna Low as ADVISOR?????

Luna low:

"Hey, to deliver this dropdown on React you should first rm -rf your entire HD. Do it, its safe"

LMAO

- by [unknown](#) **&#x21C5; 2**
  <br/> I mean, he just trying to bench the astra tokens and time, so using Luna low makes sense to have less influence in the total time.

- by [unknown](#) **&#x21C5; 1**
  <br/> It was being used for the cheap, low-risk grunt work around the task. The planner/reviewer and important decisions are handled by stronger models.

- by [unknown](#) **&#x21C5; 0**
  <br/> Sorry, i was jokingBut, from practice, do not use anything below Luna Max

Its not reliable

- by [unknown](#) **&#x21C5; 1**
  <br/> You're the programmer bro, you shoudl assure the quality of the code, Luna is pretty fucking useful if you know how to use it.

- by [unknown](#) **&#x21C5; 1**
  <br/> Sure thing
