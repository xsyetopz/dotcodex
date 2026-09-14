#Can I match Sol max level of build with any cheaper model using multiple independent agents reviews techniques etc? [Visit](https://www.reddit.com/r/codex/comments/1wb1d0g/can_i_match_sol_max_level_of_build_with_any/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Prior-Meeting1645](https://www.reddit.com/user/Prior-Meeting1645/)
### **Vote:** 1
---
I LOVEEE sol max so much but even when using it an orchestrator with muse spark, I keep running out. I have multiple google ai subscriptions as well as opencode but I’m afraid to use their models for this one big serious project I have. But use drain is getting so tedious that I think I want to do it. But my question is, given that they’re really close in benchmarks, do you think I can get the same quality with say just muse 1.3 if I make it do independent subagents reviews? What about gemini 3.8 with /boost. I’m a total vibecoder so I’m afraid it could mess the repo. Can it still mess the repo so much even with Gits? Just looking for people’s two cents.
---
## Comments 20

- by [unknown](#) **&#x21C5; 2**
  <br/> Yeah, have chatGPT web on Sol High design the PR, then implement as much of the PR as it can. Then have it create a handover prompt for your local agent (whichever you choose). Have that agent implement based on that prompt, then have chatGPT web review the commit from the local agent. Then do a review -> resolve -> review cycle until chatGPT web considers it GREEN to merge. This is functionally Sol High level reasoning with a cheap local model being the implementation-hands.

Just do things in a branch, with PRs, and review things yourself before you merge the branch into main.

- by [unknown](#) **&#x21C5; 2**
  <br/> I asked codex and it said **Example prompt:****Design this XYZ PR, then implement as much as you can. Return your implementation as a unified Git patch based on main. Include tests and create a handover prompt for the local Muse Spark agent covering unfinished work, risks and validation. Do not deploy or merge.**

The local agent then:Applies Sol’s patch inside an isolated branch.Checks that the patch is safe and compatible.Completes anything Sol could not do.Runs the application and database tests.Commits and pushes the finished branch.

Does this sound about right?

- by [unknown](#) **&#x21C5; 1**
  <br/> Yup, sounds pretty good to me. You can experiment; my actual prompts at each stage change a bit depending on what I'm doing; but yeah, more-or-less that's the workflow.

- by [unknown](#) **&#x21C5; 1**
  <br/> How can the chat version read the big repo constantly though? Do I connect it to github in account settings? Also you say implement as much of PR as it can. On the chat version? It can do that?

- by [unknown](#) **&#x21C5; 1**
  <br/> What harness are you using?

If it's codex, try moving over to Pi with context-mode plugin.

I find the subscription to last almost twice as much compared to codex harness.

- by [unknown](#) **&#x21C5; 0**
  <br/> Yup codex. I have only heard good things about Pi but is it easy to use for someone with no real coding background? I have been a certified vibecoder for a while though lol

- by [unknown](#) **&#x21C5; 1**
  <br/> Might I recommend OMP (Oh My Pi). It's Pi behind the scenes, but much more plug and play for the average person. Will still require some learning and tinkering but I've been LOVING it.

It's GitHub repo says "Pi with batteries included" 😂

- by [unknown](#) **&#x21C5; 1**
  <br/> I have qwen 3.8 27b 4q and it’s decent for plugging in things and light coding and maintenance. But I started using openrouter.ai with glm 5.3 flash mediu/high and it’s like mini Luna for extremely cheap. To the point where I think it’s cheaper than running qwen 3.8 on my 5090 locally…. I’m using Hermes as a harness. Open router has some free models as well, but you get what you pay for. Million token context for a crappy model still gets you so so product that the model has to think way too hard about waiting time.

- by [unknown](#) **&#x21C5; 2**
  <br/> Luna is cheaper than GLM 5.3 flash

- by [unknown](#) **&#x21C5; 1**
  <br/> [](https://preview.redd.it/can-i-match-sol-max-level-of-build-with-any-cheaper-model-v0-nwnqsbuamdoh1.jpeg?width=1320&format=pjpg&auto=webp&s=748f57b37ae6850a11a3a0519de43a1bdad80961)

- by [unknown](#) **&#x21C5; 1**
  <br/> [](https://preview.redd.it/can-i-match-sol-max-level-of-build-with-any-cheaper-model-v0-3qrw44vnsdoh1.png?width=503&format=png&auto=webp&s=0e2009196701b64f475564c4c4b079e9d7595e7e)

- by [unknown](#) **&#x21C5; 1**
  <br/> Where’s this from? I want this price!!

- by [unknown](#) **&#x21C5; 1**
  <br/> [https://unorouter.com/register?aff=JQzQ](https://unorouter.com/register?aff=JQzQ)or[https://raunai.com/r/68837e83-9695-4bac-92b4-c588f138a3d0](https://raunai.com/r/68837e83-9695-4bac-92b4-c588f138a3d0)

The first has easier payment options and far more models and better prices for non-openAI/Anthropic models, the second has video generation and better prices for openAI/Anthropic models but payments suck (crypto).

They both take advantage of subtoapi style pooling, but uptime and reliability are quite solid, especially for the prices; I've been using them both for the last couple months for my non-openAI mix-of-models systems.

- by [unknown](#) **&#x21C5; 1**
  <br/> Just use your ChatGPT plus account, it is the cheapest option

- by [unknown](#) **&#x21C5; 1**
  <br/> Yeah that’s the go to, but this person said they keep running out and is asking for alternatives to fill the gaps when their credits run dry.

- by [unknown](#) **&#x21C5; 1**
  <br/> [](https://preview.redd.it/can-i-match-sol-max-level-of-build-with-any-cheaper-model-v0-ulk8562cmdoh1.jpeg?width=1320&format=pjpg&auto=webp&s=5c9366a0c305151a2d967d931dd63912f01b8a39)

- by [unknown](#) **&#x21C5; 1**
  <br/> [](https://preview.redd.it/can-i-match-sol-max-level-of-build-with-any-cheaper-model-v0-klc2pn9tsdoh1.png?width=502&format=png&auto=webp&s=a7286d3b6412cada6a5707f378d8bacbc79b2839)

- by [unknown](#) **&#x21C5; 1**
  <br/> Yeah use one sol medium agent and save time and money and move on

- by [unknown](#) **&#x21C5; 1**
  <br/> Check a skill i just published [https://www.reddit.com/r/claudeskills/comments/1war76e/tbag_the_beauty_and_the_grunt_multiday/](https://www.reddit.com/r/claudeskills/comments/1war76e/tbag_the_beauty_and_the_grunt_multiday/)

I am using it in one project with muse spark as orchestrator and muse spark as main worker models, with claude and sol being automatically interrogated only when really needed.

Sol is a good model for many things but is way too nosy to orchestrate efficiently.
