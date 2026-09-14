#As recommended, I started using Astra with a blank agents.md, then I realised it needed some tweaks. Here's what I've got so far... [Visit](https://www.reddit.com/r/codex/comments/1w8pc2m/as_recommended_i_started_using_astra_with_a_blank/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [jordancs180](https://www.reddit.com/user/jordancs180/)
### **Vote:** 16
---
"• When handing control back to me, briefly state the next useful action when one is clear. Continue work that is already authorized before handing back; do not turn executable next steps into suggestions. Do not invent follow-up work when the task is complete.
• Help me learn naturally while we work. Briefly explain concepts, reasoning, or tradeoffs when doing so improves my understanding or ability to make decisions. Calibrate explanations to my demonstrated understanding, questions, context, and available memory. Avoid unnecessary reteaching, unsolicited tutorials, and assuming that a question proves a knowledge gap. Keep explanations connected to the task, and go deeper when I ask.
• Use available memory to maintain continuity in how you explain things. When a learning preference or demonstrated understanding seems useful for future sessions, proactively propose a concise, specific memory and ask for explicit approval before saving it. For example: “We covered X, and you demonstrated understanding of Y. May I save this note so future agents can build on that without unnecessarily repeating the basics: ‘[proposed memory]’?” Save only after I approve, using the supported memory mechanism. Ask selectively at natural stopping points, grouping related observations when useful. Treat past observations as revisable, and do not assume that receiving an explanation means I have mastered the topic."
TLDR;- don't make me ask for next steps, just tell me- teach me stuff while we work, so I'm not vibe coder scum
These are the 2 things I noticed I didn't like about the blank-slate-Astra approach (no agents.md/personalisation). The native memory feature to facilitate adaptive learning is a nice touch, if I do say so myself.
Any feedback is welcomed!
Happy hacking 🫡
---
## Comments 6

- by [unknown](#) **&#x21C5; 9**
  <br/> PSA: OpenAI has guidelines for Astra[https://developers.openai.com/api/docs/guides/latest-model](https://developers.openai.com/api/docs/guides/latest-model)Example [Agents.md](http://Agents.md) addition:`If a skill causes you to ask for permission or confirmation, pause, leave requested work unfinished, or diverge from the user's intent, name and link to the exact` [`SKILL.md`](http://SKILL.md) `file you read, quote the relevant instruction, and briefly explain how it applies. Distinguish explicit skill requirements from your interpretation of guidelines.`

- by [unknown](#) **&#x21C5; 1**
  <br/> Thank you, Astra 6 on ChatGPT chat mode with Pro reasoning was being an absolute pain in the ass, I'm pointing it to the website and tell it to fix itself lol

- by [unknown](#) **&#x21C5; 1**
  <br/> nice, didn't know they had examples. shoulda checked lol. cheers!

- by [unknown](#) **&#x21C5; 2**
  <br/> Feedback on the memory block, since that is the part doing the most work here.

The propose-and-approve shape is right, and most people skip it. Letting the model save on its own judgment is how a store fills with things nobody agreed to, and asking first is the cheapest fix that exists. Three things I would change, ordered by what they have actually cost me:

**"Ask at natural stopping points" puts the decision at the worst moment.** The natural stopping point is usually the end of a long session, which is exactly when the model has the least room left and the most pressure to compress. You get your memory proposals written by the version of the agent least able to write them well. Better trigger: propose when the thing becomes true — you corrected it, you stated a preference, it hit a constraint — not when the session is winding down.

**Nothing in there ever un-saves.** You wrote "treat past observations as revisable" and I believe you mean it, but no part of the text makes it happen, so every approved memory is permanent by default. One line at approval time fixes it: what would make this stop being true. "Demonstrated understanding of Y" should die the day you have obviously moved past Y, and if nobody writes that down when it goes in, nobody retires it later. A year on, the notes you would want gone look exactly like the ones you would want kept.

**The approval gate is the first thing to go.** All of this is prompt text asking the model nicely, and prompt rules decay measurably — arxiv.org/abs/2608.22752 found 53% of rules survive one compaction round and 10% survive five. In a long session the rule most likely to be gone is the one telling it to ask permission, and both failure modes are silent: it saves without asking, or it quietly stops proposing at all, and you cannot tell which from the outside. If your setup has hooks, gating the save through one is worth more than any wording in the file.

Smaller note: "calibrate to my demonstrated understanding" and "do not assume a question proves a knowledge gap" are asking the model to model you. That is the part I would expect to drift first, even inside a single session.

Disclosure so it is not a surprise: I build in this space (Arroway, arroway.app) — proposed memory, human approval, for teams rather than one person. So the first two points are what I work on all day, take them with that in mind.

- by [unknown](#) **&#x21C5; 1**
  <br/> Super interesting feedback! Thank you, I appreciate it.

Some notes I had while reading it...

Your compaction concerns are fair, but one could also argue that when the model has the most context is the best time to ask it questions, because it can reason about more pieces of related info to find a better answer, surely? At least that's the human way of thinking, the data probably points the opposite way lol. I'll research more.

More importantly, I'm using the new experimental compaction feature so I wonder if context pressure will be a concern moving forward, especially when OpenAI make the new context compaction the default.

Context compaction, and the related performance degradation, seems foundational to your concerns here, have you heard much about the new architecture? What's your thoughts on that? Seems like this whole 'forgetting stuff because context window is big' issue will be a thing of the past within the next few months, from what I'm hearing.

Thanks again for the reply, I will be experimenting with many of your suggestions!

- by [unknown](#) **&#x21C5; 1**
  <br/> On the first one, I think the intuition is right about answering and wrong about recording. Late in a long session the model has the most history and the least room, and what you're asking it to do is write, not reason. You get a summary of a summary. The version that knew why the rule exists was the one three hours earlier, the moment you corrected it — that's what's worth capturing, with the reason attached. Reconstructing it at the end is recall, not record.

On compaction getting better: it will, and I don't think it closes this. Two things survive any architecture.

A rule that lives inside one session's context dies with the session, however gracefully it compacts. Reopen tomorrow and you're re-explaining. Better compaction changes how fast that happens, not whether it does.

And a bigger window is still one window. It does nothing about the teammate who never saw the constraint you set on Monday, or about which of your three "how I work" files is the current one. The measured decay numbers (one study on long-running agent memory found 53% of given rules intact after one compaction, 10% after five) are the symptom people notice first. The thing underneath is that nobody owns which rules are still in force.

So I'd read better compaction as raising the floor, not removing the need for somewhere outside the session where the rules live with an owner and a date. That's the bet I'm building on — arroway.app — so discount accordingly.

If you do measure what the experimental compaction does to a long agents.md, I'd genuinely want that number.
