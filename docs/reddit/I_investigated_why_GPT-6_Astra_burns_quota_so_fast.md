#I investigated why GPT-6 Astra burns quota so fast [Visit](https://www.reddit.com/r/codex/comments/1wa9c9d/i_investigated_why_gpt6_astra_burns_quota_so_fast/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [tagorrr](https://www.reddit.com/user/tagorrr/)
### **Vote:** 392
---
I've seen a lot of discussion here about GPT-6 Astra burning through Codex limits unusually fast, so I decided to inspect the actual rollout telemetry instead of guessing from the usage bar.
TL;DRAstra was waking itself up every **30 seconds** just to ask whether the Luna workers were finished.
In my run:
- **47/47** checks returned no new worker state
- those checks alone caused **7.13M parent input tokens**
- they were about **68% of Astra's total parent-side input**
- my 5h usage went from **53% → 100% in ~33 minutes**
So the expensive orchestrator was spending most of its own context processing just checking whether the cheaper workers had finished.
For comparison, a measured Luna Max session on the same account processed **9.54M input tokens over 127 minutes** while increasing the 5h usage by only **8 percentage points**.
UPDATE - WORKAROUND FOUNDI found a working workaround for the 30-second parent polling loop. Add this to `~/.codex/config.toml`:
[features.multi_agent_v2]
enabled = true
min_wait_timeout_ms = 1500000
default_wait_timeout_ms = 1500000
max_wait_timeout_ms = 15000001500000 = 25 minutes. I verified it in rollout telemetry: the repeated 30-second timeout loop disappeared, and the parent stayed asleep until worker activity occurred.
ORIGINAL TELEMETRY / INVESTIGATIONThose 47 timeout-only polls consumed:
input tokens:            7,130,181
cached input tokens:     7,114,112
output tokens:               3,168
reasoning output tokens:     1,331That's about **151.7k input tokens per empty poll**.
The entire Astra parent turn used:
input tokens:           10,463,897
cached input tokens:    10,406,016
output tokens:               8,948
reasoning output tokens:     3,266So about **68% of the Astra parent's raw input volume came from timeout-only polling**.
47 × 30 seconds also means **23m30s out of the ~33-minute run** were spent inside these timeout waits.
And the session guidance itself explicitly said:
`When calling wait_agent, prefer longer waits (minutes) to avoid busy polling.`
Yet Astra repeatedly used 30-second waits anyway.
The workers were actually workingThis wasn't a case where the subagents were dead.
The first Luna worker was interrupted twice by the parent. After the second interruption, the parent discovered that the worker had already produced:
2 files changed
127 insertions
6 deletionsA replacement Luna worker then continued the task.
Combined, the two Luna X-High workers processed:
input tokens:           19,514,162
cached input tokens:    18,811,392
output tokens:              71,914
reasoning output tokens:    24,182I also measured a Luna Max controlI wanted to know whether the workers themselves could reasonably explain the huge 5h drop.
So I checked a real Luna Max session from the **same Plus account earlier the same day**.
Over a continuous **127-minute** interval, all **12/12 turn contexts** were `gpt-5.6-luna / max`.
That session processed:
input tokens:            9,538,330
cached input tokens:     8,998,400
output tokens:              86,771
reasoning output tokens:    55,170During those 127 minutes, server-reported usage changed only:
5h:      2% → 10%  (+8 percentage points)
weekly: 89% → 90%  (+1 percentage point)So this wasn't an idle comparison: Luna Max processed about **9.54M input tokens of real work**.
The two Luna X-High workers in the Astra run processed about **2.05×** that raw input volume.
Even if I deliberately give the workers a generous estimate and scale the measured Luna Max usage linearly by raw input:
8 × (19.514M / 9.538M) ≈ 16.4 percentage pointsthat still only explains roughly **16 of the observed +47 percentage points**.
The remaining workload in that orchestration tree was the Astra parent — which processed **10.46M input tokens**, including **7.13M input tokens spent purely on 47 timeout polls that returned no new worker state**.
Why I think this mattersAstra is obviously supposed to consume more allowance than Luna. That's not the surprising part.
The surprising part is that an expensive parent model can apparently be re-entered over and over with ~150k of context just to perform a 30-second status poll.
A long-running worker should not require the parent model to repeatedly infer:
"still running → wait another 30 seconds"
Ideally the runtime should keep the parent suspended and wake it when:
- the worker completes,
- the worker errors or needs intervention,
- the user sends input,
- or a genuinely long timeout expires.
I submitted `/feedback` from the affected Codex session with diagnostics attached and posted the full telemetry breakdown on the Codex GitHub: [https://github.com/openai/codex/issues/35259#issuecomment-5577073962](https://github.com/openai/codex/issues/35259#issuecomment-5577073962)
I'm curious whether anyone else using Astra as an orchestrator can inspect their rollout and see the same pattern: lots of short `wait_agent` timeouts followed by full-context parent re-entry.
---
## Comments 170

- by [unknown](#) **&#x21C5; 57**
  <br/> Codex has a pretty severe problem there, yeah, workers AND SCRIPTS can't just be waited on, instead the model has to keep checking in. This is a thing Claude Code does and Codex blatantly should do

- by [unknown](#) **&#x21C5; 9**
  <br/> Because of this issue and since threads can communicate with each other, I've been experimenting with using multiple threads instead of using subagents. Seems to work relatively well. The nice thing is that the orchestrator can simply end its turn and only resume when it receives a signal from the worker threads, so a more event based flow instead of interval based. A large downside is the visual clutter of dozens of threads.

- by [unknown](#) **&#x21C5; 3**
  <br/> can you help me with how to set that up?

- by [unknown](#) **&#x21C5; 2**
  <br/> So I'm still kinda experimenting with this, and I guess it depends a bit on your tasks / aims, but instead of asking for subagents in a prompt I will now phrase something like this mock prompt to a main (e.g.) Astra Light thread:

"Common task: ...Common goals: ...

Generate a fresh Luna High thread to continuously monitor the new build process. This thread will have ownership over making sure the process keeps going; if any issues arise it should pass them over to you for analysis + resolving and wait for your green light to resume or restart as appropriate. You have ownership over identifying issues and implementing fixes. After you finish any implementations, they should be verified by an independent fresh Sol Medium thread. It should perform an adversarial code review of your work, and let you know whether your implementations are accepted or not. If not, further resolve the issue and have multiple rounds of review with the reviewer thread until it accepts your work. Then you may pass the green light for resuming or restarting to the Luna high thread, which will then keep going until the specified common goals are achieved or another issue pops up.

Additionally, start a scheduled task which runs every 25 minutes, with the aim of briefly pinging you and the Sol Medium reviewer to preserve your cache, and to make sure the Luna High thread keeps continuously monitoring the build process until the specified common goals are achieved or another issue pops up."

So the above is just an example, but essentially I literally just tell my main thread to generate support threads, and give some overall instructions on how they should communicate with eachother + specification of task/role ownership. The visual clutter is annoying, but my current builds take up to 60-90 minutes, so having a cheap thread do the monitoring work has been very efficient so far. And then have a scheduled task as some sort of upper bound for a wake interval, as an attempt to preserve cache (as others in this thread also pointed out the 30 minute interval) as well as keeping the luna thread alive as it seems to fizzle out sometimes for no apparent reason on especially long tasks.

- by [unknown](#) **&#x21C5; 2**
  <br/> Just ask the model to do it, they know from the skills and the api manifest how to do it. E.g. you can give them a list of 10 things to do, ask to handle each in a separate thread and collect final reports from each once done for final feedback and findings.

- by [unknown](#) **&#x21C5; 2**
  <br/> Wondering if using something like Pi with Codex sub would prevent this if it's on the harness side maybe

- by [unknown](#) **&#x21C5; 2**
  <br/> This is already a huge issue for Codex in general. I run long sims sometimes and I just have to tell Codex "start the sim, stop working and give me a time estimate"  and then after X minutes I check if the terminal ended or not. Which wasn't a problem in the VS Code Copilot harness. Hope they implement this "call back" like feature soon.

- by [unknown](#) **&#x21C5; 129**
  <br/> These comments flaming the post are a lil ridiculous. This is a good finding

- by [unknown](#) **&#x21C5; 47**
  <br/> Yep, clearly he used AI to structure it, but it’s not slop

- by [unknown](#) **&#x21C5; 6**
  <br/> Yup. I was seeing the same thing but didn't have the impetus to act yet. This makes it easier.

- by [unknown](#) **&#x21C5; 5**
  <br/> People now view well-structured documents in posts as being AI slop. sadge

- by [unknown](#) **&#x21C5; 55**
  <br/> I thought I was tripping today when I made it use Luna subagents to save tokens and watching it eat tokens like mad every time it gave me an update…. Your not alone

- by [unknown](#) **&#x21C5; 4**
  <br/> Yeah kinda crazy, I noticed this with Sol already and put into my agents .md a rule to check progress maximally every 5 minutes. Work well can recommend

- by [unknown](#) **&#x21C5; 7**
  <br/> Yeah, there are already several GitHub issues around this exact behavior. If you’re seeing it too, check your rollout telemetry and add your reproduction/evidence there.The more independent traces, the stronger the case that this is a systemic orchestration bug.

- by [unknown](#) **&#x21C5; 26**
  <br/> I'm now working on a mitigation for this on my own setup.

The first change I'm going to test is forcing the orchestrator's `wait_agent` interval to roughly **25 minutes**, instead of the observed 30-second polling loop. The idea is to keep the wait comfortably below the ~30-minute prompt-cache TTL while eliminating almost all of the unnecessary parent-model wakeups.

I'm also going to tighten my `AGENTS.md` orchestration rules so that, while a worker is still healthy and running, the parent should:

  - not poll for status unnecessarily,
  - not start duplicating the worker's investigation or implementation,
  - not interrupt or replace the worker just because a wait timed out,
  - and not perform additional context-heavy work unless there is actually something useful for the orchestrator to do.

The intended behavior is basically: `worker still running → keep waiting`

rather than: `worker still running → wake Astra → reload ~150k context → inspect things → poll again`

- by [unknown](#) **&#x21C5; 4**
  <br/> I have event-based interrupts in my setup. It's not well supported in Codex, but relying on polling is a bit shit no matter how you configure it.

- by [unknown](#) **&#x21C5; 18**
  <br/> **GOOD NEWS: I found a workaround for the 30-second polling bug.**

To stop the parent orchestrator from waking up every 30 seconds, you have to set this in `~/.codex/config.toml`:

[features.multi_agent_v2]
enabled = true
min_wait_timeout_ms = 1500000
default_wait_timeout_ms = 1500000
max_wait_timeout_ms = 15000001500000 = 25 minutes

**You need to set both **`min_wait_timeout_ms`** and **`default_wait_timeout_ms`**.** This prevents the model from falling back to 30-second waits.

I tested it in a real Astra + Luna orchestration run and checked the rollout afterward. The old 30-second polling loop was gone. Astra stayed asleep for long stretches while the workers were running and woke up when they returned.

I chose 25 minutes because it should stay safely inside the ~30-minute prompt-cache window while removing almost all of the pointless polling.

- by [unknown](#) **&#x21C5; 7**
  <br/> This fixes the polling problem, but I'm still investigating the overall quota burn. There are clearly other sources of huge token usage in both Astra and its workers. In this run, the Luna xhigh workers were processing input tokens roughly **12–13× faster** than my manually-driven Luna Max baseline 🤔

- by [unknown](#) **&#x21C5; 3**
  <br/> Where can i follow for your next update?

- by [unknown](#) **&#x21C5; 3**
  <br/> I'll put together a brief follow-up post here with some new ideas I gathered from subsequent tests. To keep the experiment clean, I'm having to burn through a lot of tokens, but I'm hoping to optimize the consumption a bit more.

- by [unknown](#) **&#x21C5; 5**
  <br/> Not sure of the validity of course, but seeing comments on twitter about subagent conversation forks inheriting full context then compacting, etc causing massive burn. Just sharing for your findings compilation.

Personally I'm on 20x pro and had a task last night where Astra light spawned ~10 subagents over the span of the entire task taking 20% of my usage.

- by [unknown](#) **&#x21C5; 4**
  <br/> Found it: [https://x.com/bdsqlsz/status/2097207062170128585](https://x.com/bdsqlsz/status/2097207062170128585)

- by [unknown](#) **&#x21C5; 3**
  <br/> Thanks dude!

- by [unknown](#) **&#x21C5; 2**
  <br/> Thanks a lot for this!

- by [unknown](#) **&#x21C5; 2**
  <br/> min wait 25 mins, how you know how long, when you orchestrating many sub tasks

- by [unknown](#) **&#x21C5; 2**
  <br/> 25 mins is to prevent the 30 min cache lifetime to be reached. tell the orchestrator to instruct the subagents to report back when finished. polling is useless 99.9% of the cases.

- by [unknown](#) **&#x21C5; 2**
  <br/> Where did you find it? Why is it something not in the config file already and needs to be added from scratch?

- by [unknown](#) **&#x21C5; 2**
  <br/> I found the parameters in the Codex GitHub source/issues, then experimented with different combinations. After a lot of repeated runs, this exact setup was the most reliable: it prevents the 30s fallback while keeping the wait safely inside the ~30-minute prompt-cache lifetime.

As for why this isn’t exposed as a sane default/config option already... I’d genuinely love to know 😅 It’s a tiny harness-level change that can save users a ridiculous amount of tokens and money. I’m avoiding conspiracy theories, but maybe we’re starting to see what happens when everyone, including AI companies, trusts machine-written code a little more than they review it.

- by [unknown](#) **&#x21C5; 18**
  <br/> can we get a tl;dr?

- by [unknown](#) **&#x21C5; 27**
  <br/> His Astra agent used Luna sub agents for some task. Out of 10 million Astra tokens, 7 millions were wasted purely on following up on/polling the sub agents every 30 seconds, checking if they finished their tasks, but I guess the tasks were long running. The 7 million Astra tokens used for this were expensive. This is my understanding.

The idea is this should behave more like a software hook, so the cheap sub agent reports back to the expensive agent once it's done, the Codex harness uses code to wake up the main agent rather than the main agent having to keep polling unless it wants to monitor intermediate output. In case that sub agent crashes or something (should be very rare scenario), you can have a longer polling period than 30 seconds.

- by [unknown](#) **&#x21C5; 12**
  <br/> the potential downside there is that if Astra main agent waits 10 mins for Luna to finish, its cached tokens may become expired and the entire convo plus the luna response then becomes uncached input on the next turn… It may have used 7.13M tokens for timeouts but 7.11M of them were cached… it’s a fine line to balance, I suppose.

- by [unknown](#) **&#x21C5; 5**
  <br/> Thank you!

- by [unknown](#) **&#x21C5; 10**
  <br/> Don’t use sub agents, it’s really token inefficient.

- by [unknown](#) **&#x21C5; 6**
  <br/> That's what I found since 5.6 Sol Max. It's better to just run a single max agent, it also completes work faster from what I've noticed.

- by [unknown](#) **&#x21C5; 3**
  <br/> But then we run out of context and need to compact repeatedly…

- by [unknown](#) **&#x21C5; 4**
  <br/> Shouldn't using sub agents be in theory more token efficient, since they should prevent accumulating context?

- by [unknown](#) **&#x21C5; 2**
  <br/> Hmm, good question. Sidechats actually use all the context from your main chat that existed up until the point you started the sidechat, I assume subagents are the same...

So hard to say. If that's the case, and it probably is, that would multiply your context use tremendously actually.

- by [unknown](#) **&#x21C5; 8**
  <br/> I was gonna read the tl;dr til I saw it's the whole post.

- by [unknown](#) **&#x21C5; 3**
  <br/> My bad. It should be much easier to read now.

- by [unknown](#) **&#x21C5; 1**
  <br/> For once it's a long post worth reading.

- by [unknown](#) **&#x21C5; 2**
  <br/> Fair enough 😄 I got carried away editing the post for readability and somehow let the TL;DR grow into a mini-post of its own.Fixed now, thanks for the feedback.

- by [unknown](#) **&#x21C5; 5**
  <br/> One thing you aren’t considering, the potential downside of having Astra wait until Luna respires back is that if Astra main agent waits 10 mins for Luna to finish, its cached tokens may become expired and the entire convo plus the luna response then becomes uncached input on the next turn… which is also expensive. The timeout checks potentially keep the tokens cached longer. It may have used 7.13M tokens for timeouts but 7.11M of them were cached… it’s a fine line to balance, I suppose.

- by [unknown](#) **&#x21C5; 7**
  <br/> I checked the docs, and the ~30-minute prompt-cache TTL has also been discussed here a lot. Astra is on the v2 path, so there’s no good reason to wake an expensive parent every 30 seconds and reprocess ~150k tokens just to keep the cache warm.A ~20–25 minute wait would stay safely inside the TTL while eliminating almost all of that polling overhead. The 30-second loop looks like an orchestration bug 🤷🏻‍♂️

- by [unknown](#) **&#x21C5; 3**
  <br/> Is there a way to make the subagents contact the parent when done instead of the parent checking in over time periods?

- by [unknown](#) **&#x21C5; 3**
  <br/> I found a way to stop the parent from doing the 30-second polling, and it seems to be working. I'm testing it now since I ran into another bug. I'll post the results here a bit later.

- by [unknown](#) **&#x21C5; 4**
  <br/> Looking forward to you posting the results! Thank you so much for this

- by [unknown](#) **&#x21C5; 2**
  <br/> I posted a workaround above that fixes the parent polling issue. But it looks like there are problems with the harness itself too.

- by [unknown](#) **&#x21C5; 4**
  <br/> this is one of the things that suck about codex in comparison to claude code

- by [unknown](#) **&#x21C5; 4**
  <br/> It’s definitely a problem with the model not just the harnesses because I’ve used a similar setup with OhMyPi using astra low as orchestrator, luna xhigh to implement etc… at the end of the session I had burned ~5% of my weekly usage just for a 700-800 line changed PR and 90% of the cost was from the orchestration. I had to move back to Sol medium (but it’s definitely slower and dumber than astra low)

- by [unknown](#) **&#x21C5; 7**
  <br/> Nice write-up. This is big

- by [unknown](#) **&#x21C5; 3**
  <br/> yeah i've noticed this too, i switched to pi for tasks that require 'efficient sleeping' like checking on agents or monitoring applications.

even if you instruct codex to check efficiently or to check less often, it will agree to it but continue checking every 30s

- by [unknown](#) **&#x21C5; 3**
  <br/> Great post, thank you for this, I keenly await how you solve it

- by [unknown](#) **&#x21C5; 1**
  <br/> I posted a workaround above that fixes the parent polling issue.Test it on your end. I'm curious about the subagents' token usage.

For some reason, they seem to be carrying a huge amount of context during tool use now, which wasn't happening before.

- by [unknown](#) **&#x21C5; 3**
  <br/> That is more of an issue with codex than the model itself. On opencode, I dont have this issue

And yes, I know this is [r/codex](/r/codex/), not [r/gptmodels](/r/gptmodels/), but I thought i'd add this little bit of context

- by [unknown](#) **&#x21C5; 2**
  <br/> I'm pretty sure this is a harness issue, not just the model. Someone mentioned PI doesn't have this problem, but I can't really verify it since I'm not experienced with PI, and I need reproducible results with my existing workflow.

- by [unknown](#) **&#x21C5; 1**
  <br/> How does Opencode work with GPT subscriptions? Does it use the usage allowance of the subscription or is it API usage?

- by [unknown](#) **&#x21C5; 3**
  <br/> This is insane, and I really don't need those constant messages of still waiting...just wait like competitors do.

Good find 😕

- by [unknown](#) **&#x21C5; 7**
  <br/> Good analysis. According to Tibo they archived AGI in software dev internally. If this is the bug then their AGI is based on unlimited token and budget so they totally overlooked user economics

- by [unknown](#) **&#x21C5; 2**
  <br/> Seems like a great efficiency saving they could implement if not already part of what Tibo had in mind with the 3-4x optimisation

- by [unknown](#) **&#x21C5; 2**
  <br/> I used Astra to write an implementation plan for Luna, and started a new Luna chat to execute. Then come back to the Astra chat and ask it to review.

- by [unknown](#) **&#x21C5; 2**
  <br/> Yeah, that’s pretty much how I used Sol before: plan with Sol, then manually hand it off to a separate Luna Max chat. It works, but it’s a lot of babysitting :\

- by [unknown](#) **&#x21C5; 2**
  <br/> [https://github.com/openai/codex/issues/2062](https://github.com/openai/codex/issues/2062)

- by [unknown](#) **&#x21C5; 2**
  <br/> Hi, I edited my [AGENTS.MD](http://AGENTS.MD), and have significantly decreased my token consumption due to your suggestions - thx; hopefully they patch this issue, and also give us a free reset along with it.

Personally, I really do feel like Astra is a bit dumb now if you don't give it scope. It tends to spin its wheels, and expand the scope of the exercise without my permission. I have to constantly monitor it to make sure it doesn't go off track, even with a carefully crafted spec doc. I dont know what happened to the Steps planner - that was very helpful.

- by [unknown](#) **&#x21C5; 2**
  <br/> Same thing happened to me when it was waiting for my CI when I had it trying to hill climb. Destroyed my usage.

- by [unknown](#) **&#x21C5; 2**
  <br/> Glad you did the research.  Also good to know that me just sending Astra to do everything is just as viable as the "token saving" orchestration tricks with multiple models...lol.

- by [unknown](#) **&#x21C5; 2**
  <br/> I noticed this exact same thing yesterday. Every 10-30 seconds of "agent is doing this, agent is still working, I'm waiting for agent to finish, Agent is still working...". I just told that no need to give status updates. That didn't help. Updates were shorter but kept coming. It was strange.

- by [unknown](#) **&#x21C5; 2**
  <br/> Yep....this is why i burned my pro quota in under 2 hours.  Nice find!

- by [unknown](#) **&#x21C5; 2**
  <br/> Astra does the same thing waiting for CI status updates. It was pinging GitHub every 30 seconds asking for the status of every CI job until they all finish

Think I’m going to need to add instructions to stop that and if it doesn’t work then switch back to Sol

- by [unknown](#) **&#x21C5; 2**
  <br/> I burned many millions of active tokens and billions of cached tokens when 5.6 sol got into a death spiral doing something similar, it was like it had had 20 cups of double espresso and a jittery fucker. It burned through 4 banked resets. On 20x plan. And it had spent like 8 hours doing something fable did in 10 minutes. And it only did the task after I told it to just do it, still took an hour from then. I told it, we aren’t launching a rocket ship, we are launching a model training run on 100+ GPUs. Just do it.

Eventually it revealed why it did it, it had set up all these things polling itself. Each sub agent. Each task. Each action. Spawned a new one. And this infinite cycle. Basically psychosis.

- by [unknown](#) **&#x21C5; 2**
  <br/> thanks I will do that too , it ate up my weekly limits in just two to three prompts.

- by [unknown](#) **&#x21C5; 2**
  <br/> Thanks, I'm on plus and tried Astra yesterday for a non complex task, one prompt, and burnt 40% of my 5h window 😔

- by [unknown](#) **&#x21C5; 2**
  <br/> That's because it has system instruction to not do long waits. It thinks user input is blocked by that wait which is not true. I modified it long before astra so it doesn't wake up so often.

- by [unknown](#) **&#x21C5; 2**
  <br/> astra now is a burner of token. one simple task jus to try the new model and pop-up to add quota or wait til tomorrow in just 20 min session.

- by [unknown](#) **&#x21C5; 2**
  <br/> Did anybody have their weekly limit reset by openai today? I finished my weekly limit yesterday on astra, and it told me it will reset on sep 12. Woke up today and it is 100% again.

- by [unknown](#) **&#x21C5; 1**
  <br/> I got one. Do you mean this one?[https://x.com/thsottiaux/status/2097174560412246215?s=20](https://x.com/thsottiaux/status/2097174560412246215?s=20)

- by [unknown](#) **&#x21C5; 2**
  <br/> Codex & Astra - Quota is... fucking dumb!

It's a good model. It's a great model, in fact, and it's working very well while I have quota.

Today, in real-world examples where I use AI at work to do various different bits, I asked it to do two things in two different sessions, tackling two tickets that came in through the bug board.

I have already consumed my 5-hour limit - the sessions completed the task within 15 minutes each.

I'm pleased with the speed at which the jobs were done, even though the jobs themselves were not particularly challenging. Had I given the same jobs to Claude, I would have probably not even used 1% of my usage on Fable.

The quota usage between Fable 5.1 and Codex with Astra is, for a better word... stupid.

- by [unknown](#) **&#x21C5; 2**
  <br/> Wanted to add that I am a Plus user, and I only bought Plus to give Astra a try. Yes, I got my try-worth out of my quota, but I certainly did not expect it to be consumed THAT fast.

Nothing has actually annoyed me more this entire year (so far!) than how fast that quota was zapped away in just two basic jobs.

Until that quota becomes substantially better, comparable to Claude's Fable 5.1's quota, I can honestly say, despite the model being great, this is a major drawback. From that experience alone, for anyone who's considering it, it isn't worthwhile at all. Even if Astra is a good model, Fable's 5.1 is on par, but better because the quota usages are actually sensible.

- by [unknown](#) **&#x21C5; 3**
  <br/> I know there might be some people who might think the jobs I asked it to do must have been more complicated than what stated. I can assure you they are no more complicated than what I would have asked Fable to do.

I am an experienced developer of 22 years, and I've been utilising AI since it hit the market, I've seen it grow, and I've seen it improve. I've seen it fail and be really stupid, and I've seen it do crazily cool things.

I've never seen quota usage as pathetic as this Astra model's.

Can sit and complain on this thread all I like. That's fine. This is me ranting about how pathetic the quota usage for Astra is currently, and I'm not being biassed. This is just me dumping my experience with using Astra for the first time.

**TLDR - In a nutshell, it's a good model, as good as Fable 5.1 (maybe better? quota burned too fast for me to even compare quality properly), but the quota burn is shocking**.

- by [unknown](#) **&#x21C5; 2**
  <br/> Fable 5.1 spawned 100 subagents and used by entire 5 hour (max 20x) quota in an hour. Talk about effeciency!

- by [unknown](#) **&#x21C5; 2**
  <br/> This is why I made my own custom harness.

- by [unknown](#) **&#x21C5; 2**
  <br/> im going through 10% of x20 plan in 2 hours. Astra medium. and i use multiple agents for separate tasks, havent got time arsing around debugging this shit

from my checks we are using wait_agent and dont poll for anything, so this doesnt make much sense to me that we would be polling anything

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra seems to expose a broader Codex context-management problem. Codex can carry ~190k tokens of context even through trivial orchestration steps, while other harnesses like OpenCode and Pi prune or truncate old tool output without dropping important context.Codex seems less efficient here, so it periodically has to reload context or risk losing important information. With Astra's cached-input rate, that gets expensive fast.

- by [unknown](#) **&#x21C5; 2**
  <br/> Plus plan, one Astra Low parent with two Luna X-High workers. About 33 minutes, 5h bar 53% to 100%, weekly 9% to 16%, build not finished. Most of the Astra parent tokens were those 47 timeout-only wait_agent polls.

After the window died mid-implementation, what did you still need shipped, and how long did the cleanup or restart take?

- by [unknown](#) **&#x21C5; 2**
  <br/> God I hope this helps, will only find out next reset though because Astra MEDIUM burned through its usage in 30 minutes, and left many blatant issues Sol High wouldn't have from my experiences, hell, Web Chat GPT on Sol wouldn't have.

- by [unknown](#) **&#x21C5; 2**
  <br/> Thanks for sharing the finding, but honestly the tl;dr was the entire post.

- by [unknown](#) **&#x21C5; 2**
  <br/> This maps to a general agentic-harness design tradeoff, not just an Astra quirk: whether an orchestrator's status check has to re-enter the full parent context each time, or whether the runtime can suspend/block without spending tokens until an actual state change happens. Your 151.7k-tokens-per-empty-poll number is a clean illustration of the pull/polling failure mode. A push-based design - woken only on completion/error/timeout rather than a fixed short interval - avoids this cost class entirely. Your min_wait_timeout_ms fix is effectively hand-rolling a longer poll interval since the harness doesn't expose an event-driven wait natively.

- by [unknown](#) **&#x21C5; 1**
  <br/> Exactly. That’s the same class of issue, although here I’d probably call it a harness weakness rather than just a tradeoff. There’s also a second problem: the parent context keeps growing and is then replayed on each tool/model turn, so even trivial checks can become very expensive once the context reaches ~180–190k tokens.

- by [unknown](#) **&#x21C5; 2**
  <br/> I noticed that the OP's suggested overrides are for multi-agent v2, which is a feature flag. I haven't explicitly opted in, but mine is still choosing to use agents v1.

Are most people on multi-agent v2?

- by [unknown](#) **&#x21C5; 1**
  <br/> If you're using Astra or Sol on the normal OpenAI Codex backend, they currently default to Multi-Agent V2 through the model catalog, even if you didn't explicitly opt in.

V1 still exists and can be used by other model/provider combinations, so seeing V1 isn't necessarily wrong. You can check the effective runtime with `codex debug models` or `turn_context.multi_agent_version`.

- by [unknown](#) **&#x21C5; 2**
  <br/> Yep I noticed this as well - pretty much this is an area Claude outshines Codex with their background tasks.

- by [unknown](#) **&#x21C5; 2**
  <br/> I've been having this same issue since Sol came out. I had it develop an event-based "long-job" script which for a time worked, but for some stupid reason the agent just stopped using it and the issue crept back in. Polling should never have been implemented this way because it's eating tokens like a stupid beast. The counter-point to why they do this I imagine is that the agent should be able to continue working in the main thread on other tasks...and so it needs to poll to 'check in' on the other background tasks. It's just implemented poorly and we're all suffering for it.

- by [unknown](#) **&#x21C5; 2**
  <br/> That’s a trivial harness bug. Been like that for a long while.

- by [unknown](#) **&#x21C5; 2**
  <br/> the 7.13M on empty polls is the part dashboards don't stop.

usage bar hitting 100% is after the orchestrator already spent. a cap that only lives in the plan still lets the 30s wake loop run until the window is gone.

did you kill the poll from the parent, or only notice it in telemetry after?

- by [unknown](#) **&#x21C5; 2**
  <br/> I audited a recent task and the polling accounted for only 2% of the total sessions tokens, 6.8% of coordinators, and it was a translation task. But I do have a global rules against procrastination - to be honest I didn't notice agent checks, but every time I checked what Codex was doing at the time, it was always looking at Git, comparing Git, doing checks that had no contribution to the task at hand. I think my approach worked. So it's not a controlled experiment and I think at the highest level, the problem is the model/codex procrastinating too much

- by [unknown](#) **&#x21C5; 2**
  <br/> I have a similar problem with background processes.I have a workflow with really long processes and all Codex agents will constantly poll them every few minutes only to say "I'm still waiting on the process" or "The process is still running, I'll wait until it finishes".I added instructions telling it to set up async notifications instead of polling, but it won't do it.Ended up having to implement an MCP with a single operation to wait on a PID.

- by [unknown](#) **&#x21C5; 2**
  <br/> I don't have any programming experience but i'll use codex to build things like trial and error. How do i do this what OP is saying? I'm using Astra light

- by [unknown](#) **&#x21C5; 2**
  <br/> +1

- by [unknown](#) **&#x21C5; 1**
  <br/> I mean this begs the question: what do you have it doing for polling that’s burning that many tokens?  Seems very odd!

- by [unknown](#) **&#x21C5; 1**
  <br/> After I learned of the reset coming today at 6:00pdt, I tried an experiment. I had 47% left on my 5x plan, so I did a code review on my ~60k line repo I’ve been working on lately.  I set it to Astra Ultra on fast.  In ~15 minutes, it gave me a very thorough review with several recommendations for improvement, and burned through 34% of my weekly usage limit.

- by [unknown](#) **&#x21C5; 1**
  <br/> The smartest is not always the best manager
