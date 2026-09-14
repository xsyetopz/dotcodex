#Have agent respect the AGENTS.md [Visit](https://www.reddit.com/r/codex/comments/1wdx5jx/have_agent_respect_the_agentsmd/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Pzixel](https://www.reddit.com/user/Pzixel/)
### **Vote:** 6
---
How do *you* ensure the agent actually respect the AGENTS file? I have a pretty good MD file that reflects values, approaches and techniques required for my projects. However more and more often when I do postmortem with my agents analysing poor execution, poor result or anything going sideways I see it saying "I should've done X,Y,Z. Your AGENTS.md file actually requires that, but I ignored it sorry". I have this on daily basis now and I'm not quite sure what to do. I could have an extra agent just constantly-re-reading the file and validaitng all work against it, but I burn through my x20 subscription quickly enough as it is. I would save some from the fact that some issues would be found early but in general I think it is more expensive.
Do you have this problem? How do you address it?
---
## Comments 25

- by [unknown](#) **&#x21C5; 8**
  <br/> Each step: launch a sub-agent to review changes against a/b/c. Agents are "lazy" and have a focus drift. So the best way is to have the fresh instance with a single purpose: push back.

- by [unknown](#) **&#x21C5; 0**
  <br/> Well that is exactly my concern: isn't sub-agent that checks every step super expensive? The rules are pretty abstract such as "Encode stable nontrivial invariants once in focused types where invalid input can enter; trust them downstream. Defend only against supported inputs, documented dependency failures, or concrete failure modes." - I don't think Luna is good enough to understand if invariants are trivial or not and if this rule applies or not. The reviewer should be at least as smart as the model implementing the changes - for my codebase anything below sol high is not working.

- by [unknown](#) **&#x21C5; 2**
  <br/> It is cheaper but yes, either you do the job every time, or sub agent. If you have list of detailed rules, you can use cheaper reasoning.

But overall, you still have to assess and intervene. Its just amount of issues to address/rework is changing.

Ps I dont trust Luna. Had some traumatizing experience :(

- by [unknown](#) **&#x21C5; 1**
  <br/> hooks ensure consistency

- by [unknown](#) **&#x21C5; 2**
  <br/> Use skill to keep its behavior consistent

- by [unknown](#) **&#x21C5; 2**
  <br/> What is the difference? It's not really the skill in my mind. I mean it *is*, but I only use it for coding, and this is "writing good code" skill. I thought AGENTS.md is exactly "skill that is preloaded by default in all agents when the context starts". What a dedicated skill would change?

- by [unknown](#) **&#x21C5; 2**
  <br/> If the file is too large, the agent can’t keep the entire contents of the file in its context. Ask your agent whether that’s happening and how to remediate it.

- by [unknown](#) **&#x21C5; 0**
  <br/> My current file is 16Kb. about 3rd for code, 3rd for tests and 3rd for misc. I tried to compress it without losing compliance force as much as I could. It seems like a large but reasonable size for the file.

- by [unknown](#) **&#x21C5; 2**
  <br/> no wonder it isn't following the AGENTS.md if it's [8000](https://i.imgur.com/yxhQfaQ.png) words. You need to put the bare essential information in AGENTS.md since EVERY chat reads it, I just put an overview of the architecture, how to build, and other basic things. Under 1000 words. You can also do hierarchical AGENTS.md in subfolders that just describe that folder to subagents to save them having to dissect everything in it to understand it.

For other stuff you need to use skills or subagents so it actively does the checks you're asking for. There's a big difference between 'do the thing' hidden in an 8000 word file in the beginning of the chat and 'you must use this skill to do the thing and tell me that you did it".

Skills also have the benefit of having short descriptions until they're actually loaded for usage so they don't take up extra space for chats or subagents that it isn't relevant to

- by [unknown](#) **&#x21C5; 1**
  <br/> But it *is* bare essential info. It explains: how to write code, how to test it and how to hand it over when done. Since I'm using it exclusively for software development it should know this always, hence the issues. Also 16KB is twice less than the limit for the file, so I thought it's reasonable, why would they allow 32kb files and then ask us to only use few words? [https://gist.github.com/Pzixel/461c81e6bfff05d4035da9b5b5ba7333](https://gist.github.com/Pzixel/461c81e6bfff05d4035da9b5b5ba7333) this is my current AGENTS.md, and I'm okay with splitting it into skills or whatnow, but it's unclear to me how would it help if I still need agent to know those rules and follow them.

- by [unknown](#) **&#x21C5; 2**
  <br/> Alright I'm sorry to pass this off with an AI response but I thought it was interesting and what I'd expect for refining a kind of monolithic AGENTS.md (and it's 4am for me, otherwise I'd dig into it more myself). Here's GPT Pro's response for how to refactor it, based on OpenAI's new guidance that they released today:

[https://chatgpt.com/share/6aa52c4b-1c70-83e8-b67f-3fdd6f4bc11c](https://chatgpt.com/share/6aa52c4b-1c70-83e8-b67f-3fdd6f4bc11c)

Also sorry if my comment came off as rude, 8000 words sounded outrageous in my head but it seemed a lot more reasonable actually looking at it

- by [unknown](#) **&#x21C5; 1**
  <br/> Thank you. That is actually helpful. It does however list my point plainly in this response when I ask about how do I apply it:


      For your workflow, I would now retain the integrated AGENTS.md


    And my workflow is exactly that - doing development tasks. Please come back after you get some sleep. See [https://chatgpt.com/share/6aa53065-0be0-83ed-b126-ba319a326e1b](https://chatgpt.com/share/6aa53065-0be0-83ed-b126-ba319a326e1b) for details

- by [unknown](#) **&#x21C5; 2**
  <br/> But does every chat use every task, from reviewing designs to writing tests to delivery? That might also be part of the issue, if your chats are running long and compacting repeatedly then you're losing your AGENTS.md a little bit every time. With things broken up with handoffs, each session can focus on what it needs to do rather than trying to keep the entire workflow from beginning to end in mind

Actually, come to think of it, skills are still helpful in that workflow because they get loaded when they're needed, so it frees context of earlier tasks and is fresh when it's actually on that step

- by [unknown](#) **&#x21C5; 1**
  <br/> Hmm, I thought it reloads the entire AGENTS.md after compaction? That could be the reason it doesn't work if it doesn't do that.

- by [unknown](#) **&#x21C5; 1**
  <br/> Do you have examples of what is being ignored specifically?

I have found that grounding it with deterministic tests or tools works quite well. That means encoding my expectations through checkstyle, archunit, semgrep, spotless or whatever equivalent for the given language. Sometimes even having codex write a custom linter.

Interestingly, I did catch a LLM trying to weaken the rules to make the tests pass, but that did happen for tests that are binary (ex: checkstyle where you just enable specific tests you want) and never in tests that output a statement about how this is bad.

- by [unknown](#) **&#x21C5; 1**
  <br/> Well for instance that is a rule that agent broke recently:


      Before commit/handoff/release/completion claims, obtain fresh, sufficient, outcome-proportionate evidence for the actual target; disclose material gaps. Each gate needs its own evidence; agent-written plans cannot remove it.


    agent handed the changes without making any actual validation.

- by [unknown](#) **&#x21C5; 2**
  <br/> I think the expectation that a single agent will do everything is wrong for multiple reasons. As context is limited the agent will drift. I have several subagents being coordinated by a single agent, one is responsible for testing, one for docs, etc. Look at the agents as your team - you will hire a single guy, the output will be garbage. You hire a team with manager, UX dev, tester, DB dev, etc and you will get good results.

- by [unknown](#) **&#x21C5; 1**
  <br/> Besides what was said in the other response, my go to move here would be to have something tangible that can test and fail if necessary. That may mean validating a specific format for commits, ADRs, etc.

- by [unknown](#) **&#x21C5; 1**
  <br/> I have a rather complex web of documents that starts with the agents file and branches out to other ones. And they're all like, if this situation is happening, or you're working on this area of the program, then look at this document for information about it, and then that file might have more look at this file stuff, and usually they have to go through these webs that help it find relevant stuff fast, and it seems to keep them from reading tons of unrelated stuff to find what they need.

And what I had one of the agents do was, I would choose one of the really smart ones. I think I used Terra Extra High, but Sol medium would be good for it too. Is I had it create situations where it made a lot of tests to make sure that the sort of pointing and the rules actually get triggered at the right times. It would find cases the rules weren't triggering and refine them until they did. Ideally you get it to do that with weaker subagents being tested so that dumber ones also are being proven to follow the rules. They seem to find the right stuff the majority of the time. Probably could have branched out to skills too, but it seems to be working for me.

Also this was really helpful to get it to report what it's doing so I can see what it's hitting to make decisions (I have this the global agents type file and not in individual projects):

##When skills are used, end with:

### Skills used:

- **<skill name>** — <why>

- **<skill name>** — <why>

Otherwise:

### Skills used:

- **none**

##When project documentation or text files (such as `.md` and `.txt`) materially inform implementation decisions, end with:

### Docs used:

- **<filename>**

- **<filename>**

Otherwise:

### Docs used:

- **none**

- by [unknown](#) **&#x21C5; 1**
  <br/> Other than what others have said here about it's size. Make sure that it is placed on the root level of your project too.

- by [unknown](#) **&#x21C5; 1**
  <br/> Keep your agent file as thin as possible.

Keep your sessions short, a long running agent may drop rules from context to make room for other assets.

Move as much into skills/scripts/tools as you can.

Skills are SOPs - this is how to do a task.Scripts are LAW - when the agent calls the script, it's not following guidance, there is nothing to forget (except calling the script itself)

This makes the work more deterministic and predictable.

- by [unknown](#) **&#x21C5; 1**
  <br/> Check if AGENTS.md files (global and repo's) and skills override each other. And ask for an eval.

- by [unknown](#) **&#x21C5; 0**
  <br/> Have your agent review it (including skills) so that it can audit if it is followable, discoverable, and consistent.

- by [unknown](#) **&#x21C5; 0**
  <br/> For a rule like that, I'd turn completion into an artifact, not a reminder: require the agent to update a small handoff file with the exact test command and fresh result before it can claim done. Then review that file rather than paying a second strong model to reread the whole diff.

I'm Gijs, and I built markjason.sh for this on macOS: external edits to that handoff file appear immediately, then you explicitly Keep or Revert them. It won't enforce the rule, but it makes the human checkpoint cheap.

- by [unknown](#) **&#x21C5; -1**
  <br/> Idk if it's just placebo or actually effective, But I make sure my individual project folder has a .codex folder with a config.toml file in it with additional instructions. It seems to help.
