#Is it more costly to switch between models or to use the same model with lower thinking effort? [Visit](https://www.reddit.com/r/codex/comments/1wcv2sb/is_it_more_costly_to_switch_between_models_or_to/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [kyrax80](https://www.reddit.com/user/kyrax80/)
### **Vote:** 6
---
Every time I switch to a lower model I get this notification that the conversation will be degraded and context compacting stuff. If I plan for Astra, for instance, and switch to Terra to implement something easy, is it bad or more costly?
Thanks.
---
## Comments 22

- by [unknown](#) **&#x21C5; 8**
  <br/> Both ding your entire cache as new input. So, it depends. If you're using luna and accrue a large context and then switch to Astra, you're getting that full cache as new input pricing. If you're using Sol xhigh and accrue a large context, and then switch to sol medium, your entire context is a new input hit.

If you're using Astra and accrue a large context and then switch to Luna, the entire context is a new input hit, but at luna pricing, so meh.

So functionally, you don't really want to do either, unless for some reason you're switching from a high capability model to luna. Better to finish your task/slice, compact, and switch models, or have a handover document created and start a new session and give them the handover doc.

It's part of "planning on high, implementing on medium" is a decent approach. Plan with lots of reasoning, have PR slices or tightly scoped phased implementation plans, or whatever be created at high costs. Then start new sessions and have lower-cost models/reasoning implement those highly spec'd models.

- by [unknown](#) **&#x21C5; 1**
  <br/> Wrong.  Reasoning level changes NO LONGER INVALIDATE YOUR CACHE.

- by [unknown](#) **&#x21C5; 5**
  <br/> Wrong that is only for Astra. I suspect the gpt 6 range may not need but currently sol still do that.

- by [unknown](#) **&#x21C5; 1**
  <br/> Both wrong! reasoning is not a Cache issue, and KV Cache embedding for MLA depend on the matrix being used, and this is observed by switching from 5.5 to 5.6 and seeing the compaction required to process that. However, that is not happening between 5.6 to 6 as they seem to be using the same underlying Paged Attention system with some edits.

- by [unknown](#) **&#x21C5; 6**
  <br/> ERRBODY WRONG UP IN ERE

- by [unknown](#) **&#x21C5; 2**
  <br/> WRONG! **errbody but me**  I'm not wrong!

- by [unknown](#) **&#x21C5; 1**
  <br/> What is paged attention system? Hearing it for first time.

- by [unknown](#) **&#x21C5; 1**
  <br/> Chunks the KV Cache in memory. Pages are memory blocks beens around since windows 3.1 its why there is a page file on a Windows computer.

Pages Attention is just a KV Cache version

- by [unknown](#) **&#x21C5; 2**
  <br/> Yes but what I can't understand is how does paging reduce usage? In the end the kv cache used by model would be equal at all times, sorry for asking stupid questions it's been a long time.

- by [unknown](#) **&#x21C5; 2**
  <br/> Its not stupid,

The KV cache must be rebuilt every time a session starts. However, with page attention we can manipulate managed chunks, allowing smaller edits and re usability across sessions. Therefore, instead of a full re-compaction, The model can just carve out what doesn't match.

Simple put, Fresh token cost is reduced and cached token usage increases which are cheaper, it also helps on output because we don't repeat ourselves. (though thats' a slightly different process)

- by [unknown](#) **&#x21C5; 2**
  <br/> Wow I thought nothing has changed since CoT days amazing to hear about these changes, Thanks for the insight.

- by [unknown](#) **&#x21C5; 2**
  <br/> No problem look up Multi-head Latent Attention when you have the time its a nice system used for this now. Nothing ever leaves the matrix until its processed on output now.

- by [unknown](#) **&#x21C5; 1**
  <br/> Settled on creating a work directive in chat on pro 6 then Astra low to implement working well so far

- by [unknown](#) **&#x21C5; 1**
  <br/> When you switch models in the same chat it reads the  chat history  as uncached input tokens, lower reasoning will use the existing cache. You can open a new session with the other model and point it to the same project and it won't read all of the history or tell your current model to use a subagent of the lower model

- by [unknown](#) **&#x21C5; 1**
  <br/> it just makes more sense to gather the context you actually need for plans than giving every detail of source code syntax from a builder so you can have the builder gather a package and prompt an agent with no context or better just use chatgpt to inspect the repo through a connector yourself and issue a new plan without using your codex quota for plans and reviews.

- by [unknown](#) **&#x21C5; 1**
  <br/> Plan with Astra but switch to Luna may work because Luna is dirt cheap. So bursting the cache for it is fine. But moving from Luna to Astra is going to hurt

- by [unknown](#) **&#x21C5; 1**
  <br/> Sol and Astra are on the same KV cache system, I have not noticed a issue. As other users have stated, this is not the case with all models, going from Sol to 5.5 does break the cache and require a re-compile / embedding update.

So planning in Astra and executing in sol may be good. But tests have shown the average intelligence is identical between Sol and Astra,

Astra only excels in Cyber, benchmarks and computer use for 2.5x token usage.

- by [unknown](#) **&#x21C5; 1**
  <br/> /compact and then switch

- by [unknown](#) **&#x21C5; 1**
  <br/> It depends...but I do be switchin

- by [unknown](#) **&#x21C5; 1**
  <br/> Yes, use subagents or make a handoff, switching models is incredibly wasteful. Think of it as replaying the entire conversation up to the point you're at

So it's not like Astra does steps 1 through 10 and Terra does step 11, It's like Astra does steps 1 through 10 then Terra does steps 1 through 11

- by [unknown](#) **&#x21C5; 1**
  <br/> I created a skill, actually modified a skill to switch models, sol is used to plan a task and luna to implemenet said task, then sol does code review and luna fixes whatever needs to be fixed.

It burned 50% more tokens than using sol alone and wasted 8.5 hours on a task that sol can complete in 3 hours or less.  Wasted almost 15% of my weekly quota on this. Im never touching luna again for anything. Its literally the worst model ever created. Technically gemini 3.8 is the worst model ever created but at least its a 100 times faster than luna.
