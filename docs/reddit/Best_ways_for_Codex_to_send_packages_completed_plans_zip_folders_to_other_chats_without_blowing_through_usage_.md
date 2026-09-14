#Best ways for Codex to send packages/completed plans/zip folders to other chats without blowing through usage? [Visit](https://www.reddit.com/r/OpenaiCodex/comments/1w6pfxq/best_ways_for_codex_to_send_packagescompleted/)
### **Subreddit:** [r/OpenaiCodex](https://www.reddit.com/r/OpenaiCodex)
### **Author:** [Abel_091](https://www.reddit.com/user/Abel_091/)
### **Vote:** 6
---
Hello,
I am wondring if anyone can recommend an optimal way that Codex within desktop app can share a packages/completed plan/zip folder to other chats without blowing through usage?
I am use to using Codex Cli as its been such a workhorse and has always worked well however im trying to create a more integrated workflow so I've moved my project to Codex Desktop App and just trying to figure out what are best ways to do this?
I will often put completed plans by Codex into a zip folder with all components and then I will want chats within my chat gpt project to inspect,  however apparently those project chats do not have access to the project in the ways Codex does and can view.
Basically it seems I need to actually find a way that the zip folder package can be sent to those chat gpt project chats in the best and most efficient way.
I believe I have seen people reference using the github connector as in -- having Codex send a message to the project chat regarding using the github connector to access the zip package? does anyone find this effective?
besides that option I am wondering if having Codex save to some cloud source is also an option that Chats can then access?
I basically looking for the best option or most effective option where this works relatively smoothly and may not blow through usage if possible?
Any assistance or suggestions are greatly appreciated, thank you!
---
## Comments 6

- by [unknown](#) **&#x21C5; 3**
  <br/> this should attach files for you automatically to your chatgpt chat from codex and vice versa

[https://github.com/agentify-sh/desktop](https://github.com/agentify-sh/desktop)

- by [unknown](#) **&#x21C5; 1**
  <br/> Don't send the zip to project chats, that's what kills your usage.Best way: have Codex push it unzipped to GitHub with a summary.md, then tell your project chat to pull it via the GitHub connector. It only loads what it needs instead of tokenizing the whole zip.GitHub connector is the most efficient for this right now.

- by [unknown](#) **&#x21C5; 1**
  <br/> Or precalculate what it needs and send exactly that.

- by [unknown](#) **&#x21C5; 1**
  <br/> The pattern that works: Codex finishes a plan, writes the files to ./handoff/ with a one-page [MANIFEST.md](http://MANIFEST.md), and the other chat only opens that folder. The moment you zip and re-upload, you pay for the same tokens twice.

- by [unknown](#) **&#x21C5; 1**
  <br/> Hmm im wondering whats the solution when you do want more of the entire package viewed/sent ? Like id say for the actual coding plan and all its components  yes while I could probably make the feedback package more efficient

I was thinking have GPT work download and attach coding zip package and give to Codex and then Codex do an abbreviated version of the zip package back as suggested using github connector?

How does that sound?

- by [unknown](#) **&#x21C5; 1**
  <br/> If you ask ChatGPT to help you integrate Jira/Confluence into your workflow, it should help solve much of the problems you're looking to solve
