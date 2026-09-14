#Blender MCP vs Computer Use for 3D Modeling with GPT-6 Astra [Visit](https://www.reddit.com/r/codex/comments/1w8nco7/blender_mcp_vs_computer_use_for_3d_modeling_with/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [JMolto98](https://www.reddit.com/user/JMolto98/)
### **Vote:** 6
---
Has anyone here done a direct comparison between using the Blender MCP + GPT-6 Astra in Codex vs letting GPT-6 Astra work on Blender via Computer Use?
I would assume the lack of vision in the former would make GPT-6 Astra struggle more, as it would have to rely completely on code to generate the 3D models without any sort of visual verification/feedback. Regardless, seems like both methods yield good results.
OpenAI must have sourced some really good 3D modeling datasets for GPT-6 Astra's pretrain; this is the first OpenAI model with such strong capabilities in this area. I remember attempts to do this type of work with older models would often be fruitless. Fable 5/5.1 is also solid, but I feel like GPT-6 Astra's results are often more polished.
---
## Comments 23

- by [unknown](#) **&#x21C5; 7**
  <br/> Mcp and have it create a visual audit loop. More efficient iteration than computer control by a lot.

- by [unknown](#) **&#x21C5; 1**
  <br/> Oh? Any more advice on how to set that up?

- by [unknown](#) **&#x21C5; 3**
  <br/> What I did was have it make a turn table in blender with mcp, set up 10-20 camera angle, make the turn table spin. Now I have it make things with mcp and view it with the turn table.

- by [unknown](#) **&#x21C5; 1**
  <br/> I would imagine enable "Computer Use" plugin. Tell Astra "Use <MCP> to edit and use Computer Use to verify your changes."

- by [unknown](#) **&#x21C5; 1**
  <br/> Yeah, this could work. I may run some experiments later to compare outputs vs tokens burned using a similar technique

- by [unknown](#) **&#x21C5; 1**
  <br/> I haven't used Astra (no access yet...) but with other non-Codex models I literally just told them "take screenshots and evaluate your work before deciding you're finished" and they knew what to do. Found folders full of images they'd taken

- by [unknown](#) **&#x21C5; 1**
  <br/> Can you share what kind of images the models took? I'm curious how the AI sees/thinks.

- by [unknown](#) **&#x21C5; 1**
  <br/> Fair enough. I still have two banked resets, but I am trying to be smart with my $20/mo subscription and don't want to burn all my usage. I figured doing it all through 'Computer Use' would be a surefire way to burn through my weekly quota but haven't really gauged whether there's a significant difference in output quality vs usage between the two. Your approach sounds solid though

- by [unknown](#) **&#x21C5; 1**
  <br/> Do whatever codex picks. Computer use is on another level. Mcp still works good.

- by [unknown](#) **&#x21C5; 1**
  <br/> Valid point. I have seen good outputs from both methods. But I guess my question is about output quality vs usage, as I am on the $20/mo plan and cannot afford to just go ham all the time

- by [unknown](#) **&#x21C5; 1**
  <br/> probably not viable then if you need a pipeline setup for many assets. Have you tried local models yet? They are insanely impressive even on low vram setups. The only catch is retopology, which isn't too difficult to learn and there are a few free apps and plugins that help do the initial work and then you just touch up as necessary

- by [unknown](#) **&#x21C5; 1**
  <br/> I haven't tried local models yet. I heard Qwen-3.8-27B is one of the leading OSS models that can realistically run on consumer hardware, and I did see some impressive results for its size, but I am on an RTX5060 Ti (16GB VRAM, GDDR7) GPU, so I guess I would still need some heavy quantization?

- by [unknown](#) **&#x21C5; 1**
  <br/> 16gb is more than enough to produce incredibly high quality 3d models. But like I said the only catch is the topology is so terrible. You can definitely tweak and adjust the weights to finetune it to your needs though.

Look up trellis 2 or pixel3d

Not sponsored just sharing where I first learned about this stuff:[PixelArtistry](https://www.youtube.com/@PixelArtistry_)

- by [unknown](#) **&#x21C5; 1**
  <br/> Cool! Thanks for linking that channel. I have always been interested in trying local models for this, so might be worth giving it a shot

- by [unknown](#) **&#x21C5; 2**
  <br/> no problem - input image is really important. Try to get it as close to your desired 3d model. gpt is great at making 3d model reference images.

- by [unknown](#) **&#x21C5; 1**
  <br/> Any usage approximation needed for a simple 3d, multiplayer, poker game via unity?

- by [unknown](#) **&#x21C5; 2**
  <br/> 20 minutes 150% usage

- by [unknown](#) **&#x21C5; 1**
  <br/> The useful comparison is probably error recovery, not first-pass quality. MCP should win on deterministic scene edits, while Computer Use may recover better when the result is technically valid but visually wrong.

- by [unknown](#) **&#x21C5; 1**
  <br/> 400% plus usage + 11% pro5x usage for a small sized low poly map matching reference not too bad output, decent quality roughly 1 hour plus usage was all on Fast mode, pro5x was normal speed i used mcp in general

- by [unknown](#) **&#x21C5; 1**
  <br/> Thanks for sharing these numbers. 400% of Plus usage is kind of wild, though lol

- by [unknown](#) **&#x21C5; 1**
  <br/> oh oops there is a correction it is actually wild for sure a more accurate number is maybe 400% of the 5 hour limit that it was , was 4 times 5 hour window reducing weekly usage from 100->(79-83) ish using resets in between to make that happen, whenever the 5h window ran out so actually, so we could call it 100% of weekly plus usage roughly, maybe up to 150% worst case

- by [unknown](#) **&#x21C5; 2**
  <br/> Yeah, this actually makes more sense. Thankfully I haven't gotten the 5-hour limit window back on my ChatGPT Plus account

- by [unknown](#) **&#x21C5; 1**
  <br/> That’s crazy
