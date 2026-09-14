#We’ve discovered the issue behind codex harness input token drainage. [Visit](https://www.reddit.com/r/OpenaiCodex/comments/1wdpuub/weve_discovered_the_issue_behind_codex_harness/)
### **Subreddit:** [r/OpenaiCodex](https://www.reddit.com/r/OpenaiCodex)
### **Author:** [Fit_Concept5220](https://www.reddit.com/user/Fit_Concept5220/)
### **Vote:** 8
---
tl;dr
The codex harness turns waiting for background work into a loop with repeated model calls, each carrying the existing context even when nothing has changed. Unlike api pricing there is no discount for prompt caching for subscription originated usage so every loop iteration adds to your input token usage. And if you use API you still massively overpay for your input tokens even with cache. ‘goal’ amplifies this by orders of magnitude by automatically starting another turn, but polling anyway burns tokens without it too.
Claude code is engineered in way where suspensions works exactly as intended and goals have proper fallbacks. Codex now ships with similar tools but they only work for astra.
—
the toolchain to independently verify on your personal sessions is here (local scripts - just feed this to your agent) [https://github.com/relux-works/codex-rollout-audit](https://github.com/relux-works/codex-rollout-audit)
---
## Comments 13

- by [unknown](#) **&#x21C5; 3**
  <br/> Unlike api pricing there is no discount for prompt caching for subscription originated usage so every loop iteration adds to your input token usage


    Wait what? Is this true?

- by [unknown](#) **&#x21C5; 4**
  <br/> No.

- by [unknown](#) **&#x21C5; 1**
  <br/> This is true and the only logical explanation why session with 98% cache drains limits. Please read the blog. And even if it’s somehow not true and cache hit input tokens are discounted in subscription same as api, you still ‘billed’ with order of magnitude more input tokens than with proper harness.

- by [unknown](#) **&#x21C5; 2**
  <br/> Your post is correct regarding the issue; I am not saying otherwise. Your comment about cached input not being discounted is incorrect.

Remove that part and simply say that the constant recaching is so heavy that it consumes your usage, and it would be fine. We also do not know the actual conversion formula for plan usage, as it is not merely a token-to-usage ratio.

If there was no discount, id be using my 20x plan in less than 10minutes instead of every few days.

The post is good, but you went off track a bit and it hurts everything else you said; that is all, do of it as you will.

- by [unknown](#) **&#x21C5; 1**
  <br/> I appreciate how you stand for factual correctness and you are right in that regard but I will not correct the post simply because after all the investigation the non-fact that cache hit input tokens are not discounted is the only explanation of the data I see from logs.

I could be wrong with that in the end but as you pointed - it does not really matter. I am human after all and ok with being wrong.

Also, in the original post I state the issue much more accurately

- by [unknown](#) **&#x21C5; 2**
  <br/> The cache demolishing your usage doesn't need to be full price to do so; it just needs to cost something. If you have hundreds of millions of cached tokens more than you used to for the same output, it will set fire to your usage and costs, discounted or not. But in the end, your point still stands, no question there.

It is one of multiple small problems going on at the moment. Another one is the hover verification loop, which needs to be explicitly limited as per OpenAI's team. I saw a couple of posts today going over the few problems that are piling up.

- by [unknown](#) **&#x21C5; 1**
  <br/> Yes, cached tokens on the API are discounted.

- by [unknown](#) **&#x21C5; 0**
  <br/> There is no public formula what goes into subscription but it’s the only logical conclusion you get after analysing that much logs from problematic sessions. And even if not exactly correct, the misbehaviour we described still leads to ~10x more usage from input tokens because they still charge toll for cache hits

- by [unknown](#) **&#x21C5; 2**
  <br/> That makes sense, it explains why my tokens disappears when trying coding with Astra and doing reviews and plans is OK. It's running the big test suite that takes a lot of time.

- by [unknown](#) **&#x21C5; 2**
  <br/> Aaaaah! Dammit. Why did I trust it just works out the box? Tibo promised! I have then wasted so many damn tokens

- by [unknown](#) **&#x21C5; 2**
  <br/> Reset pls

- by [unknown](#) **&#x21C5; 1**
  <br/> Does codex know?

- by [unknown](#) **&#x21C5; 1**
  <br/> I also noticed this when I tried using Astra as an orchestrator, burned way more tokens compared to when using it as a worker directly.
