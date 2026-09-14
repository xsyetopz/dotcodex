#Codex' system prompt still forces agents to wake up each minute = tons of wasted tokens when using subagents or waiting on background tasks (like CI, etc). [Visit](https://www.reddit.com/r/codex/comments/1wffvur/codex_system_prompt_still_forces_agents_to_wake/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Pimpmuckl](https://www.reddit.com/user/Pimpmuckl/)
### **Vote:** 13
---

![Codex' system prompt still forces agents to wake up each minute = tons of wasted tokens when using subagents or waiting on background tasks (like CI, etc).](https://preview.redd.it/codex-system-prompt-still-forces-agents-to-wake-up-each-v0-tuft18sd1cph1.png?width=640&crop=smart&auto=webp&s=28ebdffd1970d0ef0559e62141dacd636093a50f)
---
## Comments 5

- by [unknown](#) **&#x21C5; 4**
  <br/> Basically: Three ways to fix it

  1. Put explicit instructions in your `AGENTS.md` that the agent should ignore the system prompt instruction about updating the user unnecessarily. This didn't really work in my experience.
  2. Use a custom `model_instructions_file` and adjust the system prompt that way
  3. Make your own fork (or use one that fixes it) and update the system prompt that way. That's what I did and the results are pretty crazy in these examples.

I wrote a bit more about this on twitter, but tl;dr:

Because these agents are forced by the system prompt to "update the user every 60s" there is a LOT more unnecessary model calls than what you'd usually need.

Pair it with the very expensive cache read from Astra and suddenly it explains the disaster that are the current limits.

- by [unknown](#) **&#x21C5; 1**
  <br/> Do you know of a fork that fixes it

- by [unknown](#) **&#x21C5; 0**
  <br/> Changing sys prompt is pretty simple. It's a json, ask codex, he will figure it out

- by [unknown](#) **&#x21C5; 0**
  <br/> Agent's won't help, system prompt have higher level of priority. Also changing sys prompt sucks cause it's refreshed only with a new session

- by [unknown](#) **&#x21C5; 2**
  <br/> Until they fix this Astra is basically broken with subagnents
