#GPT 6 Astra - Thoughts & Feelings After A Long Weekend & Two Resets on 20x - Non Developer Working On Already Profitable Sites' Perspective [Visit](https://www.reddit.com/r/codex/comments/1waaw8s/gpt_6_astra_thoughts_feelings_after_a_long/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Public_Reality_4401](https://www.reddit.com/user/Public_Reality_4401/)
### **Vote:** 61
---
Hey All!
Like a lot of you, I've been messing with Astra since it released on Friday.
I run a site, [miniskyline.com](http://miniskyline.com), that was entirely vibecoded via Codex and Claude. It started back in June and has had constant work done with every frontier model that has been released since. GPT 5.4 and Opus 4.6 on up.  The site pays for my subs, grossing 200-300 a month purely on donations. I've gotten good traction in the 3D Printing community, and got very lucky with some competitor shutdowns. I am not a classically trained developer. I messed with VBA and some C++ in college and in my career (Pricing Management) but it never really clicked. Coding agents have made it accessible to me and the way I work.
Enough preamble on who I am and why what I say matters (it doesn't really, but I create revenue generating software so maybe?)
**TLDR:** The model is fast, it seems to be efficient with its thinking and gives concise answers without exploring out of where it should. Time to response (TTR) is great! Using [Model guidance | OpenAI API](https://developers.openai.com/api/docs/guides/latest-model) to update my repo, I found it was more efficient than just letting it loose on an un-migrated repo. Efficient doesnt mean cheap, and I've gone through 3 resets in 4 days. My fastest was today, in 6 hours I drained from 100% -> 0% with 1 Ultra x Fast and 1 Ultra working on a refactor of my map softwares geometry engine, and new module respectively. It is hungry, but I also don't want to reach for the older models due to the work I typically need to do holding their hands. Either usage limits need to change, or more pricing tiers need to be introduced.
In depth info on my usage, patterns and thoughtsOverall I feel the model is a good value given our current offerings. Here are some comparisons to other models i've reached for to test against.
GLM 5.3 flash is cheap as chips, but at least in my repo, takes 30 minutes to do a basic task and it doesnt keep up when I try larger work. Local models that run on my 5090 are quick, Qwen 3.8 32b, but they produce work that needs many iterations to get to a suitable point. 5.6 Sol works as a strong implementer for Astras orchestration, but is expensive enough that I'd rather just use Astra Light/Medium. Terra is a far enough degradation that I dont feel it's worth switching to except for very specific tasks. Same for Luna. Fable 5.1 is just Astra, but worse and even more expensive. Opus, save for its communication issues, I generally like but usage limits overall are too restrictive with the 5H windows and lack of resets. Sonnet is unfortunate. I haven't tried the Grok models outside of Openrouter but generally haven't thought they provided anything special, so never enough to invest more into that ecosystem. I've tried a number of other models via open router, but my issue then becomes the harness. I'm very comfortable with the layouts and abilities that Codex provides.
Moving on to how Astra has performed for me and the way I use it.  I use it in the codex gui and remote control from my phone. As I stated in my TLDR, I'm not a coder by trade. I do research into what i'm trying to do so I can use more technical jargon, and I find that gets me more focused, quality outputs but I do not know proper development workflows/practices. Shoot from the hip, give the model what I want, and occasionally I throw in a prompt from the aforementioned codex model guidance page. UI work goes to Light, questions about how the software works go to Medium, implementation & planning typically go to high. Rarely will I use xhigh unless i'm just trying to burn tokens as I dont typically see a major quality difference. High seems like the sweet spot from my usage so far. It takes its time when it needs to, but seems fine with thinking for a very short period if its confident.
Where did my 3x resets go during the weekend?- Primarily a 3 day long horizon /goal rebuild of my geometry engine. Around 70 hours now on it. One astra high session instructed not to use subagents was use for the first 24 hours and drained roughly 60% of my 20x. UI work and other optimization passes accounted for the other 40%, and my first full usage of Astra ended around 36 hours. Reset. Feeling good so I put astra high on Fast instead. Well. That killed my reset in about 12 hours on that /goal. Reset again and work like normal most of this morning, until Tibo announced reset in the evening. 1 Ultra x Fast &  1 Ultra x Standard took me from 90% to 0% in just under 6 hours. I now sit here waiting for Tibo. I will note, I do not typically use /goal. This was a rare case where I wanted to test the claims of long horizon abilities of Astra. The refactor is still not complete, though it is being done on a 100K+ LOC codebase. I will update this post in the coming weeks as the refactor finishes.
- I had it work on some 3D models for a game I'm working on centered on 3D printers and was generally very happy with the outputs vs what I was getting with Sol. The GIF is of an animated asset. The prompt was very basic "Produce a GLB asset pack for a game about X. The printer must appear to work properly with all of its major hardware fully modelled and animatied where necessary. I dont want it to look fancy/modern, more junky/put together.
- Then I had it add DLSS support to some shaderpacks for minecraft, as well as port some mods to a version I was trying out. It handled these beautifully and within minutes.
- I had it rebuild some animated loading screens for my site. These turned out wonderfully. Astra took design direction much better than sol and required fewer iterations to get something I was happy with.
Overall I wasted a lot of usage this time just sinking more time into the rebuild of my geometry engine. Its over 100K+ LOC and I naively kept believing Astra when it told me we were hours, not days away from completion.  I feel Astra usage is acceptable on Light-High, but do not feel there is much value in /fast unless you know a reset is coming or you have tokens to burn. I found Ultra only worked well when I would copy in the Agent text blurb from the OpenAI model guide. It lowered the number of agents and I felt Ultra was more tame that way.
Astra is simply the best model I've used and I can't wait to see what OpenAI continues cooking. I hope other AI labs are able to put up a fight, as I do not want competition stagnating and costs inflating more than they already are.
**What are you using Astra for?** Is it working better than Sol? Is it working better than other labs alternatives? Hows your usage been on 1x and 5x accounts?
---
## Comments 19

- by [unknown](#) **&#x21C5; 16**
  <br/> It's good that there is no laser in the image.

- by [unknown](#) **&#x21C5; 5**
  <br/> I take solace in not being the only one to think of that

- by [unknown](#) **&#x21C5; 5**
  <br/> Same here. Had to see what sub i was in

- by [unknown](#) **&#x21C5; 4**
  <br/> I saw this and it freaked me out for a moment. Shit's triggering

- by [unknown](#) **&#x21C5; 2**
  <br/> I'm afraid I slept on it, and still can't figure out what this was a reference to!

- by [unknown](#) **&#x21C5; 2**
  <br/> Fukouna shoujo by vvindowsme, very common shock content back from the early-mid 2010s (probably earlier too). Funnily enough, the gif series itself was mainstream enough not to really be considered "shock" content for a 4chan regular at the time.

censored here but you get the gist: [https://www.youtube.com/watch?v=SCtkcTaQeEU](https://www.youtube.com/watch?v=SCtkcTaQeEU) you really hit the perspective and pixelartiness on the spot lol.

Shock images later unfortunately degenerated to stomach-churning illegal content and that was the end of old /b/ as we know it.

- by [unknown](#) **&#x21C5; 2**
  <br/> Ah gotcha. Yeah I see the similarity in style now. Unfortunate!

- by [unknown](#) **&#x21C5; 1**
  <br/> thank you for sharing, though the rebuild of your geometry engine feels similar to my experience, you can waste alot of usage quickly if you just let it run, especially once the chats start /compacting or if you've enabled the experimental recall thing where it can search through previous contexts - this i feel can send it into almost a death loop, where you end up burning way more cached tokens than required.

I'm having alot more success and making more progress with smaller iterationsPlan > build, plan > build etc. i guess alot of that depends on how much context your specific repo requires to start each loop, mine is only around 40k tokens.

but 100k LOC :O - im impressed it was able to work on it at all tbh.

- by [unknown](#) **&#x21C5; 1**
  <br/> oh forgot to ask, did you feel the result on your geometry engine rebuild was worth it afterwards?

- by [unknown](#) **&#x21C5; 1**
  <br/> From the start, I made it a core tenant that It would be very modular. There are a lot of different functions in different files that can be worked on in blocks. I then have a dependency map for the pipeline so agents can more efficiently bounce around in it without getting overwhelmed. Nothing special, I just asked for that word for word basically.

To hit your other reply, it isnt done. The main point was to reduce complexity, and make it impossible for non-manifold/open edge geometry to form while staying within the same memory and time envelopes of my current one. What takes my current one 8 seconds and 800Mb is taking the new one... 8 minutes and 4Gb. But boy is it watertight!

So the results are yet to be seen! I will update you when I figure it out. At this point, it may have been better to have Astra make more targeted fixes on my existing pipeline. The reason there are so many lines is that it has to support all of the different feature types from multiple planets and setting combinations. Its a doozy. Im sure someone will come along and do it in a couple thousand lines of code, but I'm not that guy!

- by [unknown](#) **&#x21C5; 1**
  <br/> Not exactly sure what the requirements for your geo engine are, but generating watertight meshes is a pretty well solved problem (though it was still somewhat of an open research problem way back in my graduate years - oddly enough thank kinect for the explosion of research and techniques here). I'm not totally up to date myself, but various retriangulation strategies exist with reference implementations, from marching cubes to using signed distance fields for non-convex, up to fasthull for convex, or combinations of exact convex decomposition + fasthull if you want to get fancy.

Your pipeline then could possibly become generate point-cloud with some guaranteed rho density => surface reconstruction of your choice. Fast and cheap.

- by [unknown](#) **&#x21C5; 1**
  <br/> That "hours, not days" part is the bit I'd stop trusting.

At 70 hours, I'd stop asking Astra for an ETA and use the old pipeline as the progress check instead: run the same geometry cases through old and new after each meaningful slice, compare the correctness checks you care about, and record runtime + peak memory. If the new path is still around 8 min / 4 GB and those results aren't moving, that's a much better signal to stop or narrow the rewrite than another estimate from the model.

- by [unknown](#) **&#x21C5; 2**
  <br/> As of this morning, im below 800mb and 40s. On the right path!

Ive switched to using Astra high as an orchestrator of a Sol high session. Burns at 1/3 the rate of just having a single astra high session on /goal and seems to be making more progress.

- by [unknown](#) **&#x21C5; 1**
  <br/> That's a huge improvement from 8 min / 4 GB. Memory is already back inside the old envelope, and <40s is over a 12x speedup from the 8-minute state. If the same geometry cases are still watertight, that's the kind of progress signal I'd trust.

The Astra-high -> Sol-high split is interesting too. If the ~1/3 burn holds through the rest of the refactor, that may end up being the most useful result from the whole test.

- by [unknown](#) **&#x21C5; 1**
  <br/> ... So whats the site? Be great to see what 80x is actually capable of

- by [unknown](#) **&#x21C5; 1**
  <br/> To avoid getting warnings for spam, I wont link it again here, but its in the first couple sentences of the post my guy!

- by [unknown](#) **&#x21C5; 1**
  <br/> lmao sorry - i went straight for the tldr 😄

- by [unknown](#) **&#x21C5; 1**
  <br/> Aha all good. Maybe I should have put the link there!
