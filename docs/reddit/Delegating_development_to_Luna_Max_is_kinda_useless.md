#Delegating development to Luna Max is kinda useless [Visit](https://www.reddit.com/r/codex/comments/1wa29us/delegating_development_to_luna_max_is_kinda/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [HighwayRelevant](https://www.reddit.com/user/HighwayRelevant/)
### **Vote:** 12
---
I was working on my own SDLC for a while, where Sol acted as an architect and delegated development, maintenance, documentation, scouting and verification to Luna max sub agents. It became very reliable and I enjoyed a lot how it worked feeling happy with myself.
But then astra came out and I decided to optimize the SDLC in a better way. So I made it create a benchmark that uses 8 different development scenarios, runs different workflows through it and calculates time, token count and token cost.
And I was shocked, that 95% of tokens and cost were still done by architect (Sol) even though 100% of the code was done by Luna Max. The amount of bureaucracy added quadrupled the cost per task.
So I gave it a goal to run different variations recursively and find the best possible shape to optimize token use without sacrificing requirements for task ledger, documentation, ci/cd, etc.
And it ended up with main agent just doing all the work, and giving short messages to subagents to do scouting, maintenance and testing.
Unfortunately it seems that the idea of an expensive agent just being a manager has the same problems as management in human teams. You as a manager get more busy, efficiency drops, just the total capacity and scalability rises. And sometimes you think you could just do it yourself much faster.
Do with that information what you may, but in my case subagents now are more secretaries that bring coffee and handle the schedule, than actual executors of anything. Maybe the guys that actually used Luna max for management and sol for execution were right. This is still to be tested.
But if you have a workflow I suggest you ask astra to benchmark it. Took around 2 billion tokens in my case unfortunately to get this knowledge.
---
## Comments 16

- by [unknown](#) **&#x21C5; 3**
  <br/> I just dont have enough tokens to have astra or even sol do all the work. It works well for me to have astra write a thorough implementation plan, and have luna execute it. Its rather cheap

- by [unknown](#) **&#x21C5; 3**
  <br/> If it’s manual then yes. Im my case sdlc maintains the full lifecycle of documentation, so it’s less manual.

But switching models invalidates your cache, so I hope you’re doing it in different chats, otherwise, every time you switch to astra you get all Luna context fed into it and pay for the input tokens.

- by [unknown](#) **&#x21C5; 1**
  <br/> You just press 2 instead of 1 when you implement plan. Which clears the context and only hands the plan to luna

- by [unknown](#) **&#x21C5; 2**
  <br/> This makes sense to me, the times that I've just come up with a plan with SOL and then had it actually implement it have worked great and it doesn't seem like it burns tokens. But do you think there are cases like where what you're actually handing off to Luna is kind of like high volume, but really kind of simple stuff? Like let's pretend you're making just a simple SAAS and it had 1 million features for inst, feels to me like it would still be easier to hand it off here. Whereas if you're doing something a little more complex or that required a little more intelligence, maybe this would be the case? What do you think on this?

- by [unknown](#) **&#x21C5; 2**
  <br/> There’s definitely nuance to this, but delegating to Luna also adds overhead. You need to check it after with sol, otherwise it’s kinda yolo. I use verifier agent for this which is also Luna, so at least the results are doublechecked, but the whole bureaucracy seems to burn a lot still.

Also Lunas may redo the whole thing multiple times after fix requests from Sol, and every time Sol has to re-read the whole code. This adds to token cost too I suppose.

I’m working on hardware, hardcore C++ btw, so not checking after Lunas is not possible. I guess on simpler projects you could just let Sol/Astra do the plan and forget it.

- by [unknown](#) **&#x21C5; 2**
  <br/> I'm glad you mentioned you're doing C++ on hardware, I think this may be part of the thing I wonder about: I think there are some rtasks (many of which I am doing) which aer very easy and braindead.. website stuff, and I think Luna might be better for those, because it's probably just going to get them right quickly.

For something more coimplex it totally makes sense to me that a better model would just be the best way to go. I was doing something with a mobile apps earlier and I definitely got much better results by just going to the highest model after a while of sort of fighting with lower ones because I was trying to be efficient - which cost me in the end

- by [unknown](#) **&#x21C5; 2**
  <br/> In general people also do this separation of work for context management as well as it being less error prone as orchestrators can prevent drift and catch errors the implementors are blind to

- by [unknown](#) **&#x21C5; 2**
  <br/> That’s true. It’s more of a scaling thing, than a speed up/make it cheaper thing. But still I was kinda expecting sol to be less busy when all code is made by sol/astra

- by [unknown](#) **&#x21C5; 2**
  <br/> I think claude code has a better default harness for the orchestrator (subagents progress statements can trigger the orchestrator to think again).

In codex I had a hard time balancing the orchestrator between over monitoring and just stopping - you really gotta tweak your agents md and sometimes your prompts too

- by [unknown](#) **&#x21C5; 2**
  <br/> Haven’t played too much with CC harness, but by what I heard, I tend to believe

- by [unknown](#) **&#x21C5; 3**
  <br/> It's been working quite well for me with Luna High - setup here [https://github.com/breko861-hash/sol-luna-codex-orchestrator](https://github.com/breko861-hash/sol-luna-codex-orchestrator)

- by [unknown](#) **&#x21C5; 2**
  <br/> That’s the thing, I’ve been happy with mine too. Until I actually benchmarked it. And that’s what I suggest people do.

- by [unknown](#) **&#x21C5; 2**
  <br/> Fair. I guess it depends on how you prompt it to delegate and what you’re using it for. I’ve also been keeping track of token use by model, and Luna is doing most of the work. My limits feel noticeably longer too.

- by [unknown](#) **&#x21C5; 1**
  <br/> How did you benchmark it? i am looking for a reliable way of figuring out if what i am dong is actually saving me tokens would really appreciate some help with this.

- by [unknown](#) **&#x21C5; 1**
  <br/> I asked Astra to build 8 scenarios of different complexity levels, then run them, compare token counts, split of tokens between models, cost and speed. It required some tweaking, so that you can run full suite, one bench or even pieces of it, took a lot of tokens itself to write the benches, and running them also, but I wanted to know.

- by [unknown](#) **&#x21C5; 1**
  <br/> tell that to my x feed
