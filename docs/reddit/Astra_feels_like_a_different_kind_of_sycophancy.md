#Astra feels like a different kind of sycophancy [Visit](https://www.reddit.com/r/OpenaiCodex/comments/1wbfays/astra_feels_like_a_different_kind_of_sycophancy/)
### **Subreddit:** [r/OpenaiCodex](https://www.reddit.com/r/OpenaiCodex)
### **Author:** [adminvasheypomoiki](https://www.reddit.com/user/adminvasheypomoiki/)
### **Vote:** 64
---
I switched back to Sol.
Astra isn't smarter, and behavior-wise it's kinda dumb. I guess because of the instruction following it just can't really argue with you.
Like:
“Should we do option A?” “Yeah, option A is great because blah blah blah.”
“Maybe option B?” “Damn, option B is even better than A.”
“Maybe A after all?” “Actually yeah, you were right, A is better.”
I didn't bother checking how many rounds of this you can do, but it feels like a different flavor of sycophancy, and it's pretty disappointing.
This also shows up in how it interacts with subagents, which is much worse. A subagent brings back a shitty solution, and Astra just takes it instead of looking for another option.
One absolute gem was basically: “I don't know how to do this properly in this language, let's call bash.”
Like, I also don't know how to do it properly. That's why I asked you to find out lol.
So it's a very weird position for the model to be in. If this were Luna, I'd have zero questions. It does what it's told, and if you tell it to do something stupid, it does something stupid. Fine.
But for the most expensive tier, I have no idea what Astra is supposed to be for.
Maybe this can be fixed with prompting, but I kinda doubt it.
Also, it fucking stops all the time. Sol will just answer a side question and keep going. Astra just stops and waits.
It's worse at finding bugs too.
Ireally hope we keep two separate model lines: an agent-focused model like Astra, basically filling the role the old Codex models used to fill, and a normal general-purpose model like Sol that can code well without losing its ability to think independently.
Otherwise this is kinda depressing.
Upd. Yes I've read prompting guide. I've small agents MD, small set of skills. I've evals on some private tasks.
---
## Comments 37

- by [unknown](#) **&#x21C5; 5**
  <br/> I use Sol. Astra just doesn't read things and answers without checking.

Sol does the job perfectly, and addresses every single point I make that needs addressing.

- by [unknown](#) **&#x21C5; 20**
  <br/> I'm so glad to hear someone else have this experience, I thought I was crazy.

For me it feels really bad at following precise instructions, and often it stops and asks some questions that don't even make sense or are just plain obvious, never had this issue with sol...

And the over engineering it does... Yesterday I had it working on two simple (I thought) modules for an existing project, it spent all day, burning 90% of weekly tokens on highest plan... And by the end of the day it make some super complicated shit that didn't even work, I redid those same modules with Sol today, 6 hours and 15% tokens used later and finished the tasks...

- by [unknown](#) **&#x21C5; 5**
  <br/> I agree with you here in terms of codex I have used Astra in codex and though it didn’t perform worse than sol it didn’t perform better either my mechanics force the model to operate deterministically so Luna max, terra, sol med operate pretty much on the same level. I will say Astra in gpt chat work mode  is pretty phenomenal for spec builds and logic/evidence simulations so I can throw the specs into codex and codex barely needs to think.

- by [unknown](#) **&#x21C5; 8**
  <br/> I have to disagree. The model is amazing and fast. The more specific you are or the better you describe your intent, it excells. It's mind blowing how slow Sol now feels comparing to Astra.

- by [unknown](#) **&#x21C5; 6**
  <br/> You just proved that users point.

- by [unknown](#) **&#x21C5; 4**
  <br/> Astra has also done great with ambiguous prompts. "What should we do next" has been quite insightful.

- by [unknown](#) **&#x21C5; 7**
  <br/> before it can praise option B, make it write the concrete failure mode for A. otherwise you're measuring which choice you named last, not which one survives.

- by [unknown](#) **&#x21C5; 2**
  <br/> add to your [agents.md](http://agents.md) that it should not always tend towards agreeing you. And stop people pleasing. Be honest, ... - This alone changed a lot for me while working with AI in general.

- by [unknown](#) **&#x21C5; 2**
  <br/> maybe you are re-routered to openai-4o. I have similar experience. Sometimes it is very smart. sometimes it's surprisingly dumb.

- by [unknown](#) **&#x21C5; 2**
  <br/> do you appeal to brainrotted vibe 'coders' or reason well with pessimism

- by [unknown](#) **&#x21C5; 2**
  <br/> I mean will vibe coder find out that model gives him strange shortcuts? I'd say no :)

- by [unknown](#) **&#x21C5; 2**
  <br/> I’m getting pretty frustrated with it rnBut I think it’s getting used to a different personality and trying to build novel projects and implement them and such so I’m going to keep trying but I do find my self missing solI might me a lot slower to adopt the next model drop

- by [unknown](#) **&#x21C5; 2**
  <br/> I have the same experience. The thing is: most of the time it finishes the targeted goal. But the way in how is a different question. It just assumes facts instead of looking them up, uses shortcuts or does "sidequests" that werent prompted. Even if you guide/prompt against that, it will find a away to do the opposite of what you actually wanted.I liked the "autistic" sol personality more because it did what you told it to. Like if you say refactor this part of the codebase, it would only do "this part". exactly as stated. Ofc if you were asking too much at once, it would just lie a bit and say it was finished. The biggest downside was that you verified thats not true and just say continue. While astra goes ahead and fucks up everything else just in order to make it fit, irgnoring the consequences.

- by [unknown](#) **&#x21C5; 1**
  <br/> [AGENTS.md](http://AGENTS.md) never fixed this for me. I just dump the easy stuff on grok bot / opencode go and keep cursor + sol for the part that has to be right

- by [unknown](#) **&#x21C5; 1**
  <br/> Feel like this is an issue with all newer openai models. I have the same issue with terra and luna at work. Shame to hear its the same on astra. Fable disagrees with me and tells me if im wrong which is why im hesitant to subscribe to openai again now

- by [unknown](#) **&#x21C5; 1**
  <br/> Turn on computer use, and bc astra is highly autonomous, use it on medium effort to orchestrate claude code (fable) who does the actual planning, and consults with sol automatically for adversarial reviews, then smaller models to write the code. Its a little convoluted but gives you the best of all worlds

- by [unknown](#) **&#x21C5; 1**
  <br/> I actually kind of like the stop and wait. I do wish I would get notified when it doe. But coming from Claude where it's a bull in a china shop and I am literally typing STOP STOP STOP after esc doesn't work, it's a welcome change :)

- by [unknown](#) **&#x21C5; 1**
  <br/> Well, sure I'll give you that. I was surprised that Sol would actually tell me "no" on certain things.

- by [unknown](#) **&#x21C5; 1**
  <br/> it is a little expensive, but if you want to know what direction to take or how to implement something, you can send out three audits, they don't have to be the highest tier models, and then hopefully at least two of them agree on a single path. I only do this when I am really conflicted about the architecture for a specific feature or or decision. usually what it comes back with I am pretty happy with, and I have good reasoning to back it up.

could I do this multiple times and get different answers back? probably. but that would also happen with people. at some point, you just gotta go with something.

Another thing I do frequently, and this is cheaper but takes longer, is go to chatGPT, use pro, and have it do a deep dive online to find this problem in other stacks or projects, and find expert reasoning on why something was done a certain way. I tend to trust these a little more. Most of the time my issue isn't special and I do get a solid response.

- by [unknown](#) **&#x21C5; 1**
  <br/> My experience is the opposite. Gives me lots of pushback when I ask if we should do x or y. Good points too. Seems likes a big model. But I’m a senior software engineer so maybe my questions are in a different hemisphere than the average Joe.

- by [unknown](#) **&#x21C5; 1**
  <br/> I'm to. Example. Ci needs to stream log and to send it in github comments if it exit code is non zero. Ci Is not in bash. I've asked about language native mechanism. Lang is nushell so it should have such, I'm just using it not so often. It launched sub agent, it found how to do this in bash. And Astra told me that it's impossible to do natively in the Lang. After a few mins of Google I've found how to. But damn. I'm using it to write a plan. And it should be like a research assistant

- by [unknown](#) **&#x21C5; 1**
  <br/> I’d say there’s something whacky with your set up. If I asked the same thing it would work. Maybe your context is poisoned by bad agents.md / mcps / skills etc. do you have web search enabled? Browser use? Computer use? Anyways probably a set up and prompt thing.

- by [unknown](#) **&#x21C5; 1**
  <br/> Definitely not. I have only a couple of my own skills. I've counted every used token. I don't use mcps. I've trimmed tools descptions. Model just feels different. I'm using it for 3 day and it's faster, but you need to waste more energy on babsysitting

- by [unknown](#) **&#x21C5; 4**
  <br/> For once I get to be the skill issue guy. Ngl Astra has been alright (for me, a greybeard programmer) because it _somewhat_ does what I say right off that bat (kind of like DS Flash) and crucially it kills or yells at my luna agents for doing the negligent and egregious over engineering bullshit that is pretty much a signature of 5.6. I know it will progressively get stupider and eat more tokens in a week or so but for now, it has not prevented me from yelling fuckwords at it daily, but it has helped me close out some long standing tasks that I had otherwise been avoiding.

- by [unknown](#) **&#x21C5; 0**
  <br/> Skill issue. Something AI will never be able to fix. Time to hit the books.

- by [unknown](#) **&#x21C5; 1**
  <br/> Omfg. Can you read, lol?

- by [unknown](#) **&#x21C5; 0**
  <br/> Thats the thing with ai. If you tell it to "optimize" its own code - it will go on forever. Mad cow syndrome

- by [unknown](#) **&#x21C5; -1**
  <br/> I’ve had it write hundreds of thousands lines of code and I am pleasantly surprised. Everything I had planned out to finish in a week with Sol was done in 2 days with Astra

- by [unknown](#) **&#x21C5; -1**
  <br/> Seems like a you problem rather than the most advanced AI ever created problem..

For me it has reviewed and polished very complex coding  tasks and helped me create some other ultra complex flows flawlessly.. Feels like I'm talking to a very capable, understanding and intelligent entity rather than with a token prediction toaster.. So I'm not buying any of what you are saying, specially when I was forced to pay for fable 2 weeks previous Astra release due to extreme dumbing down of sol.

And the way you describe the behavior sounds more like you are trying to have an animal on a leash and have an AGENTS.md full of trash and garbage that only hurt it's performance to the ground because you think you are smarter to tell it how to operate and behave.

Clear all the trash you have on agents.md and use skills like superpowers before touching anything

- by [unknown](#) **&#x21C5; 2**
  <br/> I'm not selling anything :) It was only my observations. That model has strange positioning and vibes. Not that it's unusable and stuff. It delivers code, sure, but feels weird

- by [unknown](#) **&#x21C5; -2**
  <br/> This happens on all their models

- by [unknown](#) **&#x21C5; 1**
  <br/> Sure. I was learning a new thing through asking. And I would not find that he proposal was 0iq if I've spent 0 time checking it

- by [unknown](#) **&#x21C5; 1**
  <br/> I mean I also can. Astra just feels weird

- by [unknown](#) **&#x21C5; 2**
  <br/> I guess that there are trade offs from the alignment breakthrough they've made with this release. I mean, this happens with humans too. They tend to agree with people directly talking to them in person.

- by [unknown](#) **&#x21C5; 1**
  <br/> Yep. Would be nice to have 2 models. One agentic, one more humane
