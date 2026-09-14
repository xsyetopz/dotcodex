#Astra Orchestration & Session Management - Tips For Usage Savings - Used 4 Billion Tokens Over The Long Weekend [Visit](https://www.reddit.com/r/codex/comments/1wav530/astra_orchestration_session_management_tips_for/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Public_Reality_4401](https://www.reddit.com/user/Public_Reality_4401/)
### **Vote:** 45
---
Good morning!
I've found some really efficient workflows that seem to get the best out of Astra while maintaining lower costs closer to Sol on average for long horizon tasks. I am on the 20X plan.
TLDR: Ask Astra High to orchestrate a Sol high session. It will spin up its own session in the GUI and you can watch both.
More details:
ChatGPT can now have its sessions speak with eachother and it has unlocked some excellent abilities. I created a new skill called /orchestrate that has the following prompt:
"You are an orchestrator/manager of a Sol High effort session you create. You plan, review major milestones, and provide blocks of work to your orchestrated session. The session should only reach back out to the orchestrator when it has hit a blocker that is both meaningful to overall direction and cant be assumed from given inputs. You should check in every three hours to ensure it is still working on work that is aligned with our goal. If you feel a task should be broken into more than 1 sol session, you must ask me first before spinning it up. You will become the manager of that session as well.". So I will type /orchestrator then the goal I am working towards.
I killed 3 100% usage pools over the long weekend by thrashing Astra from light up through Ultra. One Astra high session was depleting 2.3% per hour. This new Astra - > Sol orchestrator is seeing about .38% per hour, roughly 1% ever 3 hours. As for output, it has been FASTER than just using Astra, at least in my experience. The long horizon tasks I have it working on are getting more pointed/focused improvements due to Astras management and delegation of execution/implementation.
I created a site that ultimately paid for all of my AI subs, Miniskyline.com, and that is what these agents were primarily working on.
What are your usage tips for Astra? How are you finding it works with other models? Have you tried orchestration like this?
---
## Comments 13

- by [unknown](#) **&#x21C5; 4**
  <br/> Great idea, working really well so far. I just added the following for a more optimized and autonomous job: "Sol chat can orchestrate lower models agents for suitable tasks. Ask Sol to comer back to you if the task is finished".

- by [unknown](#) **&#x21C5; 1**
  <br/> Why do you mean by Sol chat? Not sure I understand your additional prompt

- by [unknown](#) **&#x21C5; 1**
  <br/> Session/chat/window... so many IDEs I mix the names.

- by [unknown](#) **&#x21C5; 1**
  <br/> Aah! If I understand correctly, you mean that Sol agents in their own session/chat can orchestrate other lower models and open new sessions/chats (or subagents)?

- by [unknown](#) **&#x21C5; 2**
  <br/> Yup

- by [unknown](#) **&#x21C5; 2**
  <br/> Smart! Thank you for your responses

- by [unknown](#) **&#x21C5; 3**
  <br/> I will build on this idea a bit. I have a Max x5 plan, so I have to be a lot more discriminate with my usage.

What I have found works really well for me (after having burnt through hundreds of millions of tokens over the last few days as well) is for Astra-low to do a root cause analysis of any issue I am trying to tackle, then I ask it to create an pareto-frontier, token-efficient orchestration & implementation plan.

However, the pareto-frontier and token-efficient restrictions are important and then I ask it to detail which models and effort levels will be applied to every PR/milestone in the plan. All plans I have done like this have multiple PRs.

I also ask it to assign the implementation to a very token-efficient model and effort level.

The net-net typically tends to be Luna-med/high is the orchestrator, then Luna-med is the implementer for most of the work, for anything that gets a bit tricky it assigns Terra-med or Terra-high to that.

Then I insist that after every PR/milestone either Sol-high or Astra-low should do an adversarial review.

So most of the time Luna is doing both the orchestration and the implementation and Astra or higher models only tackle the things that they do really well with.

This approach has really helped me be very efficient.

That being said, Luna is much slower than other models....so things take forever (it feels like) and even still...I have been finding that I can only really run 2 - 3 workspaces with this approach at the same time all day, and get 1 - 2 days of my weekly limit.

If I don't run 2 - 3 workspaces for literally 18 - 24 hours per day, then I can stretch out my weekly limit to maybe 4 - 5 days I believe.

Since the last reset (yesterday) I have been running it every hour since then and I am now down to 22%...but I have done A LOT of work.

RIP my usage.

Hope that helps someone.

- by [unknown](#) **&#x21C5; 2**
  <br/> That’s an interesting idea. I’m having codex setup a —orchestrate flag that will launch this workflow and set codex to Astra high. I might also include a -r to adjust reasoning up to xhigh or max while keeping everything else the same.

- by [unknown](#) **&#x21C5; 2**
  <br/> Thanks for the tips. X20 account?

- by [unknown](#) **&#x21C5; 1**
  <br/> Wow, looks interesting. What would you recommend for my use case if the work isn’t really automation-focused, but more about planning, reviewing, and implementing?

What I’m imagining is that I can go back and forth with Astra to think through the direction, UI/UX, landing pages, new ideas, and the overall strategy, while Sol handles the actual implementation.

I originally assumed an automation-style setup from your prompt because it could check progress every few hours, but most of my work is happening much earlier in the process. We’re usually creating something from scratch, experimenting with the direction, refining the design, and iterating together rather than monitoring an already established workflow.

So for that kind of setup, what approach would you recommend?

- by [unknown](#) **&#x21C5; 1**
  <br/> i use an astra x high agent to orchestrate luna max and astra low agents. it maintains like 20 chats which each can have their own subagents. it's basically a swarm. They communicate back and forth. here's what's been sent to the orchestrator agent. Its currently building an orchestrator program that has loads of different providers models available in it.

 
       [](https://preview.redd.it/astra-orchestration-session-management-tips-for-usage-v0-bbja9jrdeeoh1.png?width=949&format=png&auto=webp&s=99e2643090a2fabf79231a08cfc8f0bf2f5b2321)

- by [unknown](#) **&#x21C5; 1**
  <br/> Todo esto se hace atravez de chatgtp.com?

- by [unknown](#) **&#x21C5; 1**
  <br/> I have created a plugin for hermes agent to delegate tasks to codex and or hestrate but it was before Astra. I cant stop using Astra anymore… Sol??!!!! Who is Sol😳🫣🙈🥹😂
