#GPT-6 Astra killed 12 normal repo-work turns as ‘cybersecurity risk’ [Visit](https://www.reddit.com/r/codex/comments/1w8wp87/gpt6_astra_killed_12_normal_repowork_turns_as/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [50victor](https://www.reddit.com/user/50victor/)
### **Vote:** 1
---
Has anyone else had Astra do this during ordinary repository work?
Between September 4 and 6, I had 12 turns across 8 GPT-6 Astra sessions end with:
“This content was flagged for possible cybersecurity risk.”
These were not security jobs. They were ordinary tasks on a local Flask repo: changing implementation and tests, reviewing patches, running local Docker tests, and calibrating a coding challenge. No scanning, exploit work, credentials, malware, external target, or network testing was involved.
The strangest part is how harmless some of the immediate prompts were. A few were literally:
- “go”
- “run 20 at once for next iterations”
- a target for solve-rate/test calibration
- “trigger 3 batches until we have at least 1/3 TP solves”
It also tends to happen late. Altogether, the killed turns had been running for about five hours. The worst one died after roughly 99 minutes and another after roughly 79 minutes. So this isn’t just a quick refusal — the classification can discard the useful result of a long repo run.
I checked the local session logs. All eight used GPT-6 Astra, and every failed turn ended with codex_error_info: “cyber_policy”. Five were normal user-facing Codex tasks and three were internal review/audit tasks. I’m using Codex Desktop on Windows, and it happened across bundled CLI versions 0.153.1 and 0.153.4.
And the cherry on top: my account is approved for Daybreak / Trusted Access for Cyber. But plain Flask repository work obviously should not need cyber approval in the first place.
My guess is that accumulated terms like “hidden tests,” “audit,” “solver,” and “candidate” are tripping a classifier without enough attention to the surrounding context. I’m sending the exact session IDs to OpenAI support privately.
Has anyone seen the same behavior specifically with Astra? If so, did rewording actually fix it, or did the classification return later in a long task?
---
## Comments 3

- by [unknown](#) **&#x21C5; 1**
  <br/> I had it with sol, not astra yet, but im fairly sure with astra its even more sensitive and triggers far more false positives, i found gpt 5.5 to have MUCH less false positives as it is an older classifier.

There really isnt much they could do for you, they wont fix it because one guy sent an email to support about it, anthropic though fixed their classifiers, when fable 5s classifier was too much they noticed it and they did make it more accurate for fable 5.1 but seemingly openai doesnt care lol.

- by [unknown](#) **&#x21C5; 1**
  <br/> yes, I also wanted to check by this post if others are also facing this issue

- by [unknown](#) **&#x21C5; 0**
  <br/> use /feedback
