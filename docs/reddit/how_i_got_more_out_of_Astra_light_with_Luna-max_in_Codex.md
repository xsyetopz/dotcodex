#how i got more out of Astra light with Luna-max in Codex [Visit](https://www.reddit.com/r/codex/comments/1wcuzn3/how_i_got_more_out_of_astra_light_with_lunamax_in/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [ismailihunzai](https://www.reddit.com/user/ismailihunzai/)
### **Vote:** 6
---
i use Astra light to make decisions and Luna-max for audits, searches, builds and tests. one child at a time. Astra waits for the result and doesn't repeat successful checks.
i tried a specialized routing hook for Luna, Terra and Sol before, but it didn't save me tokens. this setup worked better for me on Plus, including with goal.
- my settings in ~/.codex/config.toml (update the existing [agents] section):
- add to ~/.codex/AGENTS.md:
“After dispatching a subagent, call wait_agent with timeout_ms = 3600000. Wait for its result without short polling or routine status checks.”
*that's up to 1 hour, returning earlier when the child finishes. it's a tool-call instruction, not a config.toml wait setting.*
3. my per-thread prompt:
“Keep Astra in charge of decisions, integration and final acceptance. Delegate substantial audits, searches, builds, tests and log analysis to one Luna-max subagent with an exact scope. Wait once for up to an hour. Don't poll, overlap its work or repeat successful checks. Skip visual UI checks unless requested. Follow the existing Codex instructions.”
*attach to the end of your instructions.*
when a task is done, have handoff .md updated. start a new thread for the next task with that handoff and the prompt above alongside your own instructions. i don’t recommend waiting for the thread to fill its context and compress. new task, new thread. works for me.
---
## Comments 2

- by [unknown](#) **&#x21C5; 1**
  <br/> forcing max_depth=1 plus wait_agent up to an hour so Astra light doesn't busy-poll the Luna-max child is a clean Plus discipline. when you say the specialized routing hook didn't save tokens, was the waste mostly from overlapping children or from re-checking work the child already finished?

- by [unknown](#) **&#x21C5; 1**
  <br/> that specialized hook did not directly spawn endless children but it permitted overlapping read-only agents and added substantial lifecycle, guard, UI, and coordination context. the model still had to interpret those injections and often repeated checks
