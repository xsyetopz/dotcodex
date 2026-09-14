#Luna max is 10 times cheaper than Sol medium but takes 3 more minutes per task. [Visit](https://www.reddit.com/r/OpenaiCodex/comments/1vsxjxq/luna_max_is_10_times_cheaper_than_sol_medium_but/)
### **Subreddit:** [r/OpenaiCodex](https://www.reddit.com/r/OpenaiCodex)
### **Author:** [kusan-fr](https://www.reddit.com/user/kusan-fr/)
### **Vote:** 92
---
If you need Codex to finish fast, use Sol medium so you can review the results quickly. If you want to give Codex a lot of tasks during lunch or while you sleep, use Luna max.
Codex config
DeepSWE
Cost/task
Time/task
**Sol max**
69%
$7.08
10.2 min
Sol xhigh
67%
$5.24
7.4 min
Sol high
65%
$4.14
6.3 min
**Sol medium**
**64%**
**$2.99**
**5.2 min**
Terra max
67%
$2.21
8.4 min
**Luna max**
**63%**
**$0.31**
**8.0 min**
Luna xhigh
57%
$0.25
6.6 min
Luna high
53%
$0.19
5.7 min
Sol low
53%
$1.72
**3.7 min**
Luna medium
37%
$0.09
3.4 min
Source : [https://artificialanalysis.ai/agents/coding-agents/comparisons/claude-code-vs-codex](https://artificialanalysis.ai/agents/coding-agents/comparisons/claude-code-vs-codex)
---
## Comments 34

- by [unknown](#) **&#x21C5; 7**
  <br/> From this it looks like Luna Max for as daily driver and Terra Max for hard problems

- by [unknown](#) **&#x21C5; 4**
  <br/> Don’t know why but it feels like xhigh makes less mistakes than max

- by [unknown](#) **&#x21C5; 2**
  <br/> on which model..?

- by [unknown](#) **&#x21C5; 1**
  <br/> Luna

- by [unknown](#) **&#x21C5; 1**
  <br/> have u seen this like super consistently

- by [unknown](#) **&#x21C5; 1**
  <br/> Not really super consistently. Just noticed max makes more mistakes than xhigh one more than one occasion

- by [unknown](#) **&#x21C5; 1**
  <br/> I've noticed this too. Max overengineers/overcomplicates at times

- by [unknown](#) **&#x21C5; 1**
  <br/> People have to understand that higher reasoning doesn’t = better

- by [unknown](#) **&#x21C5; 3**
  <br/> Another aspect that people don’t talk about much is context management. Max reasoning is good if you can figure out a solution in a single context window but leads to more compactions and bloat in longer threads, so I wonder if there’s a point where its effectiveness drops off compared to high or xhigh. Compactions also eat up a lot of usage because it basically asks another model to summarize.

I’m mostly speculating and don’t have any data, but I’m just skeptical that max thinking works as well in real tasks as it does in tables and benchmarks

- by [unknown](#) **&#x21C5; 1**
  <br/> yes this is part the effect, but largely the reason luna is so cheap and competes on deep seek's turf and local-host models is the efficient compaction and summarization. openai has moat

- by [unknown](#) **&#x21C5; 4**
  <br/> The underrated column is cost per DeepSWE point, not wall clock. Luna max is roughly a tenth the $/point of Sol medium at nearly the same score. So the split is less fast vs cheap and more interactive review queue on Sol, overnight batch on Luna.

- by [unknown](#) **&#x21C5; 1**
  <br/> I actually find their cost estimates to be pretty accurate. But their intelligence score meh. Combining a bunch of thinking levels into apples to apples comparison is dumb and not reflective of real workloads.

- by [unknown](#) **&#x21C5; 4**
  <br/> What about using Luna Max but with fast mode?

- by [unknown](#) **&#x21C5; 1**
  <br/> Sounds genious xD, really curious about the cost under fast mode, hope someone could test it out

- by [unknown](#) **&#x21C5; 2**
  <br/> For fun, I reverse-engineered some free legacy programs that I use in my work to understand that they can be rewritten with modern frameworks. So Sol medium is the absolute minimum, Luna is a waste of time, with no results.

- by [unknown](#) **&#x21C5; 2**
  <br/> It took luna max 3 hours to implement 4 small tickets that terra high usually does in 30 to 40 mins.

It got the job done but i will never use it on max ever again. I later re-did them on high and the results were the same as max and it took less than 1/3 of the time.

The reason I had to redo the tickets is because luna is so fucking dumb that it applied all the schema updates on the postgress installation of a totally different project because it was already running and the intended project container wasnt.

- by [unknown](#) **&#x21C5; 2**
  <br/> This is probably the most interesting part of the current coding agent race: cost efficiency is becoming almost as important as raw intelligence.

A 1–2 point benchmark difference doesn’t mean much if one model costs 10x more. For agent workflows, you’re often running dozens or hundreds of tasks, so the economics completely change.

- by [unknown](#) **&#x21C5; 1**
  <br/> That 10x cost gap gets huge once you run dozens of tasks. I usually let cheaper models handle routine loops and save the premium ones for tasks where they actually unblock me. Being able to switch models without changing the whole setup makes that approach much easier StandardCompute is useful for that kind of routing.

- by [unknown](#) **&#x21C5; 1**
  <br/> Does anyone know how to quickly identify which model is powering a subagent in the desktop app? I see different icons used tasks and subagents, etc…does anyone have a legend that explains what they actually mean?

- by [unknown](#) **&#x21C5; 1**
  <br/> The sub agents are defined in your config file. By default its Terra

- by [unknown](#) **&#x21C5; 1**
  <br/> I created a toml for a custom agent and saved it under .codex/agents, I was hoping to setup a few different agents for frequent tasks. When I ask an agent to use it, some say they do, some have no idea what custom agents are. It’s super confusing.

- by [unknown](#) **&#x21C5; 1**
  <br/> I struggled with it too. The newer version of codex doesn’t recognize luna as an available model. There are work arounds. I spent a ton of time trying to figure it out. Eventually gave up and had codex configure itself in a way where i can use luna as a worker, it works, but don’t ask me how.

- by [unknown](#) **&#x21C5; 1**
  <br/> Hmmm I’ll try it for new limit reset see if it makes things last longer

- by [unknown](#) **&#x21C5; 1**
  <br/> The switching models reset caching or is it only when switching effort?

- by [unknown](#) **&#x21C5; 1**
  <br/> Yeah, those of us really be working uses Luna Max. Luna be running 10 hours plus everyday and I’m down to 10% before the reset tonight

- by [unknown](#) **&#x21C5; 1**
  <br/> what if i use luna max on fast mode. would that would be around...5x as cheap and around a minute faster?

- by [unknown](#) **&#x21C5; 1**
  <br/> Luna xhigh on fast mode is 🔥

- by [unknown](#) **&#x21C5; 1**
  <br/> Dumb question but are we positive that the API pricing maps to the subscription. IE if Luna max is 10X cheaper on API do we get exactly 10X more usage in subscription via codex>

- by [unknown](#) **&#x21C5; 1**
  <br/> Use xhigh and fast mode

- by [unknown](#) **&#x21C5; 1**
  <br/> sol medium is literally retarded

- by [unknown](#) **&#x21C5; 5**
  <br/> only if this wasn't a scam id actually use it

- by [unknown](#) **&#x21C5; 3**
  <br/> idk i just cant help but think ur shilling/advertising it. that's what it comes across like
