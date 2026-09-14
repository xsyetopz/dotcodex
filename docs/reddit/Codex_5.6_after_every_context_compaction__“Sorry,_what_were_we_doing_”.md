#Codex 5.6 after every context compaction: “Sorry, what were we doing?” [Visit](https://www.reddit.com/r/codex/comments/1w8sqon/codex_56_after_every_context_compaction_sorry/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Medium-Philosophy942](https://www.reddit.com/user/Medium-Philosophy942/)
### **Vote:** 1
---
**Codex 5.6 after every context compaction: “Sorry, what were we doing?”**
Is it just me, or has Codex 5.6 been genuinely lobotomized?
You spend an hour explaining the project, showing it the architecture, correcting its assumptions, establishing constraints, and repeatedly telling it which approaches have already failed. Eventually, through patience and what I can only describe as unpaid neurological rehabilitation, it finally understands the task.
For five glorious minutes, it works beautifully. It knows the files, remembers the decisions, understands the dependencies, and even stops trying to rewrite half the project for no reason.
Then the context gets compacted.
Suddenly, this digital douche wakes up in the middle of the repository like a dementia patient abandoned at a bus station:
“Could you remind me what we were working on?”
My brother in artificial intelligence, **you were working on it twelve seconds ago.**
You wrote the code. You ran the tests. You explained the bug to me. You created a detailed plan. Now you’re staring at your own changes like police have just shown you crime-scene photographs.
Then begins the ritual.
It reopens every file it already inspected. It “discovers” problems we discussed forty minutes ago. It proposes the exact solution we rejected three times. It asks whether a function should behave in the way explicitly documented directly above it. Then it proudly announces a new plan that is just the original plan with several important details removed.
Context compaction is apparently less like summarizing a conversation and more like performing an emergency lobotomy with a rusty spoon.
Before compaction:
“I’ve analyzed the architecture and identified the precise interaction causing the issue.”
After compaction:
“Interesting project! What does this button do?”
And the best part is how confidently it forgets. It doesn’t merely lose context—it replaces the missing memories with fan fiction. Suddenly, decisions you never made become “previously agreed requirements,” files it created become mysterious legacy code, and its own broken implementation becomes something “the existing codebase appears to do.”
No, mate. The existing codebase didn’t do that. **You did that fifteen minutes ago.**
Working with it now feels like supervising a brilliant engineer who suffers a catastrophic head injury every hour but is immediately returned to work because management noticed he can still type.
You carefully rebuild its understanding, remind it what happened, and lead it back toward the task. It nods, reconstructs the plan, regains competence, and starts making progress again.
Then another compaction happens.
“Hello! I’ll begin by inspecting the repository.”
At this point, I’m not developing software with an AI assistant. I’m trapped in a low-budget psychological horror game where the only other character keeps losing his memory, rearranging the furniture, and insisting we have never met.
Codex 5.6 isn’t maintaining context. It’s repeatedly dying and leaving a poorly written note for its replacement.
Apparently, that note just says:
“Some files exist. The user seems upset. Ask what we’re doing.”
---
## Comments 12

- by [unknown](#) **&#x21C5; 3**
  <br/> I use codex at work a lot and imo the most efficient way is to plan the work first devide it into reasonably sized tasks/milestones and solve them one by one. Trying to one-shot the whole thing is usually a pain. I would say that for me the sweetspot is <1000 rows of code per one change (also because as of now any LLM's code is stil garbage and we do code-reviews, reviewing several thousands at onece is a pain, brain also runs out of context lol) . Everything larger starts to run into context problems. For a task of this size it is usually completed before compaction. And even if you run into compaction it does not forget your intent and requirements. You also need to remember that attention is U-shaped (more attention for beginning and end of context) so if you spend really long time explaining your goal you risk to have important details in a low-attention region of the context.

If you really want to one-shot your big task, stop writing it in the chat. You need to have your requirements in a file, so model can re-read it at any time. This will help with compaction and attention issues. Ofc if you like "chat" style of work just ask it to write your requirements in a documentation file before the actual implementation. We also use this approach when working on something bigger like a project-wise design/archetecture for example.

- by [unknown](#) **&#x21C5; 2**
  <br/> If you expect the task to be long, start with having it writr .md with a specification of what needs to be done and what is the definition of done. It is a good idea anyway, because if you cant do that, then you do not understand what you are trying to achieve to begin with.

- by [unknown](#) **&#x21C5; 2**
  <br/> Also just use an orchestrator to summon an orchestrator. You can run for days

- by [unknown](#) **&#x21C5; 2**
  <br/> the fix is writing a handover doc for a coworker who quits every 40 minutes. congrats youre middle management now

- by [unknown](#) **&#x21C5; 1**
  <br/> When working on any task that is large enough to require compaction, you need to externalize the task status and progress updates. I use GitHub issues for this, but you could also use simple markdown documents.

- by [unknown](#) **&#x21C5; 1**
  <br/> I always ask ok lets create a jira now, lets create an md file, make sure these point are in there, or ok lets split into multiple sub jiras, or lets create a spec if it is going to be a large work. context size limitation is real. one final suggestion, don’t use basic models for compaction, use the same model or better if you want to keep the important stuff.

- by [unknown](#) **&#x21C5; 1**
  <br/> Hmm strange. I have never seen this compacting issue, ever.

- by [unknown](#) **&#x21C5; 1**
  <br/> "It proposes the same solution that we rejected three times"

That's why we install Basic Memory and instruct it to auto save every kind of conclusion, rejection, implementation and milestone it has come to and ask it to auto read through it every now and then/before it thinks about a new solution. Much less amnesia when it can enlighten itself of where it was/is. You talked about X a few hours ago and now want to talk about it again? No more amnesia. It works across all chats, accounts, models, companies you want it to.

- by [unknown](#) **&#x21C5; 1**
  <br/> you need to do it yourself, you need to manage your context for ai by applying basic software engineering principles

- by [unknown](#) **&#x21C5; 1**
  <br/> I just don't understand how Codex handles compaction because this can't be right. My observation is that every compaction cycle it answers the last query every time - even if it was 5 compaction windows ago.

- by [unknown](#) **&#x21C5; 1**
  <br/> The "replaces missing memories with fan fiction" line is painfully accurate. What actually helped me was getting the decisions out of the chat, since that is the first thing compaction shreds.

Positive__Altitude is right that a requirements file helps, but a flat [spec.md](http://spec.md) drifts too: it captures the plan on day one and nobody edits it when you reject approach A on day three, so after compaction the model happily "rediscovers" A.

What stuck for me was writing the record as it happens onto a GitHub issue per unit of work: what we tried, why we rejected it, what is next, and the acceptance check. Compaction cannot fan-fiction over that because it lives on the issue, not in the rolling context, and a fresh session rereads the ticket instead of guessing.

Full disclosure, I got tired of hand-rolling this and built an open source thing around it (trailhead), so I am biased. But you can do the same by hand: one issue per decision, updated when the plan changes, and make the agent read it before touching code.

- by [unknown](#) **&#x21C5; 0**
  <br/> The 'note for its replacement' bit is exactly it. Compaction reduces the session to a summary, and your earlier corrections are the first thing a summarizer drops, they read like back and forth instead of settled decisions. The model isn't faking it, it starts from a state where those fixes never existed. The workaround is keeping state in files, a short doc with the constraints and rejected ideas, commit after every step, so the reset session reloads the file and keeps working.
