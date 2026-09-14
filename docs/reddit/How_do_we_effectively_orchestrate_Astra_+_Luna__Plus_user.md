#How do we effectively orchestrate Astra + Luna? Plus user [Visit](https://www.reddit.com/r/codex/comments/1w8qkpz/how_do_we_effectively_orchestrate_astra_luna_plus/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Bankaren](https://www.reddit.com/user/Bankaren/)
### **Vote:** 1
---
As it isn't reasonable to only use Astra for coding due to its pricing. How do we effectively use Astra for orchestrating Lunas work? Luna would be the implementer, but which tasks specifically for coding would you delegate to which model?
I'm developing a 3d game with a lot of story and characters.
---
## Comments 28

- by [unknown](#) **&#x21C5; 5**
  <br/> I wouldn’t use Astra as the permanent “manager” for every Luna task. On Plus that’ll probably just burn through Astra for no reason.

I’d use it more like this:

  - **Astra** for architecture, tricky bugs, big refactors, unclear design decisions, or reviewing something high risk
  - **Luna** for most of the actual coding, tests, smaller refactors, scripts, tooling, docs, etc.
  - **Normal tooling** for builds, linting, tests and validation

For a game, Astra could decide how something like the quest system, save system, dialogue/state system or inventory should be structured. Once that’s clear, you turn it into a small well-defined task and let Luna implement it.

So more like:

**Astra figures out the hard part → Luna builds it → tests validate it → Astra only comes back if there’s a real blocker**

The important thing is not having Astra constantly supervising Luna.

Also keep unrelated context separate. If you’re fixing movement or a shader issue, the model doesn’t need your entire story bible and character lore in context.

That’s probably the biggest quota saver overall: give each model only the context it actually needs.

- by [unknown](#) **&#x21C5; 1**
  <br/> do you think Sol high as the main manager, luna to do task, and then if theres something too tricky or like a bug, we handle that with astra instead? or we use astra as the planner, sol as the manager, luna as the slave?

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra as planner, sol as manager and luna as slave is good, but sol in itself is pretty expensive for manager task. You could try astra -> terra -> luna. Terra could check lunas work and report to astra and astra decides what to do (worker is bugged -> Replace, worker cannot fix it -> delegate it to more competent worker etc.)

One thing to note: I havent tried if terra can spawn workers and check them

- by [unknown](#) **&#x21C5; 1**
  <br/> i havent tried terra out yet, can someone else verify this dude's claim?

also so previously it was plan with sol manage with terra build with luna for you?

- by [unknown](#) **&#x21C5; 1**
  <br/> I was using sol orchestrator/manager with luna xhigh workers.

- by [unknown](#) **&#x21C5; 1**
  <br/> hmmm, i use luna max. is luna xhigh enough?

- by [unknown](#) **&#x21C5; 2**
  <br/> I have been using luna xhigh for a quite while. There has been no real hard blocker that would escalate to more capable worker as far as i know. You can add a luna max or sol medium/high implementation worker escalation rule in your workflow if it cannot fix it.

Luna xhigh to Max cost is not really worth it and it gets pretty much everything done for me. Every project is different, we might be using it for different type of tasks so it can depend on the work you are doing, its always better to benchmark them for your project before hardcoding it into your workflow.

 
       [](https://preview.redd.it/how-do-we-effectively-orchestrate-astra-luna-plus-user-v0-j5nlobnekvnh1.png?width=828&format=png&auto=webp&s=d2bb9136e8398d56c57b6a33282d2a5451180c1b)

- by [unknown](#) **&#x21C5; 1**
  <br/> The difference isn't much in Intelligence level or price, but luna max takes like 5x longer than luna xhigh. You pay in time spent.

- by [unknown](#) **&#x21C5; 1**
  <br/> Can one explain how todo this?

- by [unknown](#) **&#x21C5; 1**
  <br/> You can show this comment and ask your chatgpt chat "Is it feasible, how can i make this in my workflow, does my project need this type of workflow? check openai documentation for ways to implement this on my project."

If you get stuck, let me know

- by [unknown](#) **&#x21C5; 1**
  <br/> Thank you for your detailed response. I use the Codex CLI, using your advice would I set up Sol (or Terra) as the main conversation, which then can choose model based on complexity of the task?

I'm thinking of how to manage a large repo without having Astra to read the full context, but still being able to work effectively with the tasks.

- by [unknown](#) **&#x21C5; 1**
  <br/> I am using an orchestrator so delegate tasks to luna with an escalation setting to terra -> sol.  But I run this with terra as I find Sol to expensive as a orchestrator on the plus sub and luna is a little too dumb as a orchestrator. I have also made antigravity a optional audit agent that terra can use to save some tokens.

But I won't even try astra as it is now.

- by [unknown](#) **&#x21C5; 1**
  <br/> how do you make antigravity an optional audit agent?

- by [unknown](#) **&#x21C5; 1**
  <br/> Codex writes a task request to a temporary file and calls a host adapter script to launch Antigravity outside the sandbox. It took a week of allowance to get this right, hehe. The adapter launches Antigravity under a dedicated, locked-down profile that strictly blocks write permissions and terminal commands, limiting it to code inspection only. Antigravity then writes back a structured report with its findings for Codex to read.

So to get it right you have to make the profile in agy on every workspace you are working inside. Mostly it's just fun to use.

- by [unknown](#) **&#x21C5; 1**
  <br/> Work in progress but, works partially(There are room for improvements). Not completed yet. This will fit your needs. I was using sol xhigh/lunaxhigh, this is astra light/luna xhigh[https://pastes.io/dfjIG6Kj](https://pastes.io/dfjIG6Kj)

- by [unknown](#) **&#x21C5; 1**
  <br/> Seems quite on point for the issue, thank you for sharing. So you use Astra Low for the conversation in the CLI?

Do you think it is more effective to use Astra Low than Sol Medium/High?

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra has long task capabilities, it will not degrade like sol does, also astra light is way faster than sol, it will use less tokens to achieve more. Just dont let astra burn tokens for tasks that dont matter for orchestrator, let dirt cheap models throw that calls.

So far im happy with astra light. Im using desktop app, yes you start with astra light on the conversation, you set up these policies and it will start the delegation work. I could squeeze out 1.30h of audit work with astra light orchestration. Im still improving the workflow so I cannot guarantee implementation capabilities but i think it can handle it. Maybe we escalate to astra medium for complicated tasks.

Check the planner notes on the bottom section for what is already inside my workflow, what will be tried later. The middle manager does not work as for now, I can only Astra light orchestrator -> workers, but token usage is improved a lot. I will post the result once im happy with the improvements

- by [unknown](#) **&#x21C5; 1**
  <br/> is astra low smart enough?

also astra low for delegation/orche and astra high for planning?

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra light is better than sol high.

Do you need more intelligence than astra light? It depends on your need. So far im happy with astra light. More reasoning uses more reasoning tokens so beware of consumption.

- by [unknown](#) **&#x21C5; 1**
  <br/> thanks for telling me, I didnt know the difference but damn

- by [unknown](#) **&#x21C5; 1**
  <br/> If you plan on orchestration, astra is to go-to. Astra was built orchestration in mind, and it shows. Its much much more capable than sol. You can unlock 1million context and just let it run for hours and days (well need to test that on better subscription haha) on same task. Just don't fill it with waste tokens, only keep whats necessary for astra to hold and think about, or you will demolish your usage.

- by [unknown](#) **&#x21C5; 1**
  <br/> hello sir I am very new to codex and AI overall, how would I start implementing this? I have been just using sol-luna without setting any agents until now

- by [unknown](#) **&#x21C5; 1**
  <br/> [https://pastes.io/nR05G3SI](https://pastes.io/nR05G3SI)

Copy this and give it to your planner agent (The agent you do the planning on your project, the agent who has the most information about your project), and tell it to analyze this instruction and execute it, it will give you information and create instruction set.

Note: Its still not complete yet and still has more room to improve. You can improve it yourself by discussing about it. For example for small changes, it recommends root to execute it but astra is too expensive to use on small tasks, it can be improved by delegating it to cheap worker.

- by [unknown](#) **&#x21C5; 1**
  <br/> I tell astra ( and before that sol )  to update design and todo ( both markdown files ) with my new thing I want. Then I /goal items in todo with Luna max ( step by step, commit each after marking down ) overnight. It works pretty well on plus, I have yet to run out of 5h window.

My agents md contains few items about keeping documentation in sync and updating others when marking todo done etc.

- by [unknown](#) **&#x21C5; 1**
  <br/> Do you like the quality of the work, is thr design/todo briefs detailed enoigh for Luna to follow well and implement it?

- by [unknown](#) **&#x21C5; 1**
  <br/> So far it has worked well for me. I have used the pattern so far only in three small hobby projects and one medium sized one. The outcome has worked fine, although sometimes design is under specified so I go for second iteration with refinements based on what I see from the first result.

- by [unknown](#) **&#x21C5; 1**
  <br/> Just use Astra to plan and fix issues, make it build a markdown at root, Luna reads it and executes

- by [unknown](#) **&#x21C5; 1**
  <br/> I made this and use it all the time and got some good feedback, it helps you setup an agent team with configurable model choice for each role in the workflow. if you want something you can just setup in your project and use read the docs and try it out. this has been tested pretty hard on all my long running projects and I get quite a good amount of usage value out of it by delegating from the main thread to luna for all my grunt work.

[https://github.com/nickyfactz/plumbline](https://github.com/nickyfactz/plumbline)
