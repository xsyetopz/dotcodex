#For plus users, Use Astra as an advisor! [Visit](https://www.reddit.com/r/codex/comments/1wag9vf/for_plus_users_use_astra_as_an_advisor/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [ychamel](https://www.reddit.com/user/ychamel/)
### **Vote:** 94
---
Astra is a really smart model, but you don't need it as your main running model except for tool use.(Ex: blender mcp)
For normal projects and coding design using Sol with Astra as an advisor. And for implementation, luna max with Astra as an advisor is one of the best and fastest way to implement your designs. Luna is mad fast, but run in circles a lot of the time. With astra as an advisor, it generally gets unblocks way faster and gets work done much faster with less hiccups.
---
## Comments 44

- by [unknown](#) **&#x21C5; 51**
  <br/> I set an astra boss man to whom I Instruct all my lunas to enquire when they have doubts. Then I leave only on instruction to astra sayin "Lunas are agents working for me so give them very summarized focused answers in aí language."

I then sit back and watch lunas build complex stuff then chatting to astra boss man asking for certain advice then being told what todo and completing the task in one shot

It’s amazing.

edit: minor punctuation

- by [unknown](#) **&#x21C5; 26**
  <br/> Curious how you set this up? Is it in agents.md or instructions in your first prompt?

- by [unknown](#) **&#x21C5; 4**
  <br/> following

- by [unknown](#) **&#x21C5; 12**
  <br/> You can basically tell them "Call on an independent read-only Astra advisor if you think you are hallucinating or you have gone excessive turns on the same problem without progress". They're smart and they figure it out.

I'm using ~0.3% of my weekly pro20x per hour so that should only be 6% of the $20 plan per hour if people mostly use Luna and use Astra just for advisement and planning too.Luna costs like nothing and is about as good as Opus Low/Medium. Just use it more like you say.

More in depth, how things are managed will be different per task. My 3D game client one is like this:

  - You: integration owner, task decomposition, evidence tracking, Git coordination, acceptance audits, and final reporting. (Luna Max)
  - Astra low: architectural advisement at startup, phase boundaries, or when evidence conflicts.
  - Luna xHigh + GLM-5.3-Flash High (`codex --profile zai`): parallel implementations and mechanical repair/merging. Each reviews the other's candidate and proposes whose is better. Independent Sol decides if they disagree. Luna does the accepted merge.
  - Independent Sol Medium: consequential code review and adjudication between candidates or proposed syntheses.

But I have significantly different setups for different tasks. People can... just ask Sol to devise these for them. That's the funniest thing I find that people don't understand with using AI. You can just ask the AI for advise on how to use it more efficiently and it'll do that just like you can ask it to do anything but somehow they never think of this.

- by [unknown](#) **&#x21C5; 7**
  <br/> Probably the shortest and best budget friendly advice

- by [unknown](#) **&#x21C5; 2**
  <br/> We need more details! Luna Max as agents? Aaaand how much effort for Astra?

- by [unknown](#) **&#x21C5; 12**
  <br/> Lunas are my main threads I talk to them directly. I open another thread for Astra. I do not use subagente or work trees. I just have threads better for control and codex allows for agents to talk and respond in between threads or chats. Reason being I can see them in my chats list and can intervene easily. Also grants me more granular control over what’s going on as well as effort setting etc.

Astra medium or low depending on task for me. Astra as a worker is unusable. I can’t afford how much it costs . But as an advisor and auditor will make the sum of your agents  do 5x less mistakes. One shotting is the key here. lunas are extremely effective  at focused scope. And I lost the fear I had to use then on complex sprints IF they are guided properly which is the key here

- by [unknown](#) **&#x21C5; 4**
  <br/> Thanks! Seems like a reasonable strategy for a cheap-ass like me

- by [unknown](#) **&#x21C5; 3**
  <br/> What's your agents.md look like, or how did you set it up? Whats your prompt?

- by [unknown](#) **&#x21C5; 1**
  <br/> followning

- by [unknown](#) **&#x21C5; 7**
  <br/> Has anyone tested Tokens usage and quality of the output comparing:

Talking to Astra and asking to use Luna subagents

Or

Talking to Luna and asking to use Astra as an advisor

Or some other mix of agents?

- by [unknown](#) **&#x21C5; 3**
  <br/> I use chat (Chatgpt project with the same GitHub repo) to chat, explain and design. Then Terra medium to orchestrate. It will hand simple tasks to Luna and very hard tasks to Astra low. Then final review and QC goes back to chat.

- by [unknown](#) **&#x21C5; 2**
  <br/> Integrating chat one way or another is key to stretching out usage. Chat can read and write to GitHub also

- by [unknown](#) **&#x21C5; 2**
  <br/> talking to astra light just to check in on the work of luna and given instructions that were previously discussed in the chat, doesn't seem to use up many tokens. I'm more comfortable talking to astra anyway

- by [unknown](#) **&#x21C5; 6**
  <br/> How I do:-> Astra medium for talk. I specifically says "NO CODE CHANGED". I talk, I ask, analysis. And than ask for instructions for AI model-> Luna MAX to implement

It works well.

Ofc I could have ask Astra to run subagents with Luna to implement -> I tried and this seems to eat usage like some cookie monster.

- by [unknown](#) **&#x21C5; 2**
  <br/> Try while running luna max to tell it to use astra as an advisor if it faces any complex issues. Should greatly improve the implementation, while being relatively cheaper on the usage.

- by [unknown](#) **&#x21C5; 2**
  <br/> Yep, Astra is really bad as an orchestrator I've found. I mean sure it gets things done quickly and effectively, and saves SOME over having Astra do it all, but it's not worth the tokens having it read the output of a lot of subagents.

Sol as an orchestrator, Luna implementing, Astra advising can be really good if you're on pro20x, but still probably not really usable on a Plus plan.

- by [unknown](#) **&#x21C5; 2**
  <br/> I actually added this to my initial prompt! The primary agent drafted the implementation plan first, then passed it off to Astra for review. Astra gave some excellent suggestions that smoothed out the whole workflow during implementation. The final output was way better than just running Terra by itself.

 
       [](https://preview.redd.it/for-plus-users-use-astra-as-an-advisor-v0-b6fz9usdr8oh1.png?width=694&format=png&auto=webp&s=e3544b3cf338ac44574440e45d5c5ad2a228cde5)
      
    Before implementing anything:

1. Inspect the current private `main` and relevant architecture.
2. Write a 
**thorough implementation plan**
 for Phases 21–22.
3. The plan must explain:
   - exactly 
**what**
 will change,
   - 
**why**
 each change is necessary,
   - 
**how**
 it will be implemented,
   - which files/components will be affected,
   - the state/lifecycle/data-flow implications,
   - Free vs Paid boundaries,
   - test strategy,
   - device-validation strategy,
   - failure/fallback behavior,
   - commit/PR structure.
4. Send that plan to an available 
**higher-IQ reviewer agent**
 for critical review before implementation.
5. Revise the plan based on that review.
6. If anything is unclear, underspecified, risky, or there are multiple plausible architectural options, explicitly ask the higher-IQ reviewer agent for guidance rather than guessing.
7. Only after the reviewed plan is solid, implement incrementally with TDD.
8. Complete verification, private commits, private PR review loops, merge, and branch cleanup.

Be thorough. Do not stop at a partial implementation.

- by [unknown](#) **&#x21C5; 2**
  <br/> Hello and thanks OP. So I should:

  1. Use the plan function
  2. in the plan, state to use Astra as advisor
  3. let Luna Max execute the plan?

- by [unknown](#) **&#x21C5; 2**
  <br/> I would like to but itd not available in chat, meaning i have to use work to access astra which burns usage like crazy making it unusable

- by [unknown](#) **&#x21C5; 2**
  <br/> It's not a finished model, they launched and are testing their paid-user base. The cost per token and limits on subscriptions are a joke, asking you to switch to Luna a slower and ignorant model for same price when they "just released" 1st AGI model.I'd rather have waited or reset everyday until they fix their stuff.

- by [unknown](#) **&#x21C5; 2**
  <br/> Any tips for that?

e.g. like consulting? Won't switching models degrade performance?

- by [unknown](#) **&#x21C5; 8**
  <br/> You don't manually switch model, just ask it to use Astra as an advisor. Codex already has a built-in tool to let running agent ask questions to another agent with a different model. So astra will be called as a subagent for specific cases to advise the running model what to do.

- by [unknown](#) **&#x21C5; 2**
  <br/> Very interesting. Is this better than using Astra and asking it to implement with Luna, or is it the same?

- by [unknown](#) **&#x21C5; 3**
  <br/> Its a lot more efficient to let luna run with a plan prepared, since all the files read will be done at luna's cost rather under Astra.

- by [unknown](#) **&#x21C5; 1**
  <br/> And which model do you use for planning?

- by [unknown](#) **&#x21C5; 2**
  <br/> I prefer sol high with astra advisor

- by [unknown](#) **&#x21C5; 1**
  <br/> Sol high with astra advisor

- by [unknown](#) **&#x21C5; 1**
  <br/> Thx!

- by [unknown](#) **&#x21C5; 1**
  <br/> I would expect there to be issues with astra being called on multiple times as an advisor for a bug or bottleneck and it over engineering a fix and blowing token use. does that happen much?

- by [unknown](#) **&#x21C5; 1**
  <br/> so i have blank chat with Sol High model. how you setup it initially to advise with Astra regarding for example design, implementation and so on. For example, you have a question to Astra, how you write it so in the chat Astra advisor will step in and answer your questions ? Thanks in advance mate !

- by [unknown](#) **&#x21C5; 2**
  <br/> Do you mean in chatgpt? I'm not sure how it operates in chat, in codex in general you specify when to use a certain model, so you can say use astra as an advisor and it will ask for advice when thinking about problems, you can also ask it to delegate to astra when the user asks a question, this will make it so it spawns an astra sub agent to answer your question. But in general use cases you want it to either support the model or takeover tasks that have 3d or tooling.

- by [unknown](#) **&#x21C5; 1**
  <br/> Yes, i meant codex. So you keep the model of the codex on Sol High, but ask it to use Astra sub agent as advisor ?

- by [unknown](#) **&#x21C5; 2**
  <br/> Exactly, and you can specify what effort level it uses

- by [unknown](#) **&#x21C5; 2**
  <br/> i dont even use astra at all. sol high and luna max/sol medium are enough for me. i just wish theyd get rid of the 5 hour limits again

- by [unknown](#) **&#x21C5; 1**
  <br/> well i do is astra adviser then opus executor  then luna for documentation

- by [unknown](#) **&#x21C5; 1**
  <br/> Is it just me or has luna been nerfed recently?  It fails to complete tasks it used to do a while ago, requires a lot more handholding as of now. And, of course luna is draining limits faster too. In its current situation id rather let Astra low do all the work,I give it focused problems to solve(that are still fairly complex), yes limits still drain fast, but work is done mostly right. Id say it’s barely usable with the 5h limits.

- by [unknown](#) **&#x21C5; 1**
  <br/> how do I even get an access to astra ain the first place? In both chatGPT and codex I have only 5.6 models...

- by [unknown](#) **&#x21C5; 1**
  <br/> I'm not sure, it should be available. Maybe they're rolling it slowly for some users? Also try to update codex to the latest version

- by [unknown](#) **&#x21C5; 1**
  <br/> I’m in $200 and still use this as orchestrator while implementations by Luna and Terra basis complexity

- by [unknown](#) **&#x21C5; 1**
  <br/> From my experience, I'd avoid using Astra as an orchestrator. It burns too much tokens for worst results. What I observed happening is that Astra keeps waiting for the subagents to complete, and this waiting period keeps on using the budget.

What I find much better is to have the worker model to be luna or terra or sol, and use astra for advising on solutions or call it to handle 3d or tool use.

- by [unknown](#) **&#x21C5; 1**
  <br/> I agree! I'm also on Plus, prompted it correctly and was able to chat with it quite a lot (not run out immediately like others).

- by [unknown](#) **&#x21C5; 1**
  <br/> Una pregunta sobre la comunicación entre los agentes la única manera es usar codex desktop? O es desde el terminal?

- by [unknown](#) **&#x21C5; 0**
  <br/> I just make it plan for antigravity and use gemini 3.8 amazing right now. And i have noticed that i used invite a friend and received credits, the astra usage is way way better there
