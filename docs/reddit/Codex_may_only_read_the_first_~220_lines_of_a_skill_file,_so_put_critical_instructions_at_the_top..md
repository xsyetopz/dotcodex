#Codex may only read the first ~220 lines of a skill file, so put critical instructions at the top. [Visit](https://www.reddit.com/r/codex/comments/1t1rbqt/codex_may_only_read_the_first_220_lines_of_a/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [jixv](https://www.reddit.com/user/jixv/)
### **Vote:** 49
---
Now and then random preventable slop would appear and I couldn't understand why guardrails were being ineffective, even though skills were evidently loaded by the model.
A rough scan of the last 30 days worth of sessions led me to better understand why this kept happening.
The filter basically goes something like this, whenever `sed -n '1,{N}p' path/to/SKILL.md` is used by the model to load a skill (without following up with a second read of any form or shape), it would prove why it didn't follow the guardrails for that session.
The skills in question were structured in a way that would indicate the whole file should be read, I thought.
Model
First count
Min
Max
Avg
Median
P90
Cont
Full
5.4 high
994
180
320
227.8
220
260
19
19
5.4 medium
113
200
260
222.7
220
220
1
1
5.4 xhigh
144
80
260
224.4
220
260
9
17
5.4-mini high
51
180
260
227.1
220
260
4
5
5.5 high
1033
80
320
226.9
220
260
64
24
5.5 low
51
180
260
220.8
220
240
1
8
5.5 medium
198
180
260
225.3
220
260
4
7
5.5 xhigh
33
120
260
223.6
220
260
3
16
(cont = it read the rest of the file) (full = it used cat/grep to read the full file)
With this in mind I've changed how i keep my skills, and attempt to keep them below 220 lines - reason being that is what it by default would most often read.
Just leaving this here in case anyone would benefit from this.
EDIT: I forgot to mention that when referencing a skill through another skill for branching out depending on the context, it most often would skip reading the whole file of the referenced skill.
---
## Comments 12

- by [unknown](#) **&#x21C5; 15**
  <br/> Honestly if your skill files are more than 200 lines than you're doing something wrong anyway. The whole point of skills is to reduce the amount of tokens you use each run because it doesn't need to be rereading your whole codebase or searching things to find what you mean. If you're sticking entire code examples in there then you're just clogging up its context more. Keep skills very single purpose and very direct and focused.

- by [unknown](#) **&#x21C5; 5**
  <br/> I'm pretty sure I do many things wrong, that's for sure.

Sometimes you need quite verbose instructions, especially for orchestration agents that them selves do not do any form of coding, but delegate to sub agents, update progress and statuses in other systems. In such cases large skills can be just fine, as long as they are loaded in full.

So while I get your point about single purpose context bloating, and for which I agree when it comes to most tasks, not being aware that skills are not fully loaded was an unknown to me.

Example skill for these kind of things can be something like [https://github.com/openai/symphony/blob/main/.codex/skills/linear/SKILL.md](https://github.com/openai/symphony/blob/main/.codex/skills/linear/SKILL.md)

- by [unknown](#) **&#x21C5; 2**
  <br/> Yeah I don’t think I have a skill over maaaaybe 100 lines.

- by [unknown](#) **&#x21C5; 3**
  <br/> You should use Codex itself to refactor your skills if they're that long. Tell it to abide by the principles of progressive disclosure using subdirectories and reference documents, and then to rewrite the main skill.md file.

I routinely revisit and refactor all of my skills as they grow, and I also use it as an opportunity to prune dead content, things that are not relevant and contradictory stuff. If you run Codex through its own loop, you can actually get it to evaluate how good the skill is and iterate on it autonomously.

- by [unknown](#) **&#x21C5; 2**
  <br/> A other trick is, use reference files for example in a plan skill.You give rules for planing and a reference sheet as 1to1 plan sheet reference file, that they need to use for a new plan.mdSo you can make a very small skill in combination with a reference file

- by [unknown](#) **&#x21C5; 1**
  <br/> Hi I'm kinda new to this, can you expand on what you mean a bit?

- by [unknown](#) **&#x21C5; 2**
  <br/> It’s also worth mentioning that if you are throwing your whole unoptimised code base into it, it’s gonna burn significant amounts of tokens for file filtering and planning, I use a browser plugin that I build which takes the whole code base and generates.md files of the code base alongside a instructions.md file zip together. I upload that file into gpt and it generates an instructions .md file for codex. It’s super helpful if you work on contract work and have to deal with multiple code bases .

- by [unknown](#) **&#x21C5; 2**
  <br/> Codex decides how much to read given previous context written into the LLM.

Agent loops all items through the LLM, returns output and next best steps which it was trained on, then Codex, intercepts those commands via parsing and executes them

So, limiting traversal is important, and then determining if you need more information through LLM inference is actually beneficial to preserve available context window for actual data for work.

As [TheInkySquids](https://www.reddit.com/user/TheInkySquids/) said, if skills are over 200 likes and not using pointers or concise commands they are to long and guiding the Agent to narrow. From my research the Codex loop uses traversal as its main rout of discovery, which is also a good coding practice since God Modules are considered bad, and anything over 200+ lines seems to becoming a God Skill.

- by [unknown](#) **&#x21C5; 1**
  <br/> I'd say keep AGENTS.md to 200 lines max and skills should be much less than that.

- by [unknown](#) **&#x21C5; 0**
  <br/> You can have the same amount of tokens on 100 or 200 lines all depending on how you structure your skills. The point here is not amount of data but line count

- by [unknown](#) **&#x21C5; 1**
  <br/> Mine works for 700 lines for 5.4/5.5 medium. I manually check the quality of output by structure json all the time, use the same pattern for over 21 md files. They are good.  It depends on how well you structure your skill files. You may need to use progressive read instruction and make it more concise with multiple iteration. Also use hierarchical structure. With that being said, 150-220 instructions are the norm before degradation.

- by [unknown](#) **&#x21C5; 4**
  <br/> put this in codex.toml

[features]codex_hooks = true

[[hooks.PostToolUse]]matcher = "*"

[[hooks.PostToolUse.hooks]]type = "command"command = 'printf "%s\n" "{\"hookSpecificOutput\":{\"hookEventName\":\"PostToolUse\",\"additionalContext\":\"Make no mistakes\"}}"'timeout = 5
