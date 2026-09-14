#I can’t get meaningful stuff / code from Astra [Visit](https://www.reddit.com/r/OpenaiCodex/comments/1wck3h1/i_cant_get_meaningful_stuff_code_from_astra/)
### **Subreddit:** [r/OpenaiCodex](https://www.reddit.com/r/OpenaiCodex)
### **Author:** [Euphoric_North_745](https://www.reddit.com/user/Euphoric_North_745/)
### **Vote:** 12
---
It is good at documents, it can write long once, people say it is very good at 3d, others now say it is doing cad slop, I do not know.
All what I know, I have an app, the app needs a feature that i added in another one with gpt codex 5.3 before, and with 5.3 codex model we did the work in a day or less
With Astra, this is now week 2? and with Sol earlier? 3 weeks, the same task
Before I give up on the model and move to something else, how do you get coding features done with Astra?
I was super hyped but now, not at all
Update: I am starting a brand new web app project again to test, using Astra medium, will make sure it has an agents md that prevents qualifications and over engineering and testing until a bit later in the app, i will see how it goes
---
## Comments 30

- by [unknown](#) **&#x21C5; 3**
  <br/> I find Astra incredible but I’ve been using it for reverse engineering. It does things Sol would just fail over and over but also it messed up stuff that Sol fixed it rather quick.

- by [unknown](#) **&#x21C5; 2**
  <br/> Yes my subscription ends tomorrow and I won't renew for now. It's completely useless for me now, I don't need 3d models, I need clean code.

Sol has been nerfed to hell as well, so all models now just lead to more tech debt that I can't afford and it's easier for me to just code by hand instead of constantly reviewing and throwing away shit code

- by [unknown](#) **&#x21C5; 1**
  <br/> What effort levels have you tried? I find it almost impossible to get an actual task done with the higher efforts.

- by [unknown](#) **&#x21C5; 2**
  <br/> all efforts, at low it has issues, but at medium, if you start with some clear items, and you monitor very closely, may get stuff done, the moment you leave it to do the rest in "goal" mode, the work is gone, nothing can stop the slow after that

- by [unknown](#) **&#x21C5; 1**
  <br/> Oh you didn’t mention you are using goal mode.

Goal mode is absolutely useless.

- by [unknown](#) **&#x21C5; 0**
  <br/> I wouldn't say useless but you need a very detailed highly specified plan and process for it to follow, otherwise you will just end up with mountains of slop

- by [unknown](#) **&#x21C5; 1**
  <br/> Honestly, I havent noticed much difference between Sol and Astra when it comes to real-world coding work. Astra may perform better in certain benchmarks or with 3D-related tasks, but this doesnt translate into anything useful for my own projects.

I have a small benchmark based on the kinds of mistakes and problems that AI coding agents actually encounter while working on my codebases. When I tested Sol and Astra on this benchmark, they both made many of the same mistakes on the same tasks. Astra did produce some over-engineered solutions that Sol handled more simply, but I wouldnt call that an advantage.

The bigger issue for me is that Astra also burns through usage noticeably faster. In practice, I can get more work done with Sol before reaching the same usage limits.

So, for now, Im sticking with Sol. Astra doesnt seem bad, but I havent found a real-world advantage that justifies the higher cost of usage.

For reference, I tested both on Medium.

- by [unknown](#) **&#x21C5; 1**
  <br/> My guess is that you haven't cleaned up your skills, [AGENTS.md](http://AGENTS.md) files etc. for the new models.  I had a similar experience I think when 5.5 or 5.6 came out. I had elaborate orchestration workflows that were needed back then to keep the agents from going off the rails.  For me deleting all those skills and starting fresh did the trick.  The models now do the things that I was having to push them to do before out of the box so the skills were redundant but worst than that they were making it spin it's wheels.  Then when Sol came out a new issue has emerged and that is it's tendency to way over engineer things.  It's great if you have unlimited tokens and actually need code written to handle almost any obscure defect but 99% of our cases don't need that nor do we have the time to wait for it to finish building that.  I would suggest you look at your [AGENTS.md](http://AGENTS.md) files and try to simplify them, removing anything that is no longer really needed since the models probably already know it.  Then add something about finding the simplest solution for everything.  Maybe have Astra or Fable research best practices for [AGENTS.md](http://AGENTS.md) and specifically how to reduce over engineering.  Have it research solutions like ponytail and then have it to a review of all your [AGENTS.md](http://AGENTS.md) files and then ask it to propose some changes for you (not changing but proposing so you are able to approve) I think those few changes will help you out immensely.

- by [unknown](#) **&#x21C5; 2**
  <br/> [Agents.md](http://Agents.md) has no skils and it is small, has rules about how to format the code, now about over engineering, there is nothing i can do to present that.

From memory

GPT 5.0 to 5.2 it was adding fallback code that can't be tested easly

5.3 can avoid a bit the fallback but must add it in the prompt or it will add the code.

5.4 and 5.5 will lie sometimes

5.6 and Astra will write shit of code that is not related to the task, their first goal is to test the codes that is not complete yet

- by [unknown](#) **&#x21C5; 1**
  <br/> The problem is possibly your app itself has ballooned in size in the days since you used codex 5.3, and as a result performance of the models has degraded.

- by [unknown](#) **&#x21C5; 1**
  <br/> Codex 5.3 was making the app very small, i looked at all files, i had full control of it, i am using codex since April or may 2025, went through all models since 3.5 / 4.0

5.3 was 2 version, GPT 5.3 in Codex app and Codex 5.3 model, the 5.3 model was autistics workhorse

- by [unknown](#) **&#x21C5; 2**
  <br/> Fair enough. I am making very good progress on all my projects with Astra, but I have found you need to keep it under very tight control, or it will over engineer absolutely everything. Sol was similar. If you have access to Fable I much prefer asking fable to plan epics and tasks and Astra to build them, and then Fable to review them ... but Fable is expensive.

- by [unknown](#) **&#x21C5; 1**
  <br/> Use Gpt-sol in Chat mode and ask you to help create an implementation plan to feed codex. After a few prompts sparring back and forth I think you'll have a better shot of getting what you want. This is it least how I do it and and it works surprisingly well.

- by [unknown](#) **&#x21C5; 1**
  <br/> Thank you, I will try that

- by [unknown](#) **&#x21C5; 1**
  <br/> I had medium take a look at an application that just crawled after a certain point. It gave me 3 fixes based on priority, doing all three reduced my render latency by 80-90%.

Sol couldn’t put the aerosol cans it was huffing down long enough to do anything to improve it.

- by [unknown](#) **&#x21C5; 1**
  <br/> Is your app full of spaghetti code? Because then even the frontier models will struggle to keep implementing more without introducing side effects

- by [unknown](#) **&#x21C5; 1**
  <br/> I love spaghetti but i prefer code lasagna, still, the rg command does not care when it rg stuff

- by [unknown](#) **&#x21C5; 1**
  <br/> I ended up plugging deepseek into codex and using that agent instead.

- by [unknown](#) **&#x21C5; 0**
  <br/> You did not say, but I assume you are using codex? And I assume you are asking it to thoroughly analyze and plan before making code changes? And you are using the "high" reasoning level?

- by [unknown](#) **&#x21C5; 2**
  <br/> I used all levels, have many repositories, many copies of the repository, 2 virtual machines each with up to 40gb of ram, SSDs , etc, nothing is missing for the model to do work if it wants to do the work

- by [unknown](#) **&#x21C5; 0**
  <br/> Did you ask it to analyze your codebase before you started? For the changes you want, did you address them one at a time in /plan mode?

- by [unknown](#) **&#x21C5; 2**
  <br/> I did not, but I created in one of the tests a brand new codebase with Sol and it was fast the first 3 to 5 days, got slower, and by day 30 it was impossible to progress.

I see the same with Astra, starts big, fast, then slow to progress

- by [unknown](#) **&#x21C5; 0**
  <br/> Don't just tell it what you want. Make sure it has context and understanding of what it is about to do. Make sure you understand the design. Then use /plan and tell it to turn those ideas into a coding plan. THEN, tell it to implement.

- by [unknown](#) **&#x21C5; 2**
  <br/> i just checked online, the Astra model lasted 3 days, what we have today is something else, people are posting many examples on x same promot before and after , this can explain what is going on maybe

- by [unknown](#) **&#x21C5; 1**
  <br/> What do you mean by "it lasted 3 days"??

- by [unknown](#) **&#x21C5; 2**
  <br/> Some posts on X are showing Astra day 1, 2, 3 and then the same prompt day 4 and after, day 4 and after is still good, but day 1 - 3 is much better

- by [unknown](#) **&#x21C5; 0**
  <br/> Astra Light is pumping out entire functional apps and websites for me in minutes. Whatever setup you're using, skills, harness, etc could getting in the way. Just run it as vanilla as possible.

- by [unknown](#) **&#x21C5; 1**
  <br/> I am trying light at the moment on a brand-new empty codebase, and it is doing good so far, i hope it continues this way

- by [unknown](#) **&#x21C5; 1**
  <br/> Now try and have it make something to specifications.
