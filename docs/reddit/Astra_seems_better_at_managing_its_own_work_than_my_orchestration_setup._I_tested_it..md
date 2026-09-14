#Astra seems better at managing its own work than my orchestration setup. I tested it. [Visit](https://www.reddit.com/r/codex/comments/1wcqfj4/astra_seems_better_at_managing_its_own_work_than/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Hot-Tale-6438](https://www.reddit.com/user/Hot-Tale-6438/)
### **Vote:** 4
---
After switching to Astra, I noticed something annoying: the orchestration setup that had felt useful with GPT-5.6 Sol and my Claude workflows was now making some tasks **slower and more expensive**.
So I tested it on real coding tasks from my repo, changed the orchestration rules, and tested again.
**My conclusion so far: I’d let Astra manage its own work before adding another layer telling it how to delegate.**
Here’s what I tried.
Just a heads-up: English isn't my first language. I ran the tests myself and wrote \ dictated the original text in my own words, then used AI to translate it and tidy up the wording a little. Please keep that in mind :)
1. Small, medium, and larger tasks — with and without orchestration rulesThe small task was a build-command fix involving log preservation and exit codes.
The medium task was selective CI, including dependencies between applications.
For larger tasks, I used two different briefs:
• One explicitly specified error-filtering and backend-diagnostics changes across three apps.
• The other described an outcome: stop development services without leaving child processes running or killing unrelated processes.
For each pair, I used the **same starting code and the same task prompt**, but separate working copies.
One agent got the orchestration skill. The other didn’t.
Results from the earlier rule version**Small task**
• Time: **+25%** with orchestration rules• API-equivalent cost: **+13%**
**Medium task**
• Time: **+18%**• API-equivalent cost: **+20%**
**Large task — explicit brief**
• Time: **+63%**• API-equivalent cost: **+71%**
**Large task — outcome-based brief**
• Time: **−45%**• API-equivalent cost: **−36%**
That last task was a real win for the orchestration rules.
**But there’s an important catch: it used zero subagents.**
So it didn’t actually demonstrate a benefit from distributing the work.
Quality didn’t consistently improve either.
Both medium-task solutions missed dependencies.
On the large explicit task, the orchestration version missed filtering edge cases that the default version handled, **despite having an independent reviewer**.
2. Simplify the rules and repeatNext I reduced the coordination overhead.
I:
• added a direct path for small tasks• shortened handoffs• made independent review depend on risk• allowed cheaper workers for limited tasks
The final series had **12 runs** across small and large tasks.
For the large task, using the median of two runs per configuration:
Configuration
Time
Cost
Default Codex
5.9 min
$7.09
Revised + Astra
9.0 min
$7.79
Economy
10.5 min
$10.38
Every configuration passed the external checks in **one of its two runs**.
So more coordination still **didn’t buy a better pass rate**.
The economy profile never actually selected a cheaper worker, so I don’t consider that result evidence against Luna.
The small task also went better with the revised Astra profile: it was faster, roughly the same cost, and all checks passed.
3. Test the worker models separatelyI also compared **Astra low vs. Sol high**, without subagents.
On the medium task:
**Astra low**
• 5.2 minutes• $1.48
**Sol high**
• 16.3 minutes• $2.05
Both missed cases, but **Sol missed one more**.
On the small task, Astra was faster, but Sol was cheaper and correct, while Astra introduced a quoting bug.
Then I ran a tightly specified function-writing test.
**Luna max was about 17× cheaper and 2.4× slower than Astra low.**
Both passed the same **15 checks in both repeats**.
That comparison excludes coordinator review and integration costs.
So I do think cheap workers can make sense.
**What I haven’t established is that adding a coordinator makes the whole task cheaper.**
Where this leaves meFor my Astra workflow, I currently don’t see a reason to impose a separate orchestration system.
**Ordinary Codex delegation with light repo-level guidance looks like the better default.**
The direction I’d still explore is Astra coordinating models from other families — for example, an Opus implementation worker or another model doing cross-review.
That’s where I’d expect complementary capabilities to potentially matter.
But that’s still a hypothesis. These tests didn’t prove it.
I’ve also seen similar experiences posted by others, which makes me wonder whether extra orchestration contributes to people burning through subscription limits.
In my earlier tests:
• Small task: recorded tokens increased by **46%**• Medium task: recorded tokens increased by **25%**• Explicit large task: recorded tokens **nearly doubled**
---
## Comments 5

- by [unknown](#) **&#x21C5; 4**
  <br/> Anecdotal but I dumped all of my previous setups and use raw codex + Astra medium/high. Seems to perform way better overall.

- by [unknown](#) **&#x21C5; 2**
  <br/> It seems that this really works better)

- by [unknown](#) **&#x21C5; 1**
  <br/> the awkward bit is the outcome-based brief winning while using zero subagents. if that win was better prompting not distribution, what are you actually keeping from the orchestration skill vs cutting entirely for Astra?

- by [unknown](#) **&#x21C5; 1**
  <br/> Yeah, that's a fair point. The zero-subagent win doesn't prove delegation helped. It could just be the prompting, or variation between runs.

For Astra, I'd probably keep two or three lines in AGENTS.md: check the actual behavior, get an independent review when the risk calls for it, and delegate when it makes sense. Let it decide how. I don't think it needs a whole skill prescribing that process when it's the main agent.

Luna can still save money on simple, clearly defined work. It did in our small function test, though it was slower. My concern with bigger tasks is that splitting them into small pieces doesn't automatically make them easy. If Astra ends up fixing everything afterward, the savings can disappear. I'd rather explicitly say “give this bit to Luna” when I see a good fit than make that the default.

I also wouldn't extend this conclusion to setups mixing providers, like Astra coordinating Claude workers, or the other way around. We didn't test that. There might be value there, but it needs its own comparison

- by [unknown](#) **&#x21C5; 1**
  <br/> yeah the 2-3 [AGENTS.md](http://AGENTS.md) lines (check behavior, risk-gated review, delegate when it fits) feels like the right ceiling. explicit "give this bit to Luna" beats a default split that Astra then rewrites anyway. mixed-provider is the experiment I'd be curious about next.
