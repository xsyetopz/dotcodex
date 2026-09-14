#Lower quality work with Astra [Visit](https://www.reddit.com/r/codex/comments/1wbemum/lower_quality_work_with_astra/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Anatomisc](https://www.reddit.com/user/Anatomisc/)
### **Vote:** 12
---
Since switching from Sol to Astra my work has been lower quality. I am really envious at this point of people showcasing incredible things they've done with it. In my case I have been really having problems making Astra do things properly.
For my work it over engineered a test system and ate three resets so far during a goal. Instead of working on actually important problems it tried to construct a heavy verification system with Claude and Codex and sub agents to independently verify issues without notice outside of scope.
For my hobby as I am trying to build a game, for days and days on it is messing up simple references.
Fair, the reference is AI but the actual problem is composition. It just absolutely can not do composition like I ask it to no matter how hard I try.
I tried single attempts with references. I tried describing the visuals in text as well. I tried making it generate art assets one by one, approving them, then asking it to place it like that. I tried asking ChatGPT Pro to review and provide prompts, feedback, visuals to assist.
Absolutely nothing is working and I am getting really really bad results visually.
So does anyone have any suggestions to fix this? I feel like Astra right now is really low quality for me. Definitely a step down from Sol where I was at least able to achieve things even with requiring guidance and interjection.
My next idea is to not even ask it to generate anything. Cut it out of the image I share and inpaint then put it like that. It will look really AI but at this point I don't know how else to move on.
---
## Comments 2

- by [unknown](#) **&#x21C5; 2**
  <br/> One thought on the chapter gaming path with the numbers, why don't you do what most games do and generate your perfect background as an image in. ChatGpt (I assume thats the first slide) then generate the buttons separately and overlay them to get highlight and click effects.  The same could be done with what I assume is the start page.

On your over engineering front, Ive done exactly the same... had loads of resets, so made Astra do a very detailed plan, and it was... Then set it off to work and was too lazy to fully check everything and it ended up hyper focusing on smalls things then doing 4493858354 tests around it , that lead to deviations and checks of things that likely will never happen and burnt through multiple resets and didnt get a ton done.

I've had stiff words with it this morning.... Now its focus on the high value , make a difference things and not fine tuning and going off path with minute details I never asked (for now)

If/when I find a reliable system/agents/agents.md to reliably do this without me needing to read Astra its last rites.... Then I'll share :-)

- by [unknown](#) **&#x21C5; 1**
  <br/> I'd treat the over-engineering part as a small 2x2 ablation before adding more instructions.

Pick one small slice that previously sent Astra into the Claude + Codex + sub-agent verification detour. Reset to the same commit and run it four ways:

  1. current setup
  2. current setup + the scope prompt below
  3. optional skills/global instructions off, keeping only project-essential instructions
  4. clean setup + the same scope prompt

Keep Astra, the task and the acceptance check fixed. Compare reset/token burn, interventions, out-of-scope work and whether it actually passes.

**Prompt:**

Stay focused on the requested outcome and take the narrowest safe path that fully solves it.

Use the existing architecture, conventions, tools and tests where they fit. Add only the minimum support work required to complete the task correctly.

Do not turn tests, reviews, agents, tooling, planning, abstractions, refactors, cleanup, infrastructure or future-proofing into separate projects around the task.

Handle real and likely edge cases, not hypothetical future requirements.

If a material scope expansion is genuinely required, stop and ask first.

Done means the requested behavior works and the relevant checks pass.If the clean runs beat the full setup, I'd start suspecting an instruction/skill interaction rather than Astra alone. If the prompt helps in both environments, then the scope guardrail itself is doing useful work. If clean + prompt still drifts, Astra becomes the stronger suspect.

Then add skills back in halves or one by one until the behavior returns.
