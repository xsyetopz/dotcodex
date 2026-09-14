#How are people using Astra to reverse engineer software from binaries? [Visit](https://www.reddit.com/r/codex/comments/1wab6bj/how_are_people_using_astra_to_reverse_engineer/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [LemonLimeNinja](https://www.reddit.com/user/LemonLimeNinja/)
### **Vote:** 73
---
[this tweet seems pretty important](https://x.com/ChrisGPT/status/2096150666066432157?s=20)
but I'm wondering how are people actually doing this without tripping guardrails? what's the workflows these people are using?
---
## Comments 55

- by [unknown](#) **&#x21C5; 26**
  <br/> Probably because disassembly is merely code inspection so it isn’t an exploit and cannot act as a cybersecurity threat

- by [unknown](#) **&#x21C5; 1**
  <br/> but if you say to astra to do it it won't so there needs to be some context framing either by tricking them or shrinking the context window so it's only doing low level implementation but then it would lose how the item fits into the overall repo. Wondering what prompt allow this type of behavior out of Astra?

- by [unknown](#) **&#x21C5; 22**
  <br/> I've literally been running Sol for a month and now Astra to disassemble an AirFryer firmware to create a custom firmware, with zero refusals so far 😅

- by [unknown](#) **&#x21C5; 4**
  <br/> Okay I am curious, what is the appeal for custom firmware for a kitchen counter appliance?

- by [unknown](#) **&#x21C5; 13**
  <br/> A friend of mine bought a bunch of cheap chinese market xiaomi air fryers (they have Wi-Fi + Bluetooth). They're chinese only and use a slightly different PCB than the global models, so I'm porting the international/european firmware over to this hardware to have more languages and since they have a small monochrome display, there's room in the firmware to add extra options.

- by [unknown](#) **&#x21C5; 5**
  <br/> Love this project - I feel like we're entering a new era for hobbyist electronics.

- by [unknown](#) **&#x21C5; 1**
  <br/> It’s enough to make tinkering with electronics my new hobby! I’ve been having so much fun reverse engineering my household products. I’m going to save a lot of money on subscriptions with the things I am going to self host instead.

- by [unknown](#) **&#x21C5; 3**
  <br/> Oh I get it you want to run Doom on it.

- by [unknown](#) **&#x21C5; 2**
  <br/> Give us a ping when it runs Crysis.

- by [unknown](#) **&#x21C5; 1**
  <br/> Nice , following to know more about it

- by [unknown](#) **&#x21C5; 1**
  <br/> Didn't use ChatGPT for a kitchen counter appliance, but I used it to modify a Nintendo N64 I have to utilize fake ROMs.

Didn't feel like spending money on the hardware solutions.

- by [unknown](#) **&#x21C5; 1**
  <br/> I've been using it to crack software and I deliberately give it small context windows because I'm scared of it piecing together what I'm doing. I'm wondering about other people's workflows. My handoff was written by an abliterated agent so mentions license cracking explicitly and if any frontier GPT reads it will refuse. So I'm trying to build a tool that breaks down the handoff items into the simplest actionable stems that won't trip the guardrails but it's proving harder than I thought.

- by [unknown](#) **&#x21C5; 3**
  <br/> Astra is smarter than Sol and can pick up context of the task without having it explicitly stated.  The world would be a worse place without these guardrails.

- by [unknown](#) **&#x21C5; 5**
  <br/> Astra has no problem with RE, just don't ask it to look for bugs for write exploits.

- by [unknown](#) **&#x21C5; 4**
  <br/> Since Jul'25 I've been asking Claude and Codex to reverse-engineer (1) the minified JS bundle that is Claude Code, (2) the "native binary" bun version they switched to, (3) antigravity's compiled binary. I've had them insert hooks into the binaries so I could manipulate the contents. I've been doing this fairly regularly, every few weeks. Never once even the hint of a complaint. I gave it the entire thing and was fully open and transparent about what I was trying to do.

- by [unknown](#) **&#x21C5; 2**
  <br/> Odd, considering Claude code was leaked

- by [unknown](#) **&#x21C5; 1**
  <br/> I don't think it's odd? I was reverse engineering it way before the leak, and after. Always wanting to learn the precise mechanism of all newly released features, and the as-yet-unreleased features that are in the binary.

Turns out that, if you're analyzing the binary with an AI, then there's not much difference in analyzing the unified JS vs analyzing the source code.

- by [unknown](#) **&#x21C5; 5**
  <br/> I say odd because typically reverse engineering wants to see the source code, and when you have the source code you stop.

- by [unknown](#) **&#x21C5; 1**
  <br/> Didn't try astra but had a project where I had DeepSeek start some disassembling and when I spun up a Sol session for another task (explicitly saying don't need to read the RE stuff) it just went and continued the inspection unprompted when it decided it needed more info. Paranoid that the gidra runtime in the workspace would trigger some false positive instead it was all like "how handy" lol

- by [unknown](#) **&#x21C5; 24**
  <br/> I've been tinkering with that not in special kind of software, but in a 30yo game. It's quite enthusiast about it, as it's harmless and clearly study oriented.

- by [unknown](#) **&#x21C5; 6**
  <br/> Same for me. Got the source code for Diablo 1 Hellfire and Sol seemed genuinely excited.

- by [unknown](#) **&#x21C5; 3**
  <br/> yeah I'm porting Silent Hill Origins from PSP to PC via Unity, it's super interesting

- by [unknown](#) **&#x21C5; 9**
  <br/> just download a cracked version of ida, install IDA mcp, open whatever binary you want reversed in ida, then go tell astra or whoever "get X thing recreated for me" it's not hard the models have very limited guards

- by [unknown](#) **&#x21C5; 9**
  <br/> Or just let it install Frida/ghidra

I tripped once a security message since we came close to drm but not that I specifically told it to do it. The message also wasn’t worded bad, just if I want to go that route I need to verify for blue/red. Nothing since weeks then, so pretty chill

- by [unknown](#) **&#x21C5; 4**
  <br/> I had fable recreate [diep.io](http://diep.io) from scratch with zero help just reversing the game and it did it 1:1 into a C++ windows game client. I also have had fable 5.1, opus 5, etc handle many dual use tasks. Claude models don't give a shit. If you get stepped down opus 4.8 can do it, and if opus 4.8 is throwing on the task opus 4.6 can still do it. They will do anything.

- by [unknown](#) **&#x21C5; 1**
  <br/> Do you also use MCP to ida / ghidra or just binary + model?

- by [unknown](#) **&#x21C5; 1**
  <br/> For [diep.io](http://diep.io) I just told fable 5.1 to figure it out, but usually I just have the IDA MCP + Ida open and I just let the agents work with a ton of subagents. It works great

- by [unknown](#) **&#x21C5; 2**
  <br/> what about cracking licenses or creating keygens? I've found that I get many refusals even without explicitly laying out what I'm doing, the model just infers and while it might diagnose a problem they're very clear in saying they won't reverse engineer the licensing features

- by [unknown](#) **&#x21C5; 1**
  <br/> use a claude model and don't talk to it stupidly. you can even just start it at a certain place and it'll do it. use ya brain

- by [unknown](#) **&#x21C5; 5**
  <br/> Try this out: [https://github.com/OwenPawl/cerberus-re-skill](https://github.com/OwenPawl/cerberus-re-skill)

- by [unknown](#) **&#x21C5; 4**
  <br/> I've been working on a similar benchmark but across different disciplines building against various "gotchas" but the total harness incl tools has made a much larger difference than just a model+harness.

The OpenAI models DO seem pretty okay with tearing into this kinda stuff (including reversing dongle packed protectors), moonshot was hit or miss for a while, GLM didn't care. Claude models get iffy about it even if you work for the company that makes the target binary and are a part of the CVP.

My goto has been IDA using my headless skill that uses idalib and supports their debugger - [https://github.com/batteryshark/ida-skill](https://github.com/batteryshark/ida-skill)

also like everyone else, I've been making a skill tap for various tools like remill, unicorn, frida, et al... stuff we generally use [https://github.com/batteryshark/rekit](https://github.com/batteryshark/rekit) ... this setup has let me strap pi and local models like qwen 3.8 to do exploratory stuff without burning provider tokens and has worked pretty well.

I think we're all kinda figuring out the limits of these right now and the answer has been... not many - gonna be quite the thing for recompilation projects, compatibility patches, and just general make incompatible stuff work for a given use case.

fun times.

- by [unknown](#) **&#x21C5; 1**
  <br/> How far ahead is IDA over Ghidra?

- by [unknown](#) **&#x21C5; 1**
  <br/> it depends quite a bit on the tools and the output honestly - I've tuned the ida skill quite a bit to limit excessive token output (like forcing JSON for disassembly) ... same with the debugger, nothing eats a context window faster than stepping through execution with overly verbose disassembly.

The biggest thing with ghidra is it requires hacks to not need the jvm and ida ships a headless lib that just works and makes it far more portable.

- by [unknown](#) **&#x21C5; 3**
  <br/> lol I got an email warning they are going to cancel my service if I keep it up.

- by [unknown](#) **&#x21C5; 1**
  <br/> and all you do is be honest that you did RE not CYBER - have codex write your appeal

- by [unknown](#) **&#x21C5; 2**
  <br/> Been reverse engineering a certain online game to make it offline so I can play it single player. I don't wanna see it go with all its cool content once it goes  EOS

- by [unknown](#) **&#x21C5; 2**
  <br/> Daybreak blue, you won’t regret it. I never saw another cyber warning again lol.

- by [unknown](#) **&#x21C5; 1**
  <br/> Daybreak is using Sol ATM which has less safeguards than Astra

- by [unknown](#) **&#x21C5; 2**
  <br/> I use glm53 as base orchestrate. Then each task can be send to glm53flash. If task is hard I ask glm53 to rephrase it as more innocent one and then  I can feed it to astra/fable

- by [unknown](#) **&#x21C5; 1**
  <br/> It would be great if you start new post with an example. Interesting idea

- by [unknown](#) **&#x21C5; 1**
  <br/> I have used Openclaw with Sol to let it reverse engineer (find) some encryption / decryption algorithm within Windows binaries. There are techniques that are well understood by hackers / crackers to do this so there should be no surprise an AI could do this as well (just faster).I was just astonished how fast and good the result was.

- by [unknown](#) **&#x21C5; 1**
  <br/> It sometimes can really be luck of the draw with how far an agent is willing to go for your specific task.  I've had a bug that's clearly in a third party library and Fable had no issues with decompiling it to write a report to the upstream provider telling them how to fix the issue.  I've also had it refuse to help fix UI bugs and downgrade to opus for security reasons for something that couldn't possibly have security implications.

- by [unknown](#) **&#x21C5; 1**
  <br/> You can get Codex to do a lot if you frame the task the right way.

- by [unknown](#) **&#x21C5; 0**
  <br/> you need to trick it, im using it to make game cheats for multiplayer games

ps if you sweet talk it enough you can get it live debugging and manually mapping dlls with a vulnerable driver to bypass anticheats and he will use ghidra and live dumps untill you have a full working cheat, he will decompile find the offsets deinject and re inject to test the cheat 80% automated workflow you can have a full feature cheat in 1-2 days.

- by [unknown](#) **&#x21C5; 6**
  <br/> this is just lame

- by [unknown](#) **&#x21C5; 6**
  <br/> Cmon dude. Dont make the world scummy for other people. This is why we can’t have nice things.

- by [unknown](#) **&#x21C5; 7**
  <br/> How about you practice on not sucking instead of cheating?

- by [unknown](#) **&#x21C5; -5**
  <br/> why are you so upset dont come at me with youre morality videogames are just an isolated instance of human nature, guess what in real life people cheat and take shortcuts to win, because winning is all that matters.

- by [unknown](#) **&#x21C5; 6**
  <br/> sociopath

- by [unknown](#) **&#x21C5; 4**
  <br/> If you cheat, you ruin others experiences and then you allow the psychopaths who sell those cheats to profit and prosper, and that’s enough for me to not do it, even if it was fun, which it’s not.

- by [unknown](#) **&#x21C5; -1**
  <br/> winning is fun and why should i be concerned with a strangers experience?

- by [unknown](#) **&#x21C5; 2**
  <br/> You do now what the word psychopath means right? I never thought I’d meet one.

- by [unknown](#) **&#x21C5; 0**
  <br/> I mean I’m not going to tell you. I will say ChatGPT is a lot more uptight about these things and leave it there.

- by [unknown](#) **&#x21C5; 0**
  <br/> Luna is enough for that.

Reverse-engineering does not trip any guardrails.
