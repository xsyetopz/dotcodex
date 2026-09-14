#If you are using Astra orchestration (Specially for plus), some findings so far. [Visit](https://www.reddit.com/r/codex/comments/1wbk5ff/if_you_are_using_astra_orchestration_specially/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Substantial-Wonder-2](https://www.reddit.com/user/Substantial-Wonder-2/)
### **Vote:** 6
---
So far, I'm using Plus subscription with Astra Light orchestration in mind. There are some improvements I have made. I'm using workflows similar to these (They are mostly specialized for my workflow);
[https://github.com/viettran-edgeAI/codex_workflow](https://github.com/viettran-edgeAI/codex_workflow)[https://github.com/donvito/codex-astra-luna-orchestrator](https://github.com/donvito/codex-astra-luna-orchestrator)
I have tried adding a persistent manager, who has sole responsibility is to take expensive token waste from astra which is spawning, and managing workers. Luna did not work, other tests were Terra and Sol, Astra could spawn Terra low, and Terra low can spawn Luna workers.
Astra's pure responsibility is reasoning. It will read your instructions, delegate tasks, hand them to the manager, and wait for the next decision. Its the brain.
Terra manager handles delegation from Astra, gets contracts, hands them over to the luna workers, and then occasionally checks them if they are working or not. When the workers are stuck, they are deviated from the task, some user or astra decision is required, it will ascalate to Worker -> Manager -> Brain.
Brain will decide the next move.
So far my findings are;
[](https://preview.redd.it/if-you-are-using-astra-orchestration-specially-for-plus-v0-eyi9e9wdlhoh1.png?width=931&format=png&auto=webp&s=58d72fc75f6876fc2dac41df7bc81d0f71605275)
Astra is still using 60 second wake ups to check terra, which is im planning to fix it next.
[](https://preview.redd.it/if-you-are-using-astra-orchestration-specially-for-plus-v0-hoofimlulhoh1.png?width=977&format=png&auto=webp&s=7a6dc774290b39bbae429dde9ff60f847650b304)
[](https://preview.redd.it/if-you-are-using-astra-orchestration-specially-for-plus-v0-3xk9lf2nmhoh1.png?width=908&format=png&auto=webp&s=864ea03869c0d08500359ab242b4f4b1d4f041e4)
[](https://preview.redd.it/if-you-are-using-astra-orchestration-specially-for-plus-v0-r5z7qbjqmhoh1.png?width=904&format=png&auto=webp&s=aca281554a5dc4791a47deb6eaded560439aaa48)
[](https://preview.redd.it/if-you-are-using-astra-orchestration-specially-for-plus-v0-0yjlp2osmhoh1.png?width=887&format=png&auto=webp&s=f5f665e327eb40b105cd14e56db9b11bd84a6aae)
[](https://preview.redd.it/if-you-are-using-astra-orchestration-specially-for-plus-v0-9jah874xmhoh1.png?width=876&format=png&auto=webp&s=e2ec27d450a80dc9bfd7eecff7a8d3e16b2eb64c)
Some improvement notes:
Even for informing the user during codex task, astra wakes up with large amounts of tokens which causes massive usage drop. Removing it completely, delegating the information to manager or another agent, only ask to give information during wake ups will improve usage. Similar thing can be done by /side chat. I will work on that
Agents md was fully redesigned with openai documentation, the tool descriptions and skills are moved away from agents md to proper places, the workers who use these tools are fed with the information they need to use the tools, astra does not read a huge agents md file. Agents md = 15kb -> 6 kb
Once astra only thinks and sleeps, this will make a huge usage optimization on usage, and actually make  astra light orchestration doable.
Adding a terra management layer adds more time. Astra -> Luna test was 67 seconds while Astra - Terra -> Luna was 110 seconds when benchmarked. Since this is not a "Faster but better" improvement, I think this is a good trade between more usage vs faster work. Luna is already slow enough.
---
## Comments 4

- by [unknown](#) **&#x21C5; 1**
  <br/> Nice, I'm doing something similar but Astra low does more of the orchestration instead of solely handing off to a different manager (20x plan). The "one-minute alarm clock" unfortunately seems like something that can't be fixed from what I can tell:

[https://www.reddit.com/r/codex/comments/1wbsw7j/astra_likes_to_tell_you_every_minute_its_waiting/](https://www.reddit.com/r/codex/comments/1wbsw7j/astra_likes_to_tell_you_every_minute_its_waiting/)

- by [unknown](#) **&#x21C5; 1**
  <br/> My manager does not handle orchestrator to worker task, manager only handles Astra - - - Manager - - - Worker bridge.

Terra can spawn luna agents, Luna cannot. Astra looking at workers every turn/60 seconds -> Astra wasting input tokens to check useless progress.

I took that away from Astra and gave it to Terra. So far Terra is doing exactly what its told. Terra doesn't think, terra doesnt decide. It just gets contract from astra, delivers it to workers, spawns them, does wait calls, checks if they are working, and then report back to astra. This is all what terra does currently.

Reason: Terra is hella cheap, even Terra Low can handle this, there is no thinking needed. It just does whats its told, not more. If luna was able to spawn luna agents, I would use it but only Terra can spawn agents under astra root.

- by [unknown](#) **&#x21C5; 1**
  <br/> But is this better than Luna xHigh alone or Luna Max alone? Damn I'm getting so confused 😰

- by [unknown](#) **&#x21C5; 1**
  <br/> If you are min maxing, yes you can do luna xhigh/max yourself, but you should not give the whole task but give small but specific tasks so they do not get confused, or deviate from task. Orchestration is for long tasks, you give a long list to do, and orchestrator will handle all of them. Its like automation for your work. You trade a bit usage to automate long tasks instead of handling them yourself. It does not remove you checking now and then but it helps a lot.

Luna xhigh can do most tasks (some tasks dont even need medium, you can try and benchmark them) luna xhigh to max cost/speed/intelligence jump is not worth it, thats why im using xhigh. I had no grand issues so far, you can always have escalation to better models for agents that cannot fix a problem
