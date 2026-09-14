#Astra likes to tell you every minute it's waiting on agents [Visit](https://www.reddit.com/r/codex/comments/1wbsw7j/astra_likes_to_tell_you_every_minute_its_waiting/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [oddslol](https://www.reddit.com/user/oddslol/)
### **Vote:** 5
---
And the annoying thing is you can't fix it:
There’s also a conflicting instruction in this session’s host guidance: it requires user-facing commentary at least every 60 seconds and discourages individual waits longer than 60 seconds. If that other session has the same guidance, it can push Astra into exactly this pattern despite your framework saying to rely on completion notifications. Framework wording alone cannot override higher-priority host instructions.
You said "it requires user-facing commentary at least every 60 seconds" - where does that come from? system prompt?
• Yes—specifically, a developer-level instruction supplied by the host, rather than your [AGENTS.md](http://AGENTS.md) or the top-level system message.
Under “Intermediate commentary”, it says:> “The user appreciates consistent, frequent communication during your turn, and should not be left without a commentary update for more than 60 seconds during ongoing work.”
Separately, under “Rules for getting work done”:> “Avoid performing blocking sleep or wait calls longer than 60 seconds, as they may prevent you from communicating with the user for their duration.”
Those instructions have higher priority than your framework instructions. I can confirm they’re present in this session; I haven’t verified that the other session received identical instructions.
They help explain the repeated wake-ups, but don’t require those lengthy, repetitive updates or justify unsupported claims about what the worker is doing.
Is there any way to override those instructions or change them?
• Not through [AGENTS.md](http://AGENTS.md), a skill, or an ordinary chat instruction. Those have lower priority than the host’s developer instructions.
Changing them requires control over the configuration or code that supplies that developer message. I don’t have a setting exposed here that lets me edit it.
I found a GitHub issue describing the problem: [https://github.com/openai/codex/issues/31935](https://github.com/openai/codex/issues/31935)
If this affects you too I think we should all upvote and comment on the issue to get it some recognition!
---
## Comments 5

- by [unknown](#) **&#x21C5; 2**
  <br/> [](https://preview.redd.it/astra-likes-to-tell-you-every-minute-its-waiting-on-agents-v0-n9t0zaj8cjoh1.png?width=973&format=png&auto=webp&s=7d087ad1213c562382b6387573cb06b7a8cc2c09)
      
    Yes its a developer instruction to check every 60 seconds.

- by [unknown](#) **&#x21C5; 1**
  <br/> I'm going to try this;

 
       [](https://preview.redd.it/astra-likes-to-tell-you-every-minute-its-waiting-on-agents-v0-x2bgdiejcjoh1.png?width=883&format=png&auto=webp&s=c9634b507ac5e05ea7baa703a46acbcdbe06e452)

- by [unknown](#) **&#x21C5; 2**
  <br/> Nice, please do let me know if this works. I guess it will only work on the subagents and not the main orchestrator thread though?

- by [unknown](#) **&#x21C5; 1**
  <br/> I'm just doing some deep dive and optimizations, I will let you know if it works. I have 26% on the 5h, im not sure if i have enough time to test it but

- by [unknown](#) **&#x21C5; 1**
  <br/> Have you found a way around it? :)
