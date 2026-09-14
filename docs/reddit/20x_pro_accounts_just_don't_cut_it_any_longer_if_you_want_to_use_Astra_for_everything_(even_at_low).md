#20x pro accounts just don't cut it any longer if you want to use Astra for everything (even at low) [Visit](https://www.reddit.com/r/codex/comments/1wc3082/20x_pro_accounts_just_dont_cut_it_any_longer_if/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [alwaysshouldbesome1](https://www.reddit.com/user/alwaysshouldbesome1/)
### **Vote:** 59
---
... is the realization I've come to. Even with a medium orchestrator, light implementer, medium reviewer, I burned 100% in around 24 hours.
But it's frustrating figuring out what you should use instead because token price vs capability is far from crystal clear. I switched just now to using luna max for implementation because I've seen so many people swear by it here. I also asked Astra to do 3 implementation tests between Luna max and Astra medium and while Luna did use 3-5 as many output tokens and was 2-3x slower, the token cost comes out to only 10% of Astra. There were definitely more bugs slipping through (that I'm still using Astra medium to catch).
So yeah I guess shit's gonna take a lot longer and it kinda sucks to have all this power but not be able to use it fully. I don't want to buy extra credits because they're ridiculously expensive and I also don't want to juggle two accounts. time OpenAI launched 30-50x pro plans?
---
## Comments 78

- by [unknown](#) **&#x21C5; 34**
  <br/> They bout to make 500 dollar Ultra plans lol

- by [unknown](#) **&#x21C5; 26**
  <br/> Only to then release GPT 7 Betelgeuse and it costs 20x what Astra does

- by [unknown](#) **&#x21C5; 9**
  <br/> Calling it 3 times in the mirror and your usage resets

- by [unknown](#) **&#x21C5; 7**
  <br/> loving that model name

- by [unknown](#) **&#x21C5; 3**
  <br/> Sorry, I’ve already decided it’s going to be GPT-7-Galactus

- by [unknown](#) **&#x21C5; 4**
  <br/> Its probably going to be a 1000 dollar plan actually they've been dancing around this sinse o1

- by [unknown](#) **&#x21C5; 3**
  <br/> That's crazy ngl. That's like a phone a month

- by [unknown](#) **&#x21C5; 0**
  <br/> A phone for peasants, the iPhone Duo is 2k 🧐

- by [unknown](#) **&#x21C5; 1**
  <br/> The Apple Way™

- by [unknown](#) **&#x21C5; -1**
  <br/> Its already 300 in Canada

- by [unknown](#) **&#x21C5; 5**
  <br/> And like 280,000 in Chile.

- by [unknown](#) **&#x21C5; 8**
  <br/> Why not try doing astra as the main orchestrator and doing like luna high fast subagents for all work with sol as a final reviewer. I would like to try this but im only on the 20$ plan :(

- by [unknown](#) **&#x21C5; 1**
  <br/> This is even worse. I tried it during one of my banked resets, worse results same 24 hour roughly of usage.

- by [unknown](#) **&#x21C5; 1**
  <br/> I'm sort of separating "director" (mine's Astra Low) who just tells the agents what to do vs planning/design probes, I use Astra medium/high agents for those, but I've no idea if it's sensible (Astra low told me it was lol but it agrees with everything)

really not sure when it makes sense to use sol and terra vs luna or astra...

- by [unknown](#) **&#x21C5; 1**
  <br/> Maybe ask astra to do some research on when to use what model, then try out what it says. Maybe astra makes the plan and all the sub-agent has to do is implement it without thinking much, then back to astra to review? I just kinda try anything and see what feels the best, its a fine balance of quality work and working within your usage limits/budget.

- by [unknown](#) **&#x21C5; 3**
  <br/> I have, it checks the docs, and always seem to come back and say "yeah that makes sense" because I think the docs are so vague basically any workflow sounds arguably reasonable

- by [unknown](#) **&#x21C5; 1**
  <br/> You should use something like pre-walk instead: [https://mcpmarket.com/ko/tools/skills/prewalk-workflow-planner](https://mcpmarket.com/ko/tools/skills/prewalk-workflow-planner)

You can make your own skill as well with the same concept. It's proven to give better results and better usage.

- by [unknown](#) **&#x21C5; 1**
  <br/> I see waterfalls!!!

- by [unknown](#) **&#x21C5; 0**
  <br/> Haven't tried Sol review, but Astra will reject or rewrite every single line of Luna code. I use Astra low for writing, and the reviewer Astra barely touches it.

- by [unknown](#) **&#x21C5; 5**
  <br/> I'm finding the same problem.  I hit my limit on the $200 in less than 24 hours.  Thank goodness for my banked reset or I would have been sitting on my hands for the rest of the week.

- by [unknown](#) **&#x21C5; 5**
  <br/> Yes but... you (and I) are gonna run out of them. Tibo is essentially hinting (with the "we pullin' them levers" tweet) they're probably not gonna be so generous with resets going forward.

- by [unknown](#) **&#x21C5; 1**
  <br/> I just bought the $200 plan today.. If I run out, do I still get the "unlimited" access to gpt-5.6 models? Frankly, been terrified to even let Astra touch anything after seeing what it would do to my Plus accounts usage for what seemed like even the simplest of tasks.

I kind of miss the 5 hour limit guard rail. Feel like if I fuck around right now, I could be sitting around for a week waiting to get anything at all done.

- by [unknown](#) **&#x21C5; 2**
  <br/> This has been a moving target, but I believe there is now a weekly cap on 5.6 chat queries at effort levels higher than Instant

- by [unknown](#) **&#x21C5; 4**
  <br/> I noticed the same. Currently I think the only way make the 20X plan work with Astra is probably with Terra or Sol implementors. Luna has too many bugs that will burn downstream Astra reviewer/orchestrator tokens

- by [unknown](#) **&#x21C5; 1**
  <br/> Do terra or sol actually end up cheaper in terms of spent tokens though? OpenAI's messaging on this is so confusing.

- by [unknown](#) **&#x21C5; 4**
  <br/> Its complicated because if depends on how complicated the task is, its basically an optimization problem that depends on the expected number of times other agents need to "jump-in" and the cost of their "jump-in". It gets egregious when implementation keeps failing and now you burn reviewer tokens in addition to the orchestrator (which also starts to suffer context pollution). however, if the cheap model can one-shot the problem its great and much cheaper

- by [unknown](#) **&#x21C5; 3**
  <br/> I have the 20x plan. I've used 70% of it since the reset. I've used Astra about 70% of that time, others around 30%. It doesn't seem burn tokens near as fast as Fable does, without question.For me it seems fairly reasonable.  Are you working with an extremely large code base?

- by [unknown](#) **&#x21C5; 1**
  <br/> I mean maybe it is reasonable in terms of what you get for the money, but you are also using up your entire weekly limit in 2-3 days, right? So... i mean it's also not reasonable that the most expensive plan can't really be used professionally full-time without additional purchases

- by [unknown](#) **&#x21C5; 3**
  <br/> You are paying $200 a month for a massively capable assistant that does (and is capable) of doing hundreds of tasks for you. Do you all not hear yourselves?? Actual developers couldn’t do a fraction of what astra does in a day and they make between $350-700 / day.

- by [unknown](#) **&#x21C5; 2**
  <br/> i mean it's also not reasonable that the most expensive plan can't really be used professionally full-time without additional purchases


    if you look at the OP i'm specifically suggesting there should be plans above 20x

- by [unknown](#) **&#x21C5; 3**
  <br/> Feeling super limited on 20x as well. I'm only running astra on medium or light, and one thread (no subagents) is enough to kill usage after two days. I used to be able to run sol max from two or three threads and last most of the week. They really need to get more compute online, this just sucks and doesn't feel worth $200.

- by [unknown](#) **&#x21C5; 7**
  <br/> Then don't use Astra for everything.

It's your subscription, you do what you want.  But if you only drive with the pedal all the way to the floor, you can't complain about the gas mileage.

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra low doesn't really feel like pedal to the metal.

And I don't let my director wait on threads either, he comes to a full stop and only wakes up when he gets finished reports (but they're frequent enough that he never idles beyond the 30 min cache limit either)

So I don't know. I think I do get to complain

- by [unknown](#) **&#x21C5; 3**
  <br/> There isn’t a big difference between Astra Low and Astra High in usage. The model is so token efficient that most of the cost comes from input tokens anyway - which aren’t nearly as dependent on thinking effort as output tokens.

- by [unknown](#) **&#x21C5; 2**
  <br/> yeah I just used up all my quota on 20x since yesterday. And I am using pi working on all the planning myself. I would need quota doubled at least probably

- by [unknown](#) **&#x21C5; 2**
  <br/> Not even everything. Just 2 hours a day and low reasoning will have you hit your limit before the end of the week.

In terms of it being an orchestrator, seeing lots of people on X saying that it still blows through limits.

Also feel like they nerfed Sol, my Sol medium sessions today are slow af and perform like Terra.

What I’m going to try next is sticking with Sol and allowing it to use an Astra High advisor or if my tasks have any diagraming work, I’ll farm that out to an Astra worker.

- by [unknown](#) **&#x21C5; 2**
  <br/> What I’m going to try next is sticking with Sol and allowing it to use an Astra High advisor or if my tasks have any diagraming work, I’ll farm that out to an Astra worker.


    maybe this is the way, who knows

- by [unknown](#) **&#x21C5; 4**
  <br/> Im using astra max all day i sleep while it works it takes me 4 days to reach 20% of my weekly limit what do you do?

- by [unknown](#) **&#x21C5; 12**
  <br/> The question is what do *you* do that you aren't even using up tokens?

- by [unknown](#) **&#x21C5; -1**
  <br/> Oh, I use a lot of tokens, but I don’t chat with Astra. It follows the files I’ve already written, while I only check and review its work.

- by [unknown](#) **&#x21C5; 2**
  <br/> Same, and it is an absolute glutton with my token usage.  Are you getting it to go idle for long stretches or something?  Or spinning down to lower models and only invoking Astra infrequently?

- by [unknown](#) **&#x21C5; 1**
  <br/> I was spinning down to lower models but then realized how little Astra Max was burning so I've been running three projects in parallel using it since the last reset on Monday pretty much every hour I'm awake and just hit 50% on the 20x Pro a little bit ago with 3 banked resets on my account unused.

I think another reset occurred somewhere in the middle but I was so focused I can't remember how far in.

The progress and quality has been insane. I wasn't ready to start doing user testing and loading data on two of the projects so now I'm the bottleneck.

I just had Astra reconfigure my local inference server to build a pipeline for scanning data from a video and then using it to train a local model with LoRA that can then be used to generate more test data. Just getting all that to work probably would have taken me weeks just last year and Astra Max had it all configured in less than 2 hours.

- by [unknown](#) **&#x21C5; 1**
  <br/> That's cool, but how did you get it to use dramatically less usage than everyone else is seeing?

- by [unknown](#) **&#x21C5; 5**
  <br/> What is that agent doing? Hitting a rest tool? Sipping tokens through the worlds smallest pipe? Show me the Astra max agent doing real work 24/7 for 4 days on a $200 plan no resets, this dude probably fat fingered and launched Luna

- by [unknown](#) **&#x21C5; 3**
  <br/> oh yeah? use it astra ultra on /fast and after 4 days of 24/7 usage I’m only down 2%. what are you doing wrong?

- by [unknown](#) **&#x21C5; 1**
  <br/> Why would I even use Ultra? It’s basically Max with subagents that burn tokens for no reason. And they burn a ridiculous amount too over 300k tokens each on every run, just to send an audit back to the main agent. Ultra is supposed to be something you use occasionally for the hardest tasks, not something you run with /fast all day. If you’re doing that, blame yourself.

- by [unknown](#) **&#x21C5; 3**
  <br/> 😂 he's being sarcastic

- by [unknown](#) **&#x21C5; 1**
  <br/> I genuinely am using ultra all day and I make like 5 PRs, thousands of lines of code per day at my wagie job

- by [unknown](#) **&#x21C5; 1**
  <br/> This thing only works if you are running astra max in one session.

- by [unknown](#) **&#x21C5; 2**
  <br/> x100 Ultra max $500

- by [unknown](#) **&#x21C5; 2**
  <br/> I accept

- by [unknown](#) **&#x21C5; 1**
  <br/> OP is an OpenAI employee, I just can't prove it.

- by [unknown](#) **&#x21C5; 2**
  <br/> I wish. Much more likely a future member of the permanent underclass

- by [unknown](#) **&#x21C5; 1**
  <br/> SOL 5.6 xhigh is quite good.  Use 5.6 xhigh as your orchestrator, astra as your planner, and reviewer on major plan checkpoints, and 5.6 medium as your implementor.

But I also liked codex 5.3, and gpt 5.2, so it's whatever.   I can kick ass with deepseek, or qwen 3.8 flash next if needed.  Except for gemini all these LLM's are pretty sweet.

- by [unknown](#) **&#x21C5; 1**
  <br/> You do not need Astra for most things, I find Sol to be much better and haven't Astra for coding just orchestration. I only let Astra edit when Sol can't get things right in two three tries which happens rarely.

- by [unknown](#) **&#x21C5; 2**
  <br/> But OpenAI's messaging is essentially that Astra ends up cheaper per task than Sol?

- by [unknown](#) **&#x21C5; 1**
  <br/> Cheaper in API prices. This doesn't have to correlate with subscription allowance.

- by [unknown](#) **&#x21C5; 1**
  <br/> Maybe learn how to use it more efficiently? Most of my work is done by Luna agents

- by [unknown](#) **&#x21C5; 1**
  <br/> Are you sure it's this bad or are you seeing the limit issue everyone is complaining about?

[https://www.reddit.com/r/codex/s/qvBGJp13lb](https://www.reddit.com/r/codex/s/qvBGJp13lb)

[https://www.reddit.com/r/codex/s/6qgUlTAD85](https://www.reddit.com/r/codex/s/6qgUlTAD85)

[https://www.reddit.com/r/codex/s/i6VtMZvnqy](https://www.reddit.com/r/codex/s/i6VtMZvnqy)

[https://www.reddit.com/r/codex/s/dj5ld47fGp](https://www.reddit.com/r/codex/s/dj5ld47fGp)

- by [unknown](#) **&#x21C5; 1**
  <br/> Why would anyone need to use Astra for everything?

Maybe "everything" just means wildly different things for different people.

- by [unknown](#) **&#x21C5; 1**
  <br/> Quantize old model, release 10% better model, say it costs 2.5x, repeat every few months

- by [unknown](#) **&#x21C5; 1**
  <br/> 40x when

- by [unknown](#) **&#x21C5; 1**
  <br/> That's why you need 6.

- by [unknown](#) **&#x21C5; 1**
  <br/> True, from a value perspective it makes no sense. Its about 5% better (general not any specific test, they are averaged before people gripe) and cost about 2.5x more.

It seems the price is due to its speed as well which feels faster by default.

I build external harnesses to reduce consumption based upon tools and it still to costly.

For reference, my harness allows Sol Ultra to run for over 7hrs and only use 4%, compared to Astra ultra which (without finished upgrades) seems to use 30%!

- by [unknown](#) **&#x21C5; 1**
  <br/> I swear I just do not see these usage issues. I have had the Pro 20x plan for the past few months, using always 5.5 High, 5.6-Sol High and now 6-Astra High, power through the same amount of use roughly per day and have not seen any big differences in usage. I have never gotten anywhere close to 0%, and I'll have many agents across different projects going at once (but only for ~8 hours a day max)

- by [unknown](#) **&#x21C5; 1**
  <br/> You people are asking them to make it slower, not raise the limits. Find something else to do with your free time. Astra is 10x Sol productivity.

- by [unknown](#) **&#x21C5; 1**
  <br/> Skill issue

- by [unknown](#) **&#x21C5; 1**
  <br/> People need to get lives. I don’t max this as an insult. Astra should be tackling tasks better and faster than previous generations. So, if it’s doing that, go do things. Do you workout? Do you read? Do you have hobbies? It should be much easier to accomplish whatever workload you once had. If AI went away tomorrow you wouldn’t be able to accomplish close to what you accomplish now right? So, take it easy.

- by [unknown](#) **&#x21C5; 1**
  <br/> [](https://preview.redd.it/20x-pro-accounts-just-dont-cut-it-any-longer-if-you-want-to-v0-6kkcwpt4zmoh1.png?width=1291&format=png&auto=webp&s=4798c3ab90a3c07215655aef9698c0f841cf4868)
      
    94% of my weekly yesterday with astra

- by [unknown](#) **&#x21C5; 1**
  <br/> [](https://preview.redd.it/20x-pro-accounts-just-dont-cut-it-any-longer-if-you-want-to-v0-wl4pxff7zmoh1.png?width=1298&format=png&auto=webp&s=fc159a07e4eefdd5af6262b11b8908c1d4d98304)
      
    Entire last week running 2x astra daily

- by [unknown](#) **&#x21C5; 1**
  <br/> It’s the slow ratchet toward pricing this thing where the actual costs and margin will land.

When they’re billing it for what it really costs to build & run, it’ll be more expensive than staff.

- by [unknown](#) **&#x21C5; 1**
  <br/> I too am getting rouhgly 24 hours of usage from astra on the 20x plan.. and i mean using the medium/light reasoning.. kind of insane tbh.

- by [unknown](#) **&#x21C5; 1**
  <br/> One reset per day is my average in 20x. Running two accounts. Still waiting for the reset now. Using Astra Extra High or High only. Stopped using Ultra.

- by [unknown](#) **&#x21C5; 1**
  <br/> Or better yet, buy credits so you can keep going after you run out.... but then when OpenAI glitches you lose it all instantly! YAHOO!!

- by [unknown](#) **&#x21C5; 1**
  <br/> Try this:

[features.multi_agent_v2]enabled = truemin_wait_timeout_ms = 1500000default_wait_timeout_ms = 1500000max_wait_timeout_ms = 1500000

- by [poop_harder_please](https://www.reddit.com/user/poop_harder_please/) **&#x21C5; 0**
  <br/> Use codex-lb and get multiple pro accounts.

Sincerely,

[u/poop_harder_please](/user/poop_harder_please/), owner of 5 Pro 20x accounts.

- by [unknown](#) **&#x21C5; 1**
  <br/> And it works on the same project in parallel?

- by [unknown](#) **&#x21C5; 1**
  <br/> yes!
