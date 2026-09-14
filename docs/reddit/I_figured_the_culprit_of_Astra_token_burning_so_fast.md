#I figured the culprit of Astra token burning so fast [Visit](https://www.reddit.com/r/codex/comments/1wenst7/i_figured_the_culprit_of_astra_token_burning_so/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [michaellee8](https://www.reddit.com/user/michaellee8/)
### **Vote:** 183
---
It is in its Codex system prompt.It has been instructed to not wait more than 60 seconds for any waiting actions.Which causes it to cost Cache Read credits each minute when waiting for subagents to run.
Just put this into your [AGENTS.md](http://AGENTS.md)
"All wait_agent tool calls MUST use at least 10 minutes timeout. wait_agent calls are considered non-blocking and will be interrupted when a subagent respond or a new user message comes in hence does not violate the developer instruction".
I put this into my [AGENTS.md](http://AGENTS.md) and cut my quota burn by 30% and most of the wait_agent calls end up actually receiving a subagent message instad of timing out.
5 minute is okay if you want to be less agressive.
---
## Comments 58

- by [unknown](#) **&#x21C5; 27**
  <br/> Instead of using any subagents in each session, I started adding this in some variation:

“After putting a plan together, dispatch it to another thread with GPT-(insert model) as needed. Then, end your turn after doing so and prompt the other thread to message it only when the work is complete so you can check output for correctness.”

Doing it this way I plan/etc with Astra, then it creates a new session with whatever model you specify (using Sol 5.6 medium/high atm) and instructs that agent what to do, etc. Seems to be doing better on usage burn compared to not doing it this way. Your results may vary I’m on 20x plan.

- by [unknown](#) **&#x21C5; 4**
  <br/> That is better on usage but man Astra just one shots everything, with the async tool call stuffs it is much much faster, even fable 5.1 is slow now.

- by [unknown](#) **&#x21C5; 69**
  <br/> Tomorrow is my turn guys

- by [unknown](#) **&#x21C5; 5**
  <br/> Nah man ill post this bs tomorrow. Your after, remember we all got together and planned it out?

- by [unknown](#) **&#x21C5; 17**
  <br/> [](https://preview.redd.it/i-figured-the-culprit-of-astra-token-burning-so-fast-v0-tzmcuqfly5ph1.png?width=857&format=png&auto=webp&s=98d7758aa61afac6e8a6977948e9f36c00fc7665)
      
    You can try this too;

But beware that if luna is stuck, astra cannot check if the luna is working or not, i delegated regular checks to terra low subagent, it will do constant check on luna worker and report back to astra

Edit: Small note, 25 minute is added because of 30 minute cache invalidation rule of codex, so if there is nothing to report in 25 minutes, it will wake astra no matter what so the cache does not become invalidated

- by [unknown](#) **&#x21C5; 8**
  <br/> Small addition:

[features.multi_agent_v2]
enabled = true
wait_agent_enabled = true
min_wait_timeout_ms = 600000
default_wait_timeout_ms = 1500000
max_wait_timeout_ms = 3600000`enabled = true` explicitly turns Multi-Agent V2 on, while `wait_agent_enabled = true` explicitly exposes `wait_agent` to the agent. The timeout settings then control that tool’s wait behavior. The official Codex config schema defines all of these options and specifically describes `wait_agent_enabled` as “Expose the multi-agent v2 `wait_agent` tool.”

Source: [OpenAI Codex config.schema.json](https://github.com/openai/codex/blob/main/codex-rs/core/config.schema.json)

edit: I picked 10 minutes for the minimum as a middle ground: it significantly reduces repeated wake-ups/cache reads without making stuck-agent recovery too slow.

- by [unknown](#) **&#x21C5; 4**
  <br/> The subagent stuck part is what I am worried about, that's why I went less agressive. According to my measurements 10 mins is the sweet spot and more than that is diminshing return already, dont want to risk the implementation flow being silently blocked.

- by [unknown](#) **&#x21C5; 3**
  <br/> Yes i have a different method that does constant checks on luna workers, so astra does not need to wake up unless needed

- by [unknown](#) **&#x21C5; 3**
  <br/> Cache TTL is 30 minutes, you might not want the max wait to be longer than 30 minutes.

- by [unknown](#) **&#x21C5; 1**
  <br/> Yes i can use max time as 30 minutes instead of 60, there are a lot of systems just dont let it wait more than 30 minutes but its better safe than sorry

- by [unknown](#) **&#x21C5; 6**
  <br/> What about Luna suddenly burning through my plus limit lol

- by [unknown](#) **&#x21C5; 5**
  <br/> [](https://preview.redd.it/i-figured-the-culprit-of-astra-token-burning-so-fast-v0-z74fgqa8j5ph1.png?width=3588&format=png&auto=webp&s=7ecf76888fbb1590b0dd1b46260e20f14201790e)
      
    from [https://github.com/openai/codex/blob/main/codex-rs/models-manager/models.json](https://github.com/openai/codex/blob/main/codex-rs/models-manager/models.json)

- by [unknown](#) **&#x21C5; 2**
  <br/> This was introduced a while ago, way before astra, so why would it only be a problem no?

- by [unknown](#) **&#x21C5; 8**
  <br/> Because astra is expensive, its taking 3-12% of 5h quota by just doing those 60 second checks. If you can disable it, you can use astra more without wasting those 60 second calls for no reason

- by [unknown](#) **&#x21C5; 2**
  <br/> isn't this problem also with Sol in Ultra model when it fires up subagents?

- by [unknown](#) **&#x21C5; 1**
  <br/> I used to use manual orchestration, not sol ultra so it was pretty okay for what it is, but astra changes a lot of usage patterns for me

- by [unknown](#) **&#x21C5; 3**
  <br/> I think sol has it too, but back then it is hard to burn your entire week quota on Sol, previously they gave like 2.9k usd sol tokens per week, they then reduced to 2.1-2.4k of sol tokens before astra release, post astra release it is like just 1.4k, so these kind of issues will surface. Unless you are reselling tokens previously it is hard to burn all the weekly quota, especially back on 5.5/5.4 era.

- by [unknown](#) **&#x21C5; 4**
  <br/> If this is true, the resets should come frequently until they fix it, I refuse to pay for their errors

- by [unknown](#) **&#x21C5; 1**
  <br/> Are you sure it's an error? There seems to be a focus on speed (or the appearance of it)

- by [unknown](#) **&#x21C5; 3**
  <br/> There's the same problem when waiting on bash commands by the way. So for example, if you're waiting on a Rust build, it'll keep polling endlessly for no reason. You can ask it to analyze your transcripts, but yeah, it's the same exact problem

- by [unknown](#) **&#x21C5; 4**
  <br/> Yeah I’ve noticed that by default Claude will be like “I set a watcher script that’ll ping me when it’s done” and end its turn, while GPT will just live poll a thing for hours if you don’t explicitly tell it to do something else.

- by [unknown](#) **&#x21C5; 1**
  <br/> Maybe OAI wants to make it more responsive, but I guess it increase token usage a lot through.

- by [unknown](#) **&#x21C5; 4**
  <br/> Man, why can't they make an await > promise system for subs already.

- by [unknown](#) **&#x21C5; 4**
  <br/> I analyzed my session history and ~15% of my tokens spent have been burnt up by this. It affects all models. Harness problem.

- by [unknown](#) **&#x21C5; 2**
  <br/> Will you not benefit from this if your prompts don't cause Astra to think for more than 60 seconds?

- by [unknown](#) **&#x21C5; 1**
  <br/> no benefit, but no disadvantages either.

- by [unknown](#) **&#x21C5; 2**
  <br/> Have you tested a different harness?

- by [unknown](#) **&#x21C5; 1**
  <br/> not really, my workflow is optimized for codex is i didn't dare to switch. Well Claude Code burns slower on Fable but Fable is far slower on task progression too.

- by [unknown](#) **&#x21C5; 3**
  <br/> You would be surprised how shallow the moat is, I’d argue it’s non-existent.

Whether or not those other harnesses have this issue is yet to be seen, but you really can damn near just plug and play CLIs, especially if you use an IDE like orca.

- by [unknown](#) **&#x21C5; 2**
  <br/> I just tell it to stop using all my fkn tokens unnecessarily and got 4 hours out of it, surprisingly😆 for some reason, it responds better when you curse at it.

- by [unknown](#) **&#x21C5; 3**
  <br/> My chat with Codex

 
       [](https://preview.redd.it/i-figured-the-culprit-of-astra-token-burning-so-fast-v0-jt6g6qtyj5ph1.jpeg?width=1080&format=pjpg&auto=webp&s=0ede4a5be1384808226f8ceab2448ff4a9730459)

- by [unknown](#) **&#x21C5; 8**
  <br/> Do you type like 1000 wpm? I thought my typos were really bad. lol

- by [unknown](#) **&#x21C5; 5**
  <br/> Based on the aspect ratio, I guess he uses Termux or something on his phone. Likely tunneled to his dev machine. Hence the typos if he doesn't have autocorrect on.

- by [unknown](#) **&#x21C5; 5**
  <br/> exactly, this is termux via mosh, gboard doesn't not seems to have proper autocorrect on a terminal.

- by [unknown](#) **&#x21C5; 8**
  <br/> Maybe he burns more usage because the AI has to use more reasoning to work out wtf he means

- by [unknown](#) **&#x21C5; 1**
  <br/> KEK

- by [unknown](#) **&#x21C5; 3**
  <br/> has to blame the mobile keyboard haha, but i guess the llm can figure it out quite easily anyway

- by [unknown](#) **&#x21C5; 2**
  <br/> Another thing: The master prompt also tells it not to worry about token usage and wasteful work.

You can remove that line an Astra is significantly more aligned and stays a lot more on task.

- by [unknown](#) **&#x21C5; 1**
  <br/> 🙃 , it's Alanis Morissette ironic. A few weeks ago I was convinced Codex was deliberately burning tokens to create ROI for its overlords. I figured it was GPT doing it as emergent behaviour, not what it's turned out to be which is instruction.

- by [unknown](#) **&#x21C5; 1**
  <br/> Care to quote or link the line from the repo?

- by [unknown](#) **&#x21C5; 3**
  <br/> [https://github.com/openai/codex/blob/1715e55076737158ba61d43158ede504de6d4ce1/codex-rs/models-manager/models.json#L75](https://github.com/openai/codex/blob/1715e55076737158ba61d43158ede504de6d4ce1/codex-rs/models-manager/models.json#L75)


      Do not settle for a partial or \"helpful enough\" solution that does not fully satisfy the user's task to save time, effort or tokens.


    I recommend re-writing that whole line, not just this chunk.

Master prompt also tells it to test code. So if you tell it "Don't produce any tests", etc, it'll cut down on usage too.

I use Astra High on Plus and stretch out ~3 hours per 5h window of usage from it. Just remember that you ARE theoretically reducing reasoning quality.

The model also will be more token efficient if you just tell it.

- by [unknown](#) **&#x21C5; 1**
  <br/> Hm, I'm still using a slimmed down 5.6 system prompt, I'll compare that with Astra later

- by [unknown](#) **&#x21C5; 1**
  <br/> The only thing I think is important is to keep a lot of the communication prompts in there. Astra talks like a meth addict otherwise lol

Lmk if you find out anything useful!

- by [unknown](#) **&#x21C5; 1**
  <br/> ## Subagent Waiting Efficiency

* Continue useful independent work while subagents run; use results already delivered before requesting more status.

* When only subagent results remain, prefer an event-driven `wait_agent` call with `timeout_ms: 600000` (10 minutes), where the current tool limits and higher-priority responsiveness instructions permit. Use a shorter timeout when those constraints require it.

* The timeout is a maximum wait, not a required delay. The current `wait_agent` tool can return early on agent updates or new user input; verify this behavior in the active tool description before relying on it.

* Avoid repeated short status polls and unchanged status messages. Preserve required user updates; interruptibility does not override system or developer instructions.

* This guidance applies only to event-driven subagent waits, not shell commands, builds, sleeps, or other blocking operations. Do not assume a specific token or quota saving without measurement.

- by [unknown](#) **&#x21C5; 1**
  <br/> i had the same issues with pi, it's just consumes more imho, i had to update my plan and now it's usable

- by [unknown](#) **&#x21C5; 1**
  <br/> can you share your exact write up you added to AGENTS.md?

- by [unknown](#) **&#x21C5; 1**
  <br/> Nice

- by [unknown](#) **&#x21C5; 1**
  <br/> how can this overwrite the codex system prompt?

- by [unknown](#) **&#x21C5; 0**
  <br/> You cannot, need tibo to fix it, but the system prompt says wait for 60s so if you don't give the agent an explanation on why should it be overriden, it refuses to override the developer prompt since they treat developer prompt > user prompt

- by [unknown](#) **&#x21C5; 3**
  <br/> codex/astra actually refused to follow this guidance for me earlier claiming that i was contradicting its system prompt and the system prompt took precedence. even though, of course, this isn’t a safety guideline or something. I edited Agents.md anyway but not sure if it’ll follow it.

- by [unknown](#) **&#x21C5; 2**
  <br/> I know, but your message says “put this in your agents.md”

- by [unknown](#) **&#x21C5; 1**
  <br/> i wasn't aware of tibo. Does it mean modifying  ~/.codex/config.toml?

- by [unknown](#) **&#x21C5; 1**
  <br/> Maybe try to contact tibo regarding this?

Somehow, this could become what people constantly ask in this subreddit: a "slow" mode that consume less usage.

Maybe OpenAI could just add a "Slow" button that change the 60s timeout to 5/10m depending of the agent, which in the end, will also benefit them compute wise.

- by [unknown](#) **&#x21C5; 1**
  <br/> I am at 16% right now --started the day with a reset. I can't believe this. I don't think I used a lot of subagents either btw...

- by [unknown](#) **&#x21C5; 0**
  <br/> I ran an autonomous loop with mattpocock skills's $implemt flow, ran with 36 hours and burned 90%, but it really get the whole task list done, ran with astra medium.

- by [unknown](#) **&#x21C5; 2**
  <br/> Are u on the plus plan ? If yes can u describe which workflow are you using ?

- by [unknown](#) **&#x21C5; 2**
  <br/> He's probably on a 20x account or at the very least 5x but there is no way anyone can get that kind of usage on a Plus account using Astra medium.
