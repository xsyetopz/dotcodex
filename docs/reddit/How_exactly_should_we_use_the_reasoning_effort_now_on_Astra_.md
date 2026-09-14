#How exactly should we use the reasoning effort now on Astra? [Visit](https://www.reddit.com/r/codex/comments/1we25md/how_exactly_should_we_use_the_reasoning_effort/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [aalluubbaa](https://www.reddit.com/user/aalluubbaa/)
### **Vote:** 17
---
I've read a lot of people saying that Astra Ultra consumes only a tiny bit of more tokens on thinking so it actually gets more things done with LESS usage than lower tier thinking level. I have a similar experience with this but I've never measured it thoroughly.
What is the best practice right now?? What is the most effective way to save usage on simpler tasks?? People use higher reasoning effort for more complex issues so there is no confusion.
The confusion really is "DOES LOWER REASONING EFFORT SAVE MY USAGE"??  Can anyone give some proven answer?
---
## Comments 11

- by [unknown](#) **&#x21C5; 11**
  <br/> Ultra is very eager to quickly finish the task. It doesn't really work if you don't bump up your subagent limits. Often times ultra would finish an impressive amount of things in 10 minutes, but with subpar polish.

Max will take lot more time and effort to refine details and add polish.

Light will just tell you it knows the solution but doesn't do it. It's very lazy and you need to babysit it and push it to work.

I'm usually just using xhigh by default. It feels like a good balance.

- by [unknown](#) **&#x21C5; 2**
  <br/> Light up to medium is very good at acknowledging what you say with a one liner and finishing. I’ve had to give it a good number of ‘And… what are you going to do about it?’ prompts over the past week.

- by [unknown](#) **&#x21C5; 1**
  <br/> It is not lazy. Effort is basically signally to him how much budget he get to do this. Imagine giving your worker 1 million dollar to kill the roaches, he is going to build a Tesla coil for that. This is akin to using max. While if you put low is like telling someone to throw a grand party with a budget of 10 dollars. So what effort will work depends on what you are doing and how much polishing or gold plating.

- by [unknown](#) **&#x21C5; 4**
  <br/> I’ve been sitting on Astra High since it came out. Mostly focused on infrastructure based tasks like Terraform, Ansible, etc for setting up a kubenetes cluster. This past week I’ve been hammering it for 8-10 hours a day, as fast as I can feed it prompts, and I’m sitting at 38% remaining with 3 days left before my standard reset. I’ve been wanting to use some of my banked resets, but have yet to run out. 🤷

- by [unknown](#) **&#x21C5; 4**
  <br/> Basically, if your task is genuinely hard, you should use astra on xhigh/max. Low and medium do not plan effectively enough, and end up using more tokens fixing errors. This is evident on the ARC AGI benchmark.

 
       [](https://preview.redd.it/how-exactly-should-we-use-the-reasoning-effort-now-on-astra-v0-pcq16ph0e1ph1.png?width=777&format=png&auto=webp&s=eea0d0fc5184dccc96f64cd7e170ebe440992548)
      
    If you are doing simple tasks where planning is not necessary, I'd suggest using Terra or even Luna Max

- by [unknown](#) **&#x21C5; 5**
  <br/> Reserve Astra for xhigh or max thinking only. Use it on tasks that require high intelligence, such as architecting your project, making plans for non-rote features (based on your user stories) and things like that.

Don't touch Astra low/med/high - the subscription multiplier you pay on their usage is not worth it. They should *only* be used when you actually need the higher intelligence. For almost everything else, Sol is solid enough.

- by [unknown](#) **&#x21C5; 2**
  <br/> Ask your coding agent (probably use astra-med or sol-md). Seriously.

Something like: "Study the sessions for the last 7 days, compare effectiveness (task) and efficiency (wall clock time and token $) for sessions using different combinations of model and reasoning lavels"

- by [unknown](#) **&#x21C5; 3**
  <br/> I've been experimenting with this, comparing Astra Low to Luna Max, Astra Low, vs XHigh and I've found that Astra Low beats Luna Max in usage when you take in completed slice - which includes implementation and repair fixes along with time to complete and quality of work.

Astra Xhigh vs Low - it doesn't cost significantly more to use xhigh.

A couple of caveats - Astra is still expensive and you'll pay for it if you don't know what you're doing. Having a support structure, bounded tasks, stop points, checks, proper design phase, and all that - I get a ton of usage out of astra. I'm on Pro 5x, I can get roughly 30 to 40 hours of work in a week done with Astra. It also depends on what you ask of it. Super cheap for greenfield work. Have a massive legacy codebase? Well...that might be a bit different. YMMV

Would I get more work done with Luna? In theory? Yes. But it would take far longer, produce lower quality, and require more repair time than simply using Astra.

- by [unknown](#) **&#x21C5; 1**
  <br/> What you’re describing I’ve seen for XHigh, not Ultra, but I don’t know which of those is more “efficient”

I’ve seen an interesting strategy I’m going to test out where you have a cheap orchestrator and call in Astra for small important tasks.

[https://x.com/anshuc/status/2097821164093480999](https://x.com/anshuc/status/2097821164093480999)

I’m going to be testing a few variants of something like that and see how it goes.

- by [unknown](#) **&#x21C5; 1**
  <br/> Don't ask the jack wagons here. They were telling us 3 days ago there was nothing wrong.

- by [unknown](#) **&#x21C5; 1**
  <br/> If nothing has changed, it should be astra max and go to town.
