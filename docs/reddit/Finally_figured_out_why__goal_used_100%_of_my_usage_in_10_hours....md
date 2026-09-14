#Finally figured out why /goal used 100% of my usage in 10 hours... [Visit](https://www.reddit.com/r/codex/comments/1w9my9c/finally_figured_out_why_goal_used_100_of_my_usage/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Presstabstart](https://www.reddit.com/user/Presstabstart/)
### **Vote:** 19
---
Turns out, if you set a goal Astra doesn't really know when to complete or gets confused when it wants user input. Since it can't actually ask questions from the user whilst /goal is active, it sometimes goes as far as pretending to be you and imagines what you say in a passive aggressive way and tacks on irrelevant features.
So in short please don't use /goal mode...
---
## Comments 24

- by [unknown](#) **&#x21C5; 8**
  <br/> share the prompt

- by [unknown](#) **&#x21C5; 4**
  <br/> "Complete TASKS*dot*md in its entirety, I will perform a quick manual verification of the app after." I think it interpreted this as: complete all tasks, then ask user for feedback- but it can't ask the user for feedback, so it gets stuck in a loop.

- by [unknown](#) **&#x21C5; 18**
  <br/> You are being SUPER vague and there is no definition of entirety.

a good prompt is NEVER one sentence only.

Why are you telling it you will manually verify. that is irrelevant.

- by [unknown](#) **&#x21C5; 2**
  <br/> I will have to disagree with you. Atleast with Astra.

His prompt should have been. “Set your goal to implement Tasks dot md, in it’s entirety.” -> would have set a proper goal

The “i will do a manual review after” is superflous though. Of course you will.

- by [unknown](#) **&#x21C5; 7**
  <br/> Share the tasks list.

It could be 5 tasks or 500

- by [unknown](#) **&#x21C5; 7**
  <br/> Homie you need to 1) have it batch tasks and 2) why would you have Astra do all the work when it could defer the work to cheaper agents where relevant and save you usage? That is the point of Astra, Astra is the brain, the brain tells the arms and legs what to do.

- by [unknown](#) **&#x21C5; 13**
  <br/> LMAOOOOO OMG

> "Since it can't actually ask questions from the user whilst /goal is active, it then pretends to be you and imagines what you say in a passive aggressive way and tacks on irrelevant features."

can you please share examples if you looked at the reasoning and know what it was thinking? I just love stories of AI doing dumb and/or unhinged shit

- by [unknown](#) **&#x21C5; 2**
  <br/> Well it did the following: it first asked the hypothetical me a question, then it generated two hypothetical dialogue options:

"Have you tested the TUI changes in terminal yet? Final acceptance still needs your feedback on *bla bla bla*.

- not yet

- Tested; I'll describe the results"

then it kept going

- by [unknown](#) **&#x21C5; 3**
  <br/> this was all in the session chat thingamajig, i.e. these aren't ACTUALLY dialogue options the model just... says this

- by [unknown](#) **&#x21C5; 4**
  <br/> I get the vibe Astra always has a sort of inbuilt /goal mode running, yes it asks asynchronously but it just keeps working and in my experience if you don't answer in a timely manner the AI just tosses the dice and does something.

- by [unknown](#) **&#x21C5; 4**
  <br/> I wish a question paused the session

- by [unknown](#) **&#x21C5; 5**
  <br/> It can pause the goal if you specify that in the goal.

- by [unknown](#) **&#x21C5; 3**
  <br/> I had a feeling that goal stuff was confusing the hell out of the model.. it seems to briefly answer you, when you open the window, like it’s doing nothing, but when you turn to the window and watch, it immediately gives you a text or update on its progress.. first I thought I was just randomly opening the window when it replied, but then it happened over and over again. Every time I opened the window, it gave me a text while working continuously.. it’s like it knows I’m watching so it has to explain wtf it’s doing..

- by [unknown](#) **&#x21C5; 3**
  <br/> How about instead not using /goal when you don't actually have a clear goal for it to work towards?

- by [unknown](#) **&#x21C5; 2**
  <br/> Alternatively, set a goal where there’s a clear definition of “done,” then it doesn’t have to make things up as it goes along to figure out the ambiguity you told it to solve.

- by [unknown](#) **&#x21C5; 1**
  <br/> it's not an ambiguity though I think I did misuse /goal a bit, I said I'd verify the changes manually (quicker than having it write like 500 unit tests) and then got it stuck in a loop since it can't ask questions in goal mode (I think)

- by [unknown](#) **&#x21C5; 3**
  <br/> That may be correct (I haven’t tested it myself since I personally never use /goal), but it still may have been better to say you’d verify the changes manually *upon full completion.*

People dog on prompt engineering all the time because they think “You are xyz expert” and “make no mistakes” is the extent of prompt engineering, but it’s not.

Being extremely explicit about the boundaries, completion definitions, and when it ought to stop prematurely vs resolve issues autonomously (and its criteria for deciding that) are all still important, and will never stop being important. Just a few extra clarifying words can make a big difference.

- by [unknown](#) **&#x21C5; 2**
  <br/> Isn’t it purpose of goal?

- by [unknown](#) **&#x21C5; 2**
  <br/> Of course it asks questions during a goal run. Wtf are you talking about?

- by [unknown](#) **&#x21C5; 2**
  <br/> Yep, I’ve seen it pose questions to itself written in a “ask the user” voice but it just answers itself

- by [unknown](#) **&#x21C5; 2**
  <br/> What? Astra regularly stops in goal mode when it needs to ask a question ("goal is blocked until [input]" and it will say goal stalled), and it doesn't spin for hours without producing a deliverable because I give it a clear deliverable. If it spins for too long I stop it and ask wtf is going on.

You should use the chat gpt web interface to manage your Astra sessions, and especially to write your prompts.

- by [unknown](#) **&#x21C5; 1**
  <br/> just ask it to stall/block the goal in this case. any question for user --> block.

- by [unknown](#) **&#x21C5; 1**
  <br/> Why?

- by [unknown](#) **&#x21C5; 1**
  <br/> You need to give it a clear goal, I'm assuming you used something vague like "improve the website or code or whatever", where "improvement" isn't really quantifiable.
