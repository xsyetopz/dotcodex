#GPT-6 Astra burns quota 4+ times faster than GPT-5.6 Sol [Visit](https://www.reddit.com/r/codex/comments/1wciwc1/gpt6_astra_burns_quota_4_times_faster_than_gpt56/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Frequent-Goal4901](https://www.reddit.com/user/Frequent-Goal4901/)
### **Vote:** 196
---
So, I tested this separately on each of my two Pro 20x accounts. They are on different computers, and both use only Codex Desktop and the CLI, with the default context limit and settings.
**TL;DR**
- **Less allowance:** On each of my two Pro 20x accounts, the weekly API-equivalent allowance fell from **$2,500+ with GPT-5.6 Sol to about $1,200 with GPT-6 Astra**.
- **Higher prices already counted:** Those dollar figures already use Astra's higher API prices. The allowance reduction is an additional cut.
- **Roughly a quarter of the usage:** Combining the higher prices with the lower allowance leaves me with roughly a quarter of the comparable usage for the same subscription fee.
- **More allowance wasted on cache reads (old work):** The cache-retention setting is dramatically shorter: **30 minutes on Astra versus 24 hours on Sol in Codex**. Alongside Codex cache failures, this means long histories can need processing again. Reusing those histories accounts for most priced usage in long agentic workloads.
Compared with GPT-5.6 Sol's launch prices, GPT-6 Astra costs 2x for input and cached input, and about 1.67x for output. The [API pricing](https://developers.openai.com/api/docs/pricing) and [Codex rate card](https://help.openai.com/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu-credit-based-pricing) don't explain the extra allowance reduction. The [subscription page](https://chatgpt.com/codex/pricing/) says half the messages; what I'm seeing is closer to a quarter.
This is worse than Anthropic restricting Claude Fable 5 to 50% of weekly usage: there, you could still use Claude Opus 5 and other models with the remaining half.
Launch resets are masking the reduction; I think many users will assume it is just Astra's higher price. [Tibo says OpenAI might pause new Pro subscriptions if demand continues](https://x.com/thsottiaux/status/2097559315150426222), while prioritizing existing users. Capacity pressure may explain restrictions, but it doesn't justify sneakily adding an extra multiplier.
I expected better from OpenAI. OpenAI says its mission is to ensure AI [benefits all of humanity](https://openai.com/about/). It points to [nonprofit control of the business](https://openai.com/our-structure/) as a way to protect that mission. **Majority of the people in this world access AI through these subscriptions.** If they behave like this, how can anyone trust them to use increasingly powerful AI for the public good?
GPT-6 Astra is an amazing model, and I really like using it. This is a criticism of how OpenAI has changed the subscription allowance, not of the model itself.
OpenAI has built a lot of goodwill with the community. Please don't lose it all.
How I measured the allowance- **Allowance:** Codex has five-hour and weekly limits. I use allowance, or quota, to mean the budget behind the percentage in the app.
- **What I counted:** Input, cached input (previously processed text the model can reuse), and output (including reasoning), measured in tokens (small pieces of text).
- **How I compared them:** I priced each token type at its [published API rate](https://developers.openai.com/api/docs/pricing), then calculated API-equivalent dollars per percentage point of weekly allowance. Requests and raw token totals miss the price differences.
Open-source tools such as [CodexBar](https://github.com/steipete/CodexBar), [Tokscale](https://github.com/junhoyeo/tokscale), and [T3 Code](https://github.com/pingdotgg/t3code) can track this usage.
[OpenAI lists Pro's 5x and 20x plan multipliers](https://help.openai.com/en/articles/9793128-what-is-chatgpt-pro); [Tibo confirms that 20x means 20 times Plus's weekly usage](https://x.com/thsottiaux/status/2094254532020818191). [OpenCode Go makes its dollar limits explicit](https://opencode.ai/v2/docs/console/go): a regular $10 subscription lists base allowances of $12 per five hours, $30 per week, and $60 per month, with smaller allowances for some models.
Plan
Monthly price
Approx. maximum monthly token value
Claude Pro
$20
$400
Claude Max 5x
$100
$2,000
Claude Max 20x
$200
$8,000
ChatGPT Plus
$20
$700
ChatGPT Pro 5x
$100
$3,500
ChatGPT Pro 20x
$200
$14,000
[Source: SemiAnalysis](https://x.com/SemiAnalysis_/status/2091631658973671900). Its June test exhausted weekly limits on long-running tasks. It measured ChatGPT Pro 20x and Claude Max 20x, then inferred the other tiers. The Claude Max 5x figure should be $4,000, not $2,000.
My results, in API-equivalent dollars:
Weekly allowance
Using GPT-5.6 Sol
Using only GPT-6 Astra
Per percentage point
$25+
About $12
Full allowance
$2,500+
About $1,200
**GPT-6 Astra's higher API prices are already included in these figures.** These are two ways of expressing the same comparison. I recalculated the Astra total when the remaining allowance reached 0%. I cross-checked using several tools above, GPT-6 Astra, Claude Fable, and some manual calculations.
I also followed [Sac's analytics method](https://x.com/Saccc_c/status/2090056975392571538): read the daily-workspace-usage-counts response in DevTools on the [Codex analytics page](https://chatgpt.com/codex/cloud/settings/analytics). My earlier weekly window showed about **54,000 credits**, versus **28,500 with Astra**. At 25 credits per dollar (the credit purchase rate), that is $2,160 versus $1,140. The latter is close to my roughly $1,200 token-based calculation.
Other users' reports- [A Pro 20x subscriber's dollar comparison](https://www.reddit.com/r/codex/comments/1w8vlnr/): $22 to $24 per percentage point with GPT-5.6 Sol, versus about $15 with GPT-6 Astra. The higher API price is already included in the comparison.
- [Nam Le's report on X](https://x.com/namletech/status/2096334362052542899): roughly half the API-equivalent subscription value with Astra versus Sol, using Sol's prices before its price cut, alongside [more cache misses—about 6% versus 1% in his tests](https://x.com/namletech/status/2097024532129230963).
Other things I want to address"Isn't this level of subsidy insane?"A $2,500 API-equivalent allowance does not mean OpenAI spent $2,500 serving that usage. In long agentic workloads, most priced usage is repeated history read from cache, reusing work already done. Calling it subsidized does not make it loss-making.
[OpenAI reportedly reached a 70% compute margin on paying users in October 2025](https://www.theinformation.com/articles/openai-getting-efficient-running-ai-internal-financials-show/); [Epoch AI cites a reported 40% gross margin for Anthropic in 2025](https://epoch.ai/data-insights/company-spending-breakdown).
The big companies that account for most token usage are not paying API prices. They are paying a lot less (probably 20% or even less). Even Codex users can buy credits at 40% discount.
Consumer subscriptions are a small part of the revenue in the [Anthropic estimates](https://x.com/IvanaSpear/status/2075227080657129631). I expect it to be similar for OpenAI.
Doubling total model size doesn't mean doubling serving cost: large batches share the weight cost, while [active parameters and per-request KV cache matter much more](https://www.dwarkesh.com/p/reiner-pope). With those quantities similar, I don't see much changing from the previous model to justify higher prices and an extra allowance cut.
[Hardware and software efficiencies](https://developer.nvidia.com/blog/?p=115040) are dramatically reducing serving costs, through newer chips, speculative decoding, better attention kernels and batching. These gains compound while our allowance is reduced.
Why do I think this is happening?I don't want to assign a malicious motive. But with [OpenAI preparing for an IPO](https://www.axios.com/2026/09/02/openai-anthropic-fable-astra-ipo), I can't help wondering whether pressure to improve margins is part of this.
Consumer subscriptions seem to be a small part of the revenue picture; it feels as though OpenAI is gradually forcing us out. An unexplained cut in what the subscription buys makes that suspicion hard to avoid. How OpenAI responds will matter more than my guess about why it happened.
Codex app and CLI issues make the usage problem worseThe Codex app and CLI have other issues that contribute to this usage problem. A side question, a new fork, or a subagent can inherit the whole conversation yet fail to reuse its cache. We end up paying to process the same history again.
These are the results from my checks in early September. “Cached” means the first request reused the conversation history, not just a small shared block of tool instructions.
Codex baseline
Cache miss?
Continue the current task
No
Resume the same task, with the same surface and settings
No
For the paired checks below, the working tree was unchanged and the existing cache was still live.
Codex action
Cache miss?
Claude Code action
Cache miss?
Change GPT-6 Astra's reasoning effort
Yes
`/effort` on Claude Fable 5.1
No
CLI `/side` question
Yes
`/btw`
No
Desktop fork, including into a worktree
Yes
`/branch`
No
CLI `codex exec fork`
Yes
`claude --resume <id> --fork-session`
No
Subagent with `fork_turns="all"`
Yes
`/subtask` or Agent tool with type `fork`
No
CLI `codex exec fork`
Yes
`/fork` background session
Yes
[OpenAI's API supports changing GPT-6 Astra's reasoning effort while preserving the cache](https://developers.openai.com/api/docs/guides/latest-model), but the Codex client doesn't preserve it in my checks. [A Codex bug report identifies why](https://github.com/openai/codex/issues/42996): the client changes the request in a way that defeats cache reuse.
Claude Code shows that most of these actions preserve the prefix and reuse the cache. There is no reason Codex should need to process the same history again for the same functionality.
Sol used a [24-hour cache-retention setting in Codex](https://github.com/openai/codex/issues/32037), as published response logs confirm. For Astra, OpenAI documents [a TTL setting of just 30 minutes after the last write or reuse](https://developers.openai.com/api/docs/guides/prompt-caching)—a dramatically shorter window to return to a task without paying to process its history again. After a long break, returning to a task or waking several idle subagents can require processing their histories again.
**Why cache misses matter.** Take a task with **200,000 tokens of history in its KV cache**. At [GPT-6 Astra's ordinary input and cache-read rates](https://developers.openai.com/api/docs/models/gpt-6-astra):
- **Cache hit:** $0.20 in API-equivalent usage to reuse that history.
- **Cache miss:** $2 to process the same history again—an extra $1.80.
- **Ten agents missing that cache:** $20 instead of $2, before generating any new output.
**Higher reasoning effort can use less allowance.** [Seth Rose reports on X](https://x.com/sethrose/status/2096669033911529688) that users running Astra High/XHigh with heavier multi-agent workflows were burning much less quota than he was on Light/Medium. [A Pro 20x subscriber on Reddit](https://www.reddit.com/r/codex/comments/1wbdcqz/astra_reasoning_usage_theory/) likewise reported rapid usage on Medium, then only 1–2% usage after an hour on XHigh. So OpenAI’s recommendation to lower reasoning effort can, in some cases, increase the total cost of getting the job done.
The [ARC Prize evaluation](https://arcprize.org/blog/astra) shows how higher effort can lower total task cost.
Subscribers get a worse product experience, and Codex still has many unresolved issues:
- **Slower responses:** [Youssof Al Toukhi measured](https://x.com/Youssofal_/status/2096860453301616837) 36 TPS (tokens per second) on Pro versus 81 through the API at the same reasoning setting. Subscription Fast mode reached only 71 TPS.
- **Missing Pro mode:** My Pro subscription still doesn't offer Pro mode in Codex, although [the API supports it](https://developers.openai.com/api/docs/guides/reasoning#reasoning-mode).
- **Later access:** OpenAI has a more capable internal model, and [Astra reached selected organizations before subscribers](https://openai.com/index/gpt-6-astra/#availability). Paying for a subscription doesn't mean getting the newest capabilities first.
- **Wasteful subagent polling:** Astra keeps checking on subagents instead of waiting for useful results. I’ve experienced this too. [One Reddit user’s log analysis](https://www.reddit.com/r/codex/comments/1wa9c9d/i_investigated_why_gpt6_astra_burns_quota_so_fast/) found 47 empty checks at roughly 30-second intervals, processing 7.13 million input tokens—mostly cached—just to learn that the workers were still running. Even cache hits consume allowance when the same history is read over and over for no useful work.
- **Broken remote control:** Remote control has been atrocious for me. For the past few weeks, trying to open running Codex Desktop chats from the app has just returned an error.
- **Memory that burns tokens:** In my experience, Codex saves unnecessary information, burns tokens maintaining it, and produces no improvement in quality. Theo’s [video on coding-agent memory](https://www.youtube.com/watch?v=Jf54k7tFeEc), focused on Claude Code, raises the same broader concern about accumulating stale or useless information.
OpenAI should put more care into its users and its products. In my experience, Codex CLI is still behind Claude Code. I want OpenAI to improve the harness (the software around the model), preserve caches across ordinary workflows, and make the cost of these actions visible. Other companies like DeepSeek are working to make model access as cheap as possible. DeepSeek has [DSH, its open-source harness](https://github.com/deepseek-ai/deepseek-harness) and [infrastructure that reuses cached prefixes to reduce users' costs](https://api-docs.deepseek.com/guides/kv_cache/). OpenAI, despite being so far ahead, is playing games with subscription usage. I want that effort going into making the product better and cheaper for its users.
I think publicly sharing these measurements is important. Without users comparing notes, changes like this can pass unnoticed and become normal. Codex reports the weekly usage limit after every request. Pair those updates with the token counts in the session logs, and you can easily track allowance consumed alongside API-equivalent spend. Or you can use [Sac's analytics method](https://x.com/Saccc_c/status/2090056975392571538). I hope people share and upvote this. If you have questions about the methodology or want to check the numbers yourself, I'd be happy to help you do that.
**TL;DR**
- **Less allowance:** On each of my two Pro 20x accounts, the weekly API-equivalent allowance fell from **$2,500+ with GPT-5.6 Sol to about $1,200 with GPT-6 Astra**.
- **Higher prices already counted:** Those dollar figures already use Astra's higher API prices. The allowance reduction is an additional cut.
- **Roughly a quarter of the usage:** Combining the higher prices with the lower allowance leaves me with roughly a quarter of the comparable usage for the same subscription fee.
- **More allowance wasted on cache reads (old work):** The cache-retention setting is dramatically shorter: **30 minutes on Astra versus 24 hours on Sol in Codex**. Alongside Codex cache failures, this means long histories can need processing again. Reusing those histories accounts for most priced usage in long agentic workloads.
---
## Comments 76

- by [unknown](#) **&#x21C5; 29**
  <br/> Can anyone tell me if Sol is "back to normal" after the pre-Astra-launch madness?

- by [unknown](#) **&#x21C5; 6**
  <br/> For me sol went to shit and hasnt recovered since astra launched

- by [unknown](#) **&#x21C5; 2**
  <br/> Same, before I never reached limits, now a few prompts and it's done.

- by [unknown](#) **&#x21C5; 17**
  <br/> Haven’t used sol. Astra is so much better except the usage limits that there is no point. Astra low/medium can do everything better than sol ultra

- by [unknown](#) **&#x21C5; 7**
  <br/> true, i've never had to use anything higher than Astra-medium. Well, I’m also afraid for my usage lol

- by [unknown](#) **&#x21C5; 3**
  <br/> I use Astra medium to plan and sol medium to code. It works fine tbh.

- by [unknown](#) **&#x21C5; 1**
  <br/> "Works fine" you're probably getting a better result than 90% of the people here, lol.

- by [unknown](#) **&#x21C5; 1**
  <br/> I've used high to do some deep level research and planning, no idea if I need to but when I want it to be sure and actually detail out those plans I just feel medium might be too low

- by [unknown](#) **&#x21C5; 2**
  <br/> That it's better, no doubt it.

But whether Astra may complete more work better within set limit vs Sol alone vs Sol + Astra as advisor, this is much more interesting question, I think.

- by [unknown](#) **&#x21C5; 2**
  <br/> Yesterday I was using sol for a moment after trying astra and it felt like 2023 chatgpt, a simple "are you sure about that?" was enough for it to completely change its opinion on something it spent 20+ minutes thinking about. Astra feels more confident in itself when asked the same (I think that hallucination benchmark might be right). Yes I was just "vibecoding" in something I don't really know a lot about, but I don't remember sol being like that when it came out. Maybe I'm just biased because with 5.6 launch it was the first time I bought a subscription and used work mode and was really impressed by it, so maybe I just didn't pay attention to things like this. Btw astra is so fast that at first I didn't trust it lol I thought it was just making stuff up

- by [unknown](#) **&#x21C5; 1**
  <br/> Kind of unrelated but I just tested out Gemini 3.8 Flash and it was just like the 2023 ChatGPT.  Same problem, any rebuttal or questioning and it went stright into syncophant mode.  It reminded me how far Claude Code and Codex have come (and how far behind Gemini is).

- by [unknown](#) **&#x21C5; 12**
  <br/> I'm running $20 USD plans on both Claude and Codex, but the token value comparison feels completely broken now.

According to my /stats usage on the Claude CLI, I can easily process up to 1B tokens a day on Sonnet + Opus across three 5-hour windows. Meanwhile, 5.6 Terra + Sol cuts me off around ~200M tokens daily, even when factoring in cache hits.

Codex is offering way less token volume than Claude for the same monthly cost. Is anyone else experiencing this?

- by [unknown](#) **&#x21C5; 3**
  <br/> yep same here. been working on a project divided into multiple phases, one phase takes approximately ~20% of weekly usage in Claude while approximately around ~60% in Codex. (both in the $20 priced plan). This equates to around 2 5hr sessions with Claude and around 4+ 5h sessions with Codex

- by [unknown](#) **&#x21C5; 1**
  <br/> No point in using terra. It's broken. It's better to use Sol low/medium instead of it.Astra low/medium + Sol low/medium should work better than your current setup.Just tell Astra to not poll subagents repeatedly.

- by [unknown](#) **&#x21C5; 5**
  <br/> I'm not sure of the claim that gpt-5.6-sol used 24 hour cache. I remember seeing that a while ago and my understanding is that change came with the gpt-5.6 release or maybe shortly thereafter. The logs in that source are from july 9, so it's very possible this was in a period of time where they changed the cache policy for 5.6.

- by [unknown](#) **&#x21C5; 4**
  <br/> Yeah, that cache claim is pretty flimsy. “30 min vs 24 hours” isn’t literally observed cache lifetime. Those are retention modes/eligibility guarantees, not proof that Astra always expires at 30m and Sol always survives 24h.

- by [unknown](#) **&#x21C5; 0**
  <br/> I checked my logs too. The cache was preserved for a lot longer in Sol compared to Astra where it's always a miss after 30 min.

- by [unknown](#) **&#x21C5; 5**
  <br/> The cache misses and extreme cost of “empty” checks by an Astra agent acting as an orchestrator (which its default training seems to highly encourage it to do) are cripplingly bad problems. I feel like my subscription and banked resets were stolen due to how insanely fast these problems burnt through my usage.

Yes I am an idiot for assuming “Astra is just working the way OpenAI intends, let it cook”, but seriously, it’s very frustrating figuring out after the fact how much “dead token expense” is baked into Astra unless you carefully model its skills, agents.md and hooks to prevent it from every losing its cache or doing dead subagent handling/checks.

Arghhh

- by [unknown](#) **&#x21C5; 3**
  <br/> It's very annoying.Good to see at least my post helped someone.If they optimize the harness, the current usage could probably last 10-20% longer. These are also not new issues.I guess they feel spending 20 million $ stealing credit from actual human mathematician solving the navier stokes problem is more important than working on improving their product.

- by [unknown](#) **&#x21C5; 3**
  <br/> Good analysis, thanks

- by [unknown](#) **&#x21C5; 3**
  <br/> Shocking ...

- by [unknown](#) **&#x21C5; 4**
  <br/> I'd be really curious if you ran tibotattle (install from tibotattle.com) and compared what it thinks your resets are versus the numbers you've got. I'm just about to launch an update which will give even more per project and model usage numbers so you can see where the usage going.

I say that because across the community data to date, Sol is actually very price efficient and it is the other models (including Astra) that is less efficient compared to the API.

Let me know if you run into any problems!

 
       [](https://preview.redd.it/gpt-6-astra-burns-quota-4-times-faster-than-gpt-5-6-sol-v0-bhifwsuk1poh1.png?width=1221&format=png&auto=webp&s=0d8956c05ad36cf903c8d2b9aa368877ec7ef55a)

- by [unknown](#) **&#x21C5; 0**
  <br/> the color is so confusing

- by [unknown](#) **&#x21C5; 2**
  <br/> [](https://preview.redd.it/gpt-6-astra-burns-quota-4-times-faster-than-gpt-5-6-sol-v0-4ehtsvcg4poh1.png?width=1218&format=png&auto=webp&s=13cb75c559ae7f9f09b39b3c49069337419cc181)
      
    Yeah sorry. You can view the graph yourself and then the models have hovers

- by [unknown](#) **&#x21C5; 2**
  <br/> that matches with my experience, 5 times faster than Sol. from 5 days to 1 day (20 x plan)

- by [unknown](#) **&#x21C5; 2**
  <br/> Can confirm with my own use of it, Astra Light burns usage about 4-5x faster than Sol Medium.

- by [unknown](#) **&#x21C5; 2**
  <br/> People need to stop blindly putting plus at 700$ because some company said it was months ago, current day plus is around 400$ of sol usage at least

- by [unknown](#) **&#x21C5; 1**
  <br/> So they measured it over a month so its a bit more than 4 weeks so i think they considered an extra week. So its a bit inflated

- by [unknown](#) **&#x21C5; 1**
  <br/> Even then, it's 100$ per week

- by [unknown](#) **&#x21C5; 2**
  <br/> API-equivalent dollars aren't the same thing as quota though. If OpenAI changes API pricing but leaves subscription limits alone, your inferred weekly budget changes on paper even though the actual quota didn’t.

Also, did you measure equal work? The important question is how much quota each model uses to solve the same task successfully, not how much quota the same number of tokens costs.

And this seems more like a before-and-after test, no? It's not an A/B test because you're measuring pre-Astra Sol vs current Astra.

I think a lot of data here is really interesting and can potentially be useful, but the conclusions drawn from the data have a lot of holes right now.

- by [unknown](#) **&#x21C5; 1**
  <br/> "API-equivalent dollars aren't the same thing as quota though"It is though. Every subscription is like this check claude, opencode, any chinese ai token plan like glm or kimi.

- by [unknown](#) **&#x21C5; 2**
  <br/> OpenAI at some point lowered Sol's token price but explicitly say the included 5-hour/weekly limits are unchanged. So if I recalculate your Sol usage using a changed new API price, its "$-equivalent quota" suddenly changes even if your actual subscription quota didn't change at all.

Your logs can still show Astra burns the meter faster. I'm just saying converting that meter into API dollars doesn't prove the subscription literally contains a fixed dollar budget.

Subscription usage can absolutely be token-weighted. But drawing conclusions from API-equivalent dollars being correlated to the quota is very misleading.

- by [unknown](#) **&#x21C5; 1**
  <br/> It's not really misleading if you think of it as the value you get from it. I think you are probably right overall. Openai doesnt assign a dollar value to the subs but there's likely token quotas per model internally. But if those do not line up with the API prices, it feels very strange and from the outside seems hard to understand. After all, why would you get 2500$ in Sol value, but only 1200$ in Astra?

- by [unknown](#) **&#x21C5; 0**
  <br/> Tokens convert to dollars.Stop falling to these companies making things deliberately obtuse.Openai is deliberately confusing you so people will stop thinking and believe whatever they say.

[https://chatgpt.com/codex/pricing/](https://chatgpt.com/codex/pricing/) here they say in a table if you scroll down that astra gives half the number of messages/ tokens compared to Sol but that’s wrong. Astra in practice gives less than 1/4 th

- by [unknown](#) **&#x21C5; 2**
  <br/> [https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex?utm_source=chatgpt.com](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex?utm_source=chatgpt.com)

> The table below shows estimated local messages per five-hour period. These are not fixed message limits. Actual usage varies by task, model and settings, and weekly limits may also apply.

If you want reliable data, your methodology should be a controlled A/B test using identical tasks, not a before/after comparison of aggregate account usage.

- by [unknown](#) **&#x21C5; 2**
  <br/> AI Generated BS,


      
        
          
              Claude Max 5x
            
              $100
            
              $2,000
            
        
        
      

      
        
            
                Claude Max 20x
              
                $200
              
                $8,000
              
          
      
    That is wrong, they 4x your 5h limit and 2x your monthly, so


      
        
          
              Claude Max 5x
            
              $100
            
              $2,000
            
        
        
      

      
        
            
                Claude Max 20x
              
                $200
              
                **$4,000**

- by [unknown](#) **&#x21C5; 1**
  <br/> [Source: SemiAnalysis](https://x.com/SemiAnalysis_/status/2091631658973671900). Its June test exhausted weekly limits on long-running tasks. It measured ChatGPT Pro 20x and Claude Max 20x, then inferred the other tiers. The Claude Max 5x figure should be $4,000, not $2,000.

I specifically mentioned it. What AI bullshit? Everything is handwritten with some light AI editing.

- by [unknown](#) **&#x21C5; 1**
  <br/> Claude Max 20x is 2* Claude Max 5x except for the 5h limit where it's 4*, that part. that part is llm generated. Even on their signup page, you see that the Claude Max 20x has a 50% discount label on it, and if you track your usage in the same time with the same models, when you max the 5h limit on the Claude Max 20x plan you end up using double the limits of the Claude Max 5x plan that maxed up the 5h limit.

- by [unknown](#) **&#x21C5; 1**
  <br/> So i said in the post and again in my comment that max 5x gives 4000$ which is half of 8000$ which is max 20x allowance

- by [unknown](#) **&#x21C5; 1**
  <br/> aint nobody gonna read your 3 volume saga mate

- by [unknown](#) **&#x21C5; 1**
  <br/> Is luna still costing 2x usage on subscription?

- by [unknown](#) **&#x21C5; 1**
  <br/> I think so.  I remember someone complaining giving luna as an example and they then bumped the limits of luna.  It's so fucked up.

- by [unknown](#) **&#x21C5; 1**
  <br/> One correction. Plus account is ~$400-$440 a month now, not $700. Measured at the maximum allowed model, which is Sol; at current promotional prices.

- by [unknown](#) **&#x21C5; 1**
  <br/> api estimates of my own usage from t3 code, looks low because cache saved a ton and isn't included but gives a good relative pricing.


      
        
          
              model
            
              cost/mtok
            
        
        
      

      
        
            
                astra
              
                $1.50
              
          
            
                sol
              
                $0.52
              
          
            
                terra
              
                $0.30
              
          
            
                luna
              
                $0.03

- by [unknown](#) **&#x21C5; 1**
  <br/> please open an issue on [https://github.com/openai/codex/issues](https://github.com/openai/codex/issues) and also use the /feedback command to send open AI your analysis! ❤️

- by [unknown](#) **&#x21C5; 1**
  <br/> Lot of these issues have already been reported

- by [unknown](#) **&#x21C5; 1**
  <br/> Might be the end of subsidization of frontier models. Same applies to Fable at Claude Code subscription (see [https://www.reddit.com/r/ClaudeCode/s/QPp04qGI5i](https://www.reddit.com/r/ClaudeCode/s/QPp04qGI5i))

- by [unknown](#) **&#x21C5; 1**
  <br/> Maybe. I hope muse watermelon and grok 4.7 are amazing so OpenAI and Claude have actual competition

- by [unknown](#) **&#x21C5; 1**
  <br/> Did you burn your quota writing this massive text blob?

- by [unknown](#) **&#x21C5; 1**
  <br/> Did anyone else summarize this with AI?

- by [unknown](#) **&#x21C5; 1**
  <br/> Read the TLDR

- by [unknown](#) **&#x21C5; 1**
  <br/> I wouldn't be so bothered by the price if it didn't take Astra 6 hours to answer "What is 1 x 2?".

- by [unknown](#) **&#x21C5; 1**
  <br/> You are basing on the launch prices but in my experience: I used only sol, 6 days ago,after banked reset, i burned weekly quota in 20 hours. Using single session, xhigh, 50k code written. When quota gets reduced, or same task eat more magic tokens compared to 1 month ago, no benchmark or diagnostics fits into meaning. All the graphs, prices, cost performance metrics gathered at the launch will be thrown into garbage bin. There is no verification, we are getting same token per task and token per quota and quota per 20x 5x etc anywhere. Because they can modify any value on the formula, without we knowing, while everyone stuck on official api prices try to figure this out...

I feel like, they dont have compute to sustain developer userbase migrated from claude. They cannot admit it publicly because its the worst thing they can do atm. So they don't want to lose the user base and have to resolve this doing shady business.

- by [unknown](#) **&#x21C5; 1**
  <br/> I have the $100 Pro and yes Astra burns through way quicker, but it's quite a bit better... I'm settling for Astra Medium or High and using reset while I have them... those are life savers

- by [unknown](#) **&#x21C5; 1**
  <br/> Seeing similar numbers on my local subscription statistics. OpenAI advertises Astra as 2.5x more expensive than Sol at API rates, but on the subscription it's more like 3.5x. A little disappointing.

- by [unknown](#) **&#x21C5; 1**
  <br/> Best theory: Astra doesnt reveal thinking tokens in the output estimations you have available. Astras thinking is in Latent Space. This is the theory.

Estimating api token value over subscription discoverable token usage isn’t perfect.

- by [unknown](#) **&#x21C5; 1**
  <br/> I used to work for a dozen prompts and took at least 1 hour before my 5h quota burn out, now with astra, is two or three prompts and about 15minutes

- by [unknown](#) **&#x21C5; 1**
  <br/> I hope Tibo reads this.

- by [unknown](#) **&#x21C5; 3**
  <br/> I more so want other content creators to see this and investigate it and make content about this.This is very unethical behavior.If they want to reduce it then do it openly

- by [unknown](#) **&#x21C5; 2**
  <br/> Unethical? The AI companies' entire business model is based on IP theft.

- by [unknown](#) **&#x21C5; 1**
  <br/> Forget it brother. No big AI creator would close their door to an opportunity of a partnership with one of the frontier labs by calling them out.

- by [unknown](#) **&#x21C5; 1**
  <br/> Probably Theo would be willing to do it. He did call out claude and codex on lot of their bullshit. Someone needs to bring it to his attention.

- by [unknown](#) **&#x21C5; 0**
  <br/> You act as though Codex users know more about the service that those who created and maintained it.

- by [unknown](#) **&#x21C5; 0**
  <br/> For those who want to see what Tibo is saying without the billionaire fascist complicity this will work [https://xcancel.com/thsottiaux](https://xcancel.com/thsottiaux)

- by [unknown](#) **&#x21C5; -4**
  <br/> Low effort AI post. Claude max x20 is roughly x8 to x10, it's the 5h limit that's x20. Since you can't get the basics right why should I trust anything else?

- by [unknown](#) **&#x21C5; 1**
  <br/> As I said in another post[Source: SemiAnalysis](https://x.com/SemiAnalysis_/status/2091631658973671900). Its June test exhausted weekly limits on long-running tasks. It measured ChatGPT Pro 20x and Claude Max 20x, then inferred the other tiers. The Claude Max 5x figure should be $4,000, not $2,000.

I specifically mentioned it. What AI post? Everything is handwritten with some light AI editing.

- by [unknown](#) **&#x21C5; 0**
  <br/> "inferred", well I can infer that my subscription uses the right amount of astra tokens as well.

- by [unknown](#) **&#x21C5; 1**
  <br/> I gave an independent source. The table are not my own numbers. I specifically linked where i got them from. For my own numbers I state them. You should work on your reading comprehension.

- by [unknown](#) **&#x21C5; 1**
  <br/> Yes you didn't fact check it, therefore you're unreliable for gathering information

- by [unknown](#) **&#x21C5; 1**
  <br/> I did fact check it. Thats why there is a note after the table. I didn’t modify the table because that was from semi analysis. I added the correction after it.

- by [unknown](#) **&#x21C5; 1**
  <br/> I don't understand how you fucked it up

Your correction is wrong, extremely. You market the X5 plan as 10 times higher than the pro. While [https://pasqualepillitteri.it/en/news/5128/anthropic-sued-claude-max-20x-usage-limits](https://pasqualepillitteri.it/en/news/5128/anthropic-sued-claude-max-20x-usage-limits) the lawsuit states the x20 plan is between x6 to x8 times higher than the pro plan.

And I'm the one with bad reading comprehension. How can I trust you with anything else you've posted when you double down on incorrect data?

- by [unknown](#) **&#x21C5; -2**
  <br/> And then what?  You don’t have to use it.

- by [unknown](#) **&#x21C5; 2**
  <br/> So saying one thing in the docs  [https://learn.chatgpt.com/docs/pricing](https://learn.chatgpt.com/docs/pricing) and then doing another thing in practice is unethical and is false advertising.This change was also done silently.

If you think its alright, then so be it. I am just informing everyone. You know my view on it.AI is increasingly becoming indispensable. It's almost like a utility.If your electricity provider or internet provider did this, would you not be angry?

- by [unknown](#) **&#x21C5; 1**
  <br/> lol.  It’s a “utility” so my socialist government should give it to me.

- by [unknown](#) **&#x21C5; 1**
  <br/> Seriously though, it’s obviously shady when you get use percentages rather than actual units….like tokens or sth :,
