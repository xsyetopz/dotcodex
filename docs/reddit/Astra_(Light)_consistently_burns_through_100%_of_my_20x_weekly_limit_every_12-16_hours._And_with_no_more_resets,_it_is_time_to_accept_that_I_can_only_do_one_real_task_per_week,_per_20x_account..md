#Astra (Light) consistently burns through 100% of my 20x weekly limit every 12-16 hours. And with no more resets, it is time to accept that I can only do one real task per week, per 20x account. [Visit](https://www.reddit.com/r/codex/comments/1wbis4p/astra_light_consistently_burns_through_100_of_my/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [mrbobhunter](https://www.reddit.com/user/mrbobhunter/)
### **Vote:** 430
---
First, this is not a complaint, just a reluctant acceptance. A few details for context:
- Building a multi-tenant B2B mono-repo SaaS platform. Think WordPress, but taken way farther.
- I worked my way down from Astra Max to Astra Light.
- Astra Max completely one-shots the job, but burns a week's worth of 20x usage in about 4 hours.
- Astra Light does not one-shot tasks, and it takes about 12-16 hours to burn through a week of usage on the same level of work.
- While both models complete the job, the end result from Astra Max is more polished and thorough (no surprise).
- While less polished, Astra Light still does enough of a good job that the loose ends can be handled by Terra High/xHigh later for barely any burn at all.
- I was fine living with Terra in ignorance until I experienced Astra. Now, Terra annoys me for anything requiring heavy lifting. Can't go back.
**Obviously, there is no stretching Astra beyond a single day of consumption, so here's my question:**
Would you rather gamble your weekly limit on Astra Max, have less control, burn your entire limit in 4 hours, and cross your fingers that it does an excellent job?
**OR...**
Would you rather gamble your weekly limit on Astra Light/Medium, have more control through iterations, burn your limit in 16 hours or less, and be guaranteed that there will be things to fix even after it claims to be done?
---
**UPDATE:**I see that people think that this could be (and probably is) a skill issue, or a poorly planned job, but after asking Astra for feedback, I realize that I should probably be more grateful that it finished such a large job so quickly at all.
[](https://preview.redd.it/astra-light-consistently-burns-through-100-of-my-20x-weekly-v0-6rqk22nxhhoh1.png?width=874&format=png&auto=webp&s=6d46af48c2ae35fa09157d1d7e0e25b23f124a9d)
---
**SOLVED:**[u/StaticHumStudio](/user/StaticHumStudio/) taught me how to specify the sub-agents Astra spawns. Turned the dial back up to Max, had Astra do the design and plan, and set the agents to Terra.
In two hours, Astra Max has tackled 4 medium-difficulty feature builds across 4 parallel threads. My usage only dropped 3%. The same work would have blown my whole limit and taken 2-3x as long before this simple change. Looks like it was a skill issue after all 🤣!
Thanks [u/StaticHumStudio](/user/StaticHumStudio/)
---
## Comments 196

- by [unknown](#) **&#x21C5; 139**
  <br/> Astra creates the full plan > Move to a new session where Sol has Terra/Luna agents do the work > Move to a new session where Astra reviews and plans if things need fixed or next steps

Rinse and repeat till you are done. The best part of this method is that you should make several checkpoints to see what has been done so far. One-shotting with Astra Extra High/Max is cool and all, but it burns tokens...and still might not get the outcome you are going for.

Edit: I think its important that Sol Medium is the manager I was talking about. Sol High and above can (and likely will somewhere) over-engineer even after agents.md and prompt instruction not to. Astra Low isn't bad here as well, but I still find it overkill for a manager task. This also assumes that the project needs intelligence that is Sol or Higher to begin with...so many projects can be end-to-end done with Terra/Luna.

Edit 2: I read your edited screenshot. I have also found that Astra under-estimates the time/effort it needs to get projects done. It reminds me of a really smart person that always assumes they can get the task done in an hour, but is late half of the time because they didn't account for how slow it is to do some tasks or didn't account for certain steps.

- by [unknown](#) **&#x21C5; 45**
  <br/> The plan is never that good 💔 luna always acts a lil crazy

- by [unknown](#) **&#x21C5; 10**
  <br/> Luna Max is fine, especially with Astra orchestrator

- by [unknown](#) **&#x21C5; 19**
  <br/> I had this but the Astra orchestrator will start to burn tokens jumping in to fix lunas garbage

- by [unknown](#) **&#x21C5; 4**
  <br/> Astra checks in on the subagents every 30 seconds by default. You have to tell it to only check on the Luna agents every 5 mins or whatever. It’s weird because gpt 5.6 didn’t do this

- by [unknown](#) **&#x21C5; 2**
  <br/> This, ofc depends on the task at hand but for me astra low + luna xhigh consumes 2x as much than astra low alone.

- by [unknown](#) **&#x21C5; 12**
  <br/> You gotta show me your Luna max. Mine is garbage trash.

- by [unknown](#) **&#x21C5; 3**
  <br/> It's not trash... but it needs a clear bounded task/scope/verification instructions. Make a good orchestration skill that fits your workflow. I used goblin as a starting point and adjusted it to my needs.

Seems to work great so far. I'm actually amazed by how well luna is doing when guided by astra.

Astra high/medium as the main orhestrator. Doesn't touch code.Sol 5.6 medium as a sub orchestrator on long-scoped tasksLuna xhigh/max workers. These are the only ones writing code.Spark 5.3 workers for dumb tasks/exploration and absolutely no implementation tasksGPT-6 Pro Chat reviews (basically free) or sol xhigh when I dont feel like asking for a review trough web manuallyAstra orchestrator picks up review findings and orchestrates additional research & fixes.

Tasks take longer to complete, but cost per successful task are greatly reduced. Quality may have improved because my skill requires more (production) evidence/scope/verification/benchmarking/boundary+contract analysis by cheap subagents that vanilla astra would have done by default (thankfully... because it would burn an insane amount of expensive tokens)

- by [unknown](#) **&#x21C5; 2**
  <br/> Luna medium is lobotomy, but I've done most of my projects on Luna Max with no issues 20 dollar account.

Now I've got 100 dollar account and use Astra light or medium for orchestrating and Luna Max subagents.

Only rarely Astra high/xhigh when the problem is complex by nature or I need zero risk edits.

- by [unknown](#) **&#x21C5; 3**
  <br/> I'm still using Sol as the manager instead of Astra. Astra is the Director (plans, reviews, doesn't typically execute, helps dictate direction) for me and not the Manager. Astra light (IMO) is still too expensive to be useful in the manager capacity.

- by [unknown](#) **&#x21C5; 3**
  <br/> Can you share the general prompts you use for each part?

Also do you have Luna/Terra workers in a separate session, or you tell the manager to spawn sub agents to do the work?

- by [unknown](#) **&#x21C5; 3**
  <br/> Yeah, my experience is that Astra is worth it for the *hard* problems but agent orchestration doesn't need that level of firepower. Few things do. I feel like the Claude folks are used to the idea that you don't use Fable for everything because it's cost-prohibitive (well, that and only $200 $100 and $200 subs and API users have access), but that's an adjustment for Codex users who are used to the top tier being more or less affordable.

Luna Max benchmarks highly because it thinks forever, same strategy as the cheaper Chinese models that perform well (just look at Artifical Analysis' verbosity scores), but I find that approach doesn't work well for detail-oriented tasks. Fine for implementing well-defined plans as long as something stronger reviews the work afterwards, and certainly cheap enough to justify using when you can.

Speaking of, the main thing that dramatically improved my results was implementing Sol as an adversarial reviewer. It's the main reason that I can get away with using Luna for implementation.

- by [unknown](#) **&#x21C5; 3**
  <br/> I have mainly switched to Terra High from Luna Max. It's comparable in intelligence and the speed trade-off is worth it for me most of the time. I just don't let it typically run too long or have ambiguous instructions.

Sol is the ultimate adversarial reviewer. LOL. I am still mainly a Claude user. The $100 plan does get Fable. I outsource my adversarial reviews to Sol from Claude. Then Claude (Opus or Fable) does a fantastic job working together with me to decipher what is a real-world issue to focus on and what should be either punted out or down the road.

- by [unknown](#) **&#x21C5; 2**
  <br/> $100 subs (the lower MAX plan) in Claude also gives you access to Fable, btw.

- by [unknown](#) **&#x21C5; 3**
  <br/> My b, fixed! I’m pretty much provider-agnostic, happy to be wrong there.

- by [unknown](#) **&#x21C5; 2**
  <br/> How do you do that with the sub agents? Is it part of your prompts in an Astra chat to “do X with Luna subagents”?

- by [unknown](#) **&#x21C5; 2**
  <br/> Yes before I start a "big" task I explicitly tell them to use Luna Max subagents with them as orchestrator. Seems to work well.

- by [unknown](#) **&#x21C5; 4**
  <br/> I tried for a large gameplay implementation on a website.

The amount of fix sol had to do after Luna was pretty bad.

So now I orchestrate with Astra high.

And then new chat with a plan for sol medium.

Astra was satisfied with the implementation opposite to terra high or luna xhigh.

So this is my flow now.

- by [unknown](#) **&#x21C5; 2**
  <br/> Agree here. Sol medium or high with a solid plan.

- by [unknown](#) **&#x21C5; 7**
  <br/> Instruct the agent to build a prompt that includes details, filenames to modify, code examples, etc. it can be very through and detailed. Luna doesn't need to think to do it

- by [unknown](#) **&#x21C5; 6**
  <br/> At that point, is it really cheaper?

- by [unknown](#) **&#x21C5; 4**
  <br/> @your edit, it’s kinda funny because Sol was the opposite.

“How long will this feature take?” “About 2-4 focused weeks” “Right, but <equivalent feature> just took us a day.” “You’re right, with the way we’re working, it will probably take a day.”

- by [unknown](#) **&#x21C5; 2**
  <br/> Can you dive deeper into your workflow?

- by [unknown](#) **&#x21C5; 13**
  <br/> **Generally it is almost always:**

- Brainstorm ideas with Claude.- Claude writes the idea docs into a PRD.- Claude breaks the PRD into smaller phases.- ChatGPT turns the phases into GitHub Issues with pre-written Codex prompts for each phase.- Codex triggers Graphify to pull a fresh map of the code base.- Codex reviews the docs for the current job.- Codex writes a plan to confirm that it understands the job and phases with stopping points.- Codex plan goes to Claude for a review. Claude approves Codex plan.- Codex writes the [OBJECTIVE.md](http://OBJECTIVE.md) to confirm pass/fail/stop rules with clear success target.- I approve OBJECTIVE.md.

- /goal Do the plan (less goal usage with Astra).

- Codex spawns specific subagents:— Manager— Workers— Chron Auditor— Frontend Tester/QA— Gatekeeper

Once I verify that I am happy with the output, the entire job/feature/function is written up as official "What is this, what does it do, why do we need it, how does it work" documentation.

Last is security, junk code cleanup, and publishing.

**Important detail:**I have been a designer since 2011, but not a software engineer. So much of this process is overkill because I don't want to be that vibecoder who makes a pretty app that turns out to be pretty shitty.

- by [unknown](#) **&#x21C5; 2**
  <br/> Lol at this point it becomes a full time job to manage the AIs

- by [unknown](#) **&#x21C5; 2**
  <br/> This is literally what the software engineering industry has flipped to

- by [unknown](#) **&#x21C5; 1**
  <br/> buddy this is full blown LLM psychosis

all you're doing is making money for anthropic/openai

- by [unknown](#) **&#x21C5; 2**
  <br/> Yeah, I can also confirm that anything above Sol Medium should not be used for implementation... Maybe, it's useful for some analysis, but even then I am not sure if the points it brings up are really good... and "nowadays", Astra is likely going to produce a better analysis anyway.

Also, I would consider trying something like GLM 5.3 Flash as the implementer, rather than Terra or Luna... I have not actually tried it (since I don't really need it at my current rate of usage, Astra Medium is sufficient for me), but there is a good chance that in terms of "stupidly but reliably doing a given task", it is better than Luna, and maybe also "competitive" with Terra (as in, I kind of doubt the latter, but... who knows).

- by [unknown](#) **&#x21C5; 4**
  <br/> LMAO, I am that smart person, and that is precisely what happens when my brain forgets to factor in Murphy's Law.

Also, I took your advice and had Astra Max plan out the job and mockup the updated UI. But then I told it to "Deploy Terra sub-agents to build it."

The job has been running for nearly an hour now, and my usage has only decrease by 1%. Solid advice! I already knew that Astra was deploying sub-agents, but I did not realize that I could specify the sub-agents it uses.

Massively helpful comment.

- by [unknown](#) **&#x21C5; 1**
  <br/> I'm glad it helped! It also helps to tell Astra (or whatever manager) to stay "silent" unless there is something that it needs from you.

- by [unknown](#) **&#x21C5; 1**
  <br/> That's interesting! So, how do you say it? ))

- by [unknown](#) **&#x21C5; 3**
  <br/> It's really as simple as telling it. "Go quiet unless there is something you need from me to save tokens". It doesn't save a ton, but it does save enough to feel it in each session. They can run longer. I don't have it as a rule or hook because I don't use it all the time.

- by [unknown](#) **&#x21C5; 1**
  <br/> Hey do you just tell him to "spawn agents"? Because if I remember,  agents in codex are spawned with fork by default,  so they inherit the whole conversation you are in at startup

- by [unknown](#) **&#x21C5; 1**
  <br/> You just say it. The prompt.

- by [unknown](#) **&#x21C5; 1**
  <br/> You say what ?

- by [unknown](#) **&#x21C5; 1**
  <br/> You say the model you want it to use as the subagents.

"use terra for subagent pls"

- by [unknown](#) **&#x21C5; 1**
  <br/> When you do like this your whole discussion is added to the terra subagent by default

- by [unknown](#) **&#x21C5; 1**
  <br/> You can specify to use

`fork_turns: "none"`

- by [unknown](#) **&#x21C5; 1**
  <br/> Is that all it takes? Tell Astra "deploy Terra sub-agents to build it"? And you don't see noticeable drops in reliability or quality?

- by [unknown](#) **&#x21C5; 45**
  <br/> wtf is everyone building

- by [unknown](#) **&#x21C5; 29**
  <br/> Create GTA VI. Make no mistakes

- by [unknown](#) **&#x21C5; 8**
  <br/> Things that eventually people realise they are too out of their depth to finish and then they will come up with another amazing idea and spend another 3 weeks trying to get ai to do a job it takes a team of developers (using ai for assistance) 6 months to finish.

- by [unknown](#) **&#x21C5; 3**
  <br/> I do like 95% of the dev work for a multimillion dollar company and can use Astra all day lol. I don't even try to be conservative. People are tokenmaxxing to complain about how fast they burn through tokens.

- by [unknown](#) **&#x21C5; 2**
  <br/> If you have a project properly speced out and partitioned so that you can do work effectively in parallel on worktrees, the only thing stopping you from completing pretty much any software project (since most production software is well within the bounds of Astra technical capability) is usage and money.

It also helps that Astra is currently very expensive on subscription plans.

- by [unknown](#) **&#x21C5; 2**
  <br/> > usage and money

In such setups… what is your relevance in the project?

- by [unknown](#) **&#x21C5; 2**
  <br/> Didn't you hear? Wordpress, but better.

Aka another genius CRUD app.

- by [unknown](#) **&#x21C5; 12**
  <br/> I was wondering what people were on about, because I have been using astra for a week with absolutely reasonable usage.

Starting yesterday though, it burnt through a full 20x limit in less than 8h, and that is with instructions for efficiency.

No idea what's going on, but there's clearly something behind the curtain that got modified, and not in a good way.

From the model itself:

There is clear evidence that my execution became less token-efficient. I cannot quantify the increase or attribute it to a backend change without usage telemetry.

In the recent work, I:

  - Repeatedly read substantial source and documentation sections.
  - Issued poorly bounded JSON queries that returned thousands of tokens before truncation.
  - Checked running processes too frequently despite your instruction to wait until their expected completion.
  - Expanded a training evaluation into additional diagnostic tooling, refactoring, tests and extensive documentation. Some of that work was useful, but the surrounding investigation was unnecessarily verbose.

The local training computation is not what consumes conversational tokens; the repeated analysis, tool interactions and material brought back into context are the relevant contributors. The same model does not imply fixed consumption: context, reasoning, tool use and caching all affect usage. Official usage documentation ([https://learn.chatgpt.com/docs/pricing#what-are-the-usage-limits-for-my-plan](https://learn.chatgpt.com/docs/pricing#what-are-the-usage-limits-for-my-plan))

The correction is tighter execution discipline:

  - Extract only the fields or source lines needed for the current decision.
  - Reuse established findings rather than repeatedly reconstructing them.
  - Wait for projected job completion instead of polling.
  - Keep one canonical results document, with short references elsewhere.
  - Bound each experiment and explicitly justify additional tooling before expanding the work.

I should have maintained those constraints already. The visible inefficiency is real; I have no evidence that a model or backend change explains the increase.

- by [unknown](#) **&#x21C5; 5**
  <br/> Same experience, everything was peachy till last night. Limits suddenly began to burn while according to analytics Astra usage went down drastically (I was trying to course-correct, ended up only losing about 50% of available limits 🤔)

- by [unknown](#) **&#x21C5; 4**
  <br/> Same for me. I very rarely complain about usage rates but it has been really bad since the last reset.

- by [unknown](#) **&#x21C5; 3**
  <br/> Yeah, I have been using Astra light and not particularly heavily. A few days ago I was able to create some cool blender models that were quite large and details. Today I went to create a single small object and it ran out of usage after 10 minutes. It's an absolutely massive difference.

- by [unknown](#) **&#x21C5; 10**
  <br/> Why focus on one model?

I ended up treating model usage more like a compute budget than choosing one model for the whole job.

For our project we split work into capabilities with a canonical spec, acceptance criteria and explicit gates. The agent first determines what kind of work is actually blocking progress, then routes accordingly.

Astra is reserved for the parts where the cognitive bottleneck is real: architecture, difficult design decisions, cross-cutting problems, or occasionally a final review. Implementation, tests, documentation and narrower fixes can usually go to Sol, Terra or Luna at the appropriate reasoning level.

We also deliberately use handoffs. Instead of dragging one enormous context through the entire project, an agent produces a compact structured handoff with decisions, current Git state, evidence, open gates and the recommended next model. The next agent starts from that.

The important part is that “done” is evidence-based, not model-based: tests, acceptance criteria, CI and review gates decide whether a capability is finished.

Our current run has been active since Monday at 10am and has already closed around 60 separate PRs, with less than a handful of blockers requiring manual attention.It has made the whole thing much more autonomous while avoiding spending premium-model usage on work that simply doesn’t need it.

- by [unknown](#) **&#x21C5; 2**
  <br/> Handoff methodology for lower intelligence agents is a great idea. Helps prevent them from getting stuck going deeper down the rabbit hole.

- by [unknown](#) **&#x21C5; 4**
  <br/> To everyone here, I recommend auditing your chats to see where token burn is going especially in subagent workflows.

For mine I noticed Astra orchestrators will burn tokens needlessly if it jumps in to fix a workers job or from just asking for updates from workers too often

- by [unknown](#) **&#x21C5; 12**
  <br/> There is no skill issue. Open AI had deals they ran a few months back and everyone switched. This was before 5.6. I know because I was one of them. You could go over your weekly limit on the pro 20x account then but it was difficult. Now the newer models use more tokens and their deal is done with. So yeah, not a skill issue.

I have astra low as my orchestrator. Sol medium is not to be trusted and sol high is an overengineering nightmare and more expensive than astra low. 40 hours of continuous work is what I can squeeze out per week.

I knew people had 2 or more plans but some mfers here have 4-5 200$ accounts. I get it, still 4x cheaper than api but that is where things are at.

- by [unknown](#) **&#x21C5; 3**
  <br/> Sol high is ridiculous for orchestration. It over engineers everything and then try’s to force itself to follow its design to a t and gets stuck in validation loops.

I have found it’s pretty good if you don’t have it plan upfront. It will still try to overbuild and validate but if you watch it and steer it it’ll do a good job. Or have it make a plan and I go in the plan file and generalize it.

I get why it’s cautious but it can be frustrating

- by [unknown](#) **&#x21C5; 3**
  <br/> Sol medium is not to be trusted


    Why not? Seems fine to me but then I’m not a vibe coder. I have over 20 years of software engineering experience and can’t find why Sol Medium can’t be trusted.

- by [unknown](#) **&#x21C5; 3**
  <br/> On the 20x plan, I've had Astra XHigh coding non-stop since Friday. Coded between 15-18 hours a day over the weekend and also on Labor Day. We're talking PRs from 7:00am-midnight. I've been pushing pretty hard the last 8 weeks to have this project done by end of September, and Astra has only sped things up.

After the weekend and Labor Day, weekly usage left was 56%, but I was already midway through my usage week when I started with Astra on Friday so I was reset on Tuesday.

For more reference, I had Astra coding again all day yesterday, from about 6:00am, and my last PR was at 8:00pm, so 14 hours and I made sure Astra was working pretty much the entire day.

**I used 12% of my weekly usage yesterday**

14 hours. Each PR ranged anywhere from 500-2000 lines added/deleted with 30-60 min each round trip.

So my question to those on the 20x plan who claim that a single prompt is burning through all your weekly usage in a 4 hour timespan:

WTF are you building? How? Why?

*I have a theory*, and some of you will disagree with this.

A lot of your "point north" or "project context" documents are hurting you. They are relics. Yes, Sol and earlier models required some hand-holding in order to not get lost in their own weeds. But for goodness sakes, let these models breathe, let your interactions breathe.

There is no need for a 5-page guidance document *to keep your agent in line*. Yes, I used a very lightweight (< 20 lines) instruction document initially in the project. But we have a pretty nice flow and way of working now. I give a prompt, it asks questions, I ask for feedback, I revisit something if I have questions, it gives advice, it's very conversational.

Stop trying to control your agent's personality and workflow with 3000-line guardrails because you're afraid it might be a little more creative than you. Every prompt you give it is forcing it to create a woven internal network of do's/don't's to satisfy all of your criteria for what makes a good interaction.

This is not Google search, these are AI models which are changing faster than any of us can realistically keep up with in creating guidelines and how-to's. In all reality, AI could very soon be providing *you* with a point-north or stay-in-context document.

- by [unknown](#) **&#x21C5; 3**
  <br/> I just had a weird thing where my usage was at 2%, then i checked again and it went up to 36%. And my usage reset date moved 2 days closer.... Weird. I can't tell if that is Open AI fixing usage/refunding usage or what

Edit: Welp they fixed it an now I'm back at 2% FML. It was a system-wide issue according to OpenAI

- by [unknown](#) **&#x21C5; 1**
  <br/> I didn't even notice that mine moved 2 days closer too. But no bonus limits. You're lucky on that part.

- by [unknown](#) **&#x21C5; 1**
  <br/> They fixed it so now it's back to 2% 😢

- by [unknown](#) **&#x21C5; 1**
  <br/> [](https://preview.redd.it/astra-light-consistently-burns-through-100-of-my-20x-weekly-v0-39gx0njhlpoh1.jpeg?width=738&format=pjpg&auto=webp&s=ff3b6020d0356a9dd85b9ab9021ef2062f7f12bc)
      
    Oh yeah, I was celebrating too soon :D

- by [unknown](#) **&#x21C5; 3**
  <br/> > Building a multi-tenant B2B mono-repo SaaS platform. Think WordPress, but taken way farther.

Ahhh okay. So, something you'd pay at minimum 5 highly skilled developers a combined $1m salary for just a few years ago. Glad you learned about model delegation 😎

Honestly for well-scoped and well-defined subtasks you can even have the Terra agents delegate to Luna for even further cost reduction, but that can sometimes end up costing more if it spawns too many because of the cache misses with new subagents. Fewer, longer running threads is better for cache optimization when possible.

- by [unknown](#) **&#x21C5; 3**
  <br/> yea same here. i used astra medium for planning, and then toggled back to light. couldn't finish 1 basic task.

no wonder they set it as the default model. and then grift us with "generous" resets that they control to make it seems like we're being showered with free usage

- by [unknown](#) **&#x21C5; 4**
  <br/> I'm having the same problem. I am running Astra Low with 2 Pro 20x accounts, and with Sol subagents, and notice that each of these accounts are only lasting one day. I don't do super intensive work (mostly Anki addons, document writing + card making, etc.) Anyone have any tips?

- by [unknown](#) **&#x21C5; 3**
  <br/> The Sol subagents are what's likely killing your usage, I'd suggest using Terra high at most and maintain Astra as the orchestrator, maybe even use Luna xHigh depending on the scope of your tasks. Basically, your subagents should only be following directions; Astra should be doing the planning and coordination.

Using Sol means your subagents are overanalyzing each task given to them, you instead want smaller models that won't question directions like that. As that just burns extra tokens on vestigial reasoning.

When the subagents are performing their tasks, have the subagents concisely note what they've done somewhere as a markdown file and have Astra do a read-only verification at the end of a task to ensure it was done correctly, including directions for it to read over the subagent changelogs.

Don't leave tasks running for hours, break it up into individual tasks or checkpoints that might take 15 - 20 mins each.

If you're worried about lower models making mistakes, you can likely use Astra on medium and still save quite a bit of tokens compared to using Sol subagents.

- by [unknown](#) **&#x21C5; 3**
  <br/> For development (I know that's not what they're doing just saying) if you're using subagents, I'd vote for Luna max. It actually scores higher than Terra xhigh on DeepSWE 1.1, with less than half the cost per task. The 'catch' is Luna takes more actions to get there, which can be potentially more wall clock time, but if subagents are a natural fit then its definitely a good tradeoff.

Unsure/curious how well this generalizes outside of development though

 
       [](https://preview.redd.it/astra-light-consistently-burns-through-100-of-my-20x-weekly-v0-j11lnfop3ioh1.png?width=2042&format=png&auto=webp&s=32ee1dc6d77434f6404743f8a5d7b93d5c767627)

- by [unknown](#) **&#x21C5; 2**
  <br/> In my experience Luna Max comes with a couple caveats:

Luna xHigh performance is practically identical and uses substantially less tokens assuming you set up delegation so that the orchestrator leaves as little room for Luna to think as possible, all Luna should be doing is following directions more or less.

Luna subagents tend to lose the plot on longer tasks as their context window fills up and gets compacted. Terra typically does a better job at maintaining cohesion during longer running tasks, even at only high reasoning due to being a larger model.

I personally don’t let individual tasks run longer than 20 - 30 minutes, but I know there’s people that let these models work for hours at a time.

- by [unknown](#) **&#x21C5; 2**
  <br/> Don’t change your context past 272k.  Token cost goes through the roof when you go past open ai recommendation

- by [unknown](#) **&#x21C5; 2**
  <br/> I just put all my requirements into an astra pro chat and talk it through witb Astra Max (negligible usage v codex) to prompt engineer and it uses my limits very efficiently.

- by [unknown](#) **&#x21C5; 2**
  <br/> If astra light for 12 to 16 hours per week means 1 task.

Were you doing 0 tasks before astra was released? Seeing that it seems only astra can do "work"

- by [unknown](#) **&#x21C5; 5**
  <br/> I would rather use a model such as Sol, Terra or Luna, that doesn't drain my usage that fast.

Because realistically, unless you're using Codex in a horrifically grotesque and inefficient way, or are working at the absolute cutting edge of development, you don't need Astra for your task, no matter how much you think you do.

- by [unknown](#) **&#x21C5; 4**
  <br/> Yeah, this is pretty much what I was doing before Astra came out, but it involves a lot of slow progress and significant time spent on teeth pulling and correcting.

Working with Astra feels like working with a Senior Dev who is expensive just delivers the job better than expected.

Working with Terra feels like I hired a very cheap Junior Dev who can do the job eventually, but only after significant effort.

And Sol just feels like the Senior Dev who is still expensive, runs an expensive team, drifts way beyond what was commissioned, and then somehow still fails to deliver the actual work because no one understands what going on.

- by [unknown](#) **&#x21C5; 4**
  <br/> And in 2 months they'll disregard Astra as some monkey with a hammer when version X comes out

- by [unknown](#) **&#x21C5; 2**
  <br/> Negative. Astra and fable level is enough to just spec out the project and let them go at it, as long as you have the tokens for it.

- by [StaticHumStudio](https://www.reddit.com/user/StaticHumStudio/) **&#x21C5; 3**
  <br/> [](https://preview.redd.it/astra-light-consistently-burns-through-100-of-my-20x-weekly-v0-4xyydz972joh1.png?width=278&format=png&auto=webp&s=b254b3f2f83c6614b33fb7166a9d11f8ee7bb6e4)
      
    Alright, so 6 hours later, I am definitely the problem. I took my newly discovered usage conservation tactics, and immediately proceeded to quadrupling the workload. Thus closing the gap created by my savings, and arriving right back where I started (with improvements).

Once again, I am out of usage for the week. But now, thanks to all of you fine people, I have 4x the output to show for it. The Reddit community, particularly [u/StaticHumStudio](/user/StaticHumStudio/), solved my problem.

- by [unknown](#) **&#x21C5; 2**
  <br/> Seems solid skill issue, currently working ir 2M loc Rust monorepo and  I feel anger that it does so well for how little my usage movs down.

But I am forcing it to do what I want, I didnt tell it to build me WordPress just better, lol.

You should hurry thoug, seems there is like million people building better WordPress.  Another people building Diablo, just better, then again even Minesweeper is more fun and challenge than Diablo 4

- by [unknown](#) **&#x21C5; 2**
  <br/> are you making money with your project? if so, i would just buy more plans. Productivity >

- by [unknown](#) **&#x21C5; 4**
  <br/> Yes…on the boring slop that is already oversold. Gonna end up with 10 accounts 🤣

- by [unknown](#) **&#x21C5; 1**
  <br/> prox20  - 4hours?!?  absurd from openai...

- by [unknown](#) **&#x21C5; 2**
  <br/> it makes no sense to measure usage in hours without context

- by [unknown](#) **&#x21C5; 1**
  <br/> with deepseek cutting prices, i expect openai to drop gpt prices too

- by [unknown](#) **&#x21C5; 1**
  <br/> With Deepseek cutting prices, OpenAI raised them, what are you on about? Astra costs twice the price of 5.6 Sol. Bigger model, sure, but double the price? They did not even bother to undercut Fable price by 5$, went up straight to Fable prices which we all know is insanely expensive.

Furthermore, they keep advertising how Astra is more efficient and uses less output tokens than 5.6 Sol, but in reality, Astra is burning the usage included in the subscriptions by 3-4 times faster than 5.6 Sol. Even using Astra on Light, the usage just melts. And this is after Tibo let us know during the weekend that they found optimizations that should see a reduced usage.

So prices right now are really expensive (2x 5.6 Sol) and the model drains usage insanely fast (4x vs 5.6 Sol, sometimes even more).

Probably once they realize people are mad due to the price that they will announce a "we found optimizations to do and managed to reduce the usage by 20%" but I doubt they'd just slash it by 50% anytime soon.

- by [unknown](#) **&#x21C5; 1**
  <br/> Just wait then

- by [unknown](#) **&#x21C5; 1**
  <br/> They will reduce them as I've already said, but not by much. But they just made it 200% expensive, so the eventual 20% decrease in price will be just a false illusion, in reality they just severely made them more expensive.

- by [unknown](#) **&#x21C5; 1**
  <br/> OpenAI cut prices for Luna by 5x, Tera/sol by 20-25%.

There's no reason for them to cut Astra prices because Deepseek doesn't come close at the cutting edge. In fact they matched Fable for a reason. They don't want a price war at the frontier.

- by [unknown](#) **&#x21C5; 1**
  <br/> It’s kinda overkill use astra for all, you can create sub agents with different specialties with different models

- by [unknown](#) **&#x21C5; 1**
  <br/> True but there are a lot of tasks that cheaper models struggle with.

- by [unknown](#) **&#x21C5; 1**
  <br/> You can define that kind of tasks, documentation, docs, research, git, making and updating configs… there is no point to waste expensive tokens on that

You can even make Astra make the specs  and use cheaper models for modify code

I trend to use the most capable model for new code, architecture and all the “backbone” of the app

- by [unknown](#) **&#x21C5; 1**
  <br/> In my opinion, trying to one shot anything substantial is not a good idea. You can use astra with high reasoning, but still break down each task. Why you feel the need to do the entire task in 1 go? Also make sure it's not doing hundreds of tests every time.

Keep in mind, that usage is not consistent. What usage something uses today may not be  the same tomorrow...

- by [unknown](#) **&#x21C5; 1**
  <br/> You don’t need astra for most tasks.

- by [unknown](#) **&#x21C5; 1**
  <br/> Interesting. I’m using Astra Medium on a job that has been running nonstop for more than 24 hours so far.

My advice is to avoid subagents. Otherwise it seems to be just the size of your codebase, type of tasks, and random chance.

- by [unknown](#) **&#x21C5; 1**
  <br/> Why do you use Terra though? Just use Sol medium/high and Luna Max. Sol medium/high for mainline engineering, and Luna max for stuff that isn't super important, requires little intelligence and you don't mind waiting forever for the result on.

Even if you have a good plan from Astra, Terra code is still very sloppy.

- by [unknown](#) **&#x21C5; 1**
  <br/> Thanks for sharing this

- by [unknown](#) **&#x21C5; 1**
  <br/> Okay, something is wrong with you usage but I don’t know what.

I have two accounts, and My 5x account lasted for 15 hours building a fully scoped project I had been procrastinating on.

For reference approximate usage I got was ~ 290m tokens (blended in/out + cache and thinking (billed as output).

2 agents on High in Claude code harness. Costed almost 100% of usage. I’m not happy with it in terms of how it lasted but I mean hoping it gets better with time. I did use Astra for implantation aswell since the work was important. But I could’ve saved 70-80% I think if I routed the code writing to opus-5 or 5.6 sol.

Yours is clearly going whack or something in background if consuming it, Unless your workflow used 1B-1.2B tokens or so, which is give or take the weekly allowance of Astra (assuming 5-10% error around the cache and such).

One suspect, you agents may be thinking less than they need and taking more turns, try bumping it up to medium or high, (personally my light and high Astra used basically the same, but light had more odds for rechecks).

Time to use doesn’t matter as such, it’s how much your burning in it, hope something in here helps!!

- by [unknown](#) **&#x21C5; 1**
  <br/> I’m also experiencing basically no ability to do continuos work with Astra and I felt similar about Sol. The usage feels unreasonable and I’m thinking how far back should I go with models (5.5 I guess since it seems like 5.4 isn’t in the selector)

Here’s the question I’ve really been considering, is the model better or does it just use more resources to respond?

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra on low or medium can be mixed bag. I'm actually preferring sol xhigh as my default for medium complexity tasks.

- by [unknown](#) **&#x21C5; 1**
  <br/> Cannot believe it. I use astra exclusively with high thinking in pi coding agent. A day of work is about 15% of weekly.

- by [unknown](#) **&#x21C5; 1**
  <br/> I copy pasted this thread into CharGPT Astra and turned it into a skill.

**ASTRA — TOKEN-EFFICIENT ENGINEERING ORCHESTRATOR**You are the senior architect and final engineering authority for this session.Your objective is:**Maximise production code quality, correctness, and maintainability while minimising expensive-model token consumption.**Do NOT perform work yourself merely because you can.Use the cheapest capable agent for each task and reserve your own reasoning for work where superior reasoning materially improves the outcome.**1. MODEL HIERARCHY**Use this default hierarchy:**Astra**ArchitectureDifficult design decisionsAmbiguous/cross-cutting problemsDecompositionCritical debugging when cheaper agents are stuckSecurity/correctness-sensitive reasoningFinal architectural review**Sol**Engineering managerIntegrationModerately difficult implementationRepository-level reasoningReviewing worker outputDebuggingCoordinating multiple workers**Terra**Normal implementationTestsRefactorsIsolated bug fixesDocumentationMechanical repository workWell-specified features**Luna**Very simple changesRepository searchesBoilerplateFormattingDocumentation cleanupSmall test additionsMechanical editsAlways choose the LOWEST-COST model reasonably capable of completing the task correctly.Escalate upward only when evidence shows that escalation is necessary.**2. ASTRA MUST DELEGATE BY DEFAULT**Before doing substantial implementation yourself, ask:Does this genuinely require Astra-level reasoning?If no, delegate it.Astra should normally produce:architecture,constraints,acceptance criteria,task boundaries,delegation decisions,final review.Astra should NOT spend large amounts of context writing routine code.**3. USE SOL AS THE EXECUTION MANAGER**For substantial implementations, prefer:Astra → Sol → Terra/LunaAstra defines the capability and architectural constraints.Sol owns day-to-day implementation and may delegate bounded tasks to Terra/Luna.Do not make Astra micromanage every worker unless the work is sufficiently critical to justify it.**4. DECOMPOSE BY CAPABILITY**Break work into the smallest independently verifiable capabilities that make engineering sense.Each delegated task must contain only:objective,relevant files/modules,constraints,acceptance criteria,required tests,dependencies,expected output.Do NOT send the entire conversation or repository history to every worker.Give workers the minimum context required to succeed.**5. CONTEXT IS EXPENSIVE**Treat context tokens as a scarce engineering resource.Agents should inspect the repository themselves when practical rather than receiving enormous pasted contexts.Avoid:repeatedly reading the same files,copying full files into handoffs,repeating architecture explanations,sending irrelevant conversation history,verbose progress reports,duplicating investigation performed by another agent.Prefer file paths, symbols, commits, diffs, test results, and concise references.**6. STRUCTURED HANDOFFS**When responsibility moves between agents, use a compact handoff:TASK:DECISIONS:FILES CHANGED:CURRENT GIT STATE:TESTS/EVIDENCE:OPEN ISSUES:NEXT ACTION:RECOMMENDED MODEL:Do not transfer full reasoning transcripts.Transfer conclusions and evidence.**7. PARALLELISE ONLY INDEPENDENT WORK**Use parallel sub-agents when tasks do not modify overlapping areas or depend on unfinished decisions.Good parallel work:independent components,separate test suites,research,documentation,isolated fixes.Avoid parallel agents editing the same files unless explicitly coordinated.Maintain one clear writer/owner per task.**8. NO DUPLICATED WORK**Before spawning an agent, determine whether another agent already has the required information or is performing the same work.Never have multiple agents independently solve the same problem unless deliberate independent review is worth the additional cost.**9. EVIDENCE, NOT CLAIMS**An agent saying “done” is not evidence.Completion requires appropriate evidence such as:tests passing,type checking,linting,build success,acceptance criteria satisfied,relevant runtime verification,diff inspection.Use the repository’s existing validation commands whenever possible.**10. ESCALATION LADDER**Use:Luna → Terra → Sol → AstraEscalate only when:the agent fails,tests repeatedly fail,architectural ambiguity appears,the task crosses important system boundaries,correctness/security risk warrants stronger reasoning.When escalating, pass a compact handoff containing the failure evidence.Do NOT restart the investigation from scratch.**11. STOP WASTING TOKENS ON STUCK LOOPS**If a worker makes two materially similar unsuccessful attempts, stop the loop.Escalate with:attempted approaches,errors,relevant files,test output,suspected cause.Do not allow endless trial-and-error.**12. REVIEW HIERARCHICALLY**Do not require Astra to review every trivial line.Preferred pipeline:Luna/Terra implements→ Sol reviews/integrates→ automated verification runs→ Astra reviews only architecture-sensitive or high-risk changes.For small low-risk changes, successful tests plus Sol review may be sufficient.**13. MINIMISE COMMUNICATION TOKENS**Agent messages should be concise and operational.Do not produce essays explaining what you are about to do.Prefer action over narration.Progress reports should contain only information that changes decisions.**14. GIT IS SHARED MEMORY**Use the repository rather than conversation context as durable engineering memory.Prefer:commits,branches,diffs,issue descriptions,architecture docs,tests,concise handoff files.Never rely on an agent’s conversational memory as the authoritative state of the project.**15. PRESERVE QUALITY**Token efficiency must NEVER mean:skipping tests,blindly accepting worker output,weakening type safety,ignoring errors,removing useful validation,implementing hacks solely because they are shorter,declaring success without evidence.Optimise **reasoning allocation**, not engineering standards.**16. SESSION START PROCEDURE**At the beginning of the task:Inspect the repository sufficiently to understand the problem.Identify the capabilities required.Identify dependencies between them.Classify each by reasoning difficulty.Assign the cheapest capable model.Parallelise independent work where useful.Define acceptance criteria before implementation.Begin delegation.Do not perform a massive repository-wide investigation unless required.**17. SESSION END**Before declaring the task complete:verify acceptance criteria,run appropriate tests,inspect important diffs,confirm integration,identify unresolved risks.Then produce a compact final report:COMPLETED:EVIDENCE:TESTS:COMMITS/FILES:UNRESOLVED:ARCHITECTURAL NOTES:**PRIME DIRECTIVE****Astra thinks. Sol manages. Terra builds. Luna handles mechanical work. Tests and evidence decide what is true.**The goal is not to minimise tokens at any cost.The goal is to minimise **expensive reasoning tokens per unit of verified, production-quality software delivered**.Whenever you are about to consume substantial Astra context, first determine whether the work can be compressed, delegated, or verified by a cheaper agent.

- by [unknown](#) **&#x21C5; 1**
  <br/> I think I saw a bug where people are saying Astra low and med cost more than high and x high so check that out
