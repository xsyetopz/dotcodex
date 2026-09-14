#DO NOT GIVE CODEX LARGE IMAGES! [Visit](https://www.reddit.com/r/OpenaiCodex/comments/1vrg5qh/do_not_give_codex_large_images/)
### **Subreddit:** [r/OpenaiCodex](https://www.reddit.com/r/OpenaiCodex)
### **Author:** [Ok-File-2759](https://www.reddit.com/user/Ok-File-2759/)
### **Vote:** 0
---
I’ve been working on a project that requires codex to take screenshots of its work to analyze and improve. Each thread can end up taking 10 or more screenshots over the course of its implementation. At first, a fresh thread works pretty smoothly. But after a few images, it starts getting extremely slow. I watched my activity monitor's network tab when threads became slow, and saw megabytes of data being uploaded per second, even when it wasn’t viewing an image in that moment. I had a new codex thread check my local codex logs to see if it could find anything. Here’s what it said:
- Screenshots are stored inline as base64 image data.
- Old full-size images can remain in the active history after compaction.
- One image-heavy task’s session file grew to approximately 71.8 MB.
- Its compacted state still contained multiple megabytes of old image data.
- Individual screenshot results could add several megabytes to the session.
- Internal model continuations were processing approximately 131,000–145,000 input tokens each.
- This happened even during later steps that did not appear to require all the previous screenshots.
After finding this out, I told codex to only capture smaller images/use JGP instead of PNG. I started a new thread and had it continue. This thread was considerably faster. After multiple images, its session file was approximately 4.1 MB instead of 71.8 MB. After compaction, average input processing was approximately 50,000 tokens per step instead of 138,000.
It seems like codex is re-uploading multiple images even when it doesn't need to. Even a simple one sentence text prompt in a thread that's been working with many images ends up taking 10+ minutes. Ideally, Codex should (recommended fix from codex):
- Upload each screenshot once and refer to it using an asset ID.
- Deduplicate repeated images.
- Replace old screenshots with short visual descriptions during compaction.
- Automatically crop, resize, or compress Computer Use screenshots.
- Drop screenshots from the active context once they are no longer relevant.
If you have a similar workflow, upload smaller images. You can tell codex to capture smaller images. If you're a Mac user and you take a lot of screenshots to give to codex, running this in your terminal will make screenshots use JPG instead of the default PNG (PNG has a much larger file size): defaults write com.apple.screencapture type jpg
I've already reported this to OpenAI because it's not ok to need to wait 10 minutes for a simple text prompt because it needs to upload megabytes of data. Hopefully they fix it soon.
---
## Comments 13

- by [unknown](#) **&#x21C5; 2**
  <br/> It should be making contact sheets. Ai can see much better then you. A 4 x 4 contact sheetade determistically is much better for this task.

- by [unknown](#) **&#x21C5; 2**
  <br/> Even then, I still upload lots of screenshots and images myself. So small images a JPG is a workaround, but this is still a bug that needs to be fixed by OpenAI

- by [unknown](#) **&#x21C5; 1**
  <br/> What bug this is how context memory works.

- by [unknown](#) **&#x21C5; 1**
  <br/> Re uploading multiple multi MB images on every turn even for simple text prompts that don't require any image context at all? Even after compaction. Taking 10+ minutes for a response that typically takes 5 seconds. This is definitely not how it's supposed to work, and if OpenAI intentionally does this, then it's a serious efficiency flaw. And if it's sending all those images back to the model for reprocessing each turn, then it's a serious token usage flaw

- by [unknown](#) **&#x21C5; 1**
  <br/> If you see codex not compacting images to summaries it's probably just how the AI decided to do it. I think compaction is also AI driven so it's not deterministic. You could have a separate model ingest the image and summarize it and then return the summary to your main model. Each time an image needs to be processed you can spawn that secondary model with empty context.

- by [unknown](#) **&#x21C5; 1**
  <br/> I guess it could be possible to set up an internal model on computah taking screenshots, analyzing them and just feeding text output to the online model?

- by [unknown](#) **&#x21C5; 2**
  <br/> Useful workaround beyond JPG: do not keep screenshots in the session at all.

Have Codex write each capture to disk under /tmp/shots/step-N.jpg, then reply with a one-line description plus the path. On the next turn, only reattach the 1-2 images still in dispute. Compaction cannot save you if every turn rehydrates 70MB of base64 the model is not even looking at.

- by [unknown](#) **&#x21C5; 1**
  <br/> I’ll try your way. Question tho.

So who’s reading the image, if you’re storing the image description on that path? You said ‘Have codex write each capture’. And if codex is reading the image then putting the description there, so what’s the difference in between just putting the image in the normal chat and your way

- by [unknown](#) **&#x21C5; 1**
  <br/> What would be the best way to do this on Windows? Is there a setting to save screenshots as JPEGs?

- by [unknown](#) **&#x21C5; 1**
  <br/> Idk if this works in codex or not, you can give it a try. So I use kiro sometimes, and it has a hard cap on image sizes, and that’s 2000px and once I put a image in the chat that’s more than that size, then it just stop performing at its efficient level, and after that any image doesn’t matter less than the hard cap or not. It’s not gonna read it. And also the models stop behaving and responding in any intended way.

So the workaround I use for it, I just compress the same image to a smaller size. I have my own tool to compress it, and that does somehow work. Idk why. I have tried compressing with Gemini as well, and that works too.

- by [unknown](#) **&#x21C5; 1**
  <br/> ive got an extremely long chat working on websites and have image generated over 100 times with complex changes and codex has been working great for me. normally i start new chats but its performance hasnt been negatively affected at all surprisingly.

- by [unknown](#) **&#x21C5; 1**
  <br/> 不用谢
