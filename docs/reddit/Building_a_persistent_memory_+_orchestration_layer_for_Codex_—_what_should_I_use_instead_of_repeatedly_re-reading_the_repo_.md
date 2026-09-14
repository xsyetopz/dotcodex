#Building a persistent memory + orchestration layer for Codex — what should I use instead of repeatedly re-reading the repo? [Visit](https://www.reddit.com/r/codex/comments/1wbznhf/building_a_persistent_memory_orchestration_layer/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [yxf2y](https://www.reddit.com/user/yxf2y/)
### **Vote:** 5
---
I’ve been building a fairly serious agent workflow around OpenAI Codex for a Laravel/React project, and I’ve hit a point where the orchestration works, but the context/memory side clearly does not.
My setup currently looks roughly like this:
- A serial orchestrator with route types like FAST_UI / STANDARD / CRITICAL
- Context Resolver → Implementer → Reviewer flow for non-trivial tasks
- Durable task state, context capsules and handoffs
- Planner / intake layer inspired by CodexQB
- Session continuity hooks inspired by AvenoxBeyin
- `codebase-memory` MCP for structural repo discovery
- Serena for exact symbol/reference navigation
- Local dashboard/telemetry for task/agent visibility
The reason I built all this was simple: I wanted to stop giving one giant prompt to one Codex agent and watching it blindly read half the repository, run dozens of commands, retry tests repeatedly, and burn a huge amount of context/token budget.
Unfortunately, that is still basically what happens.
A recent CRITICAL payment-domain acceptance task is the perfect example. I gave Codex a very detailed validation brief covering migrations, payment allocation, security boundaries, tenant/legal-entity isolation, atomicity, reporting non-pollution, exports, frontend build, etc.
The task eventually succeeded technically, but the session spent a huge amount of time repeatedly doing things like:
- raw `rg` searches
- re-reading known service/controller/test files
- rediscovering test harness behavior
- retrying multiple Laravel test files with the same CSRF issue
- manually tracing service relationships
- re-running builds and focused test groups
That single job used roughly half of my 5-hour Codex usage allowance.
The frustrating part is that a lot of the knowledge it rediscovered was already known from previous work.
For example:
- where the orchestrator lives
- which services own payment/settlement/reporting behavior
- how the domain test harness handles CSRF
- which test files cover specific finance flows
- existing project/tenant/legal entity invariants
- prior fixes and verified architecture decisions
I expected my existing tools to solve this, but I now realize they solve different problems:
`codebase-memory` gives me structural repo discovery, but it isn’t really persistent project understanding.
Serena is excellent for exact symbol/reference navigation, but it isn’t memory either.
My docs/wiki are useful reference material, but agents still have to decide to read them and often re-read large files.
Context Capsules and handoffs help within a task, but they don’t give the next unrelated task a compact understanding of the project.
So what I’m actually missing is a persistent, project-scoped, compact memory layer that can say:
“Before you start searching, here are the relevant things previous sessions already learned about this repo.”
I looked at AvenoxBeyin because I liked its idea of automatically capturing sessions, compiling knowledge, and injecting useful context back at session start.
I also looked at CodexQB because its Autopsy / Project Comprehension / Ontology approach is close to what I want for planning.
Then I looked at `2kDarki/codex-mem`.
That project is conceptually very close to what I want:
- automatic Codex transcript capture
- persistent SQLite observations
- progressive recall through search → timeline → get_observations
- automatic context injection
But after auditing it, I found some issues for my use case:
- its watcher observes all `~/.codex/sessions/**/*.jsonl`
- project identity appears to be based on `basename(cwd)` rather than a canonical repository identity
- retrieval can be filtered by project, but that doesn’t appear to be an enforced security/isolation boundary on every read path
- same-named repos could collide
- some observation retrieval paths can work by arbitrary IDs
- global `~/.codex/AGENTS.md` context injection is something I specifically do not want
- the documented npm package currently appears unavailable
So I don’t feel comfortable plugging it directly into a large multi-project Codex setup.
What I’m trying to build is something like:
User brief
↓
Planner / Orchestrator
↓
Persistent project memory bootstrap
↓
Context Resolver
↓
Only if memory is insufficient:
codebase-memory
Serena
targeted source reads
↓
Implementer
↓
Reviewer
↓
Session knowledge captured for future tasksThe memory should NOT replace source code/tests as truth.
I want it to act as a cheap orientation cache:
- “These are the relevant services.”
- “This test harness requires real CSRF session setup.”
- “This reporting path was previously verified.”
- “These files/symbols are likely relevant.”
- “This architectural relationship was confirmed in a previous task.”
Then the agent only verifies current source where correctness actually depends on it.
My requirements are roughly:
- local-only
- project/repository scoped
- automatic capture
- automatic or semi-automatic summarization
- bounded context injection
- no global [AGENTS.md](http://agents.md/) mutation
- no cloud memory dependency
- no mandatory Obsidian dependency
- source/tests remain authoritative
- ideally Codex/App Server compatible
- progressive retrieval rather than dumping whole session history
- repo identity enforced internally, not just passed as an optional search filter
- ideally reusable with existing MCP tools rather than replacing them
I’m now trying to decide between three approaches:
- Find another existing Codex/Claude coding-memory project that already does this correctly.
- Take something like `2kDarki/codex-mem` and make a very small fork that only adds canonical repo identity, watcher allowlisting and enforced repo-scoped retrieval.
- Use AvenoxBeyin’s session capture/compile/inject model and adapt it for project-scoped coding knowledge instead of personal knowledge.
What I really do NOT want to do is invent yet another custom Markdown “brain” and manually maintain architecture/domain summaries. That feels like rebuilding something that should already exist.
For people who have built persistent memory around Codex, Claude Code, Cursor or similar coding agents:
- What actually worked for you?
- Is there a project I’m missing that already handles repository-scoped persistent memory well?
- Would you fork `codex-mem` and patch the isolation model, or use a different architecture entirely?
- Is Obsidian/Markdown compilation actually better in practice than structured SQLite observations for coding-agent memory?
- How do you stop stale memory from becoming trusted over current source?
- How much context do you inject at session start versus retrieve on demand?
- Have you measured whether this actually reduces token/context consumption meaningfully?
- Do you let the coding agent write its own long-term memory, or only promote verified observations after tests/review?
I’m especially interested in systems people are actually using in real repositories, not just theoretical agent-memory architectures.
My main goal is very practical: **stop paying for the same repository discovery over and over again.**
---
## Comments 10

- by [unknown](#) **&#x21C5; 3**
  <br/> It's not really a good idea to just install some memory system and hope that the AI does it well. It's more likely to cause more problems. Of which you've just listed. Plus, adding memory will result in even more tokens being used.

Your GitHub repo is all the persistent memory that you should need.

For example, you can solve the issue with testing by adding all the information needed for testing into the AGENTS.md, or by creating a testing skill.

The agent re-reading your repo is generally the more efficient way for it figure out what to do.

If it's struggling, you should try and figure out why it's struggling and what you need to change it to repo to fix that. Like making the code more 'obvious', or improving the build process (I have a central build.py script for one of my projects), or improving the AGENTS.md and related markdown files, or the agent skills.

The Matt Pocock's retro skill is great for figuring out how to fix up this kind of stuff. Just run it after one of your big sessions.[https://github.com/mattpocock/skills/blob/main/skills/in-progress/retro/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/in-progress/retro/SKILL.md)

Also, rtk-ai/rtk can be pretty good at reducing tool output.

You might be interested to read the source code for the Codex CLI itself. You know, for reference.[https://github.com/openai/codex](https://github.com/openai/codex)

- by [unknown](#) **&#x21C5; 1**
  <br/> This is honestly the best counterweight in the whole thread, and it calls out my exact blind spot: jumping straight to building a second system instead of fixing the repo itself.

You're completely right about the token trap. Adding an external memory daemon, ingestion pipelines, and retrieval layers just burns tokens to solve a problem caused by an unhelpful repo setup. If the agent gets stuck in a 20-minute CSRF loop, that’s not a memory failure—that’s a repo clarity failure. The harness was hostile to an agent, and I should have just made it obvious in the repo instead of trying to make an AI "remember" it from an external DB.

The AGENTS.md / dedicated skill approach is so much simpler. Having a testing skill or a small test guide in the repo directly costs practically nothing, lives right in git, branches naturally, and never drifts or needs a sync daemon.

Checked out Matt Pocock's retro skill—running that after a heavy session to immediately convert friction into repo improvements or skills is brilliant. Also hadn't seen rtk, but trimming massive tool output is a huge win since raw command spam eats so much context.

Taking a hard step back from building a bespoke memory layer. Going to clean up the repo ergonomics, set up proper skills for the test harness, and check the Codex CLI source before writing a single line of memory code. Appreciate the reality check.

- by [unknown](#) **&#x21C5; 1**
  <br/> I'm currently in the middle of building such a solution for my Reverse Engineering Research projects. They're very open-ended, sometimes claims that are registered in documentations end up being wrong/disproven and that is registered on a separate new document, sometimes I bounce from one model from one provider to another, it eventually accumulates hundreds of markdown files, random dumps and overall crap.

For now my intended design is basically a daemon/MCP server that specifically constructs a structure around the kind of research checkpoints that I have (there's Claims, Assertions, Evidence, Artifacts, ArtifactSpans, Entities, among other things). The MCP server offers some useful commands to query the current knowledge database and to persist the findings of a turn using those structures and it generates a canonical transaction JSON file that I can use to rebuild the databases. The list of transactions in the repository is my source-of-truth. With each operation, besides generating the canonical transaction JSON file, it also persists the findings in two databases. SQLite and Neo4j. Neo4j is used as basically the living context offering things like indexing and full-text search. SQLite works as the actual library the agent can choose to manually query if it wants. Since Neo4j is graph-based, it can break findings into very small separate pieces that can be found later and related information can be pulled on-demand by the agent.

It's not done yet, so I can't really say if it's gonna work better than what I currently have or not, but I'm optimist about it.

- by [unknown](#) **&#x21C5; 1**
  <br/> This makes a ton of sense for your use case. In reverse engineering or open research, you don’t have a compiler or automated test suite telling you what’s true—the claims, evidence, and disproven notes *are* the actual knowledge you're building, so a Neo4j graph tracking that makes complete sense.

My situation is basically the opposite, which is why I’m trying hard not to build a second database system.

I’m building a standard web app (Laravel/React). In my world, the ultimate truth already exists: it’s the Git repo, the database migrations, and the test suite.

To give you a real example of what I’m fighting: in a recent session, I watched my agent burn through half of my 5-hour quota simply because it didn’t know how our test harness worked. It spent 30 minutes retrying tests, failing on a CSRF middleware check, reading the same controller files over and over, and doing raw regex searches across the entire repo to trace relationships that were already written in the code.

The agent didn’t need an ontology of claims or an entity graph. It just needed two practical things:

  1. *"Don't try to disable CSRF in tests; use a real session token. Docker services run under path X."*
  2. Working AST/LSP tool (like Serena) so when it needs to inspect a service, it jumps directly to the function definition instead of brute-force searching 15 files.

If I set up Neo4j, SQLite, transaction logs, and claim tracking for a web codebase, I'd end up maintaining a complex data pipeline parallel to my actual product. And the moment someone refactors a class without updating the graph, the graph becomes stale and misleading.

For open-ended reverse engineering, treating findings as an immutable transaction log sounds like the right call. But for building software, I’m realizing my solution needs to stay as boring and lightweight as possible: a small, read-only orientation cache at session start, and letting the source code and tests remain the only source of truth.

- by [unknown](#) **&#x21C5; 1**
  <br/> In my experience playing deeply with things like Lazy Graph RAG, I've discovered these systems aren't particularly great. If you disable or augment an agent's self managed search and exploration, you're often caught in a potential misunderstanding or, worse, a lie. And the computational cost of devolving your knowledge base into small pieces is extremely expensive. And then try to consider pulling disparate chunks of knowledge from across your data together as a single 'memory' or gauging how important or relevant something is. Not trivial. I'm curious about where you're starting and what base you're starting from....

- by [unknown](#) **&#x21C5; 1**
  <br/> Spot on about Graph RAG—devolving code into fragments just trades one problem for an expensive hallucination engine.

My base is a Laravel + React production app handling financial logic (clearing transactions, multi-tenancy, accruals). Zero room for error.

I built a multi-agent setup (Planner → Implementer → Reviewer), but hit brutal churn: the agent would burn half my 5-hour quota running raw rg searches and failing 30 minutes of tests over a stupid CSRF harness quirk.

My knee-jerk reaction was to build an external memory engine (SQLite/watchers). But like you said, chunking that stuff out just creates a second out-of-sync codebase that lies to the model.

Dropped the external memory idea completely. Moving to:

  1. Putting harness gotchas right into AGENTS.md / repo skills (lives in git, zero drift).
  2. Proper AST/LSP navigation instead of RAG chunks so it reads live code directly.
  3. Trusting test suites over any external "memory."

What kind of domain are you running Lazy Graph RAG on? Codebases or open-ended text?

- by [unknown](#) **&#x21C5; 1**
  <br/> I was testing it against legal corpuses. Basically find evidence of some claim across time in a corpus full of opposing and incorrect information. Incredibly hard task.

- by [unknown](#) **&#x21C5; 1**
  <br/> It's not perfect - but I've found serena to help with those searches. You could probably use any other tool that provided a semantic tooling layer leveraging an AST on top of your codebase. I don't have laravel; but I've been working in a react project a lot lately (python back end).

- by [unknown](#) **&#x21C5; 1**
  <br/> Nobody reading all that or considering this over a lab full of PhDs

- by [unknown](#) **&#x21C5; 1**
  <br/> I’ve built one at home and at work.

Basically you want mini rag, with a self reranking observer. It can talk to local models or use the embed and such from provider.

Edit: bah kid hit submit.

This should fire off of hooks: session start, pre/post tool use, etc.

Honestly for quick code search, it’s hard to beat ast-bro (no not affiliated, it’s just goddamn fast).
