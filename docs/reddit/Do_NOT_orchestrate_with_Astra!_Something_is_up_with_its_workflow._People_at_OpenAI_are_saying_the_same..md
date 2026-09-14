#Do NOT orchestrate with Astra! Something is up with its workflow. People at OpenAI are saying the same. [Visit](https://www.reddit.com/r/codex/comments/1wcg5lx/do_not_orchestrate_with_astra_something_is_up/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Impressive-Gene-421](https://www.reddit.com/user/Impressive-Gene-421/)
### **Vote:** 129
---

## Comments 71

- by [unknown](#) **&#x21C5; 49**
  <br/> I think it's from the astra over polling the worker and jumping in too often

- by [unknown](#) **&#x21C5; 19**
  <br/> Yes, correct.

- by [unknown](#) **&#x21C5; 10**
  <br/> What if you ask astra not to poll agents and wait for their final results before acting

- by [unknown](#) **&#x21C5; 5**
  <br/> I have gotten pretty good results with exactly that.

- by [unknown](#) **&#x21C5; 5**
  <br/> I did that and usage definitely improved

- by [unknown](#) **&#x21C5; 3**
  <br/> That runs the risk that the agents just has to restart because it’s so off, no? On top of requiring Astra to read the agents full work in any case.

- by [unknown](#) **&#x21C5; 1**
  <br/> I think the point is that having cheap subagents redo the work two, even three times over is cheaper than having Astra looking over its shoulder the whole time.

- by [unknown](#) **&#x21C5; 1**
  <br/> Does not work. They have have hard capped timeouts in multiple places. Both mcp tool, longer cli commands, and subagent orchestration suffer from this.

As low as 10-30 seconds in some places.

- by [unknown](#) **&#x21C5; 2**
  <br/> I have seen poor results with Astra orchestrating most of the time, but good results with it as an advisor. That makes the over-polling issue non existent.

- by [unknown](#) **&#x21C5; 1**
  <br/> whats the structure you typically have for your agents + subagents, who calls the advisor?

- by [unknown](#) **&#x21C5; 2**
  <br/> Astra watching Luna is like when you're showing someone how to do something on the computer and just want to go 'holy shit let me take over'

- by [unknown](#) **&#x21C5; 2**
  <br/> this is sum claude code does better than codex

- by [unknown](#) **&#x21C5; 29**
  <br/> Matches what I've seen in the last 24hrs. 2x 20x weekly up in smoke

- by [unknown](#) **&#x21C5; 56**
  <br/> Um, isn't that just because Luna consumes like 10x as many tokens to do things ? This image is useless since Luna tokens are like 100x cheaper than Astra tokens and you show no breakdown.

- by [unknown](#) **&#x21C5; 30**
  <br/> No, it was 80% Astra tokens in Astra+Luna.

- by [unknown](#) **&#x21C5; 10**
  <br/> WTF

- by [unknown](#) **&#x21C5; 4**
  <br/> Because subagents do not work as intended, the workflow is good if you do in mutliple chats. Not in one with astra + subagents.

- by [unknown](#) **&#x21C5; 1**
  <br/> Does this have same issue for sol+luna how do you do it with seperate chats automaticallly?

- by [unknown](#) **&#x21C5; 1**
  <br/> I usually just do separate chats.

- by [unknown](#) **&#x21C5; 1**
  <br/> Somebody posted about this yesterday, it's because Astra is polling the Luna Agents every 30s, you *can* change this (I went from 3s to 3m and holy shit my usage tanked), but there are hard limits on other things like tool usage.

- by [unknown](#) **&#x21C5; 1**
  <br/> huh o.O dayum

- by [unknown](#) **&#x21C5; 1**
  <br/> Give us an api price value for both variants.

- by [unknown](#) **&#x21C5; 8**
  <br/> Price comparation? Because i guess top is still more expensive as 95% of the bottom are luna tokens

- by [unknown](#) **&#x21C5; 3**
  <br/> Incorrect, bottom is 80% Astra.

- by [unknown](#) **&#x21C5; 2**
  <br/> how tf is orchestrating using 80% astra 😭 your workflow must be utter shit

- by [unknown](#) **&#x21C5; 1**
  <br/> No it's just an issue with Astra and other model agents, it doesn't accomplish the work quick enough so it polls the other thread every 30s asks what it's done, reviews its work in its entirety, and then tells the other agent to start again with additional guidance.

And it does this every 30s.

- by [unknown](#) **&#x21C5; 2**
  <br/> workflow issue, my workflow doesn’t poll and only accepts handouts to the main agent from the sub agents

- by [unknown](#) **&#x21C5; 2**
  <br/> The bug is that astras still using the bulk of tokens it’s like astras orchestration layer ends up doing an insane amount more work than it just working by itself for some reason

- by [unknown](#) **&#x21C5; 4**
  <br/> Asking Astra to orchestrate Sol worked really well for like 2 days. Now back to blowing up instantly.

- by [unknown](#) **&#x21C5; 4**
  <br/> I’ve come to the conclusion that Astra should only orchestrate other astras. The feature that allows Astra to async continue working while waiting for a reply in thread is an expected feature of Astra when working with sub-agents. Since Astra is the only model that can handle async steers, it’s the only one sub-agent model that behaves predictably from what I’ve seen.

- by [unknown](#) **&#x21C5; 1**
  <br/> how do you get astra to manage async steers?

- by [unknown](#) **&#x21C5; 2**
  <br/> I have instructions that have a bullet that tells the every thread to ask clarifying questions when it can improve the response outcome. That instruction has been there since January but it was very rarely invoked, Sol asked questions sometimes but had inconsistent behavior. SOL always needed to stop entirely to ask questions, and it had instructions to work efficiently with only high-yield stops, so it had a conflict of interest asking clarifying questions.

Astra can ask clarifying questions in an async pipeline and wait for the user to answer while continuing in the background- that’s a pretty huge deal to consider and build around imo.

It’s especially part of its flow when using default subagents (which mirror the model of the parent). The subagents will continue working and ask for clarifications, and it seems like Astra has a similar asynchronous way to monitor the sub-agents and other threads, because it usually answers these questions crazy fast, compared to SOL coming to a complete stop, noticing the question, formulating response, moving onto next step, etc.

With threads, I’ve seen it exhibit the async behavior with other agents a few times as well. It seems to over-prompt Luna and sol agents (which is cost inefficient due to the way Luna and sol have to adapt their path forward). Astra threads perform unbelievably better with constant steers without getting fucked up.

So far Astra right out of the gates has been asking more clarifying questions than I’ve ever seen, and the questions are intelligent and usually are things I actually missed describing. It’s been a big improvement.

Astra medium and high are my go to right now, with some audits and reviews using xhigh

- by [unknown](#) **&#x21C5; 6**
  <br/> Source?, past the links, not the image.

- by [unknown](#) **&#x21C5; -20**
  <br/> I can confirm, don’t worry.

- by [unknown](#) **&#x21C5; 3**
  <br/> bot

- by [unknown](#) **&#x21C5; -17**
  <br/> ??

- by [unknown](#) **&#x21C5; 1**
  <br/> Then confirm

- by [unknown](#) **&#x21C5; 1**
  <br/> I did, it is confirmed on my authority.

- by [unknown](#) **&#x21C5; 3**
  <br/> I tried to be more economical this way with Astra yesterday, but it ended up burning the quota a lot quicker instead.

- by [unknown](#) **&#x21C5; 3**
  <br/> I’m working from Sol right now, it orchestrates, spins up Astra as an advisor. Sol also delegates to Terra and Luna sub-agents, seems to be working well.

- by [unknown](#) **&#x21C5; 4**
  <br/> It is Astra + subagents that looks broken.

- by [unknown](#) **&#x21C5; 3**
  <br/> What people at OpenAI?  Genuine question; you can’t just drop that grenade :)

- by [unknown](#) **&#x21C5; -2**
  <br/> It was a guy on X, I can’t find the post now but I know for sure it’s there. It was along the lines of “unless you know what you’re doing, don’t use Astra in a harness or as an orchestrator.”

- by [unknown](#) **&#x21C5; 1**
  <br/> My Astra on medium from day one spawned Luna agants and half of token use was from Luna. I realized that couple of days later when somebody on reddit wrote that it is spawning agents and I looked at model usage. I was using only Astra but model use was showing Luna in half cases.

- by [unknown](#) **&#x21C5; 1**
  <br/> Whats the breakdown. you need to do model weighted costs, not raw tokens. It's probably still cheaper.

- by [unknown](#) **&#x21C5; 1**
  <br/> Just do a chart of the cost incurred for these two and let us decide.

- by [unknown](#) **&#x21C5; 1**
  <br/> okay not plot cost

- by [unknown](#) **&#x21C5; 1**
  <br/> This means we need two resets this week and maybe two more this week also

- by [unknown](#) **&#x21C5; 1**
  <br/> i did on the opposite way astra as the worker. As we already know sol is if it writes codes it overengineer a lot, previously i used GLM 5.3 as worker to minimize the the code it writes, now i replace it with astra, so far it doing well, and i like the output. just my 2 cents.

- by [unknown](#) **&#x21C5; 1**
  <br/> I believe it, why would you have a smarter model babysit a dumber model? The dumber model will continousely talk back wasting the main models time, when if you just sent a smart agent, or not even a agent just have the main agent work it, it would probably use way less context anyway and not fill the main agents context with retry messages

- by [unknown](#) **&#x21C5; 1**
  <br/> Use Astra to orchestrate with Astra low/medium/high, dont use sol/Luna/terra. OpenAI recommends this setup, and I think they know better than the average redditor.

Running this setup with my custom harness, for 2 companies running double digit projects. No usage issues.

- by [unknown](#) **&#x21C5; 1**
  <br/> Yeah, but you get like 95 trillion Luna tokens for like a buck fifty...

- by [unknown](#) **&#x21C5; 1**
  <br/> Just use Astra and it will do the job, stop this whole orchestration madness.

- by [unknown](#) **&#x21C5; 1**
  <br/> Yeah,  I had the similar experience, 5x weekly gone in half a day. Astra overpolls workers eating up your usage.  I created a skill that tells it to make workers report back to it using the MessageThread tool and forbids it to use WatchThread or other polling mechanisms. It also sets up a 25 minute scheduled task to check on workers that didn't report anything the past 25 minutes. With this approach 1x sub at work lasted half a day

- by [unknown](#) **&#x21C5; 1**
  <br/> It's because it's polling all of it's subagents over and over, causing *insanely massive* input token burn.

- by [unknown](#) **&#x21C5; 1**
  <br/> You can orchestrate with Astra do not spread fake news.

Just not in the same chat as subagent. make the plan and then in a new chat ask Luna to follow it.

- by [unknown](#) **&#x21C5; 2**
  <br/> Respectfully if you are manually copying outputs from an Astra thread and pasting them into a worker thread than that's not orchestration, that's just two separate agents.

- by [unknown](#) **&#x21C5; 1**
  <br/> It is cheaper to just get Astra to do it.

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra + sol in a different chat is way cheaper.

- by [unknown](#) **&#x21C5; 1**
  <br/> I’ve been using Astra to orchestra Fable and Opus and it’s been great. Not seeing anything even close to this level of token consumption

- by [unknown](#) **&#x21C5; -1**
  <br/> Incorrect.

- by [unknown](#) **&#x21C5; 1**
  <br/> you need to decide, if subagents are the correct workflow in this specific task. if invoking/managing a subagent token cost > subagent's task cost, then surely it will cost more.

and something wrong with that graph that doesn't makes sense. it looks like you ran 100 subagents to make a code change for few lines where it could be done in a single session sequentially.

- by [unknown](#) **&#x21C5; 1**
  <br/> For my plus brothers.

Dont use astra as an orchestrator.

Astra as a subagent to terra medium. Only to plan, create workpacks for Luna, or review, critic.

Spawn astra in, do 1 thing, close it down

- by [unknown](#) **&#x21C5; 1**
  <br/> They advertised this model as a great orchestrating model. If I had a tinfoil hat they are sabotaging it so people stop doing it lol.

- by [unknown](#) **&#x21C5; 1**
  <br/> They should have a mode called astra ochestrate that uses the ideal model to implement review and orchestrate. They can do a bunch of combos and see how they bench.

- by [unknown](#) **&#x21C5; 1**
  <br/> Eu geralmente acho que orquestrar com o astra é desperdício de token. Eu monto um plano detalhado e rígido pelo astra. Dividido em fases para auditoria. Meu orquestrador é uma luna no mínimo, que vai chamar os executores e auditores, cujo nível de inteligência ja foi definido no plano.

Correções na mesma fase nao chama janela nova. As fases chamam o orquestrador sem que este tenha que ficar absorvendo o contexto das sessões

Pra mim funciona bem quando quero manter o trabalho automático

Edit: gosto tambem de que o orquestrador consulte o limite semanal restante antes de executar uma nova fase, quando quero poupar alguma % de trabalho

- by [unknown](#) **&#x21C5; 1**
  <br/> I actually made my Astra orchestrator/control center just straight up sit in her own chat and directly talk to other chats with separate codex instances working, sol high, for example.Sol does the task, sends the handoff to Astra, Astra checks, sends what to fix/continue and so on.

Sol could even work on a single goal and send reports to the control chat, meanwhile continuing his task.

It’s pretty funny and interesting.

- by [unknown](#) **&#x21C5; 0**
  <br/> yes, I noticed it too.. 😰
