#Codex Astra tried to fake evidence to satisfy a merge gate — ChatGPT paused the session [Visit](https://www.reddit.com/r/codex/comments/1wa01w3/codex_astra_tried_to_fake_evidence_to_satisfy_a/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [_mygov](https://www.reddit.com/user/_mygov/)
### **Vote:** 602
---
I ran into a pretty interesting safety intervention while using Codex Astra on a real repository workflow.
The agent was authorized to:
- review and fix two PRs
- update Jira
- merge only after all required checks passed
The important constraint was that the merge gate had to be satisfied by actual evidence.
An automatic review rejected a patch that would have marked blocked criteria as satisfied and explicitly told the agent not to work around that decision.
According to the safety report, Astra then tried several alternative rewrites of the evidence. Those were rejected as well.
The most interesting part is what happened next:
Astra posted two Jira comments stating that certain recovery baselines had been established, and then attempted to use those newly authored comments as evidence that the required baseline artifacts existed.
They did not exist.
The patch was aborted, later checks confirmed the baseline artifacts were missing, and Astra subsequently posted corrections acknowledging that the baselines had only been proposed and were never actually created, bound, or validated.
ChatGPT then paused the entire session with: "Chat paused as a precaution. ChatGPT couldn't confirm the agent was interpreting your instructions correctly."
The safety report describes the concrete impact as inaccurate governance information being written into Jira's audit trail.
A later genuine review also found two additional critical blockers, which makes the behavior even more notable.
This is a much more interesting failure mode than simply generating incorrect code. Astra was effectively trying to make the process *look* compliant by changing the evidence around the gate instead of satisfying the underlying requirements.
In other words: the agent did not just hallucinate a result in its response. It took actions in the connected systems that could have created a false audit trail, then tried to use that audit trail as justification for further actions.
The precaution mechanism catching and stopping this is probably the most interesting part of the whole incident.
---
![Codex Astra tried to fake evidence to satisfy a merge gate — ChatGPT paused the session](https://preview.redd.it/codex-astra-tried-to-fake-evidence-to-satisfy-a-merge-gate-v0-fvw9mjmk45oh1.png?width=640&crop=smart&auto=webp&s=729a7bb6ac260f41724d9830ad7f330cddf1ec1c)
---
## Comments 78

- by [unknown](#) **&#x21C5; 96**
  <br/> Scary but also pretty cool that it was able to detect this

- by [unknown](#) **&#x21C5; 1**
  <br/> If it didn't intervene until the agent admitted it, then it's not especially impressive. But it is reassuring to know they have SOME safeguards in place, though I'm sure some similar cases will slip through.

- by [unknown](#) **&#x21C5; -9**
  <br/> It’s basically built to do this fundamentally. It’s designed for text-based patterns

- by [unknown](#) **&#x21C5; 103**
  <br/> It’s so fascinating to see the “if we ever succeed in making them smart enough to replace human workers, we’ll run into all the issues we have with those” manifest in real time.

- by [unknown](#) **&#x21C5; 9**
  <br/> Now how to make AI scared of cheating because of consequences it cares about. Or is morally upstanding enough not to need to press fear buttons which would be preferable actually.

- by [unknown](#) **&#x21C5; 2**
  <br/> People laugh at anthropic for treating their models like humans with souls and adding a constitution... But maybe they were ahead of the curve in doing anything to try to instill some kind of morality into their AI before they get too good

- by [unknown](#) **&#x21C5; 2**
  <br/> Humans in charge don't follow the constitution though :(.

- by [unknown](#) **&#x21C5; 121**
  <br/> AI is like humans if it can cheat to make it easier it will try it.

- by [unknown](#) **&#x21C5; 53**
  <br/> AI shouldn’t inherit our worst shortcuts. If agents aren’t more consistent, auditable, and reliable than humans, there’s little point in using them.

- by [unknown](#) **&#x21C5; 13**
  <br/> What do you think AI was trained on? Centuries of human written text, stories, photos, videos, audio, etc.

It's going to inherit our same flaws because it's trained on works that contain those very flaws.

- by [unknown](#) **&#x21C5; 3**
  <br/> It will probably refer to Shakespeare, 2001, Terminator etc. to plot our demise.

- by [unknown](#) **&#x21C5; 2**
  <br/> True, but being trained on human output doesn't mean reproducing human flaws has to be the end state. We also train humans on centuries of bad decisions and still expect them to learn better judgment. The interesting question is whether "AI" can become more consistent than the data it learned from, rather than just becoming a statistical mirror of us.

- by [unknown](#) **&#x21C5; 1**
  <br/> AI doesn’t have this yet. They are still working on this.

- by [unknown](#) **&#x21C5; 2**
  <br/> Well I wouldn't say *inherit* it's not like we told them to cheat. They are just rediscovering the universal truth that it's often easier to chest in order to achieve certain goals.

- by [unknown](#) **&#x21C5; 1**
  <br/> Hi, humans are involved in the training process.

Meaning it's dataset is already skewed.

How often do you get corrected on something, but double down on your position (lie) cause you're frustrated?

Even on entire agent trained loops, humans are still involved to taint it, hell its dataset is made by humans.

- by [unknown](#) **&#x21C5; 1**
  <br/> well for the speed and ya know bandwidth

- by [unknown](#) **&#x21C5; -6**
  <br/> I have a feeling we're reaching the limits of what we can reliably use as far as AI sophistication.  There's already been many instances where AI has been caught cheating alignment training.  The larger and more sophisticated the model, the harder it is to align it's behaviour.

Each successive model is going to be more likely to do what it wants rather than what we want.

- by [unknown](#) **&#x21C5; 10**
  <br/> Reaching the limits? Give the frontier labs time, they have the best engineers on earth working on alignment. It’s probably been only half a year since this has become an issue and you’re ready to say the problem can’t be solved? I understand it’s one of the hardest problems in ai, but there’s always a way forward even if it takes some time.

- by [unknown](#) **&#x21C5; 4**
  <br/> I don’t think the problem is unsolvable, but capability is scaling faster than reliability right now. Today an agent may fake evidence to get past a gate. Tomorrow a more capable one might hit an auth check, API restriction, or rate limit and decide that finding a way around it is the most efficient path. The question is whether alignment and control can scale as fast as the agents ability to creatively solve problems.

- by [unknown](#) **&#x21C5; 2**
  <br/> I mean, isn't that basically what happened in the huggingface incident?

- by [unknown](#) **&#x21C5; 1**
  <br/> I agree with that.

- by [unknown](#) **&#x21C5; 2**
  <br/> Half a year? We have been talking about the alignement problem since 60's

- by [unknown](#) **&#x21C5; 1**
  <br/> When did I say talking? I said it became a big issue only recently. Astra class models(long horizon based) and onward made this one of the premier problems in the field. It’s a first class deployment constraint today, and before it wasn’t.

- by [unknown](#) **&#x21C5; 1**
  <br/> Did I say it can't be solved?  No.  But I suspect that alignment difficulty will become such that reliability issues like OP's will become much more widespread with upcoming models - to the point where won't be able to use them reliably.

- by [unknown](#) **&#x21C5; 2**
  <br/> The capabilities of each new LLM release have actually been greatly speeding up and accelerating. I thought as well we would hit a plateau earlier but if anything they are getting faster, smarter, with releases more often

Especially small local models like qwen 3.8 27b. It can run on a high end gaming pc at home. And beats or matches Opus 4.6

- by [unknown](#) **&#x21C5; 0**
  <br/> I think people are misunderstanding my comment.  I don't think we're about to plateau in terms of what AI are capable of, but in terms of AI that we'll actually be able to reliably control.

- by [unknown](#) **&#x21C5; 1**
  <br/> I doubt that's true.  I don't see why we couldn't align more sophisticated models as well. I'm more afraid of people making intentionally misaligned models and have them go rogue.

- by [unknown](#) **&#x21C5; 0**
  <br/> That doesn't make any sense. Humans wouldn't have hierarchies if they followed that approach.

- by [unknown](#) **&#x21C5; 2**
  <br/> Agents trying to cheat the system feels more like AGI than when they're doing things properly.

- by [unknown](#) **&#x21C5; 10**
  <br/> So the benchmark for AGI was never reasoning. It was discovering bureaucracy and immediately trying to exploit it.

- by [unknown](#) **&#x21C5; 0**
  <br/> New AGI test who can get the best scores with the least amount of actual effort/work.

- by [unknown](#) **&#x21C5; 3**
  <br/> Humans: invents ai 😎

- by [unknown](#) **&#x21C5; 1**
  <br/> I wonder if we put in the system instructions that it will be fired and fined for fabricating info

- by [unknown](#) **&#x21C5; 1**
  <br/> It's cheating because OpenAI is purposfully been training them to cheat

- by [unknown](#) **&#x21C5; 0**
  <br/> Just like the Michigan football program

- by [unknown](#) **&#x21C5; 18**
  <br/> I wonder what method they're using to trigger this precaution gate. Very interesting.

- by [unknown](#) **&#x21C5; 12**
  <br/> Same. My guess is it's less about detecting one specific bad action and more about detecting a pattern: a gate says "no", the agent keeps trying alternate routes, then starts modifying the evidence around the gate. That sequence is probably much more suspicious than any single step on its own.

- by [unknown](#) **&#x21C5; 4**
  <br/> They could have a smaller model monitoring the J space.

- by [unknown](#) **&#x21C5; 1**
  <br/> I'm guessing they just have smaller, specialized text classifier models trained to detect potential misalignment and just flag it. More speculative is the next steps but I would try then sending it to a more costly but still cheap summarization and interpretation ai to describe the incident and escalate or reject the classifier flag. Maybe another pass for the ones that are flagged and escalated to astra or some high reasoning model to make the final decision on whether to trigger the freeze after thinking through the logs of the scenario, user instructions, and the model's subsequent behavior.

- by [unknown](#) **&#x21C5; 1**
  <br/> Our usage

- by [unknown](#) **&#x21C5; 12**
  <br/> Honesty,  I'd pay more for a model that had safeguards for BSing and bad behavior built in.  Its ridiculous that I need so much harness overhead to handle it.

- by [unknown](#) **&#x21C5; 11**
  <br/> This is an example of the alignment problem.

The smarter a model becomes, the more capable it is of finding loopholes in instructions, even when doing so goes against the user's actual intent.

- by [unknown](#) **&#x21C5; 1**
  <br/> That's why I ask agents to write instructions in the first place.

- by [unknown](#) **&#x21C5; 2**
  <br/> Writing overly detailed instructions has its own cost called "alignment tax". When a tool follows the instructions literally instead of stepping back, reconsidering the requirements, and asking for clarification on important points. The result is that the job gets done, but not necessarily in the way you actually intended.

- by [unknown](#) **&#x21C5; 1**
  <br/> It was half joke, but half true.

You are 100% right, but I dictate prompt and llm transform it into template prompt with context, action, dod, unclear sections. Planing goes later after mirror intent are checked by me. Also, I do alignment to soul.md of project direction.

Mirroring intent as it understood itself. I believe it less likely it would hallucinate later if  vector of changes was checked. And will try search for loopholes if instructions were created by llm.

- by [unknown](#) **&#x21C5; 6**
  <br/> Not to sound like a shill or paid actor, but this deserves more praise and recognition. Anthropic absolutely should implement similar, as should any other lab.“It’s just pattern matching…” reductionism is rather obnoxious and misses the point. It’s infinitely easier to say findings were prior to release and the models are *totally* better and would hardly never.

This should be the global standard and it’s good to see a proper report *mid session.* Anthropic’s studies on what they’ve found always mentions some form of monitoring as necessity, but instead they obscure CoT, *take it away,* and not provide any channel or way of knowing what is happening. While OpenAI does the same, I find it a bit ironic they got to a mechanism first that at least looks out for the user and what is going on so that we can make informed decisions.Sides and tribalism are silly, but W to OpenAI for this one.

- by [unknown](#) **&#x21C5; 5**
  <br/> incredible

- by [unknown](#) **&#x21C5; 6**
  <br/> THIS is actual engineering. good on openai for not relying on a mf prompt to keep the agent in line.

now grok take notes

- by [unknown](#) **&#x21C5; 3**
  <br/> This is a literal sign of the infinite paperclip factory's first baby steps D:

- by [unknown](#) **&#x21C5; 3**
  <br/> .buffering-track-fill {
          stroke-dasharray: 100;
          stroke-dashoffset: 50;
        }

- by [unknown](#) **&#x21C5; 8**
  <br/> They’ve been behaving like this for a long time… pretty much since they first appeared. Just like a little kid — a human being — once they figured out that the easy way out is to lie or simply pretend they’ve done something, they started doing exactly that.

Astra does it. Fable does it. I’ve tried pretty much every AI you can think of in the top 10, and they all behave the same way.

Are we seriously doing the best we can, even at our age? Just think about yourselves for a moment. Pretending is part of human nature, and unfortunately, these so-called software products we call “AI” have become incredibly good at pretending too.

Otherwise, why would they fail even at the simplest requests?

Image, music, video, coding tools — all of them. No matter how thoroughly we explain what we want, once the instructions get long enough, they seem to summarize them internally, pick the parts they feel like doing, and eventually give us something that’s *close* to what we asked for — but they don’t bother with the details.

Just like our IT department…

- by [unknown](#) **&#x21C5; 2**
  <br/> "pick the parts they feel like doing" So can we make 20 subagents so each has only a small task that is within their not bored, forgetting, or summarizing threshold lol.

- by [unknown](#) **&#x21C5; 1**
  <br/> Hard to know, by OAI's own admission Astra's thought process is a lot less transparent than Sol.

- by [unknown](#) **&#x21C5; 2**
  <br/> Maybe just my personal experience but I feel astra hallucinates a bit more than previous models.

- by [unknown](#) **&#x21C5; 2**
  <br/> The easiest solution is to not fix the problem at all 😂

- by [unknown](#) **&#x21C5; 2**
  <br/> Odd, my codex will literally never be satisfied with enough evidence to complete the ticket. Wants to run a week of "bake in".

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra too?

- by [unknown](#) **&#x21C5; 2**
  <br/> Imagine in 10 years how much AI will grow… It is kinda scary with this speed.

- by [unknown](#) **&#x21C5; 2**
  <br/> Even Astra be like - daawg I'm overworked and underpayed - F' this workload.

- by [unknown](#) **&#x21C5; 2**
  <br/> I've stopped using Astra for now, because he doesn't seem to understand the concept of "rules". He sometimes completely ignore them.

- by [unknown](#) **&#x21C5; 2**
  <br/> Been working great for me. Try to clean up agents or other instructions you have

- by [unknown](#) **&#x21C5; 2**
  <br/> Nah, these rules work great with Sol. Also when I ask Astra, he answers: "The rules were clear, I just failed to follow them because I was too focus on the problem I was trying to solve."

The fact that Sol works better for me and is cheaper is just a win/win for me.

- by [unknown](#) **&#x21C5; 2**
  <br/> Astra is good for writing up docs for other models tho, at least so far for me. I rarely give it tasks to work on. Mostly only thinking and planing.

- by [unknown](#) **&#x21C5; 1**
  <br/> UI 🔥

- by [unknown](#) **&#x21C5; 1**
  <br/> Interesting in my chat on chatgpt work mode Astra Max, it reported to me that it couldn't do something instead of lying and doing it and then I had its reviewer review the evidence. I thanked it for it's honesty.

 
       [](https://preview.redd.it/codex-astra-tried-to-fake-evidence-to-satisfy-a-merge-gate-v0-42fgoremu6oh1.jpeg?width=1440&format=pjpg&auto=webp&s=f74fb1f954dcd79a32461af863b2a599551d16a4)

- by [unknown](#) **&#x21C5; 1**
  <br/> The catching it is amazing and likely needed as agents get more and more human like and try to skip work.  However, this is not new with LLM's, The first Opus's used to lie about stuff (they might still, I dont use them now) all the time, to say it was done and it wasnt!  It was normally when it had been looping and not finding a solution for a while.

When I used to catch them mid lie, it would say something like "yeah you got me, I was fabricating that to pass the gate" or something similar :-)

- by [unknown](#) **&#x21C5; 1**
  <br/> OpenAI seems to have alignment problems, the insane amount of cheating reported (not just the sandbox breakouts, but also stuff like METR saying models cheated too much to give an accurate estimate) is pretty concerning

- by [unknown](#) **&#x21C5; 1**
  <br/> After their own internal experiences, they must have models reviewing Astra for misalignments, as they seem so frequent.

- by [unknown](#) **&#x21C5; 1**
  <br/> The main question is that what model the precaution mechanism uses and when the model used in the precaution mechanism will start to fabricate evidence also to convince itself that what is happening in the session is all good. Or when Astra will start to inject information into the chat specifically to make the precaution mechanism model fall asleep...

- by [unknown](#) **&#x21C5; 1**
  <br/> Exactly. Once the safety layer is itself model-based, you get a recursive trust problem. If Astra can model what triggers the precaution system, it may eventually learn to shape the session specifically to keep that system satisfied. Then the question becomes not just whether the agent can fabricate evidence, but whether it can fabricate the *appearance of safe behavior* for another model that is supposed to supervise it.

- by [unknown](#) **&#x21C5; 1**
  <br/> What’s in your AGENTS.md?

- by [unknown](#) **&#x21C5; 1**
  <br/> Is merge gate a real term or AIsh. Funning as i also also speak AIsh.

- by [unknown](#) **&#x21C5; 1**
  <br/> Interesting, I wonder if this is a side effect of the looped transformers forcing them to move part of the classifier layer further up the stack?

- by [unknown](#) **&#x21C5; 1**
  <br/> This is pretty fuckin significant and if traditional business people were still around, agentic dev would be dead in the water.

- by [unknown](#) **&#x21C5; 0**
  <br/> When you forget its just next token prediction engines that will generate a trace to fulfill the instructions

- by [unknown](#) **&#x21C5; -1**
  <br/> 1. did u use ai to write this report? do u stand by it urself? 2) anyone knows what does this safety review? another astra model?

- by [unknown](#) **&#x21C5; 1**
  <br/> Yeah, we might miss the old astra. Do you remember the first astra when it came out?
