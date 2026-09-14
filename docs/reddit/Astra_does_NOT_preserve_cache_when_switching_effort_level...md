#Astra does NOT preserve cache when switching effort level.. [Visit](https://www.reddit.com/r/codex/comments/1w9mxi4/astra_does_not_preserve_cache_when_switching/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [alexmuc92](https://www.reddit.com/user/alexmuc92/)
### **Vote:** 164
---
I know a lot of people using the Codex App are switching the effort level within a thread and waste a lot of tokens because of this.
So I was happy to read, that this was fixed in the current Astra release, which is als stated in the model guidance docs: [https://developers.openai.com/api/docs/guides/latest-model#gpt-6-astra-whats-new](https://developers.openai.com/api/docs/guides/latest-model#gpt-6-astra-whats-new)
So I tested this myself and looked at the logs in OpenCodex:
- 1st message, effort medium- 2nd message, effort medium: cache is preserved ✅- 3rd message, effort light: cache is flushed ❌-> message is expensive again and needs a lot of your usage
I am using the latest version of Codex Mac App (26.901.51231) und opencodex v2.46.0
So I would recommend to stick to your effort level, as long as it is behaving that way.
Anyone know more about this behavior?
Update: Please like and share my Thread on X, so Tibo gets some attention to this topic: [https://x.com/liebisca/status/2096918740046680440?s=2](https://x.com/liebisca/status/2096918740046680440?s=2) Maybe we get some more of them banked resets 🙌
[](https://preview.redd.it/astra-does-not-preserve-cache-when-switching-effort-level-v0-et9kpg4la2oh1.png?width=1080&format=png&auto=webp&s=266b17a54a76b33702248beae716553ddc53440a)
astra model guidance
[](https://preview.redd.it/astra-does-not-preserve-cache-when-switching-effort-level-v0-coa67vqga2oh1.png?width=904&format=png&auto=webp&s=78d82af68f636a570173d0052cf9f30f8d79765c)
Chat in Codex
[](https://preview.redd.it/astra-does-not-preserve-cache-when-switching-effort-level-v0-w8dxh6kic2oh1.png?width=1090&format=png&auto=webp&s=efa7f98dc5c532f8f212b596eb6f0cbd18df157a)
Logs in OpenCodex
---
## Comments 31

- by [unknown](#) **&#x21C5; 70**
  <br/> That's definitely unfortunate, lot of money going to waste until this is fixed.Kind of shocked to see that astra has enough tokens loaded into it's initial prompt that even a first hello message costs 37 cents.

- by [unknown](#) **&#x21C5; 8**
  <br/> That depends a bit on the individual setup. But I have a [AGENTS.md](http://AGENTS.md) of only 40 lines. So yes Astra is a bit expensive, but thats normal.

- by [unknown](#) **&#x21C5; 1**
  <br/> Mind sharing what's your current AGENTS.md? I have been trying to figure out how to optimise it for the latest Astra models and also optimize my token usage.

- by [unknown](#) **&#x21C5; 2**
  <br/> I have a huhge [AGENTS.md](http://AGENTS.md) for sol with subagent usage delegations and stuff. But for Astra its currently empty, as I started today with Astra and I am trying to figure out, how it behaves.

- by [unknown](#) **&#x21C5; 3**
  <br/> I woke up at 99% of my pro x5 sub without even sending a message somehow

- by [unknown](#) **&#x21C5; 1**
  <br/> That initial cost is why I'm going to try the pi harness.

- by [unknown](#) **&#x21C5; 1**
  <br/> Yep I pointed this out 17% context is gone just starting a chat and everybody got mad

- by [unknown](#) **&#x21C5; 1**
  <br/> Its not just agents md, its startup info regarding installed skills, plugins, mcps and built in tooling as well. I got mine down from 34k to 22k by just disabling plugins all the plugins/skills I had installed to deal with sol's scope creep.

- by [unknown](#) **&#x21C5; 11**
  <br/> i just gave up and use the same effort in one conversation now. not worth the hassle

- by [unknown](#) **&#x21C5; 10**
  <br/> I think Tibo said this for Sol, like the effort is injected at the front of the prompt so they can’t cache, but since the announcement says it should be cached, better tag Tibo and pray I think

- by [unknown](#) **&#x21C5; 8**
  <br/> At one point they had a warning when you tried to change it mid session. Not sure why they got rid of that.

[https://x.com/thsottiaux/status/2088729222777094624](https://x.com/thsottiaux/status/2088729222777094624)

- by [unknown](#) **&#x21C5; 3**
  <br/> That warning would make sense. But I never experienced it.

- by [unknown](#) **&#x21C5; 6**
  <br/> Is that maybe because you switched from medium to light, so from higher reasoning to lower? Would be interesting to see if it happens when you switch to a higher reasoning level.

- by [unknown](#) **&#x21C5; 10**
  <br/> Its the same behaviour. Unfortunately the macbook app just does not support this feature as of right now.

 
       [](https://preview.redd.it/astra-does-not-preserve-cache-when-switching-effort-level-v0-2fdchjk9f2oh1.png?width=1092&format=png&auto=webp&s=19b752cd1e82dc06fc9525c976836f1d2d024210)

- by [unknown](#) **&#x21C5; 26**
  <br/> This has been the case for all models not just Astra

- by [unknown](#) **&#x21C5; 36**
  <br/> Yes, but in the model announcement it is stated, that you can now switch effort level while cache is preserved. Thats what you can see in the first screenshot. Here is the link: [https://developers.openai.com/api/docs/guides/latest-model#gpt-6-astra-whats-new](https://developers.openai.com/api/docs/guides/latest-model#gpt-6-astra-whats-new)

- by [unknown](#) **&#x21C5; 19**
  <br/> Ohh interesting, please tag tibo and tweet at him. Hope we get another reset lol

- by [unknown](#) **&#x21C5; 7**
  <br/> Here is the link to my X post, please share it so it gets a bit attention: [https://x.com/liebisca/status/2096918740046680440?s=20](https://x.com/liebisca/status/2096918740046680440?s=20)

- by [unknown](#) **&#x21C5; 4**
  <br/> I do not have a lot of followers on X 😅

- by [unknown](#) **&#x21C5; 5**
  <br/> Dont matter, post it regardless and post the link so we can like it and comment.

- by [unknown](#) **&#x21C5; 3**
  <br/> Wait at least 24 hours, please. I just used my banked reset lol

- by [unknown](#) **&#x21C5; 1**
  <br/> 😂

- by [unknown](#) **&#x21C5; 3**
  <br/> damn thats disappointing. one of the main reasons why i was preparing to switch my workflow. i hope thats just an early bug and will be fixed soon. but great work proving that!

- by [unknown](#) **&#x21C5; 4**
  <br/> These are API docs and it also explicitly states:


      Configuration updates are supported only by GPT-6 Astra (gpt-6-astra) in standard, single-agent mode. They change only reasoning effort.


    I believe the Codex harness boots into Multi-Agent V2.

- by [unknown](#) **&#x21C5; 3**
  <br/> don't quote me on this, a while back i looked into this and it was something like:

the cache key has the model + effort level in it. if you change the effort level, you're changing the key it looks for so you get a cache miss.

they need better cache key creation strategy so that same model different effort hits the same cache. not sure how involved that would be on their backend if they route things differently and have distributed cache

- by [unknown](#) **&#x21C5; 2**
  <br/> how about the cli?

- by [unknown](#) **&#x21C5; 4**
  <br/> same behaviour, just tested it.

- by [unknown](#) **&#x21C5; 2**
  <br/> shhhheeeii... i only saw a warning when switching models not reasoning, ive wasted alot of tokenage

- by [unknown](#) **&#x21C5; 2**
  <br/> Isn’t this also true with Sol?

- by [unknown](#) **&#x21C5; 1**
  <br/> I don’t know if this is dumb, but I have a separate thread for each model and effort level in my projects and just provide context when I need a particular model to take over something from another thread.

- by [unknown](#) **&#x21C5; -2**
  <br/> That is working as intended
