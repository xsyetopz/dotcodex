#So just learned that fork_turns defaults to "all" = astra subagents get dumped with 800k+ initial context bloat [Visit](https://www.reddit.com/r/codex/comments/1wcn7yl/so_just_learned_that_fork_turns_defaults_to_all/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [swizzlewizzle](https://www.reddit.com/user/swizzlewizzle/)
### **Vote:** 18
---
So...
A little awhile ago, when we all got Astra, I thought "hey why don't we use a Astra/high/xhigh act as orchestrator, spawn a bunch of subagents to handle each task in our spec, and then let them go at it?"
Little did I know that the *default setting* in codex for how much parent turns context to shove into it's subagents is *ALL OF IT*.
I mean.. wtf.
In many cases I spent a bunch of time going back and forth with my Astra xhigh, brainstorming, setting up the plan, maybe an autocompact or two.. and then I'm thinking "OK, plan is ready, orchestrator is up to date with where we are at on this spec, let's spin up some *clean* Astra low subagents to implement and call it a wrap".
The result?
Every Astra low subagent getting 800k or so context dumped into it from my entire turns history *with the orchestrator*.
And then of course the inevitable "orchestrator pings subagents incessantly" issue, burning *even more* tokens.
This is a MASSIVE amount of token burn we are talking about.. Astra input token prices on a *starting* 800k or so context, for subagents that *should just have a clean context since we put all that effort into properly planning and setting up their tasks*!.
Arghhhh
WHY oh WHY is the DEFAULT to dump THE ENTIRE TURN HISTORY INTO EVERY SUBAGENT? How is this "feature" hidden down in the depths of the "fork_turns" setting? Why didn't my xhigh Astra gent tell me "bro, we are about to spin up like 3 million tokens worth of context across these subagents before they even do anything - r u sure you don't want to switch to fork_turns: "none"?".
Sigh.
---
## Comments 17

- by [unknown](#) **&#x21C5; 3**
  <br/> Now this explains a lot

- by [unknown](#) **&#x21C5; 4**
  <br/> It's just mad how the community debugs this shit for them.

- by [unknown](#) **&#x21C5; -1**
  <br/> I think it’s right to do it yourself.

You should know how it works before using it

- by [unknown](#) **&#x21C5; 2**
  <br/> That's not what I'm saying. I've been a developer for 15 years and these guys are just winging it. I get the competition with anthropic and the need to go to market but the constant fuck ups are stopping me from buying another plan.

- by [unknown](#) **&#x21C5; 1**
  <br/> Ah, I get the point.

It seems like OpenAI tends not to pay much attention to user convenience

It’s the same with the SLA

- by [unknown](#) **&#x21C5; 3**
  <br/> Forkturn being default has been since 5.6 was released.

That is my pet hate.

Why would I spawn agents and give them EVERYTHING?

- by [unknown](#) **&#x21C5; 2**
  <br/> Where are you seeing that documented? I can't find much except this in the OpenAI [docs](https://developers.openai.com/api/docs/guides/responses-multi-agent) that tells the root agent when doing Multi-Agent


      You can decide how much context you want to propagate to your sub-agents with the `fork_turns` parameter.


    But I don't see anywhere that it will always give all the context. And how do you decide how much context? What gets removed if you lessen it?

- by [unknown](#) **&#x21C5; 3**
  <br/> It’s also a cache miss so in your case instant 8$ cost per subagent

- by [unknown](#) **&#x21C5; 2**
  <br/> My soul hurts right now. :(

- by [unknown](#) **&#x21C5; 2**
  <br/> Wait why is it a cache miss?

- by [unknown](#) **&#x21C5; 1**
  <br/> Apparently the cache is linked to both the model and the thinking/effort level. So, if you change effort level or model, it’s a cache miss.

- by [unknown](#) **&#x21C5; 0**
  <br/> Because the subagent is getting fresh context. All of it.

- by [unknown](#) **&#x21C5; 2**
  <br/> Yeah but if it was implemented sensibly a fork would still have the same prefix so it would hit the same cache.

- by [unknown](#) **&#x21C5; 1**
  <br/> how much context does astra use actually is it not capped to 250k still by default? or is it really keeping 1m in context??

Is there a fix for this fork_turns unlimited?

- by [unknown](#) **&#x21C5; 1**
  <br/> Check your maximum context window setting. Pretty sure does it to go up to 800k you need to set it yourself, and of it does go up there, it compact it down. Your last turn should rarely be the maximum context window allowance you have, despite having a massive history. Only the last turn get fed. Probably not 800k

- by [unknown](#) **&#x21C5; 1**
  <br/> using subagents doesnt make any sense

1 session is better. using subagents is slower, uses more tokens, quality isnt even better

when you are ready to go from plan -> execution, just handoff to a new session.

the only reason to use subagents is for doing research imo

- by [unknown](#) **&#x21C5; 1**
  <br/> Yea I have my instructions set to all sub agents forked with no context, it helps a LOT. Maybe the single biggest reason the limits feel fine to me (two 20x accounts).

This has been a problem not just since astra but for 5.6 as well when they overhauled their sub agents system.
