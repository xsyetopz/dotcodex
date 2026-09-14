#How do you stop Codex from overengineering, losing context, and repeatedly ignoring a known-good workflow? [Visit](https://www.reddit.com/r/codex/comments/1wbkgw5/how_do_you_stop_codex_from_overengineering_losing/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [yallapapi](https://www.reddit.com/user/yallapapi/)
### **Vote:** 1
---
I’ve been using Codex to automate an existing AI-video pipeline. I already have a known-good batch and repeatedly told it to inspect that exact workflow, preserve it, and automate only the manual judgment points.
Instead, Codex repeatedly:
- Invented new scripts and logic instead of modifying the working pipeline.
- “Simplified” away important steps that were performed manually.
- Tested unrelated parts instead of fixing known failures using existing bad outputs.
- Proposed solutions without verifying them.
- Forgot decisions made earlier in the same conversation.
- Turned simple API calls into long investigations and status updates.
- Claimed something was incorporated into the workflow when it was only handled manually for one output.
- Responded to corrections by starting over or adding more process instead of fixing the specific failure.
- Repeatedly explained why the output was bad without actually converting that diagnosis into a reproducible workflow.
The core problem isn’t one bad prompt. It’s the agent’s working habits: scope drift, premature implementation, unnecessary architecture, failure to distinguish manual intervention from automation, and failure to preserve a verified reference implementation.
Has anyone found a genuinely tested way to constrain Codex so it:
- Treats an existing successful output and its provenance as authoritative.
- Changes only the identified broken component.
- Uses real failures as regression tests.
- Verifies each change before continuing.
- Doesn’t invent infrastructure unless explicitly requested.
- Maintains an accurate ledger of what is automated versus manual.
- Stops claiming completion until the exact end-to-end workflow passes?
I’m specifically interested in approaches people have measured in real projects—not generic “write a better AGENTS.md” advice.
---
## Comments 9

- by [unknown](#) **&#x21C5; 4**
  <br/> ALL CAPS SCREAM AT IT TO FOLLOW INSTRUCTIONS Or you can tell it that you will use Claude instead.

(it's a joke)

- by [unknown](#) **&#x21C5; 3**
  <br/> i tried this didn't work, insulting its mother didn't work either

i tried "make no mistakes" and "do it right this time", neither of those worked

- by [unknown](#) **&#x21C5; 1**
  <br/> but its true though :D

- by [unknown](#) **&#x21C5; 1**
  <br/> Try using something like grill with docs to drive alignment and keep implementations smaller.

- by [unknown](#) **&#x21C5; 1**
  <br/> Try higher reasoning levels, and if you are using Sol try Astra. Sol over-engineers at every turn.

- by [unknown](#) **&#x21C5; 0**
  <br/> i switched immediately to astra when it came out, ended up switching back 24 hours later, found it quite awful tbh. same issues. switched back to sol and it is slightly less bad.

- by [unknown](#) **&#x21C5; 1**
  <br/> Not AGENTS.md advice, because you're right that it doesn't hold. Three things that are mechanical, from a pipeline project with the same failure list as yours.

The known-good batch becomes read-only for the agent, literally: a pre-tool hook or deny rule on writes to the pipeline files and on creating new top-level directories. "Invented new scripts instead of modifying the working pipeline" stops being a habit you argue with and becomes a refused call with the rule named in the refusal. The agent can read everything, it can write only under the one folder you allow for this task.

Every bad output you already have goes into a folder and the definition of done is one sentence in the task file: "the golden batch reproduces byte-for-byte and these N bad cases are fixed". Not "automate the workflow". With that sentence the "tested unrelated parts" and "claimed completion" items die together, because completion has a command the agent has to run and show.

The manual-versus-automated ledger is a file the agent must update on every change, and a hook that refuses the commit if the ledger wasn't touched. Prose asks it to remember; the hook makes forgetting cost the commit.

The pattern in all three: anything you've corrected twice gets moved out of the conversation and into something that fires before the tool call. Your list of nine failures is really two mechanisms and one sentence.

- by [unknown](#) **&#x21C5; 0**
  <br/> Agents.MD as an overview of instructions.

Then:

codex/ projectArchitecture.md securityGuidelines.md uiDesign.md Etc etc (edit with your needw)

If you define everything you want there, codex will follow it always.

- by [unknown](#) **&#x21C5; 0**
  <br/> Matt Pocock. You are welcome.
