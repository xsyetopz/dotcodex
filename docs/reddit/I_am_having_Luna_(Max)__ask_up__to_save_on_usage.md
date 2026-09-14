#I am having Luna (Max) "ask up" to save on usage [Visit](https://www.reddit.com/r/codex/comments/1wcr2pn/i_am_having_luna_max_ask_up_to_save_on_usage/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [ganderofvenice](https://www.reddit.com/user/ganderofvenice/)
### **Vote:** 8
---
Don't know if anyone else has tried this or this is actually a bad idea, but instead of using Sol and/or Astra with Luna subagents, I'm starting my sessions and discussing ideas or problems with Luna (Max). Then, when I need something "engineered" or "brainstormed" I tell Luna (Max) to ask Sol (xHigh) or Astra (Medium) (depending on the complexity) for help and advice, basically, using them as smarter consultants or experts before implementation, which is done by Luna (Max).
I'm also having Luna (Max) asking to have its work reviewed using this same method, it has definitely been useful because, as we know, it is not the best coder.
Dumb? Maybe, but I only use Codex at work and I "only" have the 5x Pro plan. On top of that, resets and banked resets are randomly given and sporadic in nature, which I can't trust for something like work. So, I need to make sure weekly usage actually lasts 5 business days.
What do you think?Hope this helps anyone.
---
## Comments 4

- by [unknown](#) **&#x21C5; 2**
  <br/> I don't know how this would work in practice but it might avoid the issue with Astra overpolling subagents?

- by [unknown](#) **&#x21C5; 2**
  <br/> No I think this is probably a great idea. One thing to consider is, it’s probably spawning in (asking) an Astra subagent with a ‘history carrying’ subagent fork - so it is spawning Astra with Luna’s entire context window (potentially) - which means if your Luna session is 120,000 tokens then you just started a 120,000 token (mostly cached) Astra session for a review - you could try to improve that by instructing Luna to create a short packaged brief for Astra with only necessary context, hard guard would be `fork_turns=“none”` - however I am uncertain if Luna would be able to reliably determine which context is important or not to include in that “packaged” / context bloat free handoff

- by [unknown](#) **&#x21C5; 1**
  <br/> Like a handoff to a consultant subagent, basically.

- by [unknown](#) **&#x21C5; 1**
  <br/> Yes, basically Luna is saying “here’s only the context you need for what I’m asking you to do” instead of “here’s all the context that I have currently”
