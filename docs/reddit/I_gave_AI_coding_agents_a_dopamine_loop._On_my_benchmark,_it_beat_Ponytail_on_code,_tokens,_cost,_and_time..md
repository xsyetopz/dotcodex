#I gave AI coding agents a dopamine loop. On my benchmark, it beat Ponytail on code, tokens, cost, and time. [Visit](https://www.reddit.com/r/OpenaiCodex/comments/1vn0fqo/i_gave_ai_coding_agents_a_dopamine_loop_on_my/)
### **Subreddit:** [r/OpenaiCodex](https://www.reddit.com/r/OpenaiCodex)
### **Author:** [AutoProspectAI](https://www.reddit.com/user/AutoProspectAI/)
### **Vote:** 24
---
[](https://preview.redd.it/i-gave-ai-coding-agents-a-dopamine-loop-on-my-benchmark-it-v0-trorpmkgj2jh1.png?width=1194&format=png&auto=webp&s=18d9fa783df3748c4810408f8809bd523e4fd28f)
Coding agents often mistake motion for progress. Ask for a small endpoint and you may get a new service layer, repository abstraction, response wrapper, and configuration system before the route even exists.
I built Dopamine to change that behavior. It is inspired by the way prediction and feedback guide human effort. The agent predicts the result, takes the cheapest useful action, measures what happened, adjusts, and stops when the request is verified.
Before creating custom code, it checks whether the behavior already exists, whether configuration is enough, whether the project already has the right helper, whether the platform provides it, and whether an installed dependency solves it. It writes something new only after the cheaper options fail.
I evaluated it on 12 tasks in a real open-source repository. Across four runs per task, Dopamine completed 48 trials with no timeouts or nonzero exits. Compared with the no-skill agent, it used 63.8% less source code, 29.7% fewer tokens, 27.9% less estimated cost, and 31.1% less time.
It works with Codex and Claude Code, includes a dependency-free installer, and has no telemetry, runtime service, or secrets. MIT licensed.
[github.com/ujjwalredd/Dopamine](https://github.com/ujjwalredd/Dopamine)
Progress that cannot be verified is just expensive motion.
UPDATE:
A benchmark that rewards smaller output has an obvious weakness: an agent can appear efficient by leaving work unfinished.
Instead of hiding that problem, I published the complete evaluation and its limits.
Dopamine is an open-source skill that makes agents choose effort based on uncertainty, test predictions against evidence, and stop at the smallest verified result. It reduces unnecessary work without treating validation, security, or correctness as optional.
The evaluation uses a pinned real repository, 12 identical tasks, isolated workspaces, one model, one reasoning level, recorded usage events, Git-based LOC measurement, and reproducible reporting. Dopamine ran four times per task; the comparison results remain frozen at one run per task to avoid later model and service drift.
Against the recorded Ponytail result, Dopamine measured 3.7% less source code, 15.2% fewer tokens, 11.8% lower estimated cost, and 7.4% less wall time. It finished lowest on all four measured efficiency metrics in this development benchmark.
That does not prove universal superiority. The tasks were used while tuning Dopamine, competitor variance is unknown, and feature completeness was not executable-graded. Those limitations are published beside the results because a defensible claim needs boundaries.
The repository includes the raw trials, hashes, benchmark harness, rejected candidates, chart generator, installer, and reproduction instructions. Anyone can rerun it, challenge the method, or build a stronger holdout.
Repo and full benchmark: [github.com/ujjwalredd/Dopamine](https://github.com/ujjwalredd/Dopamine). If the result breaks under a better test, I want the test.
---
## Comments 1

- by [unknown](#) **&#x21C5; 1**
  <br/> This is cool will test this
