#"Stop using random multi-agent patterns" [Visit](https://www.reddit.com/r/codex/comments/1wca46x/stop_using_random_multiagent_patterns/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [harpreetchima](https://www.reddit.com/user/harpreetchima/)
### **Vote:** 221
---
Ahmed works at OpenAI: [https://x.com/ah20im/status/2097503414749909407](https://x.com/ah20im/status/2097503414749909407) and seems to investigate reports of high token usage.
"If needed Astra will delegate efficiently. Forcing the model to delegate to different models would do more harm than good"
---
!["Stop using random multi-agent patterns"](https://preview.redd.it/stop-using-random-multi-agent-patterns-v0-olx8y5vuqmoh1.png?auto=webp&s=a747c4da5736e66d18f219e350aabcfb152a75c9)
---
## Comments 133

- by [unknown](#) **&#x21C5; 46**
  <br/> smh. I did an experiment and let astra do an implementation on its own without using my orchestration workflow and the drift was wild and the result messy. i rolled back and did the same implementation with my established workflow and it was super smooth.

- by [unknown](#) **&#x21C5; 7**
  <br/> It destroyed 48 hours approved work when I was stupid enough to try that. It thought it knew better’s than all the rules and guardrails and just decided arbitrarily to ignore everything.

I now have orchestration by sol and astra is consulted within tight parameters for analysis snd review sometimes. Works really well and does what it’s told.

- by [unknown](#) **&#x21C5; 3**
  <br/> yeah keeping it on a tight leash still seems to be important. i don't think it's stupid to try .. it's good to know how a new model behaves without a tight harness. i'm just really shocked by how much codex drifted from what was planned

- by [unknown](#) **&#x21C5; 3**
  <br/> Could you share your orchestration and workflow? Sounds good!

- by [unknown](#) **&#x21C5; 1**
  <br/> What is your orchestration workflow like? I've been trying to manually dial something in to use a combo of local models and paid models, and it is a bear to get it fully set up.

- by [unknown](#) **&#x21C5; 24**
  <br/> what are the tradeoffs? What if I want parallel execution if I have been slacking off at work and the deadline is close?

- by [unknown](#) **&#x21C5; 11**
  <br/> - Fast mode- If you have the money and are time constrained, don't use cheap models, they are a bit faster but the risk that they make a mistake is higher which will cost you extra time- Different local git worktrees to let them work in different branches. Works especially good when working on distinct features, otherwise there will be merge conflicts- Make sure your testing env is quick, otherwise the models test alot. Can prompt them to only test once everything is done if testing runs take too long.

- by [unknown](#) **&#x21C5; 3**
  <br/> You’ll get merge  conflicts also in worktrees.

- by [unknown](#) **&#x21C5; 3**
  <br/> I literally said that.

- by [unknown](#) **&#x21C5; 3**
  <br/> Different local git worktrees to let them work in different branches. Works especially good when working on distinct features, otherwise there will be merge conflicts


    You saying to use worktrees, otherwise you get conflicts. I’m saying using worktrees won’t make your conflicts disappear.

- by [unknown](#) **&#x21C5; 4**
  <br/> Ok there's a semantic misunderstanding here. I meant if the work items are related to each other, merge conflicts will arise even when using seperate worktrees.

- by [unknown](#) **&#x21C5; 1**
  <br/> He will get it done much much much faster and cheaper using parallel properly than using fast mode if money isn't a concern do both

- by [unknown](#) **&#x21C5; 1**
  <br/> Yes, fast mode is kind of the hassle free but expensive instant kick

- by [unknown](#) **&#x21C5; 5**
  <br/> Subagents are usually slower in my experience.

- by [unknown](#) **&#x21C5; 4**
  <br/> Subagents slower for working on one task, for example for a plan-execute-verify chain, but is faster on working on completely independent tasks in parallel

- by [unknown](#) **&#x21C5; 4**
  <br/> have been slacking off at work and the deadline is close


    This sounds oddly specific

- by [unknown](#) **&#x21C5; 2**
  <br/> Don’t slack off in the first place

- by [unknown](#) **&#x21C5; 4**
  <br/> Sir, this is Reddit.

- by [unknown](#) **&#x21C5; 44**
  <br/> I set up a factory few months ago, dedicated agents, harnesses and system prompts, the whole delegation, communication etc and I need to admit the labs are moving much faster then I can and astra gets better results now for novel tasks.

On the other hand, anything that’s volume and loops is just substantially cheaper on my setup.

- by [unknown](#) **&#x21C5; 17**
  <br/> I would argue that for 95% of tasks... delegating to cheaper subagent is cheaper/faster in the long run.

Most people are not trying to solve fusion, build the next Meta, etc.

Luna and the likes can probably already do that without an orchastrator.

- by [unknown](#) **&#x21C5; 2**
  <br/> Yes the tweet is objectively wrong because much of the time Luna can do it for 1/20th the cost with no orchestrator at all. Astra is overkill for most tasks.

- by [unknown](#) **&#x21C5; 5**
  <br/> The tweet is coming from someone who arguably would be unrestricted with their usage or worried of the costs.   I have heard from quite a few people though Astra has a bad habit of oversteering and overengineering.

- by [unknown](#) **&#x21C5; 1**
  <br/> gonna be honest with you boss, unless the work is extremely trivial getting a smarter model to do it is almost always worth it. the number of use cases for cheaper models to run with minimal impact on output is essentially none. most people don’t consider at all how much extra processing happens for extra cacheing and exchange between agents. you can cache thrash so easy too and pollute context as agents figure out what and how to pass info back and forth. and then you also have to design them to pass back and forth efficient information - but everyone just slaps instructions in a prompt and doesn’t validate between them

i’m ranting but honestly i’m just annoyed at how imprecise it all is and how everyone just seems so willing to slop it up with near-zero understanding of how anything works

- by [unknown](#) **&#x21C5; 2**
  <br/> I feel the same way. I'm at my 4th gen factory by now and astra makes me question if all this is futile. But a good planning skill makes a world of difference. I will continue with my factory, but more for process reasons rather than extension of runtime and quality.

- by [unknown](#) **&#x21C5; 2**
  <br/> What you mean by planning skill? Any examples of that?

- by [unknown](#) **&#x21C5; 10**
  <br/> I can't even use one Astra agent for more than 1-2 days on high. How the hell are people using subagents, even on x20 that must last maybe a day at best.

- by [unknown](#) **&#x21C5; 3**
  <br/> Luna Max subagents for strongly-defined simple tasks. The cost/intelligence is unmatched

- by [unknown](#) **&#x21C5; 87**
  <br/> "please stop being dumb if you're not as smart as me".

Great post with absolutely no insight or value. Half an unsupported claim with no evidence, advice, or even explanation.

- by [unknown](#) **&#x21C5; 9**
  <br/> I would say it’s actually pretty dumb to use the highest capable model for everything. I also assume the original post wasn’t meant as a serious recommendation. But yeah if you can, why not.. most of us are doing this to save tokens and be more efficient. But if you don’t need to care about that, sure.

- by [unknown](#) **&#x21C5; 4**
  <br/> That's just X. It rewards claims without evidence.

- by [unknown](#) **&#x21C5; 3**
  <br/> So, not much different than reddit

- by [unknown](#) **&#x21C5; 1**
  <br/> The UI topology between the two are different. X stages the post and hides the comments deeper. Reddit post and comments are 1 screen scroll away, so critiques tend to surface more.

- by [unknown](#) **&#x21C5; 2**
  <br/> i mean, i see people at work set up some complex orchestrator - reviewer - sub agentx6 pattern where they all communicate, but the output is the exact same as just the base prompt in vanilla usage but now they use 5x as many tokens lol

- by [unknown](#) **&#x21C5; 2**
  <br/> Sorry, probably should have included the context that Ahmed is OpenAI staff [https://x.com/ah20im/status/2097503414749909407](https://x.com/ah20im/status/2097503414749909407)

- by [unknown](#) **&#x21C5; 4**
  <br/> Yeah that's pretty relevant, although that doesn't automatically make him correct. The lack of information in this post means we can either blindly trust him or ignore him without any chance of verification or real understanding.

- by [unknown](#) **&#x21C5; 2**
  <br/> The point is that people are trying to be cute/clever with fancy non-standard workflows and then complain if it backfires

Having a vanilla workflow means that you're closest to what the models were trained and optimised for

- by [unknown](#) **&#x21C5; 1**
  <br/> At least in Codex Desktop Astra is greedy and will not delegate unless specifically instructed to

Edit: at least in one experiment Astra@high employed 5.5@high as Independent reviewer

Edit 2: Run four independent experiments for the same task with the skill that instructs Codex to use weaker models for coding and running tests, while Astra was reserved for orchestration and then compared to no-skill Astra runs. Pricewise the results were close (not signifcantly different by Welch's t-test). With orcherstration skill: $9.06 ± $0.65. Without: $7.30 ± $2.04 (AVG API COST ± SD; n=4). Worse the skill that let weaker models (terra) and testing (luna) resulted in 3 regressions out of 4 experiments. Astra without skill delivered all 4, no problem

- by [unknown](#) **&#x21C5; 9**
  <br/> Having tried both sides quite extensively I am honestly at a bit of an impasse with this.

It makes sense in principle to use cheaper agents for grunt work, but ultimately you're almost always going to use a more capable agent to check the work, as you can never fully trust automated checks. Unless the task is pretty much brain dead, or you have a well written spec with clear scope to pass to a cheap review agent after.

But you're almost always using your capable agent to produce a spec that is detailed enough, at which point, why not just use the agent with all of the context in thread already?

Sometimes it ends up cheaper, others more expensive. Hard one to split out.

- by [unknown](#) **&#x21C5; 45**
  <br/> "Just use Astra" This guy doesn't live in the real world.

- by [unknown](#) **&#x21C5; 33**
  <br/> Astra light orchestrating luna subagents accomplished far less while burning much more tokens than just Astra high in my (limited) tests

- by [unknown](#) **&#x21C5; 5**
  <br/> I had the same experience

- by [unknown](#) **&#x21C5; 3**
  <br/> Had the same experience with Fable and Opus tbh. I stopped micromanaging any frontier model’s orchestration

- by [unknown](#) **&#x21C5; 3**
  <br/> Tokens or dollars though? Luna tokens are much cheaper than astral tokens

- by [unknown](#) **&#x21C5; 2**
  <br/> same here

- by [unknown](#) **&#x21C5; 2**
  <br/> Same. Astra low and luna high (or xhigh) used almost 2x (1.99x to be exact) to accomplish the same task with slightly more code

- by [unknown](#) **&#x21C5; 1**
  <br/> What about Fable/Opus orchestraing Luna, did you try it out?

- by [unknown](#) **&#x21C5; 9**
  <br/> I think the advice of deleting your whole instruction system when a new frontier model comes out is probably not bad advice

- by [unknown](#) **&#x21C5; 1**
  <br/> What I do is to ask the new frontier model to adjust my setup, literally my first prompt with astra was to optimise the repo for astra :)

- by [unknown](#) **&#x21C5; 1**
  <br/> But then how do you manage to actually use astra all the time without running out of usage in like a couple days

- by [unknown](#) **&#x21C5; 1**
  <br/> I'm on $200 but gotta be honest astra ultra is too much for 1 such sub, will be using astra xhigh as orchestrator with sol as implementation agent or sth

- by [unknown](#) **&#x21C5; 1**
  <br/> That lasts you more than 2 days?

- by [unknown](#) **&#x21C5; 12**
  <br/> Astra is smart. But very expensive. Using it for everything is dumb.

Also, Astra is not as fast as Luna. And yes, parallel workers. Why are people so dumb?

- by [unknown](#) **&#x21C5; 2**
  <br/> Where do you get that Astra isn’t as fast as Luna? It’s way faster because it does the work correctly the first time and doesn’t have to loop as much.

- by [unknown](#) **&#x21C5; 4**
  <br/> I ask Astra to delegate all coding to Luna Max. Am i wrong? My goal is to save tokens

- by [unknown](#) **&#x21C5; 2**
  <br/> For lack of a manual, ask Astra if you are wrong?

- by [unknown](#) **&#x21C5; 2**
  <br/> You are not wrong. Simple coding tasks should not handle by Astra. I have my own task difficulty ranking based on the agent's familiarity, then assign a rating based on that, and deploy the appropriate model. It saves token greatly.

- by [unknown](#) **&#x21C5; 1**
  <br/> You probably won’t save tokens, as Luna will make more mistakes and potentially use more tokens than Astra, but those tokens will be cheaper.

- by [unknown](#) **&#x21C5; 1**
  <br/> Yes sorry was mentioning cost

- by [unknown](#) **&#x21C5; 4**
  <br/> One thing a subagent will do better is finding mistakes in a fresh context

- by [unknown](#) **&#x21C5; 3**
  <br/> I mean it's like this...astra's default routing is probably better then whatever slopcoded vibe shit most people get from github. But it's not going to be better then something actually tuned for your actual workflow.

- by [unknown](#) **&#x21C5; 3**
  <br/> What an absolute load of complete and utter bollocks.

- by [unknown](#) **&#x21C5; 3**
  <br/> He obviously never used Astra, and watched his subscription usage limits being reached in minutes.

- by [unknown](#) **&#x21C5; 4**
  <br/> [](https://i.redd.it/xdtjmbjlvmoh1.gif)

- by [unknown](#) **&#x21C5; 2**
  <br/> Currently we're at a place with this tech where if you dont know how to manage workflows, youre going to be burning through usage limits many times faster than someone who does.

- by [unknown](#) **&#x21C5; 2**
  <br/> Astra, at least in Codex Desktop, would not delegate and will babysit even simple tests herself. You can check it youself if you asked her to breakdown the model usage during the session she will check the logs and will give you an answer. And, boy, she is hungry - just one, not even a full day, with two sessions and 22% of my Max20 are gone.

Edit:at least in one experiment Astra@high employed 5.5@high as Independent reviewer

Prompt: "Check from your logs what models did you use during this session. Provide only grounded in logs answers"

- by [unknown](#) **&#x21C5; 2**
  <br/> I use subagents solely for explorers/task watchers to reduce input token cost. I keep implementation strictly to Astra.

- by [unknown](#) **&#x21C5; 1**
  <br/> Which models?

- by [unknown](#) **&#x21C5; 2**
  <br/> Luna:high for exploration and watchers

- by [unknown](#) **&#x21C5; 2**
  <br/> Yes, if you are dumb and/or don't care about the cost, you can just spawn Astra's for everything.In big projects, smart, dynamic orchestration is proven to be about 4x cheaper. The difference in cost can be absolutely massive and quality doesn't suffer if done right.

- by [unknown](#) **&#x21C5; 2**
  <br/> I use Matt Pocock skills. Split the work to tickets, Astra then orchestrates the implementation of the tickets using Sol sub-agents to tackle each ticket.

Astra is used to write the specs and create tickets before starting orchestration in a new session.

- by [unknown](#) **&#x21C5; 2**
  <br/> Yeah, but then how will I post to LinkedIn that "I'm running 20 agents in parrallel y'allzzz!!!"

Resume Driven Development (RDD) is being replaced by AI Theater Driven Development (AI TDD)

- by [unknown](#) **&#x21C5; 1**
  <br/> I use my own multi-agent setup which instructs the main agent to delegate on large jobs where a parallel workflow is possible without conflicts. Then that work is reviewed by another agent and the main agent integrates and cleans up. This works extremely well for me and produces excellent results. Letting one agent do everything without any delegation generally produces messy work that needs fixing.

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra knows best... I believe it

- by [unknown](#) **&#x21C5; 1**
  <br/> I've strayed from my tried and tested engineering work flow to just raw dogging it with Astra (low) on a few test projects - excellent results so far, no bugs found yet.

- by [unknown](#) **&#x21C5; 1**
  <br/> so what making astra use parallel luna subagents is bad?

- by [unknown](#) **&#x21C5; 1**
  <br/> Is it ok to use ultracode or ultra?

- by [unknown](#) **&#x21C5; 1**
  <br/> Most of times when i switched to multiple subagents working on simple task, they came up with bad results i never expected.

- by [unknown](#) **&#x21C5; 1**
  <br/> I've used complex multi-agent setups with past models that did wonders for my workflow and usage. I've stopped using a good chunk of them with these newer models, only keeping the novel aspects (that the models themselves claim are novel) I agree with this post. Ego (which is rampant in this space) will convince you otherwise.

- by [unknown](#) **&#x21C5; 1**
  <br/> This is always the case with everything you do with agents. Workflows go out of date very quickly. Agent files, skills, loops, goals, orchestrator patterns, planning, short threads, long thread. Basically if you do anything else than stock agent you need to aggressively AB test your workflows/try new things or you might hit some local maximas. Agents also leave a lot of information that can later be analysed so just ask your agent if something in your workflow sucks.

For example one misconception from earlier this year is people avoid 100K+ context as the model gets "dumb". I found that since Sol this didn't happen at all. In fact I found long 100+ message threads with several dozens of compactions it did a better job at a prompt than a fresh thread, even if it was a totally separate new feature. I suspect it somehow got into the proper "mindset" from the long iterative thread knowing exactly what I was looking for. I tried to have it dump this "mindset" into the AGENTS.md but it didn't catch a fresh thread up to speed. FWIW this might use more usage than fresh treads but I didn't observe it to an absurd degree at least.

- by [unknown](#) **&#x21C5; 1**
  <br/> Sol is able to coordinate subagents and follow instructions/guidelines better than Astra, I would say. I've been waiting for Astra to come out to see the difference. But that guy is right, let Astra work on it own. In terms of coordination, Sol is better

- by [unknown](#) **&#x21C5; 1**
  <br/> how do you guys think its best to maximize tokens?

- by [unknown](#) **&#x21C5; 1**
  <br/> I've personally found it kind of helpful to use blind subagents for reviewing, because the agent that implements tends to be kind of defensive about the code it wrote

And it seemed like more eyes are better than one extra-sophisticated one due to the stochasticity of agentic outputs.

Is anyone else doing sth similar? Or have done something similar and decided it's inefficient?

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra just seems to be always unhappy with Luna Max and always asking it to fix it repeatedly. Longer and burn a lot of tokens.

Trying to use Luna Max to ask Astra to review and fix its code after it is done instead.

- by [unknown](#) **&#x21C5; 1**
  <br/> The whole point of handing work off to sub agents is literally to save $$.

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra also has a similar problem to Fable of extremely sensitive guardrails - though at least you can sorta-continue the conversation after the cybersec guardrails hit. Delegating considerable amount of work to subagents and only using Astra for coordination/planning helps a bit.

- by [unknown](#) **&#x21C5; 1**
  <br/> I just ask Astra high to look at my work and the OpenAI docs and set up appropriate roles.

- by [unknown](#) **&#x21C5; 1**
  <br/> You don't need Astra high for that. Terra medium is perfectly capable of looking at a design or implementation plan and figuring out which tasks should go with which models based on the docs.

Now, you might want Astra high for building that design or implementation plan, but that totally depends on what it is you're building.

- by [unknown](#) **&#x21C5; 1**
  <br/> It's more about usage economy than not believing in ASTRA

- by [unknown](#) **&#x21C5; 1**
  <br/> Alright well I gotta install 2000 different working systems and had Astra work for 24 hours and it did 50 so yeah no maybe if astras token use was 1/50th sure I'd take this advice.

- by [unknown](#) **&#x21C5; 1**
  <br/> These gents did it better...

[https://www.youtube.com/watch?v=lscs5ZgNQrE](https://www.youtube.com/watch?v=lscs5ZgNQrE)

- by [unknown](#) **&#x21C5; 1**
  <br/> That only works for those on 200$ plan lol. If you're a regular user, you should definitely analyze & make plans with smart model, but implement with Luna. Or you will spend all your credits in literal minutes

- by [unknown](#) **&#x21C5; 1**
  <br/> Yeah, no one answered my question on this thread, but I was wondering if using a "swarm" skill would be efficient or smart, while Astra acted as the moderator and handled the delegation. From my experience, it's just better to let Astra handle everything. I seem to end up burning less usage in the end for reasons like dumber models getting stuck on loops, when verifying their output.

- by [unknown](#) **&#x21C5; 1**
  <br/> You probably didn't notice, but Astra speed is about 20% from what it was at release. So it's not going to get much done

- by [unknown](#) **&#x21C5; 1**
  <br/> He's not wrong if you have unlimited usage...

- by [unknown](#) **&#x21C5; 1**
  <br/> Yeah I get shit results if I don't review or orchestrate

Almost every review loop catches something huge.

- by [unknown](#) **&#x21C5; 1**
  <br/> we know Astra is capable of getting most tasks done, what nonsense. Multi agent patterns is about getting thing done in the most token efficient way. I tested Astra first without any sub agent orchestration, burned nearly 70% of 20x plan weekly quota in one day.

- by [unknown](#) **&#x21C5; 1**
  <br/> So setting up an AI software factory is generally not good practice?

Damn. It made the work so much more legible and enjoyable.

- by [unknown](#) **&#x21C5; 1**
  <br/> Ahmed is likely right. I run four independent experiments for the same task with the skill that instructs Codex to use weaker models for coding and running tests, while Astra was reserved for orchestration. I then compared to no-skill Astra runs i.e. bare Codex harness.

Pricewise the results were close (not signifcantly different by Welch's t-test).With orcherstration skill: $9.06 ± $0.65.Without: $7.30 ± $2.04 (AVG API COST ± SD; n=4).

What was worse, my skill that let weaker models code (terra) and test (luna) resulted in 3 regressions out of 4 experiments. Astra without skill delivered all 4, no problem

These regressions are likely the reason the runs with the skill were slightly more expensive becoase they had to be fixed

- by [unknown](#) **&#x21C5; 1**
  <br/> If I don't use a review loop I always end up having to bug fix and if I do it seems its always one shotted I am not sure what to do.

- by [unknown](#) **&#x21C5; 1**
  <br/> So who is this guy and why should we care what he says? Unless I hear it straight from the horses mouth, I don't think so.
