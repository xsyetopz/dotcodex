#Astra Medium as Orchestrator and Luna Max as the Implementer? [Visit](https://www.reddit.com/r/codex/comments/1w9zt8r/astra_medium_as_orchestrator_and_luna_max_as_the/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Initial_Question3869](https://www.reddit.com/user/Initial_Question3869/)
### **Vote:** 3
---
Has anyone found success with this configuration? Does it burn fewer tokens?
---
## Comments 17

- by [unknown](#) **&#x21C5; 3**
  <br/> Luna Max overengineers and takes a very long time. Luna medium is way faster and only makes a few mistakes.Astra low / light is as good as Astra Medium (in my small benchmarks) as the orchestrator and faster / more token efficient.

tl;dr - Astra low orchestrator > Luna medium implementerCan then add in Terra reviewers, Sol low is also a very good reviewer. Hand really big/complex tasks to Sol High

- by [unknown](#) **&#x21C5; 8**
  <br/> Your tl;dr is nearly as long as your initial message

- by [unknown](#) **&#x21C5; 1**
  <br/> 😅 last two sentences were like afterthoughts of the tl;dr I guess lol

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra low orchestrator burned 7% of my weekly on a simple task, with sol medium implementors. Back to flat sol for now. I saved and redid the same task with sol mid from the beginning and didnt even push 1%. I'm just gunna use astra for code review intermittently

- by [unknown](#) **&#x21C5; 7**
  <br/> Luna high

- by [unknown](#) **&#x21C5; 1**
  <br/> Funny timing, I was just talking about this in another thread xD

I've gone a bit further with the same idea. I use Astra xHigh almost exclusively as the coordinator and keep implementation in separate chats. Sol ended up being my default worker, Terra for simpler bounded stuff, and Luna only when the task is really constrained

I originally expected Luna to be the obvious cheap worker, but for my workload it needs enough rework that Sol often makes more sense. For harder branches Astra sometimes hands the whole thing to Fable/UltraCode, which then runs its own Opus workflow

These are separate chats, not subagents. That's actually the part I like most because the implementation history doesn't fill the coordinator context. I haven't A/B tested the cost though, so no idea if this is actually cheaper than Medium + Luna Max

- by [unknown](#) **&#x21C5; 1**
  <br/> Sol Medium or High?

- by [unknown](#) **&#x21C5; 1**
  <br/> I actually leave that up to Astra it chooses medium or high depending on how complex the task is

- by [unknown](#) **&#x21C5; 1**
  <br/> I personally use Astra on low or Sol on medium and Luna High for implementation

My setup is here [https://github.com/breko861-hash/sol-luna-codex-orchestrator](https://github.com/breko861-hash/sol-luna-codex-orchestrator)

- by [unknown](#) **&#x21C5; 1**
  <br/> If you want speed I recommend Terra high or xhigh. Way faster than Luna and Sol.

- by [unknown](#) **&#x21C5; 1**
  <br/> I tried that and I had codex all day going. Still hasn’t finished. I’ll be running out of tokens soon

- by [unknown](#) **&#x21C5; 1**
  <br/> Plan with Astra then use Luna High to implement, Sol High to review. Ideally you want to use cheapest models possible unless you unlimited $. I dont really like using Astra at all because it chews quota even on light.

- by [unknown](#) **&#x21C5; 1**
  <br/> why aren't you using terra-high or terra-xhigh?

- by [unknown](#) **&#x21C5; 2**
  <br/> ++ sol-medium can execute what astra planned in a more comprehensive and valuable way. if you’re going to burn a lot of tokens anyway, i think the best value is astra low + luna high subagents for planning, then sol med or terra xhigh as the executor for you*

- by [unknown](#) **&#x21C5; 3**
  <br/> Terra is the worst of both worlds, its as expensive as sol while being as dumb as luna

- by [unknown](#) **&#x21C5; 1**
  <br/> It's terrable?

- by [unknown](#) **&#x21C5; 0**
  <br/> i dont think so
