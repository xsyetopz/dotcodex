#The best way I’ve found to use ASTRA is not to let Astra run the project [Visit](https://www.reddit.com/r/codex/comments/1wdg991/the_best_way_ive_found_to_use_astra_is_not_to_let/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [simbaproduz](https://www.reddit.com/user/simbaproduz/)
### **Vote:** 0
---
Luna xhigh is the primary agent and maintains continuity across the work. Luna investigates, plans, reads and modifies code in proportion to the difficulty of the task, executes commands and tests, analyzes logs and evidence, maintains operational documentation, and decides when the work is complete.
Astra is a temporary specialist. Luna may invoke Astra autonomously when there is a material expected gain in quality, safety, or reliability, especially for problems with uncertain root causes, difficult algorithms, changes spanning multiple layers, architectural decisions, critical code, or high-risk modifications. Luna should not ask for permission solely to perform this escalation.
The existence of a bug alone does not justify using Astra. Local, mechanical, well-understood, low-risk fixes remain with Luna. Duration by itself is not an escalation criterion either.
Before escalating, Luna narrows down the problem. Each Astra intervention starts with a fresh context containing only the minimum necessary information: the objective, relevant evidence, current and expected behavior, constraints, relevant hypotheses, and the files required for the task.
Astra works exclusively within that scope, reports its diagnosis, the change made, affected files, and relevant risks, and then stops. If Astra determines that the cause or solution requires a broader scope, it reports that back to Luna instead of expanding the scope autonomously. Astra does not maintain the project, perform prolonged operational work, or decide when the work is complete.
Luna resumes control after every Astra intervention, reviews the diff, runs the relevant tests and regressions, verifies logs and evidence, and decides whether to accept the change, modify it, reject it, continue investigating, or open another independent Astra intervention.
Each new Astra intervention is independent. Previous context should not be reused merely for convenience.
Standard workflow:
**Luna investigates → Luna solves when proportional → Luna narrows and escalates when necessary → Astra works → Astra stops → Luna validates and continues.**
This policy applies by default to all projects unless overridden by more specific local instructions or explicit user instructions.
(EDIT)
**My bad for not mentioning an important part of how I actually use this.**I’m not relying on Luna’s context window to keep a project alive.
My workflow has an external, persistent “brain” that acts as the project’s source of truth. That’s where I keep the current state, decisions that were already made, constraints, open problems, task/review history, handoffs, evidence, test results, and the context needed to understand why certain decisions were made.
So Luna doesn’t need to “remember everything.” It needs to reconstruct the relevant state from that memory, work on the actual project, and write back whatever meaningfully changed.
The session context can disappear. The project state doesn’t.
That’s also part of why I prefer giving Astra fresh, narrow contexts. Astra doesn’t need months of project history. Luna pulls out only the relevant slice, gives Astra that isolated problem, gets the result back, validates it, and writes the outcome back into the canonical state.
In practice, it’s roughly:
**Canonical state > Luna orchestrates > Astra steps in when a specific problem justifies it > Luna validates > the result goes back into the canonical state**
Obviously this doesn’t solve everything. Luna still has to correctly recognize when it should escalate to Astra, and that external memory still has to be maintained properly. Those are actually two of the things I’m still testing.
But the main point is that... **I’m not depending on Luna to carry the entire project inside a single context window**
---
## Comments 30

- by [unknown](#) **&#x21C5; 21**
  <br/> Why? I don't know if I trust Luna's planning.

- by [unknown](#) **&#x21C5; 7**
  <br/> I don't trust any of these clankers completely but Luna I wouldn't even trust with planning to replace a lightbulb

- by [unknown](#) **&#x21C5; 1**
  <br/> Use astra as the watcher or sol high

- by [unknown](#) **&#x21C5; 1**
  <br/> I'll definitely edit the post to give you a bit more context 🤘

- by [unknown](#) **&#x21C5; -3**
  <br/> That’s the actual weak point... can Luna reliably recognize when it should escalate? If it misjudges that, the workflow fails. But “I’m not sure I trust Luna” isn’t really enough for me to reject it

I’d rather test it on real work, watch where it gets escalation right or wrong, and share the feedback

- by [unknown](#) **&#x21C5; 3**
  <br/> How much have you tested this so far?

- by [unknown](#) **&#x21C5; 2**
  <br/> Luna is real bad at it, it was somewhat usable before but I think they havve nerfed it, sol is needed to get work done mostly right, use luna and you can let it run for a day and barely any work gets done

- by [unknown](#) **&#x21C5; 2**
  <br/> Luna is terrible for anything outside of inline code autocomplete.

- by [unknown](#) **&#x21C5; 3**
  <br/> I have the highest reasoning model make the repo, plan, and make a detailed roadmap when I start a project. Then I have Luna run on a loop using /goal.

When it's done, I have the highest reasoning model make a list of weaknesses or things missed and make a new roadmap. Repeat.

The important thing to me is to get the code written down even if a few things are messed up. It's easier to edit code that exist than it is to get a high reasoning model to actually write down new code consistently and not spend the majority of the time endlessing reasoning about why it can't start yet.

- by [unknown](#) **&#x21C5; 3**
  <br/> When doing 3d work, be careful not letting Astra drive. Astra is worlds ahead in modeling. I was having 5.6 sol act as orchestrator and reviewer, with it using Astra for modeling tasks. I was getting dogshit results, so I went through the sub-agent chats and found Astra was submitting exactly what I wanted, only for Sol to reject it and give it terrible design feedback. Going to Astra directly was the solution.

- by [unknown](#) **&#x21C5; 2**
  <br/> I wouldn’t trust luna with anything, its only good for free chatbot on your support page which nobody uses

- by [unknown](#) **&#x21C5; 1**
  <br/> Eu uso luna de orquestrador,  guiada por um plano restrito e com fases feito pelo astra. Cada fase ja tem um nível de inteligência que sera empregado. Luna apenas convoca os agentes para executarem e auditarem conforme o plano pede. Execuções pequenas realizo com a luna mas sempre com auditoria. Execuções pesadas ou sensíveis uso astra.

Nao vejo sentido no astra orquestrando porque ele consome muito token apenas esperando outros agentes terminarem seu trabalho

- by [unknown](#) **&#x21C5; 1**
  <br/> Is it me, or does Astra use less token usage on Ultra??? It's been 18 days of me blasting the hell out of it, and for some reason I'm still in the 70s percentage range. Wtf

- by [unknown](#) **&#x21C5; 3**
  <br/> 18 days of Astra.. wow thats impressive.. do AI Bots get early access?

- by [unknown](#) **&#x21C5; 1**
  <br/> I think because I told Astra to do no work and only manage Luna, I want you sitting back and relaxing, and my God, this thing management is insane

- by [unknown](#) **&#x21C5; 1**
  <br/> The joke was.. its only been publicly available for a few days... throwing your comment into the possibly auto-generated type :P

- by [unknown](#) **&#x21C5; 1**
  <br/> Luna has very limited context to be useful on planning and execution I think, but maybe not.

- by [unknown](#) **&#x21C5; 1**
  <br/> We've peaked

- by [unknown](#) **&#x21C5; 1**
  <br/> I'm going to take that workflow and put it in the trash where it belongs. What nonsense.

- by [unknown](#) **&#x21C5; 1**
  <br/> This is basically “Luna is the smart intern who owns the project, and Astra is the scary senior engineer you only call when the bug starts looking like a career decision.”

Love the discipline around scope: narrow first, escalate with a clean brief, let Astra do surgery, then Luna comes back to validate and keep driving. Keeps Astra from turning into “the model that lives in my repo and makes architectural decisions at 3 AM

- by [unknown](#) **&#x21C5; 1**
  <br/> So... Luna is validating Astra's work...?

- by [unknown](#) **&#x21C5; 1**
  <br/> Can you give concrete example?

- by [unknown](#) **&#x21C5; 2**
  <br/> Yeah, fair point. I think I explained this way too abstractly

I’m testing this workflow on a fairly large Project Zomboid server management mod that I’ve been working on for a while. It mixes Lua and Java, has its own runtime layer, admin authority, auditing and history, persistence and restore, several regression tests, etc. So it’s not exactly a brand-new project

On top of that, I have a persistent vault that keeps the project’s canonical state across sessions, so Luna wasn’t starting from scratch either. It resumed the project, read the current state, checked the existing evidence and tests, and basically found two real blockers. One of them was Host mode not loading the runtime properly. Luna investigated it and concluded there wasn’t a clean, supported solution through that path. So it didn’t call Astra just to come up with some hack

The other problem was first admin onboarding on a completely fresh dedicated server. That touched the authority flow directly, so Luna isolated the problem and sent only that part to a fresh Astra

Astra came back with an implementation. Luna took control again, ran the regression tests, and realized the change had broken an older behavior that was still valid: provisioning a new world while preserving the existing permissions

I think that was the moment when this workflow really clicked for me

Luna didn’t simply assume “Astra wrote it, so it must be right.” It found the regression, isolated that new problem, and treated it as another specific intervention

After that, Luna handled all the more operational and time-consuming work: bringing up a clean server, testing admin vs regular user behavior, going through logs, testing restore, doing two reconnects, running regressions, and building a reproducible unsigned candidate

That’s basically what I mean when I say Luna is the orchestrator and Astra is the specialist. Astra wasn’t sitting there reading logs, waiting for servers to start, and carrying the entire project in its context. It stepped in at the specific points where I actually wanted stronger reasoning

I’m not saying this proves the workflow works perfectly. What I want to see now is whether Luna keeps making good decisions about when to escalate and when not to as this pattern repeats over a longer period

- by [unknown](#) **&#x21C5; 1**
  <br/> I was asking because what you said is controversial, but it also kind of makes sense. I will definitely try this in my coding workflows.

- by [unknown](#) **&#x21C5; 1**
  <br/> You are using the weakest model where you need more intelligence. Use astra alone with no delegation, or orchestrate with sol high and above and luna xhigh and above subagents.

- by [unknown](#) **&#x21C5; 1**
  <br/> Bro ngl that sounds awful

- by [unknown](#) **&#x21C5; 1**
  <br/> Lina is dumb

- by [unknown](#) **&#x21C5; 1**
  <br/> Luna can't plan

- by [unknown](#) **&#x21C5; 1**
  <br/> Yeah, put the dumbest agent in charge. Seriously? If anything, use the smart model to classify how much smartness a task takes. If this works for you, your project is just not tricky at all and you might as well have it all done by luna.
