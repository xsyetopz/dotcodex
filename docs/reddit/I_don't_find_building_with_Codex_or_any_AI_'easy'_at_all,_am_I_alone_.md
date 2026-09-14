#I don't find building with Codex or any AI 'easy' at all, am I alone? [Visit](https://www.reddit.com/r/codex/comments/1wamtly/i_dont_find_building_with_codex_or_any_ai_easy_at/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [MrDavidP](https://www.reddit.com/user/MrDavidP/)
### **Vote:** 12
---
So I always see people on Twitter being like, oh, I vibe coded this app in one day and look how amazing it is, etc. Meanwhile, I've been trying to build a functioning iOS app + website with a backend using Codex, and I've been working on it part-time for a few months now. It's still not done.
My question is, am I using these tools wrong? Or do other people have projects they're working on for months at a time with AI tools like Codex?
The website I'm making is functional and the backend works, which in and of itself is amazing and something I could never have accomplished on my own. But I still wonder if I'm just not prompting correctly, or if others also find it time-consuming to bring their actual vision to life with AI. Thanks.
---
## Comments 63

- by [unknown](#) **&#x21C5; 20**
  <br/> I'm very skeptical about those "I did this thing in 1 day" stories. I find they are often advertising some vibecoding product.

- by [unknown](#) **&#x21C5; 6**
  <br/> they're true, is just they're slop apps with thin security. I even saw yt videos about dumbasses teaching how to make $200k apps in a day and include AI API keys WITHIN the app, fucking mindblowing

- by [unknown](#) **&#x21C5; 1**
  <br/> What are you talking about? This is awesome! Awesome for black hat dudes

- by [unknown](#) **&#x21C5; 1**
  <br/> There was a site a year or two ago that was just random API keys from vibe coders leaving them public and scrapable.

Obviously LLMs have gotten much better since then, but its still happening.

- by [unknown](#) **&#x21C5; 5**
  <br/> The thing about vibe coding is that it very much depends on your knowledge. With a precise enough plan you could one shot the craziest things, most models are very powerful at this.

But if you don't know what you actually need to build, chances are that you're going to end up with an entire site/app/game/etc. in a single .js file that will meatgrind your tokens and be a pain to edit/maintain with or without AI.

Imo the people who aren't that familiar with coding and/or best practices (and even those who do) should treat AI builds more like rapid prototypes. Make a prototype, then shape it into something, then analyze and boil it down to one prompt/md file and use it to build the next version. After a few cycles you should have a good "one-shot" prompt that you can clean up, I've seen this work very well for a couple of my non-techie friends.

- by [unknown](#) **&#x21C5; 3**
  <br/> This. Successful vibe coding requires deep knowledge of project management and system design. Without these skills, you’re just asking a magic box to flail around.

- by [unknown](#) **&#x21C5; 8**
  <br/> Note: I’m a software engineer with over a decade of experience in big tech and some well-known start-ups.

I also consume a lot of AI content on X, Reddit, YouTube and the things you need to be aware of are grifts that are self-promoting and survivorship bias — the latter being the ones that made it while there are many more that have not.

That said, the complexity that you describe is your moat and makes it difficult to copy. The building is hard if you need to involve backend systems with an API and/or database. I’ve been working on an app with some extensive social features yet to be released for almost four months now. It is incredibly polished, but there’s been many moments where I’ve literally said aloud to myself, “I have no idea how a vibe-coder is going to make the right decision here even with AI and truly understand the technical trade-offs.”

You can get there, but you’ll have to take the time to pause and understand and learn. My experience reduces the time by allowing me to understand the technical decisions being made that isn’t simply just code. Code requires massive contextual knowledge, too, but my understanding of how the web works, modeling a domain, data-modeling (how to structure databases for my data access patterns), and the tools I’m aware of for different jobs, puts me at a considerable advantage.

It’s easier to build simply an app that’s user-interface only even if it looks complex. AI is good at that, but not autonomous enough to completely architect a backend system without your input just yet. It doesn’t know what niche, what traffic patterns, what current and future features you’re thinking about, what you’re absolutely not building for. The more constrained the idea, the better it can build.

- by [unknown](#) **&#x21C5; 1**
  <br/> gotcha. Thanks for that insight. The idea is fairly constrained but yea, small things just keep popping up. It's good to know that more experienced folks than myself are also spending serious chunks of time on their projects.

- by [unknown](#) **&#x21C5; 4**
  <br/> You're not, you just dont have a CS background, so it takes you forever, but you also seem to be intelligent enough to recognize your limitations, what the tool can do and accordingly work with that.

AI makes it easy to vomit out features and a lot of velocity but half the time, they are broken in subtle ways which you will never notice in a video or twitter post. Another side effect will be that further feature gets complex even for AI. AI has far longer contextual and reasoning chains than any human, but all AI providers are compute bound and throttle everything. I suspect a lot of the people complaining about maxxing their Sol/Astra after 3 prompts are working in 300k LoC of unaudited, barely refactored AI generated code, where every change requires modifications to 17 files and has a lot of residual, irrelevent context and code, blowing up token usage.

In general, AI makes it really easy to do the 80%, but the last 20% remains as hard as ever and its where we've spent most of our time anyway. Project im working right now, it is in a functional state after 3 months of work instead of the 9 it would've taken without AI. The 12 months required after that to get it to true production tier, good testing and reliability and such did not disssapear, even with AI.

- by [unknown](#) **&#x21C5; 1**
  <br/> Thanks for that, reassuring to see others are working on stuff for longer than a few days as well. "Broken in subtle ways" would definitely be how I describe the thing I'm working on.

- by [unknown](#) **&#x21C5; 3**
  <br/> same, but its all a learning phase for me currently, never worked on an AI driven project of such size before.

I think im slowly settling into what i always thought would be the an optimal for me approach, but budgets never allowed for it - when we start a project, most of us generally have no idea what we're doing here, unless everybody is a grizzlied domain veteran, so the early phases of all projects are generally exploratory, with certain heuristics developed by the field over the years to make sure the project isn't doomed from the start. Eventually everybody develops a very good understanding of the problem domain and a rewrite would be a massively better product, but budgets and simple gain/loss never justified this.

With AI, we can throw all of that away and vibe code the crappiest project possible to test features, their flow and any pitfalls. It's fine if its subtly broken, its a throwaway in a way. But once you explored your problem domain and have a good understanding of what will work, you can refine all that into a living specification and actually start following best CS practices and port functionality, brick by brick, with review and deeper personal thinking, to the new system.

I even finally found a use for TDD (test driven development). I never quite got how im supposed to write tests first when i dont even know how my prod system is going to look like, but with my throwaway codebase, i have a very good understanding of all flows and API's and I feel like i can do TDD for the first time in my life and it will confirm spec conformance.

- by [unknown](#) **&#x21C5; 2**
  <br/> Well, I have 10+ years of commercial software experience, and I've got the same issues with AI. I tried to vibe code for a few months, but the quality just isn't there. AI overcomplicates everything. In software, the less code you write, the better. Recently, I've been cleaning up the AI slop my project gathered for the last few months, and whenever I work on new features, I'm now making the actual decisions myself.

- by [unknown](#) **&#x21C5; 3**
  <br/> It's a learning experience. Chat with GPT and learn how to make plans, ask questions, and keep it simple.You will get there...or not...who cares, enjoy the experience.

- by [unknown](#) **&#x21C5; 3**
  <br/> It's definitely fun! I love this stuff and wish i could just quit my job and build with Ai full time it's amazing to see ideas you've had for years finally come to life. But I also wanted to see if other folks spend this much time on projects.

- by [unknown](#) **&#x21C5; 3**
  <br/> anything worthwhile is still going to take some time. sure you can put something together in a day. it'll be shit though. That said, there are a bunch of techniques that make it go faster:

- don't just prompt the agent. structure your work in tasks: features, bugs, jobs, ... save these tasks with the code, they will provide a good way for the agent to understand your app, how it works, which features there are.

- use git worktrees to multi tasks

- put together a strong set of short md files with coding guide, front-end coding style, ui styling guide, architecture.

- use the tools that help you in the process. vscode is great, but it is for coding. for proper speed, you need something better. i use: [jan-bogaerts/md2: Plan, run, and track AI coding work feature by feature—with local Markdown cards and Git worktrees.](https://github.com/jan-bogaerts/md2) (my own little tool)

- by [unknown](#) **&#x21C5; 3**
  <br/> You don't have to listen to me, it is based on my personal experience so maybe it's just me, but there is a very big chance that you are the problem.

You see, I realized something a while back, AI sees your repo as holy. He thinks "this is how we do things around here", so he contorts himself into a pretzel trying to please your unholy abomination. Your brilliant ideas? Well someone did it already 100x better than you, but GPT 4.4 wanted to please you all these months back so he built a piece of shit that is held on by duct tape to this day and now here comes astra looking at the duct tape and adding some of his own because hey, it's what the user did so it must be good.

So from my experience in the last few days, telling Astra 'stop doing it like I was doing it, its shit, do it regardless of what is in the repo' literally caused him to do stuff in ways I never even imagined were possible. It hurts knowing I was the problem, and it hurts deleting work I thought was good only to see the latest LLM wipe the floor with within hours, but it is what it is. That's where I'm at, mentally defeated.

Is this story relevant to you? I don't know, but I doubt I'm the only one.

- by [unknown](#) **&#x21C5; 2**
  <br/> This post really touched my heart.

The thing is, yeah, we are now the roadblock with these models but you can still use them to achieve more than you ever could before. But yeah, it is humbling for sure.

- by [unknown](#) **&#x21C5; 1**
  <br/> that's good to know. I actually tried astra once, it went in a weird direction, and am still using Sol. but yea, this is sort of what I was worried about, thanks for sharing. There is always a big chance I am the problem with everything in my life.

- by [unknown](#) **&#x21C5; 3**
  <br/> Because they aren't building real scalable production apps, you aren't doing anything wrong. I am also building an app that I have spent months and months on, it's complex and its hard, and a single feature depending on complexity alone can take multiple sessions days even weeks.

- by [unknown](#) **&#x21C5; 1**
  <br/> good to hear. Just wanted some reassurance I think that I'm not the only one tinkering around on a single project for months with codex.

- by [unknown](#) **&#x21C5; 2**
  <br/> I'll be honest I use mostly Claude, and sometimes Codex. Codex can build a much bigger system than a problem needs which can also cause even longer work as well.

- by [unknown](#) **&#x21C5; 3**
  <br/> You can get a pretty fancy looking prototype together in a day, but to actually get the UX right, the art and models right, game mechanics (if you make a game) that shit takes time. But a quick prototype to see if the idea is worth it? That's pretty quick these days.

- by [unknown](#) **&#x21C5; 3**
  <br/> When working on something I am very experienced in, like building an ecommerce platform for example, AI does make it possible to ship in a day or two. When working on something I'm not very experienced in, like building my own compiler for example, AI turns the project into a complete mess of lies and cheats buried in abstraction hell that I am not able to follow.

I'm currently at a point where I take responsibility for the failure/success and prioritize my own knowledge, treating AI as just another tool in the box I can use to apply my knowledge to whatever problem I'm working on.

- by [unknown](#) **&#x21C5; 3**
  <br/> Yes, for large-scale projects (or often medium-size projects), codex/cc introduces unnecessary complexity, making your projects increasingly unmanageable.

Problem is taste: they lack taste - for now anyway - and thus write horribly designed code.For one-off stuff, they do fine, and most people get deceived by it.Job of us humans is to course its directions in large code base so they don't go astray.

- by [unknown](#) **&#x21C5; 3**
  <br/> Most of the I built this(great looking software game) in 1 day is either influencers that's given accounts with hourly quotas  And their able to run a swarm of xhigh thinking agents to run in parralelle

There's no way I can see it being possible  Even with clear prompting, giving it the architecture and letting it run for hours in it's own loop cycles

The outcome works but is not close to the polish they claim to achieve in a single prompt or single day

Is that polish possible?  Yes  At what expense rate?  Influences discount  Could you afford it?  Probably but won't be worth how much it would cost

- by [unknown](#) **&#x21C5; 3**
  <br/> Most of those post you sees are nothing more than shallow tech demos. If you want to build something like a real product you kind of need to know at least somewhat what to do and bow it’s supposed to work otherwise AI will produce something that is not scalable or lead you on a path that is not what you actually wanted. AI is a tool and just like any other tool you need to know how to leverage it. Just because i know the basics of how to use a hammer and a saw doesn’t mean  I know how to make beautiful furniture.

- by [unknown](#) **&#x21C5; 3**
  <br/> It is not easy. You need to give AI directions to think. You need to have a clear understanding about what the user will experience. Then spend more time to design the architecture with AI by engaging in a conversation. If you expect AI figure out problems, it wont work.

- by [unknown](#) **&#x21C5; 3**
  <br/> I have been working on my ops system for about a year now. coding with AI is not easy. once a system gets complex enough, AI is just going to have a problem since its context can only hold so much of the repo at a time.

building rails and systems for building is extremely important. I would suggest spending more time than you think you need to just on architecture and guides for the agents.

- by [unknown](#) **&#x21C5; 3**
  <br/> All my projects have a least 75 revisions. I can’t imagine doing something in one shot.

- by [unknown](#) **&#x21C5; 2**
  <br/> Yes they fill in to much on non related directions, this is a big issue! Apart from this dua to safety guidelines i am happy with codex

- by [unknown](#) **&#x21C5; 2**
  <br/> It is easy in the sense that you just type what you want and AI implements everything. The annoying part is having to click everything and making sure it works like you want it. I guess you could see that as the 'hard' part. It's a lot of trial and error.

Some things are also really hard to test properly. Try training a voice model for instance, you need hours of actual conversation with the model, not just A/B testing.

- by [unknown](#) **&#x21C5; 2**
  <br/> I built a game I find fun to play yesterday and I've never done game dev a day in my life before that. It's not close to finished or anything, but I think that's pretty wild.

- by [unknown](#) **&#x21C5; 2**
  <br/> It's not easy, it's a skill that takes time to learn. So the first time you try it, it's going to take you a lot longer than someone who's been doing it awhile.

For the done in a day projects, usually people are doing spec driven development. AI can still do most of the work for a product spec, but it has to be pretty complete or you'll spend a lot of time fixing things.

What people who vibe code things in a day leave out, is that it's never exactly what they set out to build. If you're ok with whatever you get after a day, this works, but for any real product it's still going to take a long time refining that initial product. They'll be lots of bugs to hunt down, UX usually doesn't look that good and often works very poorly. Features are straight up wrong or missing completely.

For a prototype, vibe coded in a day is usually fine. I've done it a lot to sell people on the idea, so they'll let me build it for real.

Also, based on other comments, I think you might be building UX wrong. For UX design, I'll always do mockups (non-functional versions or just images) first. ChatGPT is pretty good at this if you tell it to generate images of the UX instead of writing code. Make lots of them and choose your favorite. Then, pass that image to codex as reference to how the UX should look. This gives you 10x better results than starting with UX code. Anthropic's models do a much better job at UX too if you have access to both.

- by [unknown](#) **&#x21C5; 1**
  <br/> Good to know. yes I've been doing the create image in Chat GPT then feed to codex approach for about the last month and it's helped a ton. I have Claude also, will see if maybe that's the way to get it over the finish line.

- by [unknown](#) **&#x21C5; 2**
  <br/> take 1 day and adjust / learn matt pocock workflow. You are welcome.

- by [unknown](#) **&#x21C5; 2**
  <br/> It's easy to make *something* with AI.

If you have very specific use cases and need something complicated made, it gets a lot harder, especially if you have no tech background. The vast majority of vibe coded projects are slop with a userbase of 1 that will be binned once the creator grows bored or realizes it will never make them a horjillion dollary-doos.

I'm using codex on a personal project and I could go a *lot* faster by just giving it the wheel and letting it implement the overall plan but it'd be way harder to notice and fix issues. This means I'm honestly only developing 3x faster at most (and that 3x is because my day job usually takes most of my focus and energy for the day), but its shaping up exactly as I intended it, and I know how things work enough to do some debugging myself if Codex fails.

- by [unknown](#) **&#x21C5; 2**
  <br/> the way I have learned to see it after 3500 hours of experience with vibe coding is that its best to treat all models, whether it's codex, claude code, grok build etc, like a dumb employee that can work hard and comes up with something good every now and then, but you need to manage this employee a lot and if you don't steer it, it will start creating a lot of overhead, over-engineer things that aren't relevant and it will lose track of the goals you've set it out to do. And also his memory isn't very good; every few hours he forgets a bunch of things and is prone to making the same mistakes over and over, to the point that you can be working in a loop for weeks, or even months, because one task creates others tasks etc.

- by [unknown](#) **&#x21C5; 2**
  <br/> Yep, just you.

- by [unknown](#) **&#x21C5; 1**
  <br/> lol thanks

- by [unknown](#) **&#x21C5; 1**
  <br/> What are you trying to build? Just some examples?

- by [unknown](#) **&#x21C5; 1**
  <br/> I keep getting hit with 'spam' on reddit so I am hesitant to even share it. It's basically like a site for recommendations, where people can create a profile, post and find recs, build guides, discover good stuff. Not trying to promote with this post genuinely, but it's [www.hoodtip.com](http://www.hoodtip.com) if you want to see.

- by [unknown](#) **&#x21C5; 1**
  <br/> Why don’t you just use ChatGPT sites for a website?

No coding needed

- by [unknown](#) **&#x21C5; 1**
  <br/> not sure?? can it build the ios app and the backend and all that stuff too? never even thought about this option

- by [unknown](#) **&#x21C5; 2**
  <br/> It can build websites, as the name says.

What’s the advantage? No coding

- by [unknown](#) **&#x21C5; 1**
  <br/> Also, what's the advantage of ChatGPT doing it versus Codex?

- by [unknown](#) **&#x21C5; 1**
  <br/> 😂

- by [unknown](#) **&#x21C5; 1**
  <br/> My harness project I been at it 4 months. Some projects take a long time. I'm actually letting my subs run out and going to get a life now . Got better things to do then ai coding so I'm use up what left of my two 20x max plans.

- by [unknown](#) **&#x21C5; 1**
  <br/> go learn all about harness. Prompt engineering is level 0.

thank me later ;)

- by [unknown](#) **&#x21C5; 1**
  <br/> How complex is what you are trying to build? Where are you running into issues?Even with AI - working for months on something complex is not necessarily a signal you're doing it wrong.

- by [unknown](#) **&#x21C5; 2**
  <br/> It's supposed to be something users can log in, have profiles, create content, get notifications, post photos, build out guides, discover new things etc. All of that stuff more or less works on the website version, and the app should be done soon, but it's more like the aesthetics are just impossible to nail down, and then there's always some small little thing that either doesn't look good or more importantly doesn't work smoothly. Like you can log in, and make a post, but it's never seamless. And then I just keep playing whack-a-mole with all the issues.

- by [unknown](#) **&#x21C5; 4**
  <br/> LLMs are still notoriously _not great_ at UI / UX design, you may need to be super specific to get it to look exactly how you want it, or even use more specialized tools (like Claude Design) or even tweak the design yourself.

As for the small things here and there...I would say that is just how software development has always been. Humans or AI.

- by [unknown](#) **&#x21C5; 1**
  <br/> OK that's good to know. Thanks

- by [unknown](#) **&#x21C5; 1**
  <br/> Use AI to generate a few image mockups for you. Screenshot your design and then tell it what kind of style or vibe you're going for. Chatgpt has a great image model. Then paste those images in your coder and say "I want this, make it look like this". That works the best.

Just don't expect it to look exactly like the mockup, especially high graphic stuff. But overall layout they can definitely do.

- by [unknown](#) **&#x21C5; 1**
  <br/> I've been doing exactly this for the past month or so. It's definitely helped, but I still find Codex can't replicate the quality/design of the screen shot/image created in GPT. But yea it's still a great way to work.

- by [unknown](#) **&#x21C5; 2**
  <br/> Yeah, that's just their weakness unfortunately. They said Astra would fix this, but it's still terrible for me.

- by [unknown](#) **&#x21C5; 2**
  <br/> To hell with UI, security should be your focus and how user data is handled, and how you’ll stay compliant with whatever regulations apply. UI should be the least of your concerns at this point. And what are you going to do about content moderation? Etc, etc.

- by [unknown](#) **&#x21C5; 1**
  <br/> Having a .md file specification to your UI/UX desire has help me in design. It holds the AI accountable to match the formatting outline.

- by [unknown](#) **&#x21C5; 0**
  <br/> odd post. what's your background? if you're having difficulty it could be you lack developer experience, a clear mental model of your codebase, and are relying too much on the model to do the heavy lifting for you.

- by [unknown](#) **&#x21C5; 1**
  <br/> I'm a video producer/journalism background kinda guy. Definitely have zero developer experience. I don't know the first thing about code. So yes I'm relying 100% on the model to do all the heavy lifting in that regard and I'm acting more like a director with a vision for something..

- by [unknown](#) **&#x21C5; 4**
  <br/> So use the Superpowers skill. The moment I found that I was able to build stuff before that it was half done.

Superpowers gets me further along.

- by [unknown](#) **&#x21C5; 2**
  <br/> thanks, will check that out.

- by [unknown](#) **&#x21C5; 2**
  <br/> yes exactly. thats why i said odd post. i didn't mean to be rude but you seem to be aware of why it's happening- at some point, a director might grab the camera himself, but you seem to be asking how to avoid doing that

- by [unknown](#) **&#x21C5; 1**
  <br/> yea in this case I'm a director who doesn't know how to use a camera....
