#I have to tell Codex "pls proceed" "let's implement them all" "you have my full permissions please don't stop" constantly [Visit](https://www.reddit.com/r/codex/comments/1weuufh/i_have_to_tell_codex_pls_proceed_lets_implement/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [SeparateRemove9902](https://www.reddit.com/user/SeparateRemove9902/)
### **Vote:** 9
---
I have to tell Codex "pls proceed" "let's implement them all" "you have my full permissions please don't stop" constantly.
This is even more of a problem with astra than sol.
I feel exhausted asking for status and tell it to continue.
---
## Comments 18

- by [unknown](#) **&#x21C5; 4**
  <br/> Do you use /goal?

- by [unknown](#) **&#x21C5; 4**
  <br/> Yes, just set a goal and it'll run until the task is complete. Just be careful because if the goal is impossible or even just too hard, it won't stop until you're out of credits.

- by [unknown](#) **&#x21C5; 1**
  <br/> Just woke up this morning after a 18 hour run. +58k lines pr waiting for review.

Consumed ~35% of 20x

- by [unknown](#) **&#x21C5; 4**
  <br/> OpenAI actually documents this behavior in its [official Astra guide](https://developers.openai.com/api/docs/guides/latest-model#initiative-and-follow-through): Astra is more likely than Sol to ask for clarification where earlier models would make assumptions, which can cause it to stop when you expect it to continue.

The guide also says Astra is more sensitive to instructions in [`AGENTS.md`](http://AGENTS.md) and skills, and recommends auditing them for unclear or conflicting rules.

A practical instruction to add would be:


      
    But check existing rules too—adding this alongside “always ask before making changes” leaves a conflict. Keep explicit approval requirements for actions that actually need them.

So there’s an officially documented basis for adjusting your instructions, although it isn’t a guaranteed fix for every premature stop.

- by [unknown](#) **&#x21C5; 1**
  <br/> This ^   For Astra you really need to guide those behaviours you want with our [agents.md](http://agents.md) file more so than others

- by [unknown](#) **&#x21C5; 4**
  <br/> Yeah, that started happening along with the Astra update. I'm guessing it saves them a *lot* of peak compute to have it behave this way.

- by [unknown](#) **&#x21C5; 2**
  <br/> I was having this same issue and got told to look at [Model guidance | OpenAI API](https://developers.openai.com/api/docs/guides/latest-model) which I had not and it shows that openai knows it behaves this way and that it is intentional and you need to add in the prompts (or ones of our own making) to get it how you want it to behave.

- by [unknown](#) **&#x21C5; 1**
  <br/> I just asked Astra to create a user level AGENTS.md after researching coming Astra pitfalls and quirks. It found the most common complaints from official sources and it works perfectly now.

- by [unknown](#) **&#x21C5; 1**
  <br/> would you share?

- by [unknown](#) **&#x21C5; 1**
  <br/> Shared on another user’s reply.

- by [unknown](#) **&#x21C5; 1**
  <br/> yes, please share - highly appreciated :)

- by [unknown](#) **&#x21C5; 1**
  <br/> Here are the relevant parts from my agents file:

Carry actionable requests through implementation and appropriate verification. Make reasonable assumptions for routine, reversible decisions; briefly state assumptions that affect the result.Ask only when missing information materially changes the outcome or an action needs authorization. Continue independent work while waiting. Do not repeatedly request permission already given; respect tool permission boundaries.Keep scope focused. Preserve unrelated edits and existing project conventions. Treat follow-up corrections as steering the current task unless I change the goal.If a skill or instruction blocks progress, identify the source and exact requirement, and explain the concrete blocker rather than silently stopping.Be concise and direct. Report the outcome, relevant verification, and remaining limitations. Distinguish completed work from proposals and unverified results.

- by [unknown](#) **&#x21C5; 1**
  <br/> I have given codex the permission to do whatever it likes within the folder i start it in. I maintain github backup. i launch codex from a script that will not allow me to open it in any folder other than the git and some throwaway folders. I don't have to give any permission to codex.

- by [unknown](#) **&#x21C5; 1**
  <br/> Context pollution, also use /goal

- by [unknown](#) **&#x21C5; 1**
  <br/> having to keep saying “continue” sounds exhausting. you should be able to let it get on with the job and still have a say over the risky stuff. that’s the part I’m working on at the moment. happy to explain what I’m trying.

- by [unknown](#) **&#x21C5; 1**
  <br/> make a second session, give it the task to monitor first session and approve it each 30 seconds

- by [unknown](#) **&#x21C5; 1**
  <br/> Do you have something in your agents.md telling it to do that already? If not maybe try that
