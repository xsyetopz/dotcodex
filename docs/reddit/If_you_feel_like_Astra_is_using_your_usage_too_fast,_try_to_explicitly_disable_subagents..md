#If you feel like Astra is using your usage too fast, try to explicitly disable subagents. [Visit](https://www.reddit.com/r/codex/comments/1was4e3/if_you_feel_like_astra_is_using_your_usage_too/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Media-Usual](https://www.reddit.com/user/Media-Usual/)
### **Vote:** 0
---
In my personal testing, I haven't noticed that much of a speed difference, and I've pretty much quadrupled the amount that's able to get done for the same amount of usage.
I haven't changed anything other than this: in the middle of me working in four different sessions and projects. I just changed my global rule to disable the use of subagents unless explicitly requested. I told all my existing sessions to stop doing subagents and do their work in the main thread. That immediately caused my usage over the next 2 hours to drop dramatically.
Of course YMMV.
---
## Comments 8

- by [unknown](#) **&#x21C5; 2**
  <br/> Cause the default for subagents is to just use the same model you are using for your main thread cloned.

Astra High main thread? Every subagent is Astra High. 🤦

- by [unknown](#) **&#x21C5; 2**
  <br/> Yes, and there is also the hug where in codex Astra is pinging sub agents constantly, so the main thread is also using up a lot more tokens while the sub agents run.

- by [unknown](#) **&#x21C5; 1**
  <br/> I made an orchestrate skill that better defines when and what to use for sub agent reasoning. Dont have any issues running astra medium as an orchestrator constantly for days.

- by [unknown](#) **&#x21C5; 1**
  <br/> Yeah, there was a bug where Astra is pinging sub agents constantly that was causing issues unless you change configs.

I am using sub agents again after that fix, but a lot of people are just doing default configs which could explain the churn.

- by [unknown](#) **&#x21C5; 1**
  <br/> my biggest issue with subagents now is that luna is so damn slow, using it as a subagent drags the whole project to a snails pace, and Astra pings it regularly, *and* it doesn't stop and return a result when it's told to. I'm considering using terra or a sol-low as subagents.

- by [unknown](#) **&#x21C5; 1**
  <br/> I'm right now testing delegating more tasks.

The issue with Luna Max is that it's using tons and tons of reasoning.

If the task is small enough that Luna medium or high can reasonably do it then it should be much faster.

- by [unknown](#) **&#x21C5; 1**
  <br/> Terra medium as a subagent does wonders.

It never plans, just summons sol high, gets workers. Summon sol high again, fix fix Complete, commit push

- by [unknown](#) **&#x21C5; 0**
  <br/> Yo uso sol como orquestador y con función exclusiva de luna para búsquedas y resúmenes y Astra para consultas complejas con contexto completo procesado y una sola consulta y respuesta a la vez, mientras que luna se encarga de lo general
