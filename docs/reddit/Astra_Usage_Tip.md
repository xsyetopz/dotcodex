#Astra Usage Tip [Visit](https://www.reddit.com/r/codex/comments/1wew63a/astra_usage_tip/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [RedZero76](https://www.reddit.com/user/RedZero76/)
### **Vote:** 43
---
I've been doing this for the last 24 hours. I would say it has slowed down the usage rate overall by about 50% or so, without any difference in quality at all. Def worth doing! I have the $200 Pro plan and normally it lasts all week, but lately it is lasting 1-2 days, but now with this, think it'll last more like 3-4 days at the rate it's going now.
---
Codex has the ability to choose which models and reasoning effort are used for subagent helpers. (Claude doesn’t, btw). This is a big deal. Add something like this to the Agents.md:
`You are powered by GPT 6 Astra High. Usage goes very fast. Keep doing substantial hands-on Astra work. But, use \`gpt-5.6-sol` helpers with task-appropriate effort when suitable! Retain Astra for hard reasoning.`
This will let Astra know to use Sol for subtasks, straightforward recon, stuff like that.
I posted this to X but no one follows me there, and I'm dying to share it bc it's easy and makes a nice difference. `@SirBadfish` on X btw but that's not the only reason I'm posting this... just hope it helps.
Update: To clarify, Claude can use previously setup subagents that have dedicated models/effort/etc, yes. But Claude can't specify the model/effort it's basic "helper" subagents (like if it decides to spawn a few parallel sessions for recon for example).  So if Fabe 5.1 Max, for example, spawns a few helper subagents, it forces them to use the same model as that Fable is set to, Fable 5.1 Max will also be used for those helper agents.  If you ask Fable to spawn a recon agent using Opus, unless you ask for a specific, already-setup Subagent, it can't do it.
---
## Comments 27

- by [unknown](#) **&#x21C5; 9**
  <br/> I use Sol-high as my orchestrator, with Luna-xhigh subagents where appropriate, and it lasts a long time on Plus.

- by [unknown](#) **&#x21C5; 3**
  <br/> And how do you do it?

- by [unknown](#) **&#x21C5; 2**
  <br/> tell sol how a dedicated prompt would like for your question in luna's terms and handover all the information as baseline. you can also tell sol hes a supervisor for luna

- by [unknown](#) **&#x21C5; 1**
  <br/> same. i found out this exact combination is very efficient

- by [unknown](#) **&#x21C5; 17**
  <br/> Claude can choose subagent models.

- by [unknown](#) **&#x21C5; 6**
  <br/> Yeah idk where OP is getting that from or why it even matters to this post frankly

- by [unknown](#) **&#x21C5; 2**
  <br/> My Reddit feed is basically rhetorical variations of OpenAI vs Anthropic. So yeah, I think we should all read into that a bit right now.

- by [unknown](#) **&#x21C5; -3**
  <br/> Pasting this here, I replied to another comment:

Claude can use previously setup subagents that have dedicated models/effort/etc, yes. But Claude can't specify the model/effort it's basic "helper" subagents (like if it decides to spawn a few parallel sessions for recon for example).  So if Fabe 5.1 Max, for example, spawns a few helper subagents, it forces them to use the same model as that Fable is set to, Fable 5.1 Max will also be used for those helper agents.  If you ask Fable to spawn a recon agent using Opus, unless you ask for a specific, already-setup Subagent, it can't do it.

- by [unknown](#) **&#x21C5; 4**
  <br/> That's factually incorrect

- by [unknown](#) **&#x21C5; 2**
  <br/> lol this is absolutely not true. I literally spawn opus sub agents with fable everyday.

- by [unknown](#) **&#x21C5; -4**
  <br/> Claude can use previously setup subagents that have dedicated models/effort/etc, yes. But Claude can't specify the model/effort it's basic "helper" subagents (like if it decides to spawn a few parallel sessions for recon for example).  So if Fabe 5.1 Max, for example, spawns a few helper subagents, it forces them to use the same model as that Fable is set to, Fable 5.1 Max will also be used for those helper agents.  If you ask Fable to spawn a recon agent using Opus, unless you ask for a specific, already-setup Subagent, it can't do it.

- by [unknown](#) **&#x21C5; 2**
  <br/> This is completely wrong

Claude can set the model and effort level for all subagents it spawns, it can even overwrite the model specified in the front matter of a custom agent.

There is also the `CLAUDE_CODE_SUBAGENT_MODEL` env var that lets you set the default model for all subagents

- by [unknown](#) **&#x21C5; 3**
  <br/> your problem in the first place likely comes from relying on Astra in general. I think we have reached the point where the most frontier available model is not the model we should be using for implementation almost ever. With sol you could get away with it, with Astra it’s not worth it most of the time

- by [unknown](#) **&#x21C5; 3**
  <br/> its much cheaper to run a cheaper agent with access to advisor/consultant Astra, Astra running subagents inevitably piles stuff into its context which costs a lot.

- by [unknown](#) **&#x21C5; 2**
  <br/> Right now I’m cooking with sol xhigh and tell it to do a “bounded prompt” with astra advisor after each pr gets merged - seems ok

- by [unknown](#) **&#x21C5; 1**
  <br/> I’ll give this a try. I’m on the baby plan since they froze $200 early.

- by [unknown](#) **&#x21C5; 1**
  <br/> My fable has a hook that its subagents specifically can’t be other fables without an approval from the user. I’ve been doing that since…well I think since fable first came out and I blew an entire 5h quota on an ultra code. So a while.

- by [unknown](#) **&#x21C5; 1**
  <br/> Any performance issue? Yesterday used 40% or 200$ subscription.. even fable don't drain like this 100$ version

- by [unknown](#) **&#x21C5; 1**
  <br/> Guys you just have to put the sub agents toml files with the subagent model and reasoning.

- by [unknown](#) **&#x21C5; 1**
  <br/> I found an amazing repo that works really good! Tell codex to check it out. It’s been helpful.

[https://github.com/DannyMac180/astra-advisor](https://github.com/DannyMac180/astra-advisor)

- by [unknown](#) **&#x21C5; 1**
  <br/> Nice to see the numbers working out. Even at half the burn rate it's 3-4 days instead of the week it used to last, so usage really has crept up lately.

- by [unknown](#) **&#x21C5; 1**
  <br/> I plan in Astra and have a skill that tells it to select an appropriate lower model, such as Luna Low for routine maintenance work

- by [unknown](#) **&#x21C5; 1**
  <br/> Funny reading this, because just a few months ago I had in my agents.md instructions to always use the exact same model for every subagent regardless of task complexity.

- by [unknown](#) **&#x21C5; 1**
  <br/> y'all don't have custom subagents set up with specific models and skills for specific jobs, so all your main sessions know which to use and when?

- by [unknown](#) **&#x21C5; 1**
  <br/> I have in the past, but keeping up w them is a pain in the ass bc they need to be updated a lot. I much prefer letting the primary agent spawn parallel subagent helper sessions. It's usually for recon anyway in my case.

- by [unknown](#) **&#x21C5; -2**
  <br/> I use Gentle-AI; it’s wonderful. It has 23 agents and helps you save tokens and manage security; you can stay in the same session for a long time, and the context barely grows. Open source, GitHub gentleman-programming/gentle-ai
