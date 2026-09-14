#How exactly do you "orchestrate" with Astra [Visit](https://www.reddit.com/r/codex/comments/1w9sonp/how_exactly_do_you_orchestrate_with_astra/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [froztii_llama](https://www.reddit.com/user/froztii_llama/)
### **Vote:** 25
---
So I have heard people say you should plan out with astra and then use Luna or Sol to carry out tasks.
So how exactly do you do this? Do you use /plan with astra then switch model in the conversation to Luna?
Doesnt changing models within the same conversation degrade output quality?
I have been using agentic coding since this year but I would still consider myself a beginner as to be honest..it is very hard to catch up..
Is using Astra for planning and coding ineffecient?
Wouldn't Astra produce better coding results if I have usage to spare?
I have carried out really complex tasks with astra planning & astra performing the tasks & the result was as expected; mind blowing.
I am yet to try out to plan with Astra and use Sol to carry it out.
Please note my question is for complex tasks not basic coding.
---
## Comments 40

- by [unknown](#) **&#x21C5; 13**
  <br/> No, you instruct Astra to use Luna and sol sub agents as appropriate, either in your prompt, or project description (maybe both)

- by [unknown](#) **&#x21C5; 6**
  <br/> I've tested Terra and Luna as subagents spawned by Sol, and that combination sucks, neither do they complete work properly nor does Sol check.

Maybe Astra spawning Sol-high agents could work, but not on Plus. You have to ration Astra like water in a drought.

- by [unknown](#) **&#x21C5; 6**
  <br/> No, you instruct Astra to create implementation packages suitable for less powerful models. (As tickets or md. Files, you name it.)

Then you switch to sol (or even terra) und tell it to orchestrate the implementation of these tasks with weaker models

- by [unknown](#) **&#x21C5; 4**
  <br/> Both are effective, I'm struggling to see why one would be inferior to the other. I prefer my workflow because it is also auditing errors in the cheaper models and automatically regenerating items that don't meet audit standards

- by [unknown](#) **&#x21C5; 3**
  <br/> No, how about we all just hug it out instead

- by [unknown](#) **&#x21C5; 4**
  <br/> The issue here –at least for me– is that Astra, as an orchestrator, still consumes kind of a lot

- by [unknown](#) **&#x21C5; 2**
  <br/> TBH, I think a lot of people are loading too many responsibilities into the term "orchestrator". Planning != orchestration != review, as but a few examples.

Astra is absolutely overkill for orchestration, if you're actually having it do orchestration and nothing else.

An orchestrator can get away with using a model away from the frontier, and away from higher reasoning, as long as it can follow procedure and marshall the process.

It's planners, implementors, testers, reviewers, etc. where frontier models and/or higher reasoning should be used, and even then it can vary a lot. (ala with a good plan even the implementing agent can often get away with lower reasoning, that kind of thing.)

- by [unknown](#) **&#x21C5; 1**
  <br/> You are on plus or pro?

- by [unknown](#) **&#x21C5; 4**
  <br/> Pro

- by [unknown](#) **&#x21C5; 1**
  <br/> This can be true but it could also be a cache hit issue. In some harnesses (not sure about codex) changing models can invalidate the reusable prompt prefix so you can lose the cache hit you were getting.

- by [unknown](#) **&#x21C5; -1**
  <br/> It always consumes a lot, it’s a frontier model.

- by [unknown](#) **&#x21C5; 2**
  <br/> Noted. Will give it a shot

- by [unknown](#) **&#x21C5; 1**
  <br/> No. You ask Lunar to call up Astra for prompts, advice when stuck in loops. Lunar Max. 5 hours of usage...still limit to go on the reset

- by [unknown](#) **&#x21C5; 11**
  <br/> Basically:Use Astra when the problem itself is hard to figure out.Use Sol/Luna when the problem is already figured out and you mostly need execution.For a really complex coding task I’d do:Astra → inspect repo, reason through architecture, identify risks, write the implementation plan/spec.Then either:Astra → also execute the hardest/most interconnected parts if you have the usage.orSol → execute the well-defined plan, run tests, fix normal bugs, iterate.Luna → cheaper/faster repetitive work, smaller fixes, mechanical implementation, tests, cleanup, etc.I wouldn’t switch away from Astra just because somebody says “Astra is for planning.” If Astra is giving you mind-blowing results doing both planning AND implementation and you have the usage, keep using it.The value of orchestration is mostly economics and parallelism, not that Astra somehow becomes bad at coding after planning.For very complex work my preference would be:Astra = architect / lead engineerSol = senior implementation engineerLuna = fast workerAnd switching models in the same conversation isn’t inherently bad. The bigger danger is the second model misunderstanding all the assumptions Astra made. For serious work, have Astra leave a concrete plan with decisions, constraints, files to touch, tests, and “do not change” items before handing off.So IMO:Hard + ambiguous → AstraHard but well-specified → SolMechanical / repetitive → LunaExtremely important + interconnected → just let Astra cook if you have the quota.

I’ve been using it a bit on a 20$ plan and been decent

- by [unknown](#) **&#x21C5; 6**
  <br/> Clearly explained & Intriguing. Thanks so much for your input 🫶 Will give it a shot. Thanks again

- by [unknown](#) **&#x21C5; 3**
  <br/> Finally someone who's not on 20x usage spilling good shit.

- by [unknown](#) **&#x21C5; 2**
  <br/> Thank you, If it’s worth anything i have 2 20$ plans and have been testing between both. I think I have a decent system. Now that Astra is here I’m about to build a harness with it in an advisory role and local llm’s doing the tasks

- by [unknown](#) **&#x21C5; 1**
  <br/> Canbyou make a detailed post stating the process and the thinking behind it? I was thinking about using sol, astra for planning/reviewing and using spark 1.3 contributor to execute

- by [unknown](#) **&#x21C5; 2**
  <br/> Bro basically, I’d use the expensive/smart models as architects and reviewers, not as the guys doing every file edit.My thinking is:Sol/Astra first → inspect the problem, define scope, figure out the architecture, edge cases, what “done” actually means, and produce a really tight implementation plan.Then hand that frozen plan to something cheaper/faster like Spark 1.3 Contributor to actually do the grunt work: edit files, write tests, run them, fix failures, repeat.Then send the finished diff/results back to Sol or Astra for review. If they find a problem, they don’t redo the whole task themselves—they give the executor a focused correction and it loops again.So roughly:Sol/Astra plan → Spark executes → tests → Sol/Astra review → Spark fixes → final verificationThe whole reason is usage efficiency. I don’t want to burn the highest-end model doing 20 minutes of syntax fixes, pytest loops, boilerplate, and repo navigation when a cheaper model can follow a strong plan.For harder tasks I’d probably have Sol do the main technical plan and Astra act more like the final adversarial reviewer. The executor can be swapped for Sonnet, Spark, Qwen local, whatever is good enough at following instructions.Long term I want this automated in a harness, so I give it one objective and it handles the planning → execution → review loop without me manually copy-pasting between models.Basically: **use the smartest models for decisions, cheaper models for labor.**

**Edit: if you’re staying in just chat gpt use Luna as your worker DONT touch 5.5 or mini at all!**

- by [unknown](#) **&#x21C5; 1**
  <br/> i saw somewhere that astra on low is better and cheaper per task then sol and luna but idk how true that is

- by [unknown](#) **&#x21C5; 1**
  <br/> Used Astra low enough to tell you no F’ing way. Maybe comp to sol med but no way Luna

- by [unknown](#) **&#x21C5; 1**
  <br/> do you also know how cache works on codex? is it model specific or switching to a new model complelty resets cache?

- by [unknown](#) **&#x21C5; 2**
  <br/> Codex gets cache hits when the beginning of the prompt/context matches exactly. Changing the target model is explicitly one of the things OpenAI says can cause a cache miss. Changing tools, sandbox settings, approval mode, or working directory can also break the cached prefix.So:Sol → Sol with mostly unchanged context = good chance of cache reuse.Sol → Astra = expect a cache miss for Astra.It doesn’t necessarily mean the old Sol cache is instantly deleted. It just means Astra can’t reuse that cached computation. If you switch back to Sol while the old cache is still retained, it could potentially be useful again.Also worth separating **conversation context** from **prompt cache**. Switching models can still leave the new model with the conversation history, but that doesn’t mean the expensive prompt-processing cache carried over.So for optimizing Codex usage, I’d generally avoid unnecessary model switching in the middle of a long coding session. Keep one model on a task until there’s a reason to escalate.

- by [unknown](#) **&#x21C5; 4**
  <br/> I dont use codex or astra / sol models much anymore, tho this was my config file that helped for orchestration.

[https://tmbv.me/page/development/agent-configs#codex](https://tmbv.me/page/development/agent-configs#codex)

big however, for full orchestration you need to use codex through opencode as sub agent spawning and handling through opencode is WAY better.

too lazy to update the page with my opencode config that includes better orchestration handling

also, you can even setup opencode SDK for way deeper orchesetration setup

- by [unknown](#) **&#x21C5; 3**
  <br/> wdym anymore it just came out a couple days ago? what are you using now?

- by [unknown](#) **&#x21C5; 3**
  <br/> meta muse $50 sub is equivalent to chatgpt $200 sub without losing the quality specifically for coding

i would say meta muse $15 sub is equivalent to like chatgpt $70 to $100 sub equivalence in subscription for codex ~ as i was on the $15 sub before switching to $50 sub.

muse $15 sub has way more bang for buck compared to codex's $20

you can see my initial thoughts here: [https://www.reddit.com/r/codex/comments/1w8kkl8/for_pure_coding_muse_spark_13_is_better_value/](https://www.reddit.com/r/codex/comments/1w8kkl8/for_pure_coding_muse_spark_13_is_better_value/)

then testing [https://www.reddit.com/r/codex/comments/1w8kkl8/comment/p8a5snm/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button](https://www.reddit.com/r/codex/comments/1w8kkl8/comment/p8a5snm/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

[https://www.reddit.com/r/codex/comments/1w8kkl8/comment/p8admx7/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button](https://www.reddit.com/r/codex/comments/1w8kkl8/comment/p8admx7/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

more evals come out today confirming my thoughts exactly

[https://x.com/ValsAI/status/2096663681702723653](https://x.com/ValsAI/status/2096663681702723653)

one major downside is the coding plan on meta is tied to using meta's own coding cli. you can't use like codex / claude code / opencode / etc.

although i want to use opencode, meta muse cli is SURPRISINGLY really good

- by [unknown](#) **&#x21C5; 4**
  <br/> Just start your prompt/conversation with Astra something like this:

Your role is the orchestrator. Always use subagents for doing long tasks and use your judgement to delegate to the correct models (e.g. mechanical to Luna, complex implementation involving thinking/unknowns to Sol).<<YOUR ACTUAL PROMPT HERE>>

That’s all you need. Then converse as usual and it’ll automatically decide what to delegate what to do itself.

- by [unknown](#) **&#x21C5; 1**
  <br/> Thanks. Will try it out

- by [unknown](#) **&#x21C5; 3**
  <br/> I’m using [Agent Orchestrator](https://github.com/Untrivial-ai/agent-orchestrator) to orchestrate Codex and Claude agents. I use Astra as the orchestrator, which spins up new chats for workers carrying out separate tasks across Codex and Claude. It has a Kanban board to track progress and having chats for each worker makes it more transparent.

I think you can do something similar directly in Codex, but you can’t orchestrate Claude workers using Astra as the orchestrator. I find this works well for front-end stuff as Fable is good at this. It’s also useful using a different model family for reviews as they have different biases.

- by [unknown](#) **&#x21C5; 1**
  <br/> i downloaded AO but i don't see the newest gpt models? latest is 5.3

- by [unknown](#) **&#x21C5; 3**
  <br/> I found getting Astra to do the work on its own uses far less tokens. It has a weird issue where it likes to keep polling subagents to check their work, turning simple tasks into context bloat. It's smart enough to one shot most things including complex plans. I also found going straight from spec -> impl is better than spec -> plan -> impl most of the time

- by [unknown](#) **&#x21C5; 2**
  <br/> Not sure, I used to do planning on Sol then implementation on terra but feels like its been making a lot of mistakes

I have some resets saved up so right now im just doing everything on Astra but would like to see how folks are sidestepping this

I will say, Planning on fable 5.1 and implementing on Sonnet seems to be working better then codex models right now when it used to be the opposite

- by [unknown](#) **&#x21C5; 1**
  <br/> personally I'm building out content material for a site, so I let my main astra orchestrate / test UI bugs, sol agents to author / research, and another astra agent for review which then gets fixed by sol. Has improved token usage a lot

- by [unknown](#) **&#x21C5; 1**
  <br/> If Astra is working well and quota isn’t an issue, I’d keep it for both planning and coding.

To try splitting: plan with Astra, save the agreed requirements, decisions and checks in `plan.md`(just a markdown file to save the plan for implementation later), which gives Sol/Luna a bounded piece to implement. Then I'd use a new session with a new model (sol/luna or something cheaper) to implement the plan.

I use [Crewplane](https://github.com/crewplaneai/crewplane)to turn those stages and handoffs into reusable Markdown workflows. For me, orchestration is about organizing and improving a repeatable process, not necessarily using different models or removing human review. I still check the results.

- by [unknown](#) **&#x21C5; 1**
  <br/> I like to use 5.5 low effort as an orchestrator for Astra, just to keep Astra's ego in check. That fucker thinks he's hot shit.

- by [unknown](#) **&#x21C5; 1**
  <br/> 😂😂😂

- by [unknown](#) **&#x21C5; 0**
  <br/> Why don't you just ask Astra? It'll tell you exactly what to do.

- by [unknown](#) **&#x21C5; 0**
  <br/> [https://github.com/donvito/codex-astra-luna-orchestrator](https://github.com/donvito/codex-astra-luna-orchestrator)

- by [unknown](#) **&#x21C5; -1**
  <br/> Astra for planning and "stucks" review, sol for audit, luna for implementation and debug
