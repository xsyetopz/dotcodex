#I can use astra high a lot longer without my skills or agent prompt [Visit](https://www.reddit.com/r/codex/comments/1w8ox68/i_can_use_astra_high_a_lot_longer_without_my/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [kim-el](https://www.reddit.com/user/kim-el/)
### **Vote:** 0
---
so i try to ask astra to ignore all my skills, all prompt injected at new session, and work without any skills. and usage dosnt drain much. maybe i need astra to analysze all my skill and create router for it.
---
## Comments 22

- by [unknown](#) **&#x21C5; 1**
  <br/> [](https://preview.redd.it/i-can-use-astra-high-a-lot-longer-without-my-skills-or-v0-5lxlc4z1nunh1.png?width=257&format=png&auto=webp&s=6c21b88ee7a76e3656db591abb0d095db915c30b)

- by [unknown](#) **&#x21C5; 1**
  <br/> wow, haha. lets ask lord tibo for one banked reset for cleanup.

- by [unknown](#) **&#x21C5; 1**
  <br/> Ask sol chat to come up an updated workflow based on your needs, youll be fine

- by [unknown](#) **&#x21C5; 1**
  <br/> the problem is, i dont know what i need. 😂 my plan is to just go crazy, build away. and then save all chat transcription, and ask high intelligent model to structure a workflow suitable for me.

- by [unknown](#) **&#x21C5; 1**
  <br/> I know, you didnt take me literally enough. Literally ask chat to come up with a new usage plan based on recent openai developments and your worlkflow

- by [unknown](#) **&#x21C5; 1**
  <br/> So basically instructions or whatever we had that worked like a charm for me I should just get rid of it?

- by [unknown](#) **&#x21C5; 1**
  <br/> if youre an eginner and you know whats going on in your codebase, maybe your good. heck, you dont even need astra at all. but for non eginner like me its crucial.

- by [unknown](#) **&#x21C5; 1**
  <br/> Well, I found that lately, I didn’t even have to correct most things that GPT 5.6 would do on extra high or even high levels.

And I think that it was due to my deliberate instructions and me actually getting in there with planning and looking and knowing the code and what we’re doing or why we’re doing what we’re doing. I have built such a good rapport with my gpt 5.6 just straight in VS code that I feel like god now 😃

However I don’t use lot of skills. Maybe GPT 5.6 uses lot of skills in the background and even spawns us agents at some point but I don’t know.

- by [unknown](#) **&#x21C5; 1**
  <br/> what memory system you use? do you get anxiety to close a session

- by [unknown](#) **&#x21C5; 1**
  <br/> Yes, I have super long threads/sessions to try to not loose context from sessions and that’s the tricky part. I think it may be eating through my usage but I believe it’s worth it. Also I try to ask general questions outside codex env entirely and if I still have to ask I use light or medium effort for that.

- by [unknown](#) **&#x21C5; 1**
  <br/> Also just simple thing as plan this implementation into 4 batch’s and each batch having 4 runs is an interesting structure I’ve been using lately.

It basically gives you more control as there are smaller runs and you can observe more and see usage and iterate better as opposed to letting it run for hour eat through all your usage only to find out that what it made doesn’t work.

Also having a .md file that it needs to update after each run on what was implemented what is left etc etc helps either model not having to have all this context in its inference I think(I might not be right in that though)

- by [unknown](#) **&#x21C5; 1**
  <br/> Could be the skills themselves? I’d add them back one at a time and see which one causes the jump.

- by [unknown](#) **&#x21C5; 1**
  <br/> maybe my skills are not fundamental enough

- by [unknown](#) **&#x21C5; 1**
  <br/> What kind of skills do u use?

- by [unknown](#) **&#x21C5; 1**
  <br/> i have instruction for it to read okf for context, and write okf for checkpoint. so i can cd into a folder and spawn new session and ask it to continue. and some other skills that i dont know what task it do at the back.

- by [unknown](#) **&#x21C5; 1**
  <br/> maybe I can recommend one(:

- by [unknown](#) **&#x21C5; 1**
  <br/> How many kb is your agents.

- by [unknown](#) **&#x21C5; 1**
  <br/> honestly, i dont know bruh.  😭

- by [unknown](#) **&#x21C5; 1**
  <br/> No seriously. Agents.md in your project folder root.

- by [unknown](#) **&#x21C5; 1**
  <br/> 12kb. i have okf, and beads, for memory. i dont know what memory system to use so i can cd to a folder, spawn an agent and ask it to continue.

- by [unknown](#) **&#x21C5; 1**
  <br/> Just a heads up, Astra doesn't drain much because everyone is being throttled. It's extremely slow compared to pre-release.

When the server load comes down and compute frees up, your 1 hour task by Astra that doesn't use a lot of usage will be done in a a few minutes and you'll be burning 1% of a x20 plan every 2 minutes.

- by [unknown](#) **&#x21C5; 1**
  <br/> You should look into what you load in the context window. Your system prompt, enabled tools, skills, agents.md and more is always loaded in the context. That's your warm-up cost before even starting.

Then for every turn, the same data remains as a payload in the context, and is resent. Over time, that compounds, and you can end up spending millions of tokens on just for the agents.md.

First check what fills your context. Then learn how what's in there changes your workflow.

Then build your scaffolding of agent definition, tools, skills and agents.md to be effective for your tasks.

Too lean is also bad.

---

Picture showing that enabled tools and skills consume over 50% of the warm-up cost in this example.

 
       [](https://preview.redd.it/i-can-use-astra-high-a-lot-longer-without-my-skills-or-v0-xxdjoltlqunh1.png?width=1238&format=png&auto=webp&s=77bc8643fb8d8470ff711431d00ddd404e730125)
