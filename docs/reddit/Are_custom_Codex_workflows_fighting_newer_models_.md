#Are custom Codex workflows fighting newer models? [Visit](https://www.reddit.com/r/codex/comments/1wbtzyg/are_custom_codex_workflows_fighting_newer_models/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [true_emptyness](https://www.reddit.com/user/true_emptyness/)
### **Vote:** 2
---
I've been wondering whether some of the problems I'm seeing with newer Codex models come from a conflict between custom workflows and the models' own learned agentic behavior.
I built my Codex workflow around GPT-5.0. It uses skills and structured artifacts to make Codex behave somewhat like a state machine.
For example:
- "grooming" (analyze the problem)
- "epic" (a large unit of work)
- "macro" (a task inside an epic)
- "slice" (a smaller implementation unit)
There are also controlled transitions and dedicated skills (implementation, modeling/architecture, planning, etc.).
For example:
- activating an epic may require creating its Git branch
- explicitly requesting an analysis is supposed to trigger actual code inspection
- some transitions require specific planning/tracking artifacts
- some skills define what must be inspected before conclusions are produced
This worked extremely well for me with GPT-5.0 through GPT-5.4.
Since GPT-5.5 and GPT-5.6 (and I see similar tendencies with GPT-6.0 Astra), the same kind of workflow feels much less reliable.
The models seem much more eager to decide for themselves how much investigation is enough, what should be inferred, and what additional concerns should be taken into account.
Code reading is a good example.
I often see newer models inspect signatures, callers, or surrounding types, then infer the behavior of a dependency without actually reading the relevant function bodies.
If the assumption is wrong and I point it out, the model then goes back, reads the implementation properly, and discovers that the assumption was indeed false.
For my use case, this is worse than simply reading more of the relevant code before forming conclusions.
I also increasingly see things such as:
- explicit requirements being forgotten
- workflow rules being neglected
- the model deciding it has "enough context" too early
- specifications being added that I never requested
- backward compatibility being anticipated for projects that are not in production
- migration concerns being introduced when there is no production data
- secret-management concerns being introduced when they are unrelated to the task
- hypothetical concerns consuming attention while explicit requested changes remain unfinished
I want to distinguish the model from the Codex harness here.
By model behavior, I mean things such as when the model decides it has enough information, how aggressively it infers missing details, whether it invents additional requirements, and how strongly it tries to drive the task according to its own assumptions.
By harness, I mean the surrounding Codex machinery (tools, skills, context management, agent loops, planning mechanisms, delegation, etc.).
My question is whether newer models have simply been trained with much stronger priors about how an agentic coding task should be performed.
Not necessarily better priors (I often find the resulting behavior worse), just stronger ones.
If so, workflows that successfully constrained GPT-5.0 through GPT-5.4 may now be competing with the model's own preferred way of working.
For example:
- my workflow says "inspect the relevant implementation before concluding"
- the model decides "I have enough evidence to infer the rest"
Or:
- my grooming workflow says "formalize what the user actually requested"
- the model decides "I should infer additional requirements and anticipate risks"
That makes me wonder whether heavily structured skill-based workflows have become counterproductive with newer models (even if the model's default behavior is itself not better).
Have other people with custom Codex workflows noticed the same thing?
In particular:
- Did workflows that worked well with GPT-5.0-5.4 become harder to enforce with GPT-5.5/5.6 or newer models?
- Do newer models seem more resistant to user-defined execution flows?
- Have you found that simplifying or removing custom orchestration improves instruction-following?
- Do you now use skills mainly as capabilities/procedures rather than as a way to control the entire lifecycle?
- Have you noticed newer models inferring code behavior too early instead of reading the implementation?
I'm mainly trying to figure out whether this is a genuine regression in instruction-following, a conflict between custom orchestration and stronger learned agentic behavior, or some combination of both.
---
## Comments 6

- by [unknown](#) **&#x21C5; 1**
  <br/> "inspect the relevant implementation before concluding"

You are basically just saying "make no mistakes"? Have you actually defined what relevant is? In my workflow for example, I use a ticket based system that I created. I attach files to each ticket for things like notes, research, and files that need to be examined or edited as part of the ticket. So the model gets instructed to read an exact list of files before planning/implementing

- by [unknown](#) **&#x21C5; 1**
  <br/> How is that the same as saying "make no mistakes"?

Even much older models can identify the dependencies of a function, follow call sites, or determine which files are related to a feature. What I'm trying to enforce is that they actually inspect those dependencies before drawing conclusions.

I've had multiple instances where the model looked at a function signature, its name, or some callers and then inferred its behavior without reading the implementation.

A very simple real-world example: one of my colleagues named a function "upsert", even though its actual behavior is not really an upsert.

If the model stops at the name and signature, it gets the semantics wrong. If it reads the implementation, the answer is right there.

Of course I define what is relevant when I can. But there is a limit to how far that can reasonably go.

At some point, explicitly listing every relevant file, dependency, function, and code path myself becomes dangerously close to doing the entire analysis and specification by hand. That's precisely what I don't want.

Most of the time, the information needed to determine what is relevant already exists in the repository. The model is perfectly capable of discovering it. My issue is that newer models increasingly seem too eager to infer from partial information instead of actually reading the code.

And just to reiterate, this isn't a workflow I've just invented and am now struggling to make work. The same workflow worked extremely well for me from GPT-5.0 through GPT-5.4. I could rely on those models to explore the relevant code thoroughly and keep track of the details without me having to manually enumerate every file they should inspect.

That's the regression I'm trying to understand.

- by [unknown](#) **&#x21C5; 2**
  <br/> There’s some operating guidelines that Astra has that is screwing it up. Ask it what they are.

- by [unknown](#) **&#x21C5; 1**
  <br/> Hmm yess, grooming, you couldn't find a better noun? Are you grooming underage AI agents?

- by [unknown](#) **&#x21C5; 1**
  <br/> Sorry, I am french native. We used to call "grooming sessions" the meetings in which we design a feature and ask ourself all sort of questions. I never questioned the meaning of the word afterwards.

- by [unknown](#) **&#x21C5; 2**
  <br/> Haha grooming sessions 🤣 thanks for the laugh.

I hope I didn't ruin the meaning of the word for you in that particular context.

I forgot to mention, yeah I had to completely update my workflow, it was specifically build around Sol, it worked fine, but caused all kinds of problems with Astra, I'd definitely recommend not keeping it the way it is if you are noticing weirdness, problems
