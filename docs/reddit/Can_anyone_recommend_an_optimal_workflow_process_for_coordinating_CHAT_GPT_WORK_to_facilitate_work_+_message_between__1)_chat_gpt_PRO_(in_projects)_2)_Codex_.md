#Can anyone recommend an optimal workflow/process for coordinating CHAT GPT WORK to facilitate work + message between: 1) chat gpt PRO (in projects) 2) Codex? [Visit](https://www.reddit.com/r/OpenaiCodex/comments/1w2bbki/can_anyone_recommend_an_optimal_workflowprocess/)
### **Subreddit:** [r/OpenaiCodex](https://www.reddit.com/r/OpenaiCodex)
### **Author:** [Abel_091](https://www.reddit.com/user/Abel_091/)
### **Vote:** 5
---
Hello,
I have been quite impressed with how effective chat GPT WORK has been so far at performing some autonomous tasks.
I was wondering if there are some optimal way or workflows to get it to help me with the ultimate task..
I'm building a big coding project and usually feed between chat gpt PRO (within projects) into Codex, back and forth rinse and repeat = building.
Does anyone have recommendations for using chat gpt WORK to eliminate the constant copy and pasting and facilitating between the two?
I typically use Codex Cli because its always worked best but I'm thinking if I switch to the more integrated Desktop/App Codex where both GPT PRO + Work are there might be an optimal way to do this?
Any assistance or suggestions are greatly appreciated, Thank you!
**UPDATE***
Ok maybe I should clarify exactly what im trying to do and why as Im seeing comments about "dont try and loophole the system"
I am not an experienced coder and I find this process helps in terms of:
- PRO always seem to catch things + make amendments so that big plans integrate successfully
And most importantly..
2) I believe there is a massive advantage to the PRO chats within projects because they all seem to have a deep context understanding of the project that ive been working on for almost a year now.
I think this is the biggest issue or advantage to wanting to do this is utilizing those PRO chats/agents from those project conversations to function as like coding project Manager.
Im not really looking to loophole anything just hoping to find a way to utilize what might be available to integrate those chats and Codex so that I dont need to feed back and forth non-stop.
Even if it ment somewhat reducing all the time I need to be present doing this for all integration plans would be a massive help, if possible?
Thanks!
---
## Comments 15

- by [unknown](#) **&#x21C5; 3**
  <br/> There's many out there. You can call codex or Claude or whatever u wan with chatgpt developer plugin, directly from chatgpt chat. But u need to do your own searching because we don't want them to fix this

- by [unknown](#) **&#x21C5; 1**
  <br/> Como fazer isso?

- by [unknown](#) **&#x21C5; 1**
  <br/> You can’t really do that with regular ChatGPT. It’s basically unlimited for a reason - it isn’t designed to be used as an agentic coding backend in the same way as Codex or Work.

And I’d be careful trying to find loopholes to make it behave that way. We literally just saw something similar happen with Codex: there was a behaviour where an already-running task could keep working after you hit your limit, and people started deliberately launching huge tasks right before their quota ran out to take advantage of it. That trick got shared around quite a bit, and now the behaviour has been tightened so tasks get stopped when the limit is reached.

So even if someone figures out a clever way of using regular ChatGPT Projects to orchestrate Codex/Work autonomously, I probably wouldn’t advertise it. If it effectively bypasses the intended agentic limits, there’s a good chance it just gets patched and we all end up with more restrictions 😂

- by [unknown](#) **&#x21C5; 1**
  <br/> why not just put the chat gpt work stuff in codex

- by [unknown](#) **&#x21C5; 1**
  <br/> Ok maybe I should clarify exactly what im trying to do and why if that helps

I am not an experienced coder and I find this process helps in terms of PRO always seem to catch things + make amendments so big plans integrate successfully

And

I believe there is a massive advantage to the PRO chats within projects because they all seem to have a deep context understanding of the project that ive been working on for almost a year now.

I think this is the biggest issue or advantage to wanting to do this is utilizing those PRO chats/agents within the project conversations to function as like coding project Manager.

Im not really looking to loophole anything just hoping to find a way to utilize what might be available to integrate those chats and Codex so that I dont need to feed back and forth non-stop.

Even if it ment somewhat reducing all the time I need to be present doing this for all integration plans would be a massive help

- by [unknown](#) **&#x21C5; 1**
  <br/> I do something pretty similar, just with the roles separated more. I use regular ChatGPT as the product/architecture side where I figure out what my program should do, work through ideas, and make sure we aren't drifting away from the overall vision. Then I have a Codex programmer that actually implements the work, and a separate ChatGPT Work supervisor that reviews the repo, tests, evidence, and what Codex changed before anything moves forward. They all work from the same repo, so the project itself holds the North Star, current state, authorization, reports, review evidence, etc instead of me constantly copying giant handoffs between chats. For higher-risk stuff I also have a fresh independent reviewer challenge the work so the same agent that wrote something isn't the only one deciding it's good.

Right now I still have to manually wake each side up when the other finishes, which is the part I'm working on eliminating. The end goal is basically an automated development loop where I approve a bounded set of work, the programmer implements it, tests it, gets independently reviewed when needed, the supervisor accepts/blocks it, and then the next already-approved offline task starts automatically. So ideally I can go to work or go to sleep and come back to several completed and reviewed milestones instead of one chat sitting at "waiting for supervisor." I'm being pretty obsessive about proving the automation itself is safe first though, because I don't want automation to make the coding worse or slowly degrade the intelligence of the project compared to when I'm manually handing things between the programmer and supervisor. Anything involving the live server, new authority, destructive actions, or major changes to the actual intelligence still stops and waits for me.

- by [unknown](#) **&#x21C5; 1**
  <br/> Ya this is basically exactly what im looking to do and I should probably just define the roles abit more specifically how you outlined, im probably adding unneeded steps.

I have been able to get CHAT GPT WORK to run some analysis tasks happening across different chats which includes collecting all the analysis reports, metrics outputs etc. From the chats and organizing into folders within my coding project + its also interacting with the chats and checking in everytime it finishes and prompting the next messages/analysis rounds..

It's because its been able to do this basically autonomous workflow perfectly and avoid the "chats waiting" that got me excited about having it lead more comprehensively the entire coding workflow with Codex.

Im thinking WORK can likely do this quite well if setup properly.

- by [unknown](#) **&#x21C5; 1**
  <br/> Work can do EXACTLY what you're wanting. It will just burn through usage.

- by [unknown](#) **&#x21C5; 1**
  <br/> I Think ive settled on sticking with my current workflow for now as PRO in projects brought up a good point.

I use Sol Ultra which I see alot of comments from users say to DEF AVOID for building due to over-engineering+ drifting concerns but I've built a pretty comprehensive process where I ask PRO to build an "optimal state of the art quality integration plan" which is usually a coded section of our bigger macro level plan and it will build it into a comprehensive zip folder of all the plan items and components to forward to Sol.

Sol Ultra will work through the plan and then it also produces a comprehensive zip folder detailing all completed items to give back to PRO.

Pro mentioned that if we werent working in this detailed comprehensive way which includes detailed guidelines, metrics, components Sol Ultra probably wouldnt perform as well, and as structured as it does (and id prob get alot of the drift + over-engineering etc). I probably wouldnt be using it at all and getting alot less completed within comprehensive plans.

I Thought that was a very strong point and makes the slower more supervised workflow seem more worthwhile now, atleast until I get out of these more core infrastructure type integration plans.

- by [unknown](#) **&#x21C5; 1**
  <br/> hmm i cant seem to get this to work i tried setting it up, chat gpt work cant seem to gather the zip folder from the PRO chat to give to Codex..i must be doing something wrong

- by [unknown](#) **&#x21C5; 1**
  <br/> Kill the copy-paste loop by making the handoff a file on disk, not a chat paste. Shared task note in the repo (goal, decisions, open questions). Pro writes it, Codex reads it, both stop being a clipboard.

- by [unknown](#) **&#x21C5; 1**
  <br/> Im totally with you on this and that be perfect but PRO keeps telling me it cant download and save the zip folder it creates

Basically i have pro build a comprehensive plan with all components into a zip folder which allows codex to complete comprehensive plans at a high level with minimal problems

Do you have any solutions for this? Basically getting the zip folder package from PRO to Codex better but you need to download it and send it to codex

- by [unknown](#) **&#x21C5; 1**
  <br/> [https://github.com/agentify-sh/desktop](https://github.com/agentify-sh/desktop)

- by [unknown](#) **&#x21C5; 1**
  <br/> once a week someone posts this. once a week.

- by [unknown](#) **&#x21C5; 1**
  <br/> Depending on your use case, I've found 2 ways to work it.

  1. A skill which bundles context (using repomix or similar) into a zip file + prompt for chatgpt web ui, and hands back an implementation or /goal contract
  2. Local codex opens an outbound secure tunnel to OpenAI, so no public port is exposed on our network. ChatGPT reaches the local MCP through that tunnel; the MCP can inspect the workspace, while actual changes are handed to Codex through a separate private controller.
