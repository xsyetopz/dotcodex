#Looks like the over engineering stories are true. [Visit](https://www.reddit.com/r/codex/comments/1wcnlfn/looks_like_the_over_engineering_stories_are_true/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Consistent_Tutor_597](https://www.reddit.com/user/Consistent_Tutor_597/)
### **Vote:** 4
---
It seems to be adding random guards for edge cases and do all this complicated stuff and is less pragmatic and you have to babysit it. Maybe it's aimed at bigger orgs? Dunno. Smart and deep model, but creates more work for me. I am trying to keep it's scope less broad for now.
---
## Comments 18

- by [unknown](#) **&#x21C5; 5**
  <br/> You have the ability to prompt. Use it. You can save instructions as skills and reuse them. If you don't want it to handle edge cases, say so. If you don't want it write test cases, say so. I don't know how you guys expect one chat interface to infer literally everything you want it to do or not do from a few sentences. If you want a specific behavior from it, ask for it.

- by [unknown](#) **&#x21C5; 1**
  <br/> You are describing babysitting, the idea of agentic programming is to reduce the human in the loop and you need a lot of harness for that, current models fails to build clean stuff without it.

- by [unknown](#) **&#x21C5; 2**
  <br/> That's why it defaults to over-engineered. Because the default is to do everything a professional would do for an enterprise project precisely so you have less human intervention. If you want something less than that, you have to specify. There is way they can tune it to always give your desired output without reading your mind, and even then, you probably don't know all your own requirements even in your own mind.

- by [unknown](#) **&#x21C5; 2**
  <br/> Because the default is to do everything a professional would do for an enterprise project precisely so you have less human intervention.


    That is not the definition of over-engineering, its only consume more token, creating software more complex to debug ,profile and change.

That is NOT how a professional would do for a enterprise project.

- by [unknown](#) **&#x21C5; 1**
  <br/> NO, it's not necessarily babysitting.  I created a skill for 'proportional engineering' , basically to avoid both over- and underengineering and edited [AGENTS.md](http://AGENTS.md) to use that skill by default. Of course, it's not to say that it works 100% perfect every time,  so occasionally in a long running session I still have to remind the agent to adhere to the principles defined in the skill.  But in general the tendency for overengineering is pretty much well tamed.

- by [unknown](#) **&#x21C5; 1**
  <br/> It is not in complex and long tasks.

For exampel for optimization problems is a disaster.

- by [unknown](#) **&#x21C5; 1**
  <br/> That would be a great suggestion if it actually followed instructions, which it's very inconsistent at.

- by [unknown](#) **&#x21C5; 0**
  <br/> Agreed, prompting is definitely a huge issue.

Oddly enough I haven’t used skills or done any changes to agents.md.

I find it extremely weird that people will attempt to have a basic conversation inside of codex lol.

I structure prompts like a actual ticket based system and usually they are in the range of 14k avg characters.

- by [unknown](#) **&#x21C5; 1**
  <br/> So you are using agents like is 2024

- by [unknown](#) **&#x21C5; 1**
  <br/> No not at all.

I’ve built my own harness

- by [unknown](#) **&#x21C5; 1**
  <br/> I haven’t used skills or done any changes to agents.md.

- by [unknown](#) **&#x21C5; 0**
  <br/> Didn’t have to make changes to that for the harness to work lol.

- by [unknown](#) **&#x21C5; 1**
  <br/> Harness is not prompting my dude

- by [unknown](#) **&#x21C5; 0**
  <br/> No shit dude. Where did I say that?

Again I built my own harness.

- by [unknown](#) **&#x21C5; 1**
  <br/> Okey, you have no idea what you are talking about

- by [unknown](#) **&#x21C5; 0**
  <br/> Yes I do. I built my own harness that is not the same thing as codex, this without the need to edit agent.md or using skills.

- by [unknown](#) **&#x21C5; 1**
  <br/> Honestly I’m working on removing babysitting issues but mostly via local workers. I’m pretty sure I can do the same with OpenAI adaptors but haven’t gotten that far yet.

Literally can’t stand constant low level approvals but I’m unwilling to give it access to just do whatever the fuck it wants.

- by [unknown](#) **&#x21C5; 1**
  <br/> Yea, letting it do whatever it wanted was a massive mistake. I had it plan out a pretty simple Anima lora training plan. It was supposed to generate the Lora's,generate a suite of images, and then use visual reviewers to compare them. Pretty simple.

Unfortunately the code it created was over engineered all to hell and was outside of the project plan. I'm talking about it creating version launch wrappers, creating detailed LLM receipts for every check and change, a scripted coordinator keep alive that wasn't necessary (and probably attributed to my massive cached token usage) it could just checked progress itself once the agents were done, but no, it needed a script for that running every 2 minutes.

The worst part about this though, is that if it found any issue with one of these over engineered scripts, it would do testing, "fix" the bug, run the script again, realize there's another bug, "fix" that again creating another bug or breaking the original fix, and then looping on itself until I ran out of tokens.

Its fucking ass when it comes to trying to engineer something into a functional product. At first it seemed fine, but as the project was built out, it slowly turned the project into unworkable self iterative slop. At least Claude puts forth code that pertains exactly to what the plan stated. It might miss shit or get stuck in deep rabbit holes trying one solution to a problem but over engineering to the point that it gets caught in a bugfix loop that it engineered itself doesn't happen. There's still a sense of progress unlike with Astra.

That isn't even taking into account the "reset" they gave me, a day-ish ago, that was only about 50% of my usage (I used my entire 20x plan reset yesterday on these bugs), AND they pushed my fucking weekly reset back all the way to the 14th, when it would've been reset today of all fucking things.

I'm literally getting scammed by this fucking corporation.
