#Is Astra Light better than Sol medium? [Visit](https://www.reddit.com/r/codex/comments/1w9s0f4/is_astra_light_better_than_sol_medium/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [rehanadil_](https://www.reddit.com/user/rehanadil_/)
### **Vote:** 14
---
I am using Astra High for planning, and Sol medium for implementation. Saw Tibo's post on X that Astra 'Low' (I see light on my app, not low) is better than Sol medium. Anybody can verify that statement? Don't wanna end up with a mess. Also the token usage, same or more expensive on Astra light compared to Sol medium?
---
## Comments 22

- by [some1else42](https://www.reddit.com/user/some1else42/) **&#x21C5; 32**
  <br/> astra low is better than sol high even

- by [some1else42](https://www.reddit.com/user/some1else42/) **&#x21C5; 4**
  <br/> what about the cost? same or cheaper or more expensive?

- by [unknown](#) **&#x21C5; 11**
  <br/> depends heavily on the task. on complex tasks it can be similar / sometimes even cheaper because it needs only so little output tokens to solve a task. however in other cases it will be way more expensive

- by [unknown](#) **&#x21C5; 3**
  <br/> Number of input tokens is the main variable. On complex tasks with relatively few input tokens, Astra low is cheaper. If you're feeding a ton of context to the model, Sol will be cheaper.

- by [unknown](#) **&#x21C5; 2**
  <br/> Yes my experiments have been showing it's loading context that's the expensive part. Everything else is relatively cheaper, due to it's efficiency.

The best way to work with Astra is to have a cheaper model load all the context and send Astra the tiniest possible workload and have Astra ask the orchestrator for more context if needed.

That's been keeping my quota down, Astra on a plus plan has been perfectly usable for me, you just can't expect to get by loading a mature repo and think it won't cost.

- by [unknown](#) **&#x21C5; 1**
  <br/> So astra being the subagent?

- by [unknown](#) **&#x21C5; 1**
  <br/> Yup. Astra low has been proving a better sub agent/worker than Luna max. Way faster, better quality, less errors

- by [unknown](#) **&#x21C5; 2**
  <br/> Hey, what model do you use as the main agent (which I assume is your orchestrator)? And to clarify, Astra low as the implementor?

- by [some1else42](https://www.reddit.com/user/some1else42/) **&#x21C5; 2**
  <br/> you should route specific workloads to specific models. you shouldn't just chase latest. that is how you keep things cheap enough while getting to use the latest models but focused on where they excel.

as an example, the project i'm working on, i let astra low run on it, and within 18 hours I was out of my weekly budget on 20x Pro. but after having astra review and make a project specific skill that understands cache read/write to take advantage of it, while routing specific work to specific model + reasoning levels. now i'm using about 1.5% weekly utilization an hour.

you can have a diff codex session review another session and produce this per project subagent routing skill for you. and then a day or more later, have it re-review and confirm it is working as expected.

- by [some1else42](https://www.reddit.com/user/some1else42/) **&#x21C5; 2**
  <br/> [u/some1else42](/user/some1else42/) you changed my life with this: "but after having astra review and make a project specific skill that understands cache read/write to take advantage of it, while routing specific work to specific model + reasoning levels", thanks for that

- by [unknown](#) **&#x21C5; 5**
  <br/> So far Astra seems to be more efficient at task even in light or medium than Sol.It’s use more tokens than Sol, but this is to be measured in long term for the same task. Dunno if someone did it already

- by [unknown](#) **&#x21C5; 7**
  <br/> It's the opposite for me. A really simple task with Astra light consumes like 20% of my 5hour usage (I'm on the plus plan). But the same task done by sol high consumes like 4%. Quality wise, it's the same because it's a simple task but yeah. I can't use Astra tbf.

- by [unknown](#) **&#x21C5; 1**
  <br/> Check this skill i developed

[https://www.reddit.com/r/ollama/s/Ka9MCikYdF](https://www.reddit.com/r/ollama/s/Ka9MCikYdF)

Is like a harness to use Ollama’s cloud models as executors for Codex using Claude CLI, the models tested are listed: GLM, Deepseek, Kimi, Nemotron, etc …

I am planning to update the skill so use Ollama CLI directly instead Claude.

- by [unknown](#) **&#x21C5; 3**
  <br/> Astra low is suppose to be better than Sol medium. I never had any proper success with anything over Sol medium. Sol high was my last cut off on highest effort level. Astra medium is my new cut off, returns above that are deminishing. Terra xhigh and high are good for editing and Luna xhigh is good for read only. Astra low or medium is a good orchestrator.

- by [unknown](#) **&#x21C5; 2**
  <br/> Better, yes, more expensive, yes. The takeaway I got from it was, if you are used to using Sol High, and you are burning through usage trying Astra (assuming on High), then that's overkill, because Astra Low/Light is better than Sol High. It is a better model, it can do things better than Sol, it costs more, that is the tradeoff.

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra light is just above sol high in terms of price and quality like poor man's sol max

Main benefit in addition to being a new model it works about twice as fast so you get the same job in twice the speed for the same price and quality

- by [unknown](#) **&#x21C5; 1**
  <br/> For everything except writing, info retrieval, and chatting, Astra Low is even better than Sol High, but it consumes 2.5x more tokens.If you have Plus, you're doing right, it's best to use Astra only for short but tricky tasks or complex planning, for everything else it's overkill and Sol is already good.

- by [unknown](#) **&#x21C5; 1**
  <br/> astra low is godly i just figured it out

have the main agent ping pong a subagent in implementation both astra low/light

and have your planning done by astra pro, or sol in chat if you are plus

the most reviewed code in history + you can't get more value than this

on top of that it is fast

- by [unknown](#) **&#x21C5; 1**
  <br/> how do you design your prompts? via main agent and send it to the subagent in codex? do you use a fresh codex slice for each slice/workpackage? i found astra low to drain all my usage so fast =(

- by [unknown](#) **&#x21C5; 1**
  <br/> In a complex project I'm working on I find Astra Low to be better at coding than Sol medium, but it also suffers from insufficient thinking sometimes. It's very lazy and just doesn't go as far as I'm used to with medium effort, which isn't really a surprise. So it can write the code, but don't count on comprehensive results without a coordinator keeping tabs on it. I've had poor results from delegated work in the past so for now I keep the complex tasks on medium.

- by [unknown](#) **&#x21C5; 1**
  <br/> I think Sol is no good at this point. It basically ignores most of my instructions at higher intelligence levels. I have not used Astra until today but apparently, I have been wasiting my time with Sol for the past few days.

- by [unknown](#) **&#x21C5; 0**
  <br/> Astra light is better than any prev gen model including sol ultra for tasks like computer use, 3-D modelling, unreal engine and blender, so it depends heavily on the task for coding and planning it might be on par, but I have tried sol ultra for unreal engine and computer use and 3-D modelling and it’s not even 20% of what Astra light can do. So in terms of computer use and 3-D modelling and game development. It’s on a different level when it comes to coding and planning in general, I’m not quite sure, but it’s quite expensive. The light version is like more expensive than extra High of 5.6 sol
