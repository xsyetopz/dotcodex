#The Orchestration Architecture That Lets You Run Sol/Astra for Hours Within the Plus Plan’s 5-Hour Limit [Visit](https://www.reddit.com/r/codex/comments/1wbtgyn/the_orchestration_architecture_that_lets_you_run/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Otherwise-Sir7359](https://www.reddit.com/user/Otherwise-Sir7359/)
### **Vote:** 150
---
[](https://preview.redd.it/the-orchestration-architecture-that-lets-you-run-sol-astra-v0-55acq0zqbjoh1.png?width=1920&format=png&auto=webp&s=ea90de4da443da7bfcfe984b980ba2b6338cb8e8)
Codex_workflow : Heavy route
> Note: `doc-writer` and `closure_steward` have been merged into single role `archivist` since 1.1.14 version.Been building this since 5.6 dropped with optimizing token usage as the ultimate goal, and tweaking it pretty much every day since.
Role
Model
Primary Responsibility
Quantity
Main Agent
Session-selected model
Primary orchestrator. Owns the core task context, makes high-level decisions, coordinates the workflow, and distributes the knowledge required by specialized subagents.
1
Companion
Luna · xhigh
Persistent secretary and context assistant. Reduces context pressure and operational overhead on the Main Agent by handling supporting context, organizing information, consolidating reports, and taking care of lightweight auxiliary work.
1
Investigator
Luna · xhigh
Research and investigation specialist. Searches for clues, technical evidence, documentation, prior art, and potential solutions, including information available on the Internet. Investigators can operate in parallel across independent research lanes.
As needed
Default Executor
Luna · max
Default implementation worker. Handles normal production tasks delegated by the Main Agent, including coding, modifications, integration work, and other routine implementation activities. Multiple Default Executors may work in parallel when tasks can be safely decomposed.
As needed
Senior Executor
Sol · medium
High-capability implementation specialist. Reserved for exceptionally difficult or high-impact work where stronger reasoning is justified, such as project-core changes, complex algorithms, architectural modifications, or mathematically demanding tasks.
1 maximum
Tester
Luna · max
Independent verification specialist. Designs, implements, and runs tests; validates requirements and acceptance criteria; identifies regressions or defects; and provides verification evidence before work is accepted.
As needed
Archivist
Luna · xhigh
Documentation and closure specialist. Handles assigned documentation outside the three main-owned deployment-state documents, performs the read-only Git handoff, and produces the end-of-deployment token report.
1 per substantive deployment, plus as needed
What's special about the system:
- Flexibility: The system doesn't force the main agent into a rigid process: requiring coordination in this way or that way... It provides it with resources and power (specialized agents) and fine-tuning and guidance based on hundreds of trials.
- Fine-tuned balance: Main agent's control <---> costs & task completion capabilities.
- Knowledge distribution: Each task package from the main agent to the workers includes a task completion guide.
- Batching guidelines prevent excessive main agent rollout.
- Addresses the issue of the main agent waking up workers too often.
- Built-in token report: End-of-session token statistics for each agent, allowing you to monitor how much each agent rolls out and how they use their tokens.
......
Real-World Testing: Sol xhigh vs. Astra highI gave both of them a broad and difficult task:
**Perform a comprehensive upgrade of an OCR + AI chatbot project running PaddleOCR and Gemma 4 on a Jetson Orin Nano.**
Codebase details, prompt, output, and interface result of the test:
[https://github.com/viettran-edgeAI/OCR_workflow_variants](https://github.com/viettran-edgeAI/OCR_workflow_variants)
Below is a comparison of the resulting interface and token statistics.
The top result is Sol, and the bottom one is Astra.
[](https://preview.redd.it/the-orchestration-architecture-that-lets-you-run-sol-astra-v0-zmhak24jcjoh1.png?width=1920&format=png&auto=webp&s=9e9e1075249586627fc096e6f9cb84aa9a0979e4)
Main Agent
Runtime
5h Limit Usage
Weekly Limit Usage
Share of **Uncached Tokens**
Share of **Total Tokens**
Share of **Total Cost**
**Sol 5.6**
4h 22m
90%
15%
**6.2%**
**12.8%**
**60%**
**Astra**
2h 30m
260%
43%
**14.2%**
**13.8%**
**88%**
About their orchestration behaviorSolSol showed extremely broad coverage and missed very few edge cases.
It was very comprehensive, had excellent verification, strong traceability, and rarely overlooked things. But it also showed signs of over-owning the work.
AstraAstra seemed particularly strong at finding the actual core problem instead of just patching symptoms.
It was less exhaustive than Sol, but its architectural reasoning was extremely sharp, and it handled resource contention particularly well.
My honest advice: keep using Sol for this job. Astra didn't show a significant difference, but it cost 4-7 times more in my tests. It doesn't even follow the instructions as well as Sol.
----------------------
The setup process and usage is as simple as it gets, I've packed everything in here :
[https://github.com/viettran-edgeAI/codex_workflow](https://github.com/viettran-edgeAI/codex_workflow)
----------------Edit : I've noticed quite a few people downvoting. Honestly, this is my third post about this workflow; the previous two are still in my profile. I apologize if that bothered you. The most recent post, from a month ago (version 1.1.3), was still quite basic. I've been testing it for over a month, ran hundreds of tests, fixing all the observed problems until everything worked effectively based on experimentation, not just on feeling. Therefore, I wanted to inform those who have installed version 1.1.3 - most of them from Reddit, since I only posted this workflow here.
Edit 2: Edit 2: For those wondering why things aren't simpler, how the codex works & rollouts, what problems arise in creating an efficient workflow, and issues related to awareness of three levels of Perspective (Designer <-> Main agent <-> Workers), etc.. see here, as I can't include everything in this post:
[https://github.com/viettran-edgeAI/codex_workflow/blob/main/workflow_breakdown.md#0-a-deep-dive-into-codex-orchestration](https://github.com/viettran-edgeAI/codex_workflow/blob/main/workflow_breakdown.md#0-a-deep-dive-into-codex-orchestration)
---
## Comments 57

- by [unknown](#) **&#x21C5; 6**
  <br/> Really interesting architecture. A few things I was wondering about specifically from the token-efficiency angle:

  1. Why keep Light / Medium / Heavy as separate routes? Have you experimented with just having a cheap direct “leaf” mode for small tasks and one adaptive orchestration contract for everything substantive? It seems like Heavy could decide dynamically whether it needs 0, 1 or many workers, which would remove route-selection policy and duplicated instructions.
  2. Why make the full "agent_docs/" intake mandatory at deployment entry? Wouldn’t proportional reading be cheaper — start from the current checkpoint, read only the docs/sections relevant to the task, and expand only when context is missing? If the optimization target is Main context size, loading every module-specific document into Main once per session seems potentially expensive on larger projects.
  3. Related to that: why is Companion mandatory on first deployment entry? Have you benchmarked mandatory persistent Companion vs creating it only when it can actually replace multiple Main reads/tool calls or when retained context will be reused? A persistent Companion is useful, but its own context also gets replayed on subsequent rollouts.
  4. Does the Deployment Token Report actually pay for itself? I like the observability, but generating it through an Archivist also creates another LLM operation at every substantive closure. Have you compared that against either dropping the report entirely or collecting the same telemetry deterministically outside the agent workflow?
  5. Why does Main still directly update all three deployment-state documents at closure? If Main's most expensive resource is context/rollouts, wouldn't it be cheaper for Main to record only genuinely architectural/lasting decisions and let Archivist own progress/latest-session/handoff updates from verified worker evidence?
  6. One last token-efficiency question: what about silent orchestration by default? Routine Main messages like “waiting for executor”, “resuming worker”, “moving to next task”, etc. don't really help execution, but each Main turn can replay a huge cached prefix. Have you measured the effect of doing routine lifecycle coordination entirely through tool calls and only surfacing meaningful milestones/blockers to the user?

Curious whether you tested any of these and found a reason to prefer the current design.

- by [unknown](#) **&#x21C5; 1**
  <br/> 1. `Light` essentially doesn't use workflows. `Heavy` involves using a main agent for coordination. `medium` is for situations where people want the main agent to deploy it self when the Luna exxecutor + tester aren't trusted enough.
  2. agent_docs/ essentially provides a condensed context of the entire project. The coordinator needs to have a comprehensive overview. It will automatically decide which modules/components to read for the task, and which parts to delegate to a companion.
  3. The Companion is Luna, so it's also very cheap. Creating it when entering the deployment state only costs one rollout of the main agent, and that rollout happens at the beginning of the mission, when the main agent's context is still very small. Summoning it later when the main agent's context is much more expensive.
  4. I created it to observe and fine-tune the workflow. It was a bit expensive, costing around a few hundred main agent tokens.
  5. I used to design it that way. But updating them directly only adds a few hundred tokens out of the main agent, instead of creating a task package for Archivist, which would be more expensive.

6.I fixed that issue in version 1.1.3. The current version is 1.1.17.

Thanks for asking the questions. I ran hundreds of tests from version 1.1.3 up to 1.1.15 before the official release.

- by [unknown](#) **&#x21C5; 4**
  <br/> Thanks, that clarifies a lot. Your point about spawning the Companion early actually makes sense to me — I hadn't considered the difference between paying for that Main rollout while its context is still tiny versus summoning it later after Main has accumulated a large prefix. I'll have to rethink that one.

There are three things I'd still be curious about though.

On "agent_docs/": I actually ran into this problem in practice.

I've been using "codex_workflow" for the last few days on a project that maintains my whole homelab. The same project contains context for Unraid, Home Assistant, OPNsense, Node-RED, Codex/update tooling, and quite a few other components.

If I started a deployment that was purely about Unraid, the initial intake still caused Main to read documentation about Home Assistant, OPNsense, Node-RED, Codex updates, etc. — a huge amount of information that had absolutely nothing to do with the task.

After basically the first substantive prompt, Main's context was already around 75% full. That was pretty brutal, especially knowing that this prefix then gets replayed on subsequent Main rollouts.

I agree that the coordinator needs a comprehensive project overview. But I wonder if there is a useful distinction between foundational project context and module detail.

For example:

  - always read overview / architecture / structure / progress / diary / latest-session;
  - but don't automatically read every module-specific document;
  - select module docs based on the task and let Companion pull in additional modules when a dependency or missing context makes them relevant.

That would still give Main the global map of the project without loading the entire Home Assistant subsystem when the task is just an Unraid change.

I think this might matter especially for "umbrella" projects that manage many loosely related systems.

On Main updating the three deployment-state docs:

I understand the argument that directly writing them only costs a few hundred generated Main tokens.

What I'm wondering about is the cached-input side, rather than just the generated-token count.

At closure, Main may already have a very large context. So even a small "update these docs" operation can cause another rollout that has to process/replay that large prefix.

And Archivist is already mandatory for substantive closure anyway.

So would it perhaps be cheaper to let Main retain ownership only of information that genuinely requires Main's judgment — e.g. lasting architectural decisions / lessons — while the already-required Archivist updates mechanical state such as "project_progress.md" and "latest_session_work.md" from verified evidence?

Especially since the closure Archivist can already inherit recent Main context, it seems like this wouldn't necessarily require Main to construct a large additional handoff package.

I'm curious if you benchmarked Main writes + Archivist closure against minimal Main decision recording + Archivist does the closure-state writes, including cached input rather than only generated tokens.

And regarding #6: I checked the current 1.1.17 instructions after your reply.

I can see the fixes around event-driven waits, avoiding polling, status-only requests, repeated evidence checks, etc. So yes, that part is definitely there.

What I couldn't find is an explicit rule about user-facing narration of routine orchestration.

What has worked extremely well in my testing is making that a separate hard rule: routine orchestration happens silently through tool calls. No user-facing message just because Main waited for a worker, resumed one, checked thread state, sent a worker a message, reused a result, queued the next package, etc.

Only surface something when:

  - a meaningful stage is completed and verified;
  - there is a blocker requiring user input;
  - there is a security/publication risk;
  - the plan or scope materially changes;
  - or the whole task completes.

With that explicit instruction, Sol and Luna are basically silent during orchestration. Astra still occasionally ignores it, but Sol/Luna follow it extremely well.

The distinction seems important because "don't poll workers" prevents unnecessary worker-management operations, while "don't narrate routine orchestration" prevents unnecessary Main turns. And those Main turns are exactly where a huge cached prefix can become expensive.

Maybe I'm missing another instruction surface where 1.1.17 already enforces this explicitly?

- by [unknown](#) **&#x21C5; 2**
  <br/> Regarding the remaining issues you mentioned:

- It's true that Sol adheres better than Astra.

- Regarding main handling project_progress.md and latest_session_work.md: the trade-offs between the two options are generally quite similar, but I chose that method because I really just wanted things to be faster and more accurate. Using the other method is also fine.

- by [unknown](#) **&#x21C5; 1**
  <br/> Which version are you using? I recently added instructions to the main agent about which important sections to read during task initialization, plus a request for Copmaion to briefly initialize agent_docs/ (it was quite disorganized before) in version 1.1.17. A few days ago, the repo was probably still at 1.1.3, and that version was still quite rudimentary.

- by [unknown](#) **&#x21C5; 3**
  <br/> I checked the timeline and the actual 1.1.17 files.

It looks like I was most likely using 1.1.14 when I first ran into this. I installed it before 1.1.15 was published, so you're right that I wasn't testing the current 1.1.17 behavior at that point.

I also checked 1.1.17 directly though, and I think the specific issue I described still exists.

On first deployment entry, Main is still instructed to read the complete "agent_docs/" framework, including every module-specific Markdown document, before Heavy builds the Direct / Companion / Investigator context map.

So for an umbrella project like my homelab, a task purely about Unraid can still initially load docs about Home Assistant, OPNsense, Node-RED, Codex maintenance, etc. The newer context routing helps a lot after that initial intake, but the expensive part I'm referring to happens before the routing.

The Archivist initialization in 1.1.17 does look much cleaner, especially only initializing new/template-marked docs and preserving the healthy ones. I wasn't referring to that installation-time initialization though — specifically to what Main loads into its own context when a deployment starts.

Would you consider making the initial intake proportional instead?

Something like:

  - always load the core project overview/current checkpoint;
  - load only module docs relevant to the current task;
  - let Companion pull in additional modules when dependencies or missing context require them.

That would still give Main the project-level overview without front-loading every subsystem into its context.

Also, your point about creating Companion immediately while Main's context is still small convinced me. That part makes a lot of sense.

- by [unknown](#) **&#x21C5; 1**
  <br/> Thanks for pointing that out. There are still areas for improvement. All my time outside of work is dedicated to this project, and since it's not very long, mistakes or omissions are inevitable. Alos, frankly, Companion isn't working as well as its theoretical design suggests and still needs improvement.

- by [unknown](#) **&#x21C5; 5**
  <br/> Thanks for posting this! Just to clarify, would you recommend Sol-xhigh or Astra High when optimizing for saved usage? Does it depend on the scope of the project? What circumstances would one be preferable to the other, again prioritizing usage savings? I am also on a Plus plan trying to finish up a project on our meager usage limits, and this orchestration workflow has helped me tremendously so far.

- by [unknown](#) **&#x21C5; 2**
  <br/> You know, reasoning effort levels only increase output tokens, while the input tokens used for a task remain unchanged. However, in this scheduling process, the main agent doesn't handle deployment, so using a low level significantly reduces its scheduling capabilities, while only saving a few thousand output tokens for the main agent. I default to using Sol xhigh / Astra high. But I honestly advise against using Astra; it's not significantly better than Sol for these kinds of tasks, but the cost is 4-7 times higher, as I've observed.

- by [unknown](#) **&#x21C5; 1**
  <br/> Thanks, appreciate the response.

- by [unknown](#) **&#x21C5; 3**
  <br/> I have been deep diving into this too you can find some findings of my optimizations  to get rid of astras burden;[https://www.reddit.com/r/codex/comments/1wbk5ff/if_you_are_using_astra_orchestration_specially/](https://www.reddit.com/r/codex/comments/1wbk5ff/if_you_are_using_astra_orchestration_specially/)

- by [unknown](#) **&#x21C5; 3**
  <br/> You know, people are usually too lazy to read long posts. The original version of this post was even three times longer, but then I had to shorten it. Well done anyway, bro

- by [unknown](#) **&#x21C5; 1**
  <br/> Im just giving away my optimizations for people to use it, if don't care to read it its okay. Whoever needs it might use it :)

- by [unknown](#) **&#x21C5; 4**
  <br/> Great work!Could you point to differences between it and superpowers maybe?Thanks!

- by [unknown](#) **&#x21C5; 2**
  <br/> Read up on superpowers. It's recommended to not use it. It actually increases token usage quite a bit and doesn't actually produce much better results if at all than without it.

- by [unknown](#) **&#x21C5; 1**
  <br/> My workflow is much more efficient, that's all. I bet Superpower can't run Sol xHigh for over 4 hours while only using 80% of the 5-hour limit on Plus plan like the test I showed in the post.

- by [unknown](#) **&#x21C5; 1**
  <br/> Yea you are doing great work utilizing Luna, which is a dream I had for a long while. Superpowers will eat up tokens in the spec and planning phase but then it delegated work to sub agents with clear instructions to use the lowest possible model and escalate on failures.

- by [unknown](#) **&#x21C5; 4**
  <br/> Gonna need a TLDR, this is pretty tough to read. "Lets You Run Sol/Astra for Hours" soundsclickbaity unfortunately, since there's (I would think) no way that can be true for Astra

- by [unknown](#) **&#x21C5; 3**
  <br/> not clickbait , look at image in the post. Sol xhigh run 4h22 mins on Plus plan.

 
       [](https://preview.redd.it/the-orchestration-architecture-that-lets-you-run-sol-astra-v0-xum9fbm3ojoh1.png?width=1920&format=png&auto=webp&s=9b0854d9c1de47352579f0fbaba37f8eb96def02)

- by [unknown](#) **&#x21C5; 3**
  <br/> [](https://preview.redd.it/the-orchestration-architecture-that-lets-you-run-sol-astra-v0-o9b3hgydojoh1.png?width=1894&format=png&auto=webp&s=0cc52cde40ebe625659e7e631f78fc4cb1805106)
      
    Sol - xhigh : 4h22 mins

- by [unknown](#) **&#x21C5; 3**
  <br/> [](https://preview.redd.it/the-orchestration-architecture-that-lets-you-run-sol-astra-v0-x999070mojoh1.png?width=1920&format=png&auto=webp&s=a7417e87dbb8f4bb8c219a474e1d0e54f9ac117a)
      
    Astra high  - 57 mins, 24% left

- by [unknown](#) **&#x21C5; 2**
  <br/> Thank you for this. I once tried making a bridge, where I went through the Spec-kit workflow up until implementation, bridged the docs into a codex-workflow format, and then had workflows (heavy) plug away at it. It spawned hundreds of different luna subagents and took a very, very long time. Burned through 2 weekly quotas on Plus plan for a texture generating local web-app. I eventually paused it 75% of the way as it had already built the foundation (quite well I might add), and then just had a standard codex /goal finish implementing per the specs.

Would not recommend the above as it took longer and spent more to accomplish the task, but I still need to try codex-workflows by itself, and perhaps I'll just use idea-refinement and grill-me to establish input context.

- by [unknown](#) **&#x21C5; 2**
  <br/> This is amazing your setup is similar to mine except I run qwen 3.8 27b q6 as the implementation and codex similar to yours for the rest with Astra medium as a one time escalation if Luna max or Sol medium can’t solve an issue. Super token efficient this way.

- by [unknown](#) **&#x21C5; 2**
  <br/> Thank you for sharing your hard work. Looks very interesting, i might give it a try.

What would you change tho if you were on x10 or x20 plans?

- by [unknown](#) **&#x21C5; 1**
  <br/> Coincidentally, I also plan to create a pro mode for this workflow, where Senior_executor is Astra high, allows senior_executor to be used more frequently and enable fast mode with (# service_tier = "fast" in .toml) for all workers. However, there is currently no time to test and deploy this idea.

- by [unknown](#) **&#x21C5; 4**
  <br/> If this works for you I'm happy for you but I've found this idea of personally carving out roles for different subagents has been made redundant by the models' improved innate delegation abilities and not trusting the main agent to make those decisions leads to tons of tokens wasted on ceremoniously spinning up a bunch of subagents for tiny tasks because that's what the [agents.md/skill](http://agents.md/skill) said it had to do.

- by [unknown](#) **&#x21C5; 2**
  <br/> I had a very long post about this before, but it seems people were too lazy to read it so I deleted it. If you want, I can send you a detailed analysis of the problems when simply saying "Hey Sol, plan this mission and coordinate the Lunas to deploy." Furthermore, my coordination process has eliminated the rigid philosophy of: you have to coordinate them this way, that way... and restored flexibility to the main agent.

- by [unknown](#) **&#x21C5; 1**
  <br/> I’m running something similar: constant thinking, with GitHub and Notion connected.

In ChatGPT, I research and plan the work, create “task cards” (basically Jira-style), and build the orchestrator prompts.

When I’m ready to kick things off, I fire up Codex with Sol *light (this is crucial)*, which gets the full task context and writes the OpenSpec.

From there:

  - Sol passes the task to Luna Medium to implement.
  - Terra reviews the implementation and passes feedback back to Sol.
  - Sol updates Notion, finds the next task, and keeps the loop going.
  - It continues until it hits a blocker.

I’m also thinking about adding another step where the orchestrator sends a ping-back message to ChatGPT with status updates, since Codex can send messages back to ChatGPT. That would make the loop feel a bit more closed and keep the planning context in sync with what’s actually happening during execution.

- by [unknown](#) **&#x21C5; 1**
  <br/> This is actually very interesting to me. Could you describe your setup in a bit more detail?

I already work in a somewhat similar way: I use regular ChatGPT for research, architecture and planning, then Codex for implementation. But so far I've been manually moving prompts, plans and status updates between ChatGPT and Codex, usually through GitHub files.

So the part that really caught my attention was:

«Codex can send messages back to ChatGPT»

I assume you don't literally mean both conversations share the same context, but rather that Codex leaves some kind of message/state that ChatGPT can pick up without you manually copying it.

How exactly are you doing that? Is Notion acting as the communication/state layer, or are you using some other integration/hook?

I'd also be interested in how you structure the task cards. Are they roughly equivalent to milestones, or smaller Jira-style implementation units underneath a milestone?

And when you say ChatGPT builds the orchestrator prompts, does ChatGPT prepare a separate prompt for every task card ahead of time, or do you have one persistent orchestrator prompt and Sol dynamically picks up the next card and turns it into an OpenSpec?

I've been doing the planning side manually so far, so your workflow sounds very close to what I'm already doing, just with much less manual handoff.

- by [unknown](#) **&#x21C5; 1**
  <br/> I assume you don't literally mean both conversations share the same context, but rather that Codex leaves some kind of message/state that ChatGPT can pick up without you manually copying it.


    Just ask codex (desktop) to post something in some chatgpt chat and see the result.


      I'd also be interested in how you structure the task cards. Are they roughly equivalent to milestones, or smaller Jira-style implementation units underneath a milestone?


    Accepted/Deferred/Implemented/Rejected/Review with cards dependency on other cards, priority, metadata (complexity, phase, where relevant code is located).

Essentially I have couple big pages with sub-entries (cards), each page is like a specific topic (Architecture, Technical) - you can consider them as Epics in jira words.


      And when you say ChatGPT builds the orchestrator prompts, does ChatGPT prepare a separate prompt for every task card ahead of time, or do you have one persistent orchestrator prompt and Sol dynamically picks up the next card and turns it into an OpenSpec?


    Single prompt I iterate and refine on in the ChatGPT, which uploads it into Notion as a durable storage, and each time I want to pick up fresh work - I just copy that prompt and paste it in Codex, it kicks off the whole process. Here's edited version with stuff removed: [https://pastebin.com/QciVJyap](https://pastebin.com/QciVJyap)

- by [unknown](#) **&#x21C5; 1**
  <br/> Is this for solving millennium prize problems? Can I get a TLDR?

- by [unknown](#) **&#x21C5; 1**
  <br/> No, mainly saving tokens for the poor 😅 (its me)

- by [unknown](#) **&#x21C5; 1**
  <br/> Do you have benchmarks comparing usage using more straight forward systems? (Like making a detailed plan with Sol and executing with Luna or Sol medium?).

Luna is ridiculously slow so saying that it can run for hours when Sol medium might have done the same job in 20 mins with the same usage doesn't seem like the right metric. Most reviews I've seen of these types of orchestration systems say that most of the usage is taken by Astra checking in on Luna agents, which makes it really inefficient on token usage.

- by [unknown](#) **&#x21C5; 1**
  <br/> How does it compare with [https://github.com/alvinunreal/oh-my-opencode-slim](https://github.com/alvinunreal/oh-my-opencode-slim)?

- by [unknown](#) **&#x21C5; 1**
  <br/> Mine is only used in codex. I don't use that repo, you can ask codex to compare, will be faster and more accurate.

- by [unknown](#) **&#x21C5; 1**
  <br/> This post makes no sense. Ur astra used 260% of 5h weekly yet u claim it can run for hours

- by [unknown](#) **&#x21C5; 1**
  <br/> 57 mins, 24% left. Thats better than about 15-20 mins using Astra and 5h limit gone. Anyway, I don't force anyone to use it.

- by [unknown](#) **&#x21C5; 1**
  <br/> And sol used 96% and u didnt include luna usage. Not meaning to trash on ur project but the math dont add up.

- by [unknown](#) **&#x21C5; 2**
  <br/> [](https://preview.redd.it/the-orchestration-architecture-that-lets-you-run-sol-astra-v0-rnlrwwsofkoh1.png?width=1894&format=png&auto=webp&s=88f6951ab70bbdcdea1eeebd69ad9e1b252563c2)
      
    All the numbers are publicly available, including Luna's token. I don't know how you calculated it. Where did you get that 96% figure from? In the statistics table, input tokens include cached input token, u must subtract it first.

- by [unknown](#) **&#x21C5; 2**
  <br/> My bad 90%. Now i see you meant using Sol as main agent used 90% of 5h usage and astra 260%? How did u calculate 260% weekly usage when 100% is the max? Not bad tho if u managed to run Astra orchestrated workflow for over 4 hours. The problem is the main agent: if astra is required more work the price goes up instantly, not all sessions are the same. Still one of the most interesting posts here in a while 👍

- by [unknown](#) **&#x21C5; 1**
  <br/> I ran it through 3 sessions. Pause when the usage limit reaches 1% and tell it to continue after that. The first starts from 85%, lasts 59 minutes. The second uses 100% of the 5-hour limit and lasts for 1 hour and 34 minutes. The 3rd time lasts 57 minutes and costs 76% as shown in the picture. I hang it, not turn it off and reopen the session.

- by [unknown](#) **&#x21C5; 1**
  <br/> I’ve been thinking of such a framework, but does yours look into codex’s polling mechanism? Specifically Astra seems to constantly poll its subagents frequently burning tokens everytime and checking its work.Any agent that tracks task and only calls the orchestrator when needed? Or subagents calling orchestrator only when issue or completion instead of constant polling of work progress?

- by [unknown](#) **&#x21C5; 1**
  <br/> I have fixed that problem from the first versions. And the second problem you mentioned: at first I let companion do that, but in the codex, the subagent cannot communicate on an equal level with other subagents, and there is no mechanism for the main agent to "sleep" and wake up by the subagent under it

- by [unknown](#) **&#x21C5; 1**
  <br/> They did recently add it where chats can talk to each other. if you have seen now subagents can message the orchestrator. i've seen some people do the sleep by telling it be in a timer sleep for 20minutes etc. and only poll after timer to update on progress. and keep cache warm.

- by [unknown](#) **&#x21C5; 1**
  <br/> We actually ended up solving the polling part in a very similar way in my local fork.

Main doesn't periodically ask workers for progress. It delegates the task and continues any independent work it still has. Once there's nothing useful left for Main to do, it enters a long event-driven `wait_agent` — currently 25 minutes in my setup.

The important part is that the 25 minutes is only the maximum wait. If the worker finishes after, say, 3 minutes, Main resumes immediately.

And if the wait times out with no new worker state, that timeout is explicitly NOT treated as a reason to start polling/listing threads/messaging/replacing the worker. Main simply enters another long wait.

I also have the same idea for the persistent Companion: start it early, let Main continue independently, and only wait when the Companion result actually gates a decision.

So effectively:

Main → delegate → do independent work if available → event-driven wait when idle → wake immediately when child completes → no repeated status polling

The new `send` thing you mentioned is interesting though.

If a subagent can now proactively message/wake the orchestrator while it's still running — for example only when it hits a blocker or needs a decision — that could be a useful extra layer on top of the long wait.

I wouldn't want workers constantly sending progress updates because that could just recreate the token problem in the opposite direction, but:

long `wait_agent` + worker → Main `send` only for blocker/material event

sounds potentially ideal.

I'm going to look into exactly how the new inter-agent `send` behaves.

- by [unknown](#) **&#x21C5; 1**
  <br/> the only thing that matters is the outcome and quality of the task. If you ran for 4 hours but didnt finish the task it doesn't matter.

- by [unknown](#) **&#x21C5; 1**
  <br/> Yes, have to trade.slower to save more tokens. With the same test, assign Sol to take care of it. It was completed in 23 minutes but everything didn't work, patchwork and had to be edited a lot later for everything to work

- by [unknown](#) **&#x21C5; 1**
  <br/> Gracias por compartir amigo soy nuevo sobre el tema orquestación. Tengo la duda desde donde sería bueno probarlo con codex desktop o desde el terminal?

- by [unknown](#) **&#x21C5; 1**
  <br/> both of them

- by [unknown](#) **&#x21C5; 1**
  <br/> can this be used for non-coding projects, or it's optimized for coding?

- by [unknown](#) **&#x21C5; 1**
  <br/> it's optimized for coding .

- by [unknown](#) **&#x21C5; 1**
  <br/> Genuine question because im trying to find some reliable information about AI workflows (which has been very hard)

Have you compared this Orchestration approach vs Single Agent workflow?

Like simply using a capable agent like Sol High or Astra low/medium and compared the usage?

Do you have evidence or tests that proved that orchestrating agents is token efficient or produces a beter output than simply prompting agents directly on a continuous worktree? Or with a set goal?

- by [unknown](#) **&#x21C5; 1**
  <br/> Of course it's there, in my previous post. I didn't want to put everything in the post. Or you can check it out here: [https://github.com/viettran-edgeAI/codex_workflow/tree/main/light_benchmark](https://github.com/viettran-edgeAI/codex_workflow/tree/main/light_benchmark). Basically, it will be faster, but it misses more details.

- by [unknown](#) **&#x21C5; 1**
  <br/> ty will take a look
