#This is where your limits have gone. [Visit](https://www.reddit.com/r/codex/comments/1wdpdpt/this_is_where_your_limits_have_gone/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Fun-Stick3234](https://www.reddit.com/user/Fun-Stick3234/)
### **Vote:** 4
---
This is ONE of 6 back to back tool calls.  I asked chatgpt to check a PR on a GitHub that involved training a 21m llm that has failed.  It loaded the logs over and over and over.  All 6 hours of logs.  ANY codex agent would have burned the 5 hour limit on that.  Just figured I'd let the confused people know.
---
## Comments 7

- by [unknown](#) **&#x21C5; 1**
  <br/> A tip for readers: you typically want your checks in GitHub actions ALSO to be run on precommit and prepush locally. Use lefthook or something to set these up so your development loop is local and you don’t need to constantly query GitHub for CI failures

- by [unknown](#) **&#x21C5; 1**
  <br/> That wasn't a GitHub action. That was me asking chatgpt what happened to the training run. Best practices or not, there was no reason to load the log ~18 times. The tool call usage is absolutely ridiculous this week. That's my point.

- by [unknown](#) **&#x21C5; 1**
  <br/> Oh I see.

In that case, what I do is make a custom CLI that filters structured logs for errors, warnings, or specific message types that I want to see. I cut my input token use by actual 99% on my builds this way. Same concept for a research loop.

Instead of dumping 10,000 lines, the model gets 5 back.

Same with unit tests. Just show it failures, don’t show all of the successes or test logs.

- by [unknown](#) **&#x21C5; 1**
  <br/> Honestly I use chatgpt to orchestrate and Luna high/max and can use it pretty much non stop and never hit my limit.  This was the first time I ever actually tried to fully train a model from nothing.  It's also right when I learned I could use GitHub actions to trigger codex.  So I didn't have the normal codex view I usually do.

I did have chatgpt look to see if there were any reports of excessive tool calls lately and there is a significant amount of reports everywhere BUT reddit it seems. Openai (to my knowledge) hasn't acknowledged it.

I started a new repo two nights ago.  I got to PR 5 and my chat ran out of space and I had to start a new one. It was less than 30 prompts.  And they weren't large prompts in comparison to my normal chats. Not even close and my normal chats typically last 5-7 days. But I started a new chat.  That one started complaining about context by pr 14 - about 4 hours later.  The screenshot I posted made it to around pr 27, but didn't really do much until that set of toolcals which timed out shortly after the screenshot and then maxed out on the retry.

Openai wanting to be all secretive about everything and doing their rolling releases just adds ambiguity to these issues.  I'm not sure if everyone has the ability to see the tool call usage like that.  I only noticed it a day or two ago.  But anyone who is burning through limits faster than they feel they should - that's where you should look first. Luna has been okay for me... But I don't dare to ask it to inspect a repo. I'd rather not see my week limit gone in a single prompt.

- by [unknown](#) **&#x21C5; 1**
  <br/> why is this deleted lol

- by [unknown](#) **&#x21C5; 2**
  <br/> Because "it belongs in the megathread" where it'd get buried so no one would see it.

Edit: if I had to guess, anyway.
