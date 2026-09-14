#I tested open-so"save 90% of your tokens" tools to beat my Astra limit. The model spent more tokens deciding which command to run than the tools ever saved. [Visit](https://www.reddit.com/r/codex/comments/1wbm4eq/i_tested_opensosave_90_of_your_tokens_tools_to/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Delicious-Flan88](https://www.reddit.com/user/Delicious-Flan88/)
### **Vote:** 4
---
5 coding tasks, GPT-6 Astra with a bash tool, 4 setups (no tool / RTK / Headroom / both, the two most-starred open-source token-saving repos on GitHub), 3 runs each. 60 sessions, all correct, priced at API rates with cache.
RTK beat no-tool in every run on one task, a multi-file grep (87 lines to 29). Headroom's win on its JSON task: $0.0054 vs $0.0066. Everything else moved more with the model's own command choices than with any tool: one cell went 2, 5, 9 turns across three runs because Astra kept re-running a directory listing.
Every command and answer, per run: [https://astra-token-burn.vercel.app](https://astra-token-burn.vercel.app)
---
![I tested open-so"save 90% of your tokens" tools to beat my Astra limit. The model spent more tokens deciding which command to run than the tools ever saved.](https://preview.redd.it/i-tested-open-so-save-90-of-your-tokens-tools-to-beat-my-v0-op6nsgv30ioh1.jpeg?width=640&crop=smart&auto=webp&s=d9e6c79f1555557f8a43e6739d7216d3c7ab180f)
---
## Comments 0

