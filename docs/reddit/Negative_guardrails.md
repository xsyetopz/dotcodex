#Negative guardrails [Visit](https://www.reddit.com/r/codex/comments/1wb9v8p/negative_guardrails/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [AvailableSecret5161](https://www.reddit.com/user/AvailableSecret5161/)
### **Vote:** 1
---
Can anyone share a good set of negative guardrails. I feel like with every new model release my stress levels keep on increasing on how to contain the model with negative instructions like testing, browser and tool usage. All my documentation has changed from what to do to what not to do 😑 models keep creating stupid tests running tests after every edit. Excessive skill/tool usage. Skill issue sigh!
---
## Comments 3

- by [unknown](#) **&#x21C5; 2**
  <br/> The shift from "what to do" to "what not to do" is the right one, you just have too much of it in prose. Two moves that took the stress out for me.

Keep the NOT list to ten lines and put it at the very top of the rules file, alone. Long negative lists in the middle of documentation get read as background. Ten lines at the top get read as rules.

Then take the three or four that have a cheap trigger and move them out of prose into a hook, so they stop depending on the model's mood. "Don't run the test suite unless I asked" is a command match, a pre-tool hook can refuse it. "No new processes beyond N" is a check on what's already running. "No new dependencies" is a match on install commands. Those never slip on a long session; the prose version does, which is why your stress goes up with every release.

What stays in prose is the judgement stuff, and that list gets short once the mechanical cases are hooks. The other guy's every-ten-calls "check your scope" hook is a good third layer for the middle.

- by [unknown](#) **&#x21C5; 1**
  <br/> I have a hook that triggers every 10 tool calls to tell Astra to check it's scope and chill

- by [unknown](#) **&#x21C5; 1**
  <br/> Yesterday I saw 20 node processes running during a implementation phase. My most used command these days is taskkill /F /IM node.exe
