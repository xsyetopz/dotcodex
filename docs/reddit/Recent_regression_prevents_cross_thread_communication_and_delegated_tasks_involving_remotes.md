#Recent regression prevents cross thread communication and delegated tasks involving remotes [Visit](https://www.reddit.com/r/OpenaiCodex/comments/1w1tdzr/recent_regression_prevents_cross_thread/)
### **Subreddit:** [r/OpenaiCodex](https://www.reddit.com/r/OpenaiCodex)
### **Author:** [mldevvv](https://www.reddit.com/user/mldevvv/)
### **Vote:** 1
---
I’m trying to raise some visibility around what looks like a pretty serious Codex Desktop regression affecting inter-task / multi-agent workflows.
For at least the past week, cross-task communication has effectively been broken for me.
Previously, Codex tasks could use first-party inter-task tools such as `send_message_to_thread`, `create_thread`, and `handoff_thread` to coordinate with other tasks. Now the behavior is inconsistent depending on the session:
- Older/retained tasks may still expose `send_message_to_thread`, but calling it fails with a message saying the tool is no longer available through dynamic tools and to use the `codex_app` MCP server instead.
- Fresh tasks still get read-only tools such as `list_threads`, `read_thread`, and `wait_threads`, but the effectful communication tools are missing.
- There is no corresponding callable `codex_app` MCP replacement available to the task.
So Codex is essentially being told “use the replacement tool,” while the replacement tool is not actually exposed.
This has completely broken the multi-task workflow I was using in Codex Desktop.
I’ve already reached out to OpenAI support about the ongoing Codex Desktop issues and have received no useful response. I’ve also been reporting/reproducing these problems through the Codex GitHub repo, but at this point I’m trying to get more visibility because this has gone from buggy to unusable for this workflow.
There are currently two particularly relevant GitHub reports:
[https://github.com/openai/codex/issues/40865](https://github.com/openai/codex/issues/40865)
This covers the Remote SSH version of the regression. Previously working inter-task communication stopped working before the remote runtime was even updated. Updating the remote Codex runtime did not fix it. Retained tasks are redirected to the `codex_app` MCP server, while fresh tasks expose only the read side of the thread-management tools with no usable MCP replacement.
[https://github.com/openai/codex/issues/40852](https://github.com/openai/codex/issues/40852)
This is a separate macOS Desktop reproduction showing essentially the same split in the tool surface: `list_threads`, `read_thread`, and `wait_threads` remain available, while `send_message_to_thread`, `create_thread`, `fork_thread`, `handoff_thread`, etc. are omitted. The reporter also confirmed that the installed app still contains the tool definitions, but they are being filtered out of the callable tool catalog.
I also posted about it on the OpenAI Developer Community here:
[https://community.openai.com/t/inter-task-tools-lacks-codex-app-mcp-replacement/1393362/](https://community.openai.com/t/inter-task-tools-lacks-codex-app-mcp-replacement/1393362/)
That thread is mainly an attempt to get visibility outside of GitHub and see whether anyone from the Codex/Desktop team can confirm whether this migration was intentional, whether the missing `codex_app` replacements are a known regression, or whether anyone else is seeing the same thing.
If you rely on Codex Desktop for multi-task / multi-agent workflows, I’d be interested to know whether `send_message_to_thread` / `create_thread` are still available to your tasks, particularly on macOS, Remote SSH, or Docker/dev-container setups.
---
## Comments 0

