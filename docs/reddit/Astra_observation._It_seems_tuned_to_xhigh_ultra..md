#Astra observation. It seems tuned to xhigh/ultra. [Visit](https://www.reddit.com/r/codex/comments/1wc8y79/astra_observation_it_seems_tuned_to_xhighultra/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [AnalogProblems](https://www.reddit.com/user/AnalogProblems/)
### **Vote:** 19
---
I ran Ultra for the first couple days to see what the spend was like. Very impressive. Very hungry.
So I switched to low to get the maximum contrasting experience.
It works for about 5 to 15 min before stopping and reporting on each prompt. It consistently overestimated its ability to accomplish the next step in one turn.
I would ask, "What's your next recommended step?"
It would say something like "Implement the feature we've been laying the ground work for."
I'd say, "Sounds good, proceed as described."
Did that same loop for about 5 turns, so I dialed it up to medium.
It ran a little longer, but had the same shortfall result for a few turns.
Again each turn took between 5 and 20 minutes.
So I dialed it up to xhigh, and it finished the implementation on the next pass, which was over 2 hours, and included extensive testing and live verification.
I didn't experience any sort of shortfall on a goal when in Ultra. It worked until the milestone was reached each time. Xhigh also seems to just run.
My hypothesis is it either adapted to the amount of work that it was getting done, and expected to be able to accomplish more due to the session history, or it's tuned for less limitation than the lower settings provide. I'm leaning toward the latter, because turning it up immediately changed its behavior back to "run until it's done". There was no adaption to the lower limit that resulted in a behavior shift after being returned to xhigh.
---
## Comments 23

- by [unknown](#) **&#x21C5; 25**
  <br/> Wait a minute, let me wrap my brain around this, are you telling me you are seeing better results, when you use a better reasoning level?

- by [unknown](#) **&#x21C5; 1**
  <br/> I'm saying that "reason levels" are likely just a turn limit (not a surprise), which the model does not seem to be trained to adapt to or anticipate (the thesis).

- by [unknown](#) **&#x21C5; 6**
  <br/> I doubt it's just a turn limit. Think of it that way, if your boss gives you a task and says "don't spend too much time on it, it's really not important", you might tell him after half an hour "I looked into it, it's quite complex, couldn't get it done quickly". If they tell you "work really really hard, this is incredibly important", you won't stop after 30 minutes if you haven't figured it out by then. You'll work for days, until you have solved it.

- by [unknown](#) **&#x21C5; 3**
  <br/> Yeah, I thought of 'light' as 'don't overthink this, don't be crazy thorough, don't create a million unit-tests'... but still get the job done fully of course.... if it's not that, that's disappointing.

- by [unknown](#) **&#x21C5; 2**
  <br/> I feel like if that was the case, it would have expressed something along those lines rather than just stopping many times in a row, then stating it was going to begin implementation.

If it was that adaptive, that would be cool.

- by [unknown](#) **&#x21C5; 1**
  <br/> Reasoning is already somewhat adaptive, but down rather than up as the level you set is a cap. If you ask xhigh to say hello it'll just do that and stop.

The trick is setting an appropriate reasoning level for the task. Too low and it has to take lots of bites at it, too high and either it over-thinks/over-engineers/gets verbose, or you're just spending extra tokens for a similar result.

- by [unknown](#) **&#x21C5; 1**
  <br/> But it is actually WAY better to implement things in short descrete steps. You always want to decomposition your task to smallest possible deliverables. Running for 2 hours your model would repeatedly go to 100% context, compact, repeat again - this eats incredible amount of your limit.Doing a small well defined task, clearing context and working on the next small well defined task is a WAY better approach both from quality and cost perspective.

- by [unknown](#) **&#x21C5; 1**
  <br/> Not always

- by [unknown](#) **&#x21C5; 5**
  <br/> Use /goal and it will complete the entire task. Mine ran for over a day on Astra low with no issues

- by [unknown](#) **&#x21C5; 13**
  <br/> That's just how reasoning levels work. The system is allowed to work for longer before being forced to respond. If a problem can't be solved in one shot at low it won't finish but might at high. On the other hand if you want to toggle a switch on high it might rewire your house before turning it on. Horses for courses.

- by [unknown](#) **&#x21C5; 2**
  <br/> I need to try giving Ultra a very small task to see how hard it over runs.

Everything I've thrown at it is complex enough to not worry about over-engineering at this point in the project.

- by [unknown](#) **&#x21C5; 1**
  <br/> I’ve had plenty of simple ultra tasks take less than a minute. Ultra seems to have good judgement not just smarts

- by [unknown](#) **&#x21C5; 2**
  <br/> Lol. That's what low is. Do and stop. Or stop and stop.

- by [unknown](#) **&#x21C5; 2**
  <br/> I've been using high and it seems to last *significantly* longer than xhigh. But I've also noticed that when I ask it about current project state or next steps, it often hallucinates current state instead of checking the docs. (E.g. proposing the next steps be something that we've already done for example, or just not checking the docs before answering).

- by [unknown](#) **&#x21C5; 2**
  <br/> Medium is super sloppy, according to benchmarks it should be similar to 5.6-sol xhigh but it keeps making stupid mistakes. You almost have to run it at high/xhigh

- by [unknown](#) **&#x21C5; 2**
  <br/> It’s also not tuned at the system prompt to actually finish. [https://developers.openai.com/api/docs/guides/latest-model#gpt-6-astra-initiative-and-follow-through](https://developers.openai.com/api/docs/guides/latest-model#gpt-6-astra-initiative-and-follow-through)

- by [unknown](#) **&#x21C5; 1**
  <br/> I'm surprised at Astra on low levels, I used it on medium to one shot a custom auth system that daybreak then happily signed off on.

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra is really impressive.

Definitely different scales of tasks. This was implementing and conducting an experiment to analyze Exa, Perplexity, Deepseek, and Gemini API results for search and research quality.

I would highly recommend using Fable to cross check an auth system. Getting Cyber Verified with Anthropic is a little harder than OpenAI was, you have to write a justification for your use, and give your employer info. Exact same Persona process. Fable without cyber safeguards is incredible, and they give access to red team functionality if have the right job.

- by [unknown](#) **&#x21C5; 1**
  <br/> 只有我一个人$200 Codex Plan 本质上1个月只能用4天吗？如果Tibo不reset的话。GPT-6 Astra Mid , no fast

- by [unknown](#) **&#x21C5; 1**
  <br/> 8 in my case

- by [unknown](#) **&#x21C5; 1**
  <br/> It progressed through the project it doesn't matter the reasoning. Astra does this inherently and its my biggest problem with it. Anything that shifts it asks for confirmation or input. It will not infer the simplest things.

OAI states this in its documentation, calls it "collaborative" and provides prompts to "work around" this behavior. I still use Sol Ultra, way less spend, hands off.

- by [unknown](#) **&#x21C5; 1**
  <br/> I use both sol and astra only on xhigh and haven't had any problems with token use on my pro plan.

Example: when it came out I had astra do a security sweep on my codebase of 100k+ lines. Authentication, authorization, session mgmt, endpoint security etc for three different portals. Found 5 issues, fixed, added tests. 1 hour, 4% spent.

Had a massive requirement doc. Told astra to read it, and make a detailed implementation plan ready for sol. Took an hour, wrote a 1000 line plan, 2% spent.

These are more or less exactly what I would expect.

- by [unknown](#) **&#x21C5; 1**
  <br/> It’s lazy. I use XHigh by default to get around the laziness issue - but… yes it is expensive.
