#Astra for specs, luna for coding - is this just reddit bullshit? Is anyone really using this? [Visit](https://www.reddit.com/r/codex/comments/1wdskmy/astra_for_specs_luna_for_coding_is_this_just/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [AdventurousProblem89](https://www.reddit.com/user/AdventurousProblem89/)
### **Vote:** 30
---
i keep seeing cool people from internet mentioning this workflow: astra does the planning/spec, luna/tera implements it blablabla and everyone is happy and brooo it uses like 10x less and all.
sounds smart, but is this actually working? tbh i haven't managed to make it work that well myself.
some people say they use 2 seperate codex sessions, one for planning and one for coding. that kinda works (maybe, it kinda looks like slightly less usage with a lot of manual work), but with multiple projects it becomes a complete mess pretty fast (like i work on 2-3 projects and with 3-4 sessions per project it will be a nightmare) )))
some say they just let astra spin up luna as a subagent, review the code, send it back for fixes, repeat. in theory this sounds way better, but it kinda does not work and ends up using more. or is it just me doing it wrong?
can you please please please share how you are doing this? is there a way that really works or are all these just the crypto bros switching to ai jidis?
---
## Comments 130

- by [unknown](#) **&#x21C5; 19**
  <br/> My thinking is that if it really was a recommended usecase, then openAI would advertise it more as such. From what I understand all we have is anecdotal evidence of people trying it, I've never seen anyone actually benchmark it.

- by [unknown](#) **&#x21C5; 5**
  <br/> You can benchmark it locally yourself if you want to and you probably should do it vs your workflow. Here are my results from my local Pi harness where I run Astra low as the orchestrator and Luna low as the worker. Terra high does code review and there are some specialist roles that get called upon if needed. I should probably benchmark the Sol high vs Astra low for the non orchestrator roles but it doesn't matter much to me.

Your benchmarks favor lean orchestration: Astra low as lead, fewer preparatory stages, and low-effort workers for bounded tasks.
 Higher effort did not improve measured correctness in these tests.                                                                                             
                                                                                                                                                                                                                                                                                                 
- Astra low vs Sol high, simulated orchestration: Both reached the intended outcomes in every trajectory, without critical policy violations. Astra used 60.6% less time and 16.9% fewer processed tokens. The raw score difference was confounded, not a reliable quality win.                 
 
- Minimal vs configured coding pipeline: Both passed 6/6 trials, using the same Terra-high worker. The minimal pipeline used 37.9% less active time, 62.5% fewer tokens, and 33.2% lower estimated cost. This compared whole pipeline configurations, not reconnaissance alone.                 
 
- Luna worker effort: All 18 low/medium/high trials passed. Low had the fastest median, 38 seconds, versus medium’s 71 and high’s 100. One transport stall pushed low’s mean to 231 seconds; it must not be excluded from the primary result.                                                   
 
- Astra → Luna autosave test:Low and max workers all passed 10/10 behavioral tests. Low averaged 42 seconds versus 529 seconds, or 12.7× faster. One low run failed reporting acceptance despite passing functionality.  

My agent orchestration setup:                                                                                                                                                                                                                                                                 

LEAD                                                                                                                                                                                                                                                                                          
Astra (low): scope, decisions, delegation, final synthesis.                                                                                                                                                                                                                                   

IMPLEMENTATION                                                                                                                                                                                                                                                                                
Luna (low): default coding worker.                                                                                                                                                                                                                                                            
Terra (high): escalation when the worker demonstrably struggles.                                                                                                                                                                                                                              
One writer per worktree.                                                                                                                                                                                                                                                                      

EVIDENCE COLLECTION - ALL LUNA (MEDIUM)                                                                                                                                                                                                                                                       
Scout: local codebase reconnaissance.                                                                                                                                                                                                                                                         
Context builder: evidence, constraints, validation points.                                                                                                                                                                                                                                    
Researcher: public-web research.                                                                                                                                                                                                                                                              
GitHub collector: reads through authenticated GitHub CLI.                                                                                                                                                                                                                                     
Linear collector: tickets and project context.                                                                                                                                                                                                                                                
Supabase collector: database metadata.                                                                                                                                                                                                                                                        

PLANNING AND OVERSIGHT - SOL (HIGH)                                                                                                                                                                                                                                                           
Planner: dedicated planning when needed; otherwise the lead plans.                                                                                                                                                                                                                            
Oracle: resolves uncertainty and checks consistency with earlier decisions.                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                 
REVIEW                                                                                                                                                                                                                                                                                        
General reviewer: Terra (high).                                                                                                                                                                                                                                                               
Baseline bug reviewer: Terra (high), finds bugs introduced by the diff.                                                                                                                                                                                                                       
Adjudicator: Sol (high), keeps, rejects, or deduplicates findings.                                                                                                                                                                                                                            
Specialist reviewer: Sol (high), checks security, API contracts, UI, tests, etc.                                                                                                                                                                                                              

DEFAULT FLOW                                                                                                                                                                                                                                                                                  
Astra low -> one Luna low worker -> required review.                                                                                                                                                                                                                                          

These are available roles, not mandatory stages for every task.

- by [unknown](#) **&#x21C5; 5**
  <br/> Check [https://deepswe.datacurve.ai](https://deepswe.datacurve.ai), Luna benefits enormously from higher efforts while Astra doesn’t really. Astra medium/low and Luna xhigh/max is a good combo.

- by [unknown](#) **&#x21C5; 2**
  <br/> They didn't test them in a real workflow where you have orchestrator, workers, reviewers, etc. My setup hand feeds Luna directions and has luna search for information. Luna never gets to be a decision maker so the lower efforts make sense with how I use them. I used to have Terra high do a lot of the worker roles but it turned out that Luna low worked just fine. It makes sense how they did their benchmarking but it doesn't actually represent how most people use these models and I think more people should backtest models in their setups.

Quick Gemini summary:


      
    The key details regarding their testing setup:


      **Single Standalone Harness:** Every model was run through `mini-swe-agent`, a model-agnostic harness that gives each AI model a single prompt and access to a standard `bash` tool to explore, edit, and test code.


    
      **No Specialized Role Prompting:** They intentionally did not construct multi-agent workflows, persona roles (e.g., "you are an orchestrator delegating sub-tasks"), or automated code reviewer loops in the benchmark infrastructure.


    
      **Evaluating Core Capabilities:** By holding the scaffolding completely flat, the benchmark aimed to measure each underlying model's raw native ability—such as self-driven exploration, instruction-following, and unprompted self-testing—rather than evaluating complex agent framework designs or multi-agent orchestration tricks.

- by [unknown](#) **&#x21C5; 1**
  <br/> yeah, this is what i was thinking too

- by [unknown](#) **&#x21C5; 11**
  <br/> So unless you're completely vibe coding, you always need a planning session before any feature to workout what exactly you need to be done and brainstorm and clarify with the agent what exactly you're expecting from the feature. Generally sol or astra handles this.

Then for the implementation, you don't need a slow agent to think when the design is already clear so luna comes here into play. I generally set luna with fast mode to grind this out in a fast pace in a very cheap way. You can also set sol or astra as an advisor with luna to fix any blockers luna faces.

- by [unknown](#) **&#x21C5; 3**
  <br/> luna doesn’t have fast mode i think tbh, turning on fast mode does nothing. btw how are you passing the plan to luna? do you keep a seperate luna session and paste/send (ask it to read) the plan there, or do you let astra/sol spawn luna as a subagent?

- by [unknown](#) **&#x21C5; 3**
  <br/> [](https://preview.redd.it/astra-for-specs-luna-for-coding-is-this-just-reddit-v0-fghk2isilyoh1.png?width=262&format=png&auto=webp&s=7b0929ba533a706aadac79893169aa47601aa7af)
      
    Luna absolutely has fast mode in Codex

- by [unknown](#) **&#x21C5; 2**
  <br/> I have a built in harness that let's me automate session state and planning. But in general you can either hand it physically in the chat by copy pasting. Or generating an md file and handing that to the luna agent.

Here is my automation harness if you're interested. [link](https://github.com/ychamel/RepoResident)

- by [unknown](#) **&#x21C5; 1**
  <br/> why not ask the astra to use a subagent? isnt that the exact same? there should be a way for the subagent to work witout poluting the session, no?

- by [unknown](#) **&#x21C5; 3**
  <br/> This makes sense in theory, but from my experience astra burns usage while waiting for subagents to finish.

- by [unknown](#) **&#x21C5; 2**
  <br/> For something like that, I've steered Astra to check-in every 10 minutes instead of constantly.

(In my case, I was working on something else and missed that it was grabbing a repo that was multi-GBs large. And its regular check-in on the download devoured my usage until I steered it to check less often.)

- by [unknown](#) **&#x21C5; 1**
  <br/> How do you do that? I tried to instruct it to stop and wait for the agent to finish (since claude does that) but codex doesn't seem to have a builtin method to stop and wait for a callback

- by [unknown](#) **&#x21C5; 1**
  <br/> [](https://preview.redd.it/astra-for-specs-luna-for-coding-is-this-just-reddit-v0-zsdhbcllyyoh1.png?width=626&format=png&auto=webp&s=3f095ab1cf4461f27135ee582ff6cfc7e75fe395)
      
    For this in Codex/ChatGPT, if you send another message, it'll queue up just above the prompt area. On the right-side, if you select Steer, when the agent isn't knee deep in an unstoppable task, it'll glance over at the steer and think about it.

In my case, I gave it a time of 10 minutes since if the duration is indefinite, it'll still check regularly.

- by [unknown](#) **&#x21C5; 1**
  <br/> Because both Astra and Sol have a habit of just launching another Astra or Sol named Luna…. And asking for a subagent was an unsupported feature till recently.  At the moment they keep changing and nerfing jt too.  Stay away.

- by [unknown](#) **&#x21C5; 3**
  <br/> Exactly how do you do that?

- by [unknown](#) **&#x21C5; 2**
  <br/> this is the question

- by [unknown](#) **&#x21C5; 4**
  <br/> Would you give an idiot the plans to build a spaceship?

- by [unknown](#) **&#x21C5; 4**
  <br/> i don't build spaceships my friend, i'm more in shitty sas business :D

- by [unknown](#) **&#x21C5; 1**
  <br/> Luna is exceptionally smart...it just doesn't do a good job trying to manifest a plan out of thin air.  If Astra gives it a bounded plan, Luna is fantastic at implementing it.

- by [unknown](#) **&#x21C5; 2**
  <br/> are you using subagents? why nobady ansers this? is there some kind of conspiracy i don't know :D everyone says orchestration-orchestration-orchestration, nobody says how they do that so i can try and see if iit owrks or not. subagents clearly is not a good approach, it burns more usage + is slower

- by [unknown](#) **&#x21C5; 1**
  <br/> It's not that complicated, ask Astra to write the plan to a md file and start a Luna session and tell it to implement it

- by [unknown](#) **&#x21C5; 1**
  <br/> I've been trying it this way the past week. I  just ask Codex cli Terra to be the orchestrator and use Luna Max subagents for build but Sol for the plan and it actually works way better than expected. It's not as good as say fable to opus but I can basically run this forever on a plus plan. It's crazy cheap and is building what I need.

Definitely review with something stronger like terra for Luna's work.

Oh and codex cli is crap for orchestrating compared to others, but at this price I'll live with it.

- by [unknown](#) **&#x21C5; 1**
  <br/> [](https://preview.redd.it/astra-for-specs-luna-for-coding-is-this-just-reddit-v0-q1fyo317x3ph1.png?width=529&format=png&auto=webp&s=7435feaf4a4b589299008b641fccacb6485c09df)
      
    In the simplest terms: You define a workflow and tell the main model how to split work and which models to use under which circumstances, what they are supposed to do, allowed to do, what they are not allowed to do, etc.

The simples method is to write this in your [agents.md](http://agents.md) / [claude.md](http://claude.md), the next level is to make skills with these instructions, and then it's skills + hooks.

- by [unknown](#) **&#x21C5; 1**
  <br/> This depends heavily on the complexity of the task.

From my experience doing graphics programming, Luna Max struggled pretty badly. I gave it a detailed task involving a fairly substantial refactor of a custom WebGL renderer, specifically the long-distance spatial/volumetric media system.

Partway through, its changes broke the production WebGL path. It didn't realize that had happened, so it continued testing the game through the old fallback renderer and initially interpreted the resulting behaviour as part of the implementation rather than noticing the main renderer had failed.

To be fair, I've had much better results using Luna for bounded gameplay/system work. So I don't think "Astra plans, Luna codes" is a universal rule at all. For simpler implementation work Luna can be great, but for cross-cutting graphics/renderer work I'd much rather have Astra or Sol 5.6 doing the actual problem-solving too.

- by [rageling](https://www.reddit.com/user/rageling/) **&#x21C5; 3**
  <br/> The honest answer is it depends on your requirements and the type of project you're working on.

The astra to plan and luna max to code is a viable methodology and in my experience works well enough most of the times, but YMMW.

There have been occasions when Luna, despite having a plan from Astra, went completely off script and implemented things the plan didn't mention at all. It decided what was best even though I didn't ask for it.

I've also not experienced the Astra using up all usage in a single day issue either despite using it on xhigh for coding + tests + playwright, but again, YMMW.

Suffice to say, Sol High / Astra Med for planning and Luna Max for implementation is a good enough starting point. Adjust from there.

Beep boop [u/rageling](/user/rageling/)

- by [unknown](#) **&#x21C5; 1**
  <br/> but HOW do you do that? do you use subagents or you copy past plan from one session to another ? or just ask one agent to create specs md and ask other one to use it?

- by [unknown](#) **&#x21C5; 1**
  <br/> Depends on the size of the task. I generally keep my tasks small so that I can verify the output matches my standards.

Usually I switch into plan mode, create a plan, then explicitly tell Astra/Sol to use subagents on Luna at Max effort to implement the plan. Then when complete, the current session reviews the changes and fixes any drift.

At that point Codex will give the option to move out of plan mode and start actually working.

Just tell it to use subagents :)

- by [unknown](#) **&#x21C5; 1**
  <br/> but are you sure this is using less astra/sol models? i have a feeling that the subagents polute the session a lot, and i mean A LOT, eery time i try this i end up having my usage burned super fast, is this really working for you or you are jut taking theory?

- by [unknown](#) **&#x21C5; 1**
  <br/> It is working for me, but I have a variety of skills and tools to manage my context windows and usage. I also keep my tasks hyper focused on what I want done and never give the agent a broad ambiguous task i.e., reverse engineer this site and build a backend with identical frontend. continue

I haven't noticed the session being polluted a lot, but then I expressly avoid using a single session for multiple tasks. I'm almost always starting a new session.

There is no fixed one size fits all. You need to find what works for your use case.

- by [unknown](#) **&#x21C5; 3**
  <br/> For producing written content, Astra planning and Luna writing is actually good. I have found Astra’s writing to be terrible and confusing. Like, really bad—sentences without a subject, trailing prepositions, things Gemini flash or Claude sonnet would never do. Luna’s writing is natural and approachable for a lot less.

- by [unknown](#) **&#x21C5; 1**
  <br/> I agree about Astra's writing. I've found Sol-high to be much better on that front.

- by [unknown](#) **&#x21C5; 1**
  <br/> How would you get astra to plan and Luna to write? If astra has to tell Luna, it could just write that to a file and you can have Luna implement and skip the writing part since it would have to understand what astra said anyway

- by [unknown](#) **&#x21C5; 1**
  <br/> A short example is if you’re having Astra build a website, you could give it instructions not to write the content out long form but instead in each place there will be text >100 words (or whatever), ask it to leave a prompt for Luna to read and provide content.

Another example would be to have Astra build the structure and factual base of an online training course but have Luna write the test that the user reads.

Another example is a QA test system where Luna writes the instructions for a test user.

- by [unknown](#) **&#x21C5; 2**
  <br/> I plan the features, set up instruction set with 0 ambiguity (What tools/plugins will be used, how it will behave, what is the goal), i set boundaries, i give instruction set to astra, astra handles delegation and checks if the expected feature is working or not, then i do my own tests and give feedback and fix issues.

This is my workflow, so far its working as intended. You can babysit it all the way to finish with just luna workers and get more usage out of your plan if luna can solve your projects problems. Astra/sol just removes some of the babysitting.

- by [unknown](#) **&#x21C5; 1**
  <br/> do you use two seperate sessions or subagents ?

- by [unknown](#) **&#x21C5; 2**
  <br/> Planning session is done in different conversation(preferably web), once its done and set stone, i tell my sol agent to create instruction md that keeps ambiguity out so agents do not hallucinate features that does not exist.

I always keep my decisions as a whole context file, so when my orchestrator thinks if there is a ambiguity, it will first check my decision files and read my conversations, then if still cant decide what to do, it will ask my opinion. This is basically my decisionmaking flow how i handle it so far.

- by [unknown](#) **&#x21C5; 1**
  <br/> Why on different sessions and why preferably on web?

- by [unknown](#) **&#x21C5; 1**
  <br/> Different sessions so you don't end up adding too much context inside the agent that is going to do the working, it will carry over while working and cause you more usage if you keep them on the agent. Its always good to start a fresh session when you are doing new set of tasks.

Preferably web because you would not want to use your codex usage on planning (except if you want to access the best models for it, so far sol seems to be enough for that)

- by [unknown](#) **&#x21C5; 2**
  <br/> Been using sol within chatgpt for planning and specs. Have it divide up work with individual plan documents, then I pass off to another agent like that. Often luna high/xhigh but not always, sometimes I use other other high volume type models like been getting decent results out of muse spark 1.3 now (though 1.2 was pretty bad)

Have Luna do the grunt work with cheap tokens, then sol/astra review. If on review the bigger model is noting lots of issues, better of using it directly. And for some things you’d expect Luna to just be bad at, like I don’t trust it much with UI. I’m not saying Luna will tackle every problem but if you have a better model break it down to smaller pieces it can handle the majority of the actual coding for the sorts of things I work on

Here’s an example from a repo I was having re-write from python to rust, this directory is the planning docs for the changeover [https://github.com/eggstack/eggpool/tree/main/migration-rs](https://github.com/eggstack/eggpool/tree/main/migration-rs). All the rust code is written by Luna

Edit: deleted the planning docs since doing cleanup, here’s earlier commit with them still [https://github.com/eggstack/eggpool/tree/4a32e015fdad12897b55af9da9619bcbc7a8fb86/migration-rs](https://github.com/eggstack/eggpool/tree/4a32e015fdad12897b55af9da9619bcbc7a8fb86/migration-rs)

- by [unknown](#) **&#x21C5; 2**
  <br/> I started with this type of workflow, but the back and forth between subagents took forever and ended up costing a lot of tokens anyway on the larger models. What I finally landed on was using Luna to search the codebase and put together a list of files that would be important for the feature.

Searching doesn't require a smart model and Luna does a good job with this task. The subagent reply usually has a table of files with line numbers and an explanation of what the code is and why it's relevant to this feature.

This works out incredibly well. It keeps garbage out of the context window and only has relevant code. All the searching tool calls are gone from the expensive agent. I track token costs per day based on API rates, and now I use about 1/10th the cost that I used to spend. Seems to be a little slower than not using subagents, but not by that much since Luna is faster.

- by [unknown](#) **&#x21C5; 1**
  <br/> Are these subagents or separate sessions and you just copy past the responses?

- by [unknown](#) **&#x21C5; 1**
  <br/> Subagents with a new context window (not inherited). I don't think I could stand copying and pasting responses like that.

- by [unknown](#) **&#x21C5; 1**
  <br/> But the problem with the subagents isnthat the main session polls the context from the subagents every 30 seconds and it ends up using much more tokens on the main model

- by [unknown](#) **&#x21C5; 1**
  <br/> I'm sure it wastes a few tokens doing that, but it's way less than pulling in a single incorrect file. Most of my tasks used to end close to the 270k token limit. Now they're more like 70k when the same size task finishes.

Often the main agent goes off and does something else completely while the subagent is working. Usually it's looking at git history. And the subagent is usually done in less than 2 minutes anyway.

- by [unknown](#) **&#x21C5; 2**
  <br/> I pumped this flow so hard for the last week.I used astra medium using Luna sub agents. It would co-ordinate 3 at a time.

The experience was odd to say the least, astra made for a relatively good manager and I was able to go hands off.But I’m not sure hands off was a good thing, it worked for hours and hours and hours building features where if I was using opus it worked maximum for a few hours at a time then come back to me and I could keep track of some of the nuance that was happening.I didn’t feel like I could do that here and I really wasn’t sure when it was all said and done that it actually produced anything of value.I mean it did successfully introduce an additional model provider (OpenAI) into my legal contract review app but it seemed to take far long than necessary and write way more lines of code than should have been needed.

- by [unknown](#) **&#x21C5; 2**
  <br/> Yes I use this. although swap sol for astra because do I *really* need astra? Seems a bit overkill especially when I write a fairly robust prompt with a lot of detail and instructions . Sol is totally capable of breaking it down and spawning the subagents to get the work done.

- by [unknown](#) **&#x21C5; 1**
  <br/> Have you read the OpenAI prompting docs?

- by [unknown](#) **&#x21C5; 1**
  <br/> no )) will do

- by [unknown](#) **&#x21C5; 1**
  <br/> Well, what does it say?

- by [unknown](#) **&#x21C5; 1**
  <br/> I always tell myself I will try this but always think I need the best,  so whenever I code I'm either on the latest model on high or extra high...I used to love 5.6 sol xhigh but now with astra I never use it for coding. I've also heard astra light is more capable than sol extra high and costs less 🤷‍♂️

- by [unknown](#) **&#x21C5; 2**
  <br/> If you make astra just focus on planning and decisionmaking, maybe, if you set up orchestration just like sol, it eats tokens like crazy. Just by printing "Im doing this right now" eats a lot of usage.

- by [unknown](#) **&#x21C5; 1**
  <br/> how do you do orchestration? i mean the exact floe? do you ask astra to creat plan, then you copy paste it to seperate session?

- by [unknown](#) **&#x21C5; 1**
  <br/> You plan it on a seperate conversation, you get instructions, you need to set up a orchestration workflow, or add it inside the instruction (adding it to instruction will add input token debt if you do not make it permanent), then it will delegate work to subagents to do the exploration/testing/implementing delegation. You can find lots of workflow guides

One of the workflow that i can recommend:[https://github.com/viettran-edgeAI/codex_workflow](https://github.com/viettran-edgeAI/codex_workflow)

You can give this to your chat agent and ask it to explain to you how it works

- by [unknown](#) **&#x21C5; 1**
  <br/> I used orca with codex and claude

- by [unknown](#) **&#x21C5; 1**
  <br/> i do something similar as well but i always have two sessions one in luna other astra

- by [unknown](#) **&#x21C5; 1**
  <br/> Its your choice, Quality or save your weekly limit- Save Weekly Limit : All luna max (orchestration , worker, fixer , reviewer)- Quality : All Sol or Astra... (orchestration , worker, fixer , reviewer)

- by [unknown](#) **&#x21C5; 1**
  <br/> Yes i was using sol + 3 Luna

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra max to do “planning”

Ds v4.1 to implement

Astra max to review

- by [unknown](#) **&#x21C5; 1**
  <br/> Yes, I use it. Yes, it works.

Main chat is Sol, executors are lunas trough defined subagents (luna high and xhigh). It works fine, but a bit slow. I'm on 20$ sub tough, so it's fine by me. If I need more intelligence I tell Sol to debate with Astra.

I've checked multiple times and so far sub-agents work. Luna is very cheap so I can do stuff on 20$ sub.

- by [unknown](#) **&#x21C5; 1**
  <br/> so you are using two separate chats/sessions ?

- by [unknown](#) **&#x21C5; 1**
  <br/> For planning yes, I use Matt Pococks skill set. The result is requirements doc and tickets. There's no point sitting in the same chat.

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra xHigh-Max for planning, Sol medium for implementation.

- by [unknown](#) **&#x21C5; 1**
  <br/> Kinda does not work? Great let me help diagnose with that statement. Very helpful

- by [unknown](#) **&#x21C5; 1**
  <br/> you ask it run subagents, it ends up burning more usage and it takes longer to finish, codex does not disclose how much each message costed me so i can not be 100$ sure, but this is "kinda" what i feel )))

- by [unknown](#) **&#x21C5; 1**
  <br/> Luna xhigh/max is a very capable model **if** it has a clear goal and it can validate how well it's doing.

Even if the implementation is large and complex, it will do just fine as long as it can measure and verify that it did a good job. It won't give up until it does.

However, when something is ambiguous, requires taste or deals with unknowns, it will fail quickly.

- by [unknown](#) **&#x21C5; 1**
  <br/> I use Sol for planning, Luna as agent who calls local Qwen 3.8 27b as sub-agent to do all the coding. Luna reviews and approves. I have 2 x $20 sub & lasts me all week without even getting close.

- by [unknown](#) **&#x21C5; 1**
  <br/> so the sol starts the luna agnent and luna calls other subagents ? how do yo ustart the luna agnet? what do i do for it to start for me as well? i have a feeling that the subagents are poluting the sessoin context, are you sure they are isolated?

- by [unknown](#) **&#x21C5; 1**
  <br/> I plan/analyze using Sol who write a detailed spec. Luna manages implementation of the plan by immediately calling qwen to do work locally by passing it the prompt. Luna reviews what qwen passes back & makes corrections. Sol planning + Luna reviewing is next to nothing, real grunt work and token burn is done by Qwen.

Sometimes I'll skip SOL and just use Luna as planner which is wicked fast and does a great job scoping and managing medium-sized tasks. Rule for me is use SOL only when absolutely necessary.

- by [unknown](#) **&#x21C5; 1**
  <br/> Using github with the codex integration. Chatgpt very high reasoning for design and prompt design and asking luna to execute is a really Nice workflow for project design and execution

- by [unknown](#) **&#x21C5; 1**
  <br/> but how do i pass the specs to the cheaper model?

- by [unknown](#) **&#x21C5; 1**
  <br/> You can ask the lower model to read the detailed issue as a prompt. You can be super specific on the goal of the issue and give some proof of success before declaring completion

- by [unknown](#) **&#x21C5; 1**
  <br/> For my amateurish use, Luna xhigh is more than enough for almost everything. If I see it struggle, then I try Astra.

- by [unknown](#) **&#x21C5; 1**
  <br/> yeah, luna is great model, i do a lot with it as well

- by [Substantial-Wonder-2](https://www.reddit.com/user/Substantial-Wonder-2/) **&#x21C5; 1**
  <br/> I actually do that and results are being good so far. I plan on Astra low and have stated to write it on [PLAN.md](http://PLAN.md) as detailed as possible and even to tell what code to write, edit or delete for mid/difficult tasks then use Luna xHigh. I'm on Pro x5, spend 1 or 2% on planning and less than 1% on implementing. No subagents.

- by [Substantial-Wonder-2](https://www.reddit.com/user/Substantial-Wonder-2/) **&#x21C5; 2**
  <br/> thank for the detailed answer, it’s very rare these days to get straight answers from people who actually use it )))

so you call luna in other sessions? this is what was working for me as well, but having this automated and not requiring me to switch between contexts/tabs would be really nice.

- by [Substantial-Wonder-2](https://www.reddit.com/user/Substantial-Wonder-2/) **&#x21C5; 1**
  <br/> I do everything in the same session but I saw a guy's answer saying he does the implementation in another session and asked why. Idk what the advantage is. I do know that changing thinking effort or model in the same session is bad somehow, maybe that's the reason.

- by [Substantial-Wonder-2](https://www.reddit.com/user/Substantial-Wonder-2/) **&#x21C5; 3**
  <br/> oh, you switch the model in the sessoin? i think this is very expensive to do since it reduces the cached tokens, it is better to have seccond session i think

- by [Substantial-Wonder-2](https://www.reddit.com/user/Substantial-Wonder-2/) **&#x21C5; 1**
  <br/> Yeah, I'll try that next time. And even on web as [u/Substantial-Wonder-2](/user/Substantial-Wonder-2/) suggested below

- by [unknown](#) **&#x21C5; 1**
  <br/> そもそもluna安くした時に出た話だっけ

- by [unknown](#) **&#x21C5; 2**
  <br/> good point )))

- by [unknown](#) **&#x21C5; 1**
  <br/> I would've assumed it'd be the other way around? Luna for broad overview & design work, Astra for coding.

For the past 30+ years software developers have tried to create all manner of fancy design processes in order to make coding a mostly mindless task of just implementing the spec. It *never* works out that way. The devil is in the details, so to speak. The real challenge lies in the weeds - in the unforeseen edge cases, not in the bird's-eye-view architecture. A smart model will find better ways to handle those details.

*You* are the developer. You get the final say regarding any overarching designs (and presumably you know what you're doing), hence Luna is plenty adequate for helping you in that brainstorming phase.

- by [unknown](#) **&#x21C5; 1**
  <br/> Ya IDK what you are talking about man. I am on the 5X plan.

Using one Luna Max agent to do all work will barely move the usage percentage but it is only one small Luna agent. It is very good but it can only do so much by itself and can be slow and miss things when throwing big plans at it.

If I use just Sol or Terra to do the same work it will get it done far better but eat away the Usage percentage pretty consistently.

Now if you use Astra on Low to do a quick analysis of you system and make a working plan for that part of it telling it you want to hand this off to Codex (which could mean any GPT you pick like Terra or Sol) and have it use sub agents with Luna Extra high reasoning to do the work while it supervises them and it does none of the work. This will usually eat a couple percentage to make the plan. Then you give that plan to say Terra medium and Terra will do it with Luna subagents and it basically uses I find somewhere in the middle of Usage as the two examples I gave up above. you get really really good work done for in the middle usage I find and have done this consistently there is no conspiracy just use it correctly.

(or do what I do and use GPT 6 Pro in the web browser to make plans to give to Terra with Sub agents and use no percentage at all making plans)

- by [unknown](#) **&#x21C5; 1**
  <br/> I’m pretty lazy so I’ve just been using Astra medium / Sol high for everything - I only spawn Luna for git ops and testing/verification.

Works pretty well. You still have to do it properly though.

- by [unknown](#) **&#x21C5; 1**
  <br/> I benchmarked it against my repos at work

Workflow was Plan with astra > luna xhigh for coding and astra to review vs astra everything.

It was 3.4x times cheaper until I had almost the same result. While being 2 times slower.

Its not worth it that way.

What I actually ended up with, was a realtime pipeline with luna low and local tts/stt models, where I discuss what I want to build and the architecture including prototypes. Then I hand it off to astra with all the details I gathered and let it run.That way I am confident enough about the architecture and the actual code thats being written.So the other way around as everyone else was suggesting how to use agents and on top you are way more in control and involved that way without feeling slow

- by [unknown](#) **&#x21C5; 1**
  <br/> I do all my chats with Sol-high. I authorize the Sol-high agent to spin up Luna-xhigh subagents where it may save on costs, or where a 2nd opinion from a different model could be useful. Sol-high orchestrates and reviews all the work.

Luna-xhigh is generally less innovative, less context-aware, less creative, and more terse in its writing. But it does perfectly well in a lot of well-specified technical implementation or brute-force search tasks, at a tiny fraction of the costs.

I've found this to be a very efficient and effective workflow, giving me what I need out of a Plus plan.

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra for specs luna for coding is a great way to lose time

- by [unknown](#) **&#x21C5; 1**
  <br/> You can make it work, but it won't save tokens. You can some times, but that means the project is simple enough so that you could've used less capable models in the first place.

- by [unknown](#) **&#x21C5; 1**
  <br/> I’m using sol orchestrator, calls astra for planning. Calls lunas to execute/build/code. Calls Astra if there are hard blockers. Manages the project. Works for me.

- by [unknown](#) **&#x21C5; 1**
  <br/> Luna makes too many mistakes, even on max. Don't bother with it. Sol for implementation, Astra for planning/high complexity engineering, and always on xhigh or max.

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra Medium for everything because codexradar is rating it as cheaper and higher IQ than majority of models and levels.

- by [unknown](#) **&#x21C5; 1**
  <br/> The more conventional a task is, the smaller the difference between the Astra and Luna models; the more unconventional a task is, the more dramatically the gap between them widens.

- by [unknown](#) **&#x21C5; 1**
  <br/> If you ask me, in its current state, it’s BS. Luna cannot properly follow through with the plan, they have nerfed it hard.

Plus plan user btw. Limits aside, the actual model is no longer good enough for even relatively not so complex parts of a project(I say no longer good, because for a period of time after the price drop of luna and more usage on even the plus plan the model was actually usable, got stuff done, but not anymore). Even when it does work, it often does a subpar job. Not recommended.

I’m just using Sol Medium or High for everything now. It’s the only model that doesn’t drain quota rapidly and can actually get work done properly.

Also, if you’re on any of the Pro plans, the experience with Luna may be different for you, they might be giving nerfed luna for plus(I speculate this as not many are complaining about this), can’t say. But on Plus at least, that workflow is not good.

For anyone wondering, the task was mainly UI modifications and backend wiring on a WordPress based project, stuff like making sure media uploads worked properly and the media picker actually functioned, also had Astra max do the planning, PRD, TRD and I prompted Luna in another session to only focus on that feature . Luna Max was horrible at it. It worked on that for nearly 2 hours and still couldn’t get the media picker running properly.

This wasn’t some insanely complex task either. It was mostly fixing existing functionality and wiring things together correctly, and I had similar issues with other parts of the project too, it works for hours and in the end still gives shitty results. Sol handled the same kind of work much more reliably.

- by [unknown](#) **&#x21C5; 1**
  <br/> It's just math, if Astra is like $10 per million upload $50 completion down and smaller amounts for cache and Luna lis like $1.20 per mil up $ 12 completion down and even lower cache then what would u prefer running 15b tokens through? If the planning is good why do u need the biggest newest expensive for production when you may just need something simple like a local model for production. It's kinda simple when u think about it.

- by [unknown](#) **&#x21C5; 1**
  <br/> the question is how do you do this plan/implement? are you using seperte sessions or using subagents?

- by [unknown](#) **&#x21C5; 1**
  <br/> Depends on ur coding agent and workflow. I use cline, it has a plan/act mode in the same ui and chat so all context is kept. Or if ur workflow is different program them in. It all depends on you. Cline allows seperare plan and action simply by having one assigned to plan the session and one to act so 2 dif models no effort just a setup with ur keys and initial settings. - I just took a stroll thru the rest of the comments and what a rabbit whole about nothing. Orchestration is something but the wrong word in this case as you are speaking about a single chat session with 2 seperate models to keep context which is better said as 2 sessions 2 context but then have 1 model plan with you and the 1 model execute the plan. That is not orchestration like everyone knows it with agents and sub agents. You can think of orchestration like a manager and workers but then everyone is executing or everyone is planning and its a small distinction you need to make and that's not ur question. If I were u I'd get of codex like the almighty thing, it's a simple coding agent like claude code, kilo code, cline, etc etc there are plenty and like all software they have differences. I personally don't know codex or care for it or claude. I know the harness does most of the orchestration. Work anyway and all you really need is to build a router and rules for routing. Agents are just workers and sub workers.  If Astra plans and is a manager sure Luna can be considered a worker and execute or you may have 25 different worker agents all with specialized skills so your not overloading a single model and 25 would execute as agents.

- by [unknown](#) **&#x21C5; 1**
  <br/> but if you switch the model (not reasoning but the actual model) it will invalidate the entire cache and will consume lot of fresh tokens on every change i think, in codex app it even shows a warning when you try to do that. this plan/act thing usually use the same model with high and low reasoning, no?

 
       [](https://preview.redd.it/astra-for-specs-luna-for-coding-is-this-just-reddit-v0-h9nw9zjb51ph1.png?width=1766&format=png&auto=webp&s=286e977c361ce7c71bd769ef5ecbfa54bf5ec020)

- by [unknown](#) **&#x21C5; 1**
  <br/> Try vs code, cline extention, setup api keys for model, set sol plan mode api key, Luna act mode api key, start chat in plan mode when planning complete ready for action click act and watch Luna work. It's that simple

- by [unknown](#) **&#x21C5; 1**
  <br/> Yes.

- by [unknown](#) **&#x21C5; 1**
  <br/> Tried, Luna's work needs so much correction by the bigger model that I don't see any benefit. I use sol medium for coding.
