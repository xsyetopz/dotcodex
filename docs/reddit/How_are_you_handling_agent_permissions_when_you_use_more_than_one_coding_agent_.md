#How are you handling agent permissions when you use more than one coding agent? [Visit](https://www.reddit.com/r/OpenaiCodex/comments/1w09r13/how_are_you_handling_agent_permissions_when_you/)
### **Subreddit:** [r/OpenaiCodex](https://www.reddit.com/r/OpenaiCodex)
### **Author:** [iamarpitpatidar](https://www.reddit.com/user/iamarpitpatidar/)
### **Vote:** 2
---
I run Claude Code alongside Cursor and Codex on the same repos, and I keep hitting the same annoyance: each one defines what the agent is allowed to do (shell, file writes, git) in its own format. I update the deny list in one and forget the others, and they drift apart.
Curious how others deal with this:- Do you just maintain each config by hand?- Have you standardized permissions across tools somehow?- Or does it not bother you enough to fix?
I ended up building a small tool to define permissions once and generate the config for each runtime ([https://itslab42.github.io/agentctl/](https://itslab42.github.io/agentctl/)), but I'm more curious whether others feel this pain or if I'm over
---
## Comments 6

- by [unknown](#) **&#x21C5; 2**
  <br/> I run cursor $200, grok bot & codex on the same repos and I just let the deny lists drift lol. have not successfully kept them in sync

- by [unknown](#) **&#x21C5; 1**
  <br/> Same drift pain. I keep one deny list as the source of truth and generate the Cursor / Claude / Codex shapes from it. The day anyone hand-edits a runtime file, the lists diverge again by Friday.

- by [unknown](#) **&#x21C5; 1**
  <br/> hehe, yea shit happens. now what about other guarails, how u manage those?
