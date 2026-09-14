#Codex with Blender and Godot MCP is amazing. [Visit](https://www.reddit.com/r/codex/comments/1wen17e/codex_with_blender_and_godot_mcp_is_amazing/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [KitKatBarMan](https://www.reddit.com/user/KitKatBarMan/)
### **Vote:** 4
---
I've been messing around with a pretty fun AI-assisted game asset workflow lately. The basic idea is to let the models handle a lot of the repetitive modeling/setup work, while keeping the actual game assets deterministic and usable.
- Codex + Blender MCP generates low-poly furniture, electronics, doors/windows, bathroom/bedroom/office props, etc. at real-world scale.
- Blender builds the materials procedurally and exports everything as GLBs, so I'm not relying on AI-generated sprites for the final assets.
- Those assets get pulled into a Godot room-generation sandbox with a permanently fixed orthographic 2.5D camera, real lighting/shadows, picking, and proper 3D geometry.
- The next step is procedural rooms: randomized footprints, angled walls, doors/windows, exterior-wall logic, room types, and semantic furnishing rules instead of just scattering objects randomly.
I originally experimented with Blender blockouts -> ControlNet/Stable Diffusion -> background removal -> sprites, and it worked surprisingly well, but once I realized the game is eventually going to be fully 3D anyway, importing the actual models made a lot more sense. You get consistent geometry, dynamic lighting, arbitrary camera work when needed, and one asset instead of having to generate multiple rendered views.
The nice part is that the visual style can still stay very "2.5D" during normal gameplay, fixed camera, simple low-poly geometry, stylized materials, while underneath it's all actual 3D and can eventually support procedural houses, close-up camera shots, dynamic lighting, object interaction, etc.
The best part, all of this only costed me about 4% of my weekly use, using Astra Light.
---
## Comments 11

- by [unknown](#) **&#x21C5; 1**
  <br/> 4% of my weekly use, using Astra Light.


    Or few minutes in Blender.

- by [unknown](#) **&#x21C5; 2**
  <br/> Yeah, I've tried that 3d thing with Blender and MCP, and it burns usage like crazy. You have to be lucky enough that it doesn't mess up anything and make a really good prompt. If it messes up, I have no usage left from the 5 hours to fix it, and I have to wait, not to mention my weekly is just.... I don't even care about it anymore lol, it's just gone.

But in my exp. It's WAY better than Fable 5.1, WAY better.

- by [unknown](#) **&#x21C5; 1**
  <br/> This made 180 assets in about 20 minutes and the room generator and used 4% of my pro limit

- by [unknown](#) **&#x21C5; 1**
  <br/> What do you mean?

- by [unknown](#) **&#x21C5; 1**
  <br/> It is a primitive mesh with some colour on. And Archimesh does it asap.

- by [unknown](#) **&#x21C5; 1**
  <br/> Are you a advertisement bot for Archimesh? lol

- by [unknown](#) **&#x21C5; 1**
  <br/> Are you for Astra?

- by [unknown](#) **&#x21C5; 1**
  <br/> What Godot mcp do you use?

- by [unknown](#) **&#x21C5; 1**
  <br/> hybridindie[https://github.com/hybridindie/godot-mcp](https://github.com/hybridindie/godot-mcp)

- by [unknown](#) **&#x21C5; 1**
  <br/> The thing is that THREE.JS even is much better than Godot. And LLMs are also better in THREE.JS than Godot. It looks better, AI can develop better and faster with it, and it's browser-based. Really barely any point in using Godot, only drawbacks. And yes, I tried both a lot.

- by [unknown](#) **&#x21C5; 1**
  <br/> Yeah but I want to do this in C# so your point is kind moot?edit: to clarify, this is going to be a large production style game with a lot of compute and gpu needed eventually - so using a web-browser language doesn't make a lot of sense.
