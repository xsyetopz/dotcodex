#Simple rules to stretch your usage limits [Visit](https://www.reddit.com/r/codex/comments/1wemr7j/simple_rules_to_stretch_your_usage_limits/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Potential-Worth-7660](https://www.reddit.com/user/Potential-Worth-7660/)
### **Vote:** 6
---
- Avoid long threads. Try to get what you need done in a few turns.  [WRONG. CHECK COMMENT]
- If a thread does get long, compact the context every few turns. In my experience, doing it regularly preserves context much better than waiting for auto-compaction, which is when I start noticing memory degrade. [WRONG. CHECK COMMENT]
- Don’t use fast mode unless you actually need it. Running a few normal threads in parallel is usually a better trade.
- Give yourself a daily budget. Once you get close to it, start being much more conservative.
- Use Sol by default. Only switch when you genuinely need a stronger model. Sol can already handle most tasks. And use luna/terra for easy tasks.
- Use low reasoning by default. Raise it for genuinely hard or novel problems, or when the model clearly isn’t putting in enough work. For most coding, low is enough.
- Install the Ponytail skill. It pushes the model toward smaller, simpler, more efficient code.
So the biggest budget drainers that are easy to avoid are:
**fast mode, long threads, high reasoning on simple tasks, and using Astra for everything.**
If you’ve found any others, drop them below.
---
## Comments 13

- by [unknown](#) **&#x21C5; 3**
  <br/> Do long threads really drain more usage? Does it read messages from before the context compaction?

- by [unknown](#) **&#x21C5; 4**
  <br/> I think there's a balance where you want the thread to keep going if it's still relevant to get the benefit of cached inputs. If you're always making new threads you're going to get the uncached penalty.

But if it goes on too long performance will degrade even with compaction in my experience.

- by [unknown](#) **&#x21C5; 0**
  <br/> I checked this and input caching itself isn’t tied to a thread. if two threads share the same workspace/context, a lot of that prefix can still be cached.

so starting a new thread doesn’t mean paying for the entire codebase from scratch. the tradeoff is just that you lose the conversation-specific context from the old thread.

- by [unknown](#) **&#x21C5; 1**
  <br/> What does the prefix consists of exactly, for entirely new threads? Isn't it bare minimum (<10k tokens), and any post thread creation workspace context are uniquely constructed?

- by [unknown](#) **&#x21C5; 1**
  <br/> YOUR messages are typically preserved as-is iirc. But its own messages and tool use history is compacted.

But also: multiple turns at the same context is cheap because of cached input tokens costing only 10% of non cached tokens.

So each time you compact, you’re paying full cost for those post-compact input tokens.

- by [unknown](#) **&#x21C5; 0**
  <br/> yeah. before compaction, each new turn carries the conversation history and prior tool calls forward, so longer threads mean larger prompts.

after compaction, Codex replaces that history with a smaller compacted summary instead of rereading every old message.

I use t3code and it shows me how many tokens were compacted. Do this like 10 times in a thread and you save 1mil tokens... and scale that to other threads and you save a lot of usage.

 
       [](https://preview.redd.it/simple-rules-to-stretch-your-usage-limits-v0-j0ntcf70d5ph1.png?width=835&format=png&auto=webp&s=81a9e9cc1aacc67aac9517eafb5dd60238c6b143)

- by [unknown](#) **&#x21C5; 2**
  <br/> I liked a lot terra xhigh for implementation it was like 2x faster than Sol, and again, worked good enough for easy /low-risk tasks.

- by [unknown](#) **&#x21C5; 1**
  <br/> Yeah and if they break something astra/sol can easily fix it. I believe this to be a much better workflow.

- by [unknown](#) **&#x21C5; 2**
  <br/> 1. "Avoid long threads. Try to get what you need done in a few turns."True
  2. "If a thread does get long, compact the context every few turns. In my experience, doing it regularly preserves context much better than waiting for auto-compaction, which is when I start noticing memory degrade."

False. Absolutely do NOT follow this... This makes no sense and leads to a much lower cache hit %. Compaction of any sort should be a last case scenario when it happens automatically mid loop.

3. "Don’t use fast mode unless you actually need it. Running a few normal threads in parallel is usually a better trade."

False.Yes ofc fast mode is 50% more expensive, so good to not use it if you dont need to.But running parallel threads is 100s of percentages more expensive..? One thread with fast mode is 50% more expensive, two theeads with std means 100% increase in cache writes+uncached input, continuously keeping that cost diff.

4. "Give yourself a daily budget. Once you get close to it, start being much more conservative."

What? "being more conservative" is what youre entire list is supposed to be a guide to?

5. "Use Sol by default. Only switch when you genuinely need a stronger model. Sol can already handle most tasks. And use luna/terra for easy tasks."

False, but reasonable.

Luna is absolutely able to handle most tasks, like probably 99%, but does not handle mistakes in the instructions as well.

But Luna is so slow that it becomes impossible to use it in practice, so Sol id reasonable.

6. "Use low reasoning by default. Raise it for genuinely hard or novel problems, or when the model clearly isn’t putting in enough work. For most coding, low is enough."

True, but i would say the distinction should be related to how many steps the instruction requires to complete rather than some ambiguous "more complex" metric

7. "Install the Ponytail skill. It pushes the model toward smaller, simpler, more efficient code."

Pure cargo cult bullshit. Here you lost all credibility imo..

Do you genuinely actually belive the code generated even represents a fraction of the generated tokens?Also code style should follow repo conventions nothing else

- by [unknown](#) **&#x21C5; 1**
  <br/> Thanks for this insight I've added flags to the post.

- by [unknown](#) **&#x21C5; 2**
  <br/> 1 tip know what u doing, for eg if ur writing content for eg 1 task was writing. Content chapters for app, don't do it by astra it will makeit 100% FOR EG EVEN  fable and opus used 100% in hour ..

Give those task to lower apps,

If ur task required lots of image reading give to lower models etc

- by [unknown](#) **&#x21C5; 1**
  <br/> A lot of basic stuff but sol is good shout

Don't use astra for everything

- by [unknown](#) **&#x21C5; 1**
  <br/> Spawn sub agents for discovery, tests, etc.

Like if you use astra max and it run your full test suits after every changes tell it "spawn a luna low agent with the minimum context needed for tests, only report errors"

That way you burns meaningless credits on luna and keep astra for the good stuff.

[https://learn.chatgpt.com/docs/agent-configuration/subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
