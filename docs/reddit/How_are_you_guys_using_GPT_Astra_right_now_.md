#How are you guys using GPT Astra right now? [Visit](https://www.reddit.com/r/codex/comments/1wbaote/how_are_you_guys_using_gpt_astra_right_now/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Andremouradeandrade](https://www.reddit.com/user/Andremouradeandrade/)
### **Vote:** 8
---
How are you guys using GPT Astra right now?
I’m curious how people in the Codex community are actually using GPT Astra in their daily workflow.
Are you mainly using it in ChatGPT Work, Codex, or somewhere else?
---
## Comments 70

- by [unknown](#) **&#x21C5; 43**
  <br/> I use it for ai

- by [unknown](#) **&#x21C5; 13**
  <br/> Same here, Astra is very AI.

- by [unknown](#) **&#x21C5; 4**
  <br/> I hear it’s this thing with computers eventually too

- by [unknown](#) **&#x21C5; 1**
  <br/> Maybe in ultra

- by [unknown](#) **&#x21C5; 1**
  <br/> I ask things. It does things. It's pretty neat

- by [unknown](#) **&#x21C5; 1**
  <br/> Can it do porn

- by [unknown](#) **&#x21C5; 1**
  <br/> I am not. It eats too many tokens

- by [unknown](#) **&#x21C5; 1**
  <br/> Me too; I heard it's good for AI.

- by [unknown](#) **&#x21C5; 1**
  <br/> That’s crazy - I too have noticed how AI it seems thus can’t be a coinkydink

- by [unknown](#) **&#x21C5; 1**
  <br/> op just needs to prompt better

- by [unknown](#) **&#x21C5; 0**
  <br/> lowkey same

- by [unknown](#) **&#x21C5; 6**
  <br/> using it for documentation, planning, and orchestration until about 40% usage left in the 5h, then going pure luna until that resets

- by [unknown](#) **&#x21C5; 12**
  <br/> so 5 minutes on Astra and 4:55 hours on Luna?

- by [unknown](#) **&#x21C5; 1**
  <br/> Probably closer to 40 minutes on Astra realistically the past few days

I clear my chats for new features/implementation steps and limit the documentation it has access to based off what section of the codebase it's working in, so it doesn't have huge contexts to consider, but even using luna subagents hasn't been as effective this week, whether thats because of a bug or just the codebase growing

- by [unknown](#) **&#x21C5; 5**
  <br/> Using Astra high for assessing my current development progress and direction, and asking it to give me suggestions. I then paste that suggestion brief to my orchestrator which is Sol medium, and the orchestrator delegates the tasks to other models like glm5.3 flash, muse spark 1.3, and gemini3.8 flash. I’m on the plus subscription, and Astra high’s planning usually costs 25% of 5hr limit, and Sol mediums orchestration can delegate tasks and merge their work for about 4 iterations until the 5 hr limit is used up.

 
       [](https://preview.redd.it/how-are-you-guys-using-gpt-astra-right-now-v0-0btjjaet4foh1.jpeg?width=2048&format=pjpg&auto=webp&s=233e8832a1766ac09e5bda6c77d05f84df1b0486)

- by [unknown](#) **&#x21C5; 3**
  <br/> Could you please explain how your orchestration works and what skills are required?

- by [unknown](#) **&#x21C5; 2**
  <br/> Would also like to know

- by [unknown](#) **&#x21C5; 1**
  <br/> answered

- by [unknown](#) **&#x21C5; 2**
  <br/> answered, if you have any questions just ask, the most important thing for me is the  set up of tmux(the thing that let's you split panes in the terminal) and wezterm(customizable terminal that looks good).

- by [unknown](#) **&#x21C5; 2**
  <br/> Are you more happy with those for implementation/reviews than chatgpt's model? I have unused subs for spark, claude and grok rn, but idk which one to use for what

- by [unknown](#) **&#x21C5; 2**
  <br/> I just make unity mobile games, and I don't know if I'm more happy or not, cause I never got to let codex develop the whole game by itself, I'm a plus subscription user and the limits won't allow it. I tried sol high orchestrator and spawning luna max subagents for the heavy work, but luna mx just isn't good for game development. As for which other models(not gpt or claude) work better on which, or if I'm satisfied of any of those, I just know that glm5.3 flash is good but slow, muse 1.3 spark is the better and faster than glm5.3 flash, and gemini3.8 flash is blazing fast and pretty accurate, just not that good at modelling 3d objects. Haven;t used grok but I hear they're really good too. And the point is, I don't care about model intelligence that much(although the worker models  I use  are all close to frontier), I just care that I have enough usage to devlop the whole game 24/7 or even when I sleep, even if I don;t have pro subscriptions(glm5.3 flash is from merge gateway api and it has 90% off API price, muse 1.3 spark is free on opencode, and I have google AI pro family subscription to use antigravity's gemini3.8 flash)

- by [unknown](#) **&#x21C5; 1**
  <br/> I asked the orchestrator to answer yall:I use a simple planner → orchestrator → worker setup.

Astra High reviews the project and suggests direction. I give that brief to

Sol Medium, which acts as the orchestrator: it splits work into independent

tasks, assigns files, reviews results, merges them, runs tests, and starts the

next round.

Workers currently are:

- GLM-5.3 Flash Max via OpenCode

- Muse Spark 1.3 xhigh via OpenCode

- Gemini 3.8 Flash High via Oh My Pi

Each worker gets:

- A fresh Git worktree and branch

- A brand-new AI session

- Exact file ownership

- Clear acceptance criteria

- Focused tests

- A required commit

I use WezTerm with tmux: Sol stays in the large left pane, while three visible

worker TUIs are stacked on the right.

Workers create completion files when finished. Watcher scripts then type a

completion message into Sol’s tmux pane, waking it without polling or wasting

tokens.

Required skills are mostly Git worktrees, tmux, shell scripting, task

decomposition, code review, and testing.

I prefer stronger models for planning/review and cheaper models for bounded

implementation. On Plus, Astra planning uses roughly 25% of my five-hour

limit, while Sol usually manages around four full orchestration rounds. Usage

varies.

- by [unknown](#) **&#x21C5; 5**
  <br/> to burn away my weekly limit on my 20X plan

- by [unknown](#) **&#x21C5; 2**
  <br/> I’m working for him

- by [unknown](#) **&#x21C5; 1**
  <br/> Mostly in codex I use it as a second set of eyes on complex problems when I build with Claude.

- by [unknown](#) **&#x21C5; 1**
  <br/> Overall, my experience with Astra Ultra (calculated risk) on Plus has been pretty positive so far. I mostly give it tasks that require deep analysis. Sure, that basically nukes the 5 hour limit in one go, but it usually manages to put all of its reasoning and conclusions into a separate document, so I cant really complain. At the very least, it actually looks like it knows what its talking about, unlike some of the other models.

- by [unknown](#) **&#x21C5; 5**
  <br/> [](https://preview.redd.it/how-are-you-guys-using-gpt-astra-right-now-v0-ihiwyd175foh1.png?width=1269&format=png&auto=webp&s=7f4422cfd3c8bc1a7b498bbcaa6b6fb0cc532e34)
      
    accurate

- by [unknown](#) **&#x21C5; 1**
  <br/> i’m using it in codex for personal builds and research. it helped me put my remaining allowance on my mac’s touch bar so i can watch it disappear in real time 😂 i’ve also been using a source review loop that’s helped me cut down on retries and rework

- by [unknown](#) **&#x21C5; 1**
  <br/> I really only use it for research questions, via Work. It's too expensive for my coding tasks so I'm still using Sol Medium in Codex, which does a fine job. I've also read that Astra can be extremely verbose which I do want to see in my code.

- by [unknown](#) **&#x21C5; 1**
  <br/> My sub is 5x, so I'm giving up for now; the Astra eats through my limit like gasoline on a fire.

- by [unknown](#) **&#x21C5; 1**
  <br/> I use it for 3 projects I’m working on.

The first one is a PC port for Perfect Dark, with online multiplayer and a modding pipeline + level editor.

The second one is a multiplayer pirate adventure game with a live simulated world of 500,000 living characters, it’s been pretty awesome to get that up and running. I utilized some concepts I learned from a ton of different dev videos over the years that I always wondered, “why don’t they combine these methods?”

The third one I only just started since Astra can work in Blender. I wrote a story about three years ago or so and I am using it to help present that story via animation for people who don’t want to read it. So far it has actually been pretty damn impressive how capable it is in Blender with modeling, particle simulations, and actual animation.

That said, I am burning through usage and still likely have several more weeks before any of the three projects come to a state where I can publicly share them. I still need to do a lot of testing of the mod pipeline and multiplayer for Perfect Dark, optimizing for the pirate game, and voice work for the animation, so I’ve got a lot to do still; however, it is absolutely amazing how much labor you can offload while you focus on the creative aspects.

- by [unknown](#) **&#x21C5; 3**
  <br/> Tell me more about this PC port of Perfect Dark. Is it based off of the decomp?

- by [unknown](#) **&#x21C5; 2**
  <br/> It’s based off the decomp originally. Though I ended up rebuilding a ton of it to remove the 4/8mb ram limitation, add a toggleable jump feature for players and bots, enable 32-player online social play, add a theater mode, GPU swarm mode for a new game mode where you fight a horde of Skedar, and to facilitate me being able to include an in-client mod framework for custom weapons / characters / music / vehicles and a level editor. It was pretty extensive but I’ve been having fun with it.

It took a lot of effort because I wanted to be able to use modern file types for mods, so I had to extract base game content and then reverse the process to get the engine to utilize external files natively, but it’s actually turned out pretty awesome so far.

That said, I really don’t know where to post about it once I release it lol. Here? It doesn’t include the rom, so should be fine to release, but also a lot of people jump straight to ‘slop’ if they see AI was utilized in any capacity. I have done (only as a hobby, but extensively) quite a bit of game development over the years, and I’m not just doing the cliche “make perfect dark but with mods and internet, make no mistakes,” I’m actually taking great effort to implement best practices with asset manifests and network security, mod distribution, etc.

Edit: it actually started just because my friend wanted to be able to jump, but the game wasn’t built for jumping so a lot of places where you end up being able to jump have no collision on top so I had to rebuild the collision system to get it working practically. But then I wanted to try the Skedar swarm game mode and at that point I just kind of dove in since I needed a custom level for that mode, so needed a level editor, rebuilt the menu system with ImgUI, then added theater so I could review gameplay visually… It really snowballed but I think I’ve been pretty comprehensive to keep it tidy and properly extended without changing the vanilla experience.

- by [unknown](#) **&#x21C5; 2**
  <br/> Yeah I totally get that. To be honest, what you’re making sounds awesome and I would love to check it out if you could share it with me. Recomps are a lot of fun but the idea of a full rebuild and truly modernising the game is a really intoxicating feeling.

It’s so funny how this snowballed for you simply because your friend wanted to be able to jump.

I started making a full rebuild of Super Mario Kart because I wanted to play online with my friends… but it’s snowballed as well, into a much larger project, and I’m equally unsure what to even do with the project at this point since I think most people will just sneer and dismiss it for being made with AI. I’m even codenaming it Slop Kart heh, even though I’ve spent a month of near continuous work on it, probably like 200 hours of hands-on in-the-weeds vibecoding.

Anyway, I’d love to hear more about your project and how you’ve been setting up online play, mod importing, and other kinds of polish for adapting it as a PC game. These are things I’m working on too so I find it fascinating.

- by [unknown](#) **&#x21C5; 2**
  <br/> There are a lot of aspects to it, and some things I added just to make playtesting more fun.

I haven’t pushed a build to the GitHub in a few months, but once I push a solid build I’ll shoot you over the link. The last pushed build was quite broken as I was in the middle of migrating the asset pipeline.

For one, I added a cheat that spawns 3 enemies in the place of each non-unique enemy, scales them down so they’re tiny little dudes with high pitched voices and lowered damage. It’s pretty hilarious and fun.

As for the improvements and such:I’m working towards eventually extending the renderer to allow for PBR materials.The modding pipeline is built into the client, you can import files such as meshes or audio or animations then save them out as a \*.pdweapon file or a \*.pdcharacter file which gets scanned into the asset catalog to be included alongside the native assets.Jumping is awesome, but can be toggled.Mods can be seamlessly distributed by joining a match with trusted players / friends, or selectively for unknown players. If a friend makes, for example, a map based on halo, you can simply join them and play without having to manually add everything. This stuff gets cached temporarily but can be saved either as a whole or partially (e.g. just a specific vehicle or weapon you want).I use an ultra wide curved monitor so improving ultra wide support is a priority for me.As for networking, at the moment I have the client self-hosting and using direct connection, running bot behavior on the GPU and syncing as a texture. It comes with a little overhead but scales easily for large numbers of players or bots, I’ve run tests with 512 characters running around seamlessly, networked.As part of the modding pipeline there is a (currently only about half-polished) level editor similar to Forge in Halo, where you fly around as Dr Carroll and place objects or modify the level base mesh.ALL base game behavior has been converted to behavior graphs, and can be used as a base for making new behaviors of your own. Scripting for custom missions, new weapon or vehicle behaviors, custom bot types, etc.

I’ll try to update this a bit more but these are the major ones.

- by [unknown](#) **&#x21C5; 2**
  <br/> Wait. Astra can do animations in blender? I don't need to learn it any more?

- by [unknown](#) **&#x21C5; 2**
  <br/> I have it running a goal as we speak. It can handle model creation, rigging, key framing, particle simulations, shader tricks, lighting and camera work. Really it’s amazing. I provided a bit of a detailed prompt along with some images I made as reference material and it has been kicking ass. It even generated a fleshed out interior for my spaceship including props and greebling, an animated system of neurons which trigger similarly to facial animations for lip syncing to show synapses firing, a volumetric energy wave overtaking the ship, ripples on a lake from a rock skipping across the surface... I am thoroughly impressed and stunned at its capability

- by [unknown](#) **&#x21C5; 1**
  <br/> I’ve fully switched. It’s amazing, can’t find one complaint. It’s pretty efficient too, feels the same as Sol.

- by [unknown](#) **&#x21C5; 1**
  <br/> I use to instantly burn my weekly quota on pro 200

- by [unknown](#) **&#x21C5; 1**
  <br/> Testing Astra Ultra

 
       [](https://preview.redd.it/how-are-you-guys-using-gpt-astra-right-now-v0-r4sczerbcfoh1.jpeg?width=1170&format=pjpg&auto=webp&s=2fa7b773c1de4b64704ceeef4e92fee21a425496)

- by [unknown](#) **&#x21C5; 2**
  <br/> How is it holding that long with you? 100$ plan is only lasting for 2 hours maximum.  Mostly less

- by [unknown](#) **&#x21C5; 2**
  <br/> Resuming a goal doesn't reset its time.

- by [unknown](#) **&#x21C5; 2**
  <br/> I thought other people get some better luck than me. What if they stop resetting for us. A 200$ will be lost in 1 day of work and what to do later? I think we better get used to Chinese models

- by [unknown](#) **&#x21C5; 1**
  <br/> This will probably change once we get better models that use less compute power. It will be similar to the phone call and internet limits from decades ago. Today we have unlimited internet usage and unlimited calls at a very low price in almost every part of the world

- by [unknown](#) **&#x21C5; 1**
  <br/> this is the most optimistic view point since this all started

- by [unknown](#) **&#x21C5; 1**
  <br/> No more, unfortunately

- by [unknown](#) **&#x21C5; 2**
  <br/> Well, by points:

  1. $200 plan.
  2. Tibo posted in twitter they tuned smth to reduce token usage on long context - I can definitely confirm that.
  3. Yesterday's reset helped a lot)).
  4. I needeed to use banked reset only 2h ago.

- by [unknown](#) **&#x21C5; 1**
  <br/> yesterday's reset did lasted longer yes, 3 hours. but still that's nothing for intensive work. 2X this on 200$ plan is it worthit?

- by [unknown](#) **&#x21C5; 1**
  <br/> $200 из x4 usage compared to $100, and it's not a marketing, I checked amount of usage in tokens

- by [unknown](#) **&#x21C5; 1**
  <br/> I think at some points will need to check it

- by [unknown](#) **&#x21C5; 1**
  <br/> I have 7 projects I'm working on. They all have astra low or medium acting as the main orchestrator or implementor, in codex.

- by [unknown](#) **&#x21C5; 1**
  <br/> To build very complex things. Like this: [https://heymaikol.github.io/network-doctor/docs/scenario-lab/](https://heymaikol.github.io/network-doctor/docs/scenario-lab/)

- by [unknown](#) **&#x21C5; 1**
  <br/> Also ich suche nach dem Besonderen von Astra. Bei Codex ist es z. B. so, er vergisst Pfade, erstellt auf einmal vom Projekt abweichende Systemtiken. Die Anzeige ist zum Beispiel auch anders. Er hat mir immer geänderte Dateien angezeigt Mit +/- der geänderten Zeichen. Da musste ich ihn erst mal dran erinnern.

Was gut war ich habe ihn gebeten, ein Bild zum Thema  … zu erstellen und dann bei Kling daraus ein Video mit meinen Vorgaben zu erstellen. Alles was nötig war war das Passwort. Ansonsten kam genau das Ergebnis wie ich es mir vorgestellt hatte.

Aber da das bestimmt jede Menge Token verbraucht, würde ich das nicht häufiger machen.

- by [unknown](#) **&#x21C5; 1**
  <br/> Building Ai-first business

- by [unknown](#) **&#x21C5; 1**
  <br/> This is how I use it:

 
       [](https://preview.redd.it/how-are-you-guys-using-gpt-astra-right-now-v0-wq4h4n9wefoh1.png?width=268&format=png&auto=webp&s=303323ea5829eb1eab14f1c3b110c622cb7d2c80)

- by [unknown](#) **&#x21C5; 1**
  <br/> im using it to burn off all my tokens before i have any opportunity to waste time using it

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra is nannying my luna subagents. It has to limit scope a bunch (baby birding) But a 5x plan lasts days

- by [unknown](#) **&#x21C5; 1**
  <br/> Sadly im avoiding it due to usage costs.   I wish I could run even on astra light for most of the week but... i can't.   So stuck with sol orchestrating my low tiers.

- by [unknown](#) **&#x21C5; 1**
  <br/> Still using 5.6 Sol for two of my 9-to-5 jobs, and Astra for orchestrating my medical image segmentation research pipeline

- by [unknown](#) **&#x21C5; 1**
  <br/> Not using astra at all

- by [unknown](#) **&#x21C5; 1**
  <br/> Nothing burned thru 3 resets and went back to fable 5.1

- by [unknown](#) **&#x21C5; 1**
  <br/> I was using it for everything but I burned 25% in 8 hours today so I'm gonna shift to using it for everything else except for sol for actual implementations

- by [unknown](#) **&#x21C5; 1**
  <br/> I use it like a champ! But it still drains my

 
       
      
    
    
    
    
    
    
      
        
        
    

    
    
      
        
        
      
      
        .buffering-track-fill {
          stroke-dasharray: 100;
          stroke-dashoffset: 50;
        }
      
    
  
        
      
      
    
  
    
  
  
  
    
      
    tokens like Mohammad Ali did George Foreman in ‘74 if you let it auto review, which I do because I’m going tedious, non-creative work at the moment.

- by [unknown](#) **&#x21C5; 1**
  <br/> I'm using mine to watch a bob ross tutorial and follow it carefully

- by [unknown](#) **&#x21C5; 0**
  <br/> Codex. Mostly writing, to fix itself and other models. Now it's finally writing good prompts for other agents, and it stopped ignoring the obvious next step. I can just say "Okay." and it'll keep going and take the lead. It still fails 20% of the time, but it's getting better.

When they cook a version of Astra with RL as good as 5.6 Sol it's going to be glorious, seriously. This one is definitely GPT-5.5-like.

- by [unknown](#) **&#x21C5; 0**
  <br/> Almost entirely via Oh My Pi, my favorite harness (for now, might change tomorrow).

- by [unknown](#) **&#x21C5; 0**
  <br/> I use it for reddit.
