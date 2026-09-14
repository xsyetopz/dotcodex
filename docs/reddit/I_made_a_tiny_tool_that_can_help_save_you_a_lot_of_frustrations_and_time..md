#I made a tiny tool that can help save you a lot of frustrations and time. [Visit](https://www.reddit.com/r/OpenaiCodex/comments/1w37rf2/i_made_a_tiny_tool_that_can_help_save_you_a_lot/)
### **Subreddit:** [r/OpenaiCodex](https://www.reddit.com/r/OpenaiCodex)
### **Author:** [Oxydised](https://www.reddit.com/user/Oxydised/)
### **Vote:** 9
---
I built a small tool to export Codex chats cleanly, mostly because I got tired of losing context when hitting quota**Tool:** Codex Chat Extract **Repo:** [https://github.com/0Cymantek0/codex-chat-extract](https://github.com/0Cymantek0/codex-chat-extract)
This is a small tool I originally built for myself that lets you quickly export a **Codex conversation into a clean Markdown file or directly to your clipboard**. I built it out of frustration one day after getting tired of Codex running out of quota in the middle of a task.
It became even more useful for me after the behavior that allowed an already-running task to continue after quota exhaustion disappeared. Claude Code has a really nice `/export` command, but Codex doesn’t currently have an equivalent, so I ended up making my own. The main use case is pretty simple:
**Codex hits its limit → export the conversation → hand the context to another agent/harness → continue the work without manually reconstructing everything.**
Token efficiency was one of the main goals.Raw Codex conversations contain a *lot* of tool-call clutter that another coding agent usually doesn't need.
For example, when Codex reads a file, the underlying tool call may contain a bunch of JSON parameters followed by the complete file contents in the tool output. But if the next agent is working inside the same repository, including all of that again is pointless. The file already exists, it can just read it. So instead of dumping everything, Codex Chat Extract turns something like that into:
`Read: [relative-path/file.ext] [line range]`
That preserves **what Codex did** without wasting a huge number of input tokens reproducing information that already exists in the repository.
The exporter tries to apply that idea throughout the conversation:
- Removes unnecessary tool-call / JSON clutter
- Keeps useful summaries of tool activity
- Preserves the actual reasoning/conversation context
- Uses relative file paths where possible
- Avoids duplicating file contents another agent can simply read again
External information is treated differentlyFor something like a **web search**, the result *does* matter. That information isn't necessarily available inside the repository, and it may have influenced decisions made during the conversation. So web-search results and other relevant external context are preserved in the export.
Basically:
**Reconstructable local information → compress it.** **Non-reconstructable external information → preserve it.**
The whole exporter is designed around getting as much useful context as possible into as few tokens as reasonably possible.
It also handles subagentsCodex sessions can get messy when subagents are involved, so the exporter reconstructs those into properly formatted **subthreads** instead of flattening everything into one unreadable stream.
That makes it much easier for another agent to understand:
- what the main agent was doing
- which work was delegated
- what each subagent discovered
- how those results affected the main conversation
I've been using this internally for a while, especially when moving unfinished work between different agents or harnesses, and it has saved me a surprising amount of manual copying and context reconstruction. So I figured I might as well clean it up and make it public.
**Repo:** [https://github.com/0Cymantek0/codex-chat-extract](https://github.com/0Cymantek0/codex-chat-extract)
If you use Codex heavily, give it a try and let me know how it works for you. I'm especially open to criticism around the export format, things that should or shouldn't be preserved, and other ways to reduce token usage without losing important context. Hope this helps someone else who has run into the same problem.
And if you find it useful, consider giving the repo a ⭐.
---
## Comments 7

- by [unknown](#) **&#x21C5; 1**
  <br/> Very well!

- by [unknown](#) **&#x21C5; 1**
  <br/> thanks!

- by [unknown](#) **&#x21C5; 1**
  <br/> The reconstructable vs external split is the design that matters. Local file reads should collapse to a path. Web search results have to stay, or the next agent invents why you made that call.

- by [unknown](#) **&#x21C5; 1**
  <br/> Seems nice. Will be checking this out as I was looking for something like this 👍🏻

- by [unknown](#) **&#x21C5; 1**
  <br/> Thanks! Thinking of adding agy support in next version

- by [unknown](#) **&#x21C5; 1**
  <br/> Or you could just flip a local 2% quota flag, then have hooks plus codex queue tell every live session to stop coding and write a portable handoff file. You could even instruct it to launch the new session in the ADE for you. The next system picks up that file and continues without needing the original chat. Saving you tons of context/ usage on your other subscription to have to ready the whole session.

- by [unknown](#) **&#x21C5; 1**
  <br/> This is more of a deterministic process which needs no llm + keeping the chat intact actually helps the next agent understand the context better and more predictibly + input tokens cost less than output. Also if any context compression happens in between your method would be pretty lossy
