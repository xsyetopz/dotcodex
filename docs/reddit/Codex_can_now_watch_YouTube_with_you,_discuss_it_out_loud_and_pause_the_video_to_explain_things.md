#Codex can now watch YouTube with you, discuss it out loud and pause the video to explain things [Visit](https://www.reddit.com/r/codex/comments/1w9lucp/codex_can_now_watch_youtube_with_you_discuss_it/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [ajajkaka](https://www.reddit.com/user/ajajkaka/)
### **Vote:** 107
---
I built this for OpenAI’s WebMCP Challenge. A small page where I could open a video and have my existing Codex conversation follow it with me.
Originally, I had to type questions or tap emoji reactions below the player. Codex could explain what was happening, pause the video and react back. It worked, and I thought it was a decent little project.
But what I actually wanted was to just watch something and talk. I kept mentioning voice and even put it in the submission as the next step. I assumed I’d have to bolt another system onto it, and the whole thing would feel awkward rather than native.
**Then I tried it with the updated Codex voice mode.**
I ended up watching a video and having an actual conversation about it. “Wait, what did he mean by that?” “Do you agree with him?” Sometimes asking for an explanation, sometimes just commenting on what we were watching. Without stopping to type or explain which part I was talking about.
To start, I paste a YouTube link into the page and ask Codex to connect to the session (screenshot in comments). Then I turn on voice in the same chat.
**It keeps following the video even when I’m not saying anything.** I have it set to check the current frame and visible subtitles every five seconds of playback. The video keeps playing between checks. I don’t have to upload screenshots, send another prompt or keep telling it to continue.
Through WebMCP, it also knows the playback position and can control the player. It can pause for a longer explanation, resume afterwards and put reactions over the video. I can tell it to stay quiet unless I ask something, or let it comment when it notices something worth discussing.
The emoji buttons still work too. I can tell Codex what I want them to mean, so a question mark could mean “explain this part” or “check whether that claim is true.”
**There’s no separate chatbot on the page.** It’s a small site hosted on ChatGPT Sites, connected to the Codex conversation I already use. No copying subtitles into another service or starting a different conversation every time I want to ask something.
I’ve wanted this for ages, but I expected it to feel like a workaround. The text version was useful. This feels like something I’d actually leave on while watching a lecture, interview or video essay. I built the thing and it still feels like magic to me lol.
Still a prototype. For videos where the dialogue matters, captions need to be available and turned on.
Try: [https://watch-with-gpt.vechenkovh.chatgpt.site](https://watch-with-gpt.vechenkovh.chatgpt.site)
Repo: [https://github.com/miuuyy/watch-with-codex](https://github.com/miuuyy/watch-with-codex)
---
## Comments 25

- by [tHEuKER](https://www.reddit.com/user/tHEuKER/) **&#x21C5; 1**
  <br/> **You might want to consider listing your project on the weekly Show-Us-What-You-Built post**. Watch for it on Wednesdays. Highest commented project wins a week promotion on [r/Codex](/r/Codex/) and gets on the Hall of Fame sidebar. See what that looks like below with last week's winner.

*Last week's most popular project was *[u/tHEuKER](/user/tHEuKER/)*  with the *[*Blur2 racing game project*](https://www.reddit.com/r/codex/comments/1w4jr2f/comment/p7853as/)* which is a recreation of an unreleased sequel to the 2010 battle racing game, made by reverse engineering the Xbox 360 prototype discs available online, and rebuilding the whole thing from the ground up in Unity.*

*Join their YouTube channel here: *[*https://www.youtube.com/@tHEuKER*](https://www.youtube.com/@tHEuKER)* and follow updates on the project at *[r/BlurGame](/r/BlurGame/)*.*

- by [unknown](#) **&#x21C5; 6**
  <br/> [](https://preview.redd.it/codex-can-now-watch-youtube-with-you-discuss-it-out-loud-v0-2rzutngs12oh1.png?width=2550&format=png&auto=webp&s=559250e8d8e3783bb9a05edeea53fe7185784770)
      
    I was surprised myself at how native it wasI decided to just try it because I found out that the voice mode had been updated, in fact the project had been submitted a couple of days before that

- by [unknown](#) **&#x21C5; 4**
  <br/> Really appreciate the response here. I also posted the demo on X, where it’s been a bit rough. If you enjoyed it, a like or repost there would genuinely mean a lot:

[https://x.com/miu21590/status/2096855885817532911](https://x.com/miu21590/status/2096855885817532911)

This is an open-source hackathon project, not a separate AI service. But I’m not dropping it after the hackathon, I’ll keep updating the repo and improving stability.

If you try it and something breaks, please open an issue or let me know here. I’m happy to work through it. I’ve wanted this kind of experience for a long time, and now that it actually works, there’s a lot more I want to do with it.

- by [unknown](#) **&#x21C5; 6**
  <br/> How much usage would this cost?

- by [unknown](#) **&#x21C5; 11**
  <br/> [](https://preview.redd.it/codex-can-now-watch-youtube-with-you-discuss-it-out-loud-v0-yz5pmoxnb2oh1.png?width=969&format=png&auto=webp&s=3c566cb9c6a4ecbf0695bbfcce5d8bbd0b411d40)
      
    300 images is 1,500 seconds of video (over 20 minutes), and about a million tokens.

using Terra (which is actually suitable) it costs much less than it seems, via the API less than a 2 dollars, with a Codex subscription it's negligible

it sounds scary but in practice coding is just much more heavier

- by [unknown](#) **&#x21C5; 19**
  <br/> ALL OF IT

- by [unknown](#) **&#x21C5; 2**
  <br/> I guess that’s for 10sec video only

- by [unknown](#) **&#x21C5; 10**
  <br/> I also think Theo is an annoying idiot

- by [unknown](#) **&#x21C5; 3**
  <br/> besides vibe coding a below average codex app clone... what does he actually ship? he yaps too much

- by [unknown](#) **&#x21C5; 3**
  <br/> he has shiooed t3 code, which is actually good, but the app is damn slow. If you use a lot of subs like cc and codex and opencode, you should try it atleast once. It is not for me, as the app is very slow, and i dont mind switching tabs. Also it is an overkill for me, i am not running 10 parallel agents😅

- by [unknown](#) **&#x21C5; 2**
  <br/> He’s basically just an influencer chasing views. The annoying part is watching dev tool companies bend over backwards for him just for free marketing, not because his opinions are actually good.

- by [unknown](#) **&#x21C5; 1**
  <br/> haha, i'm a redditor! I know things! my opinions are superior!and Yes! popular guy bad!

- by [unknown](#) **&#x21C5; 1**
  <br/> Found Theo's #1 fan

- by [unknown](#) **&#x21C5; 2**
  <br/> I built something similar yet different but using Gemma 4 12b local model and have used a lot when watching football World Cup clips on YouTube and asking questions when was not able to understand why penalty, player info etc

- by [unknown](#) **&#x21C5; 1**
  <br/> there are a lot of ways, im sure probably some plugins even exist specifically for this, but thanks to webmcp here you just open link and ask chat gpt to join, not much context needed

- by [unknown](#) **&#x21C5; 1**
  <br/> I like Gemini better for this. Just give URL and it transcribes, sums up does everything.

- by [unknown](#) **&#x21C5; 1**
  <br/> youtube summarizer is good, but this is quite a different thing

with codex voice you can discuss the video while it’s playing, ask about the exact moment, pause it, explain something and keep watching

I think it can be useful for lectures, long interviews, accessibility, or simply when you don’t want to constantly pause, type and switch tabs

- by [unknown](#) **&#x21C5; 1**
  <br/> The problems we discovered while testing this repository were:

  - It does not preserve the frame from the exact moment of a question. The ❓ reaction records the correct timestamp, but the screenshot may be captured several seconds later. For example, a question submitted around 27 seconds was paired with a frame from approximately 34 seconds.
  - The five-second interval is not guaranteed. Processing delays caused actual gaps of roughly 9–15 seconds, and the observer reported missed checkpoints.
  - It cannot hear the video’s audio. It receives frames and playback information only. If captions are unavailable or not visible, it cannot understand the dialogue or sound.
  - It sees snapshots, not continuous video. Short actions occurring between captured frames can be missed or only inferred.
  - Playback and observation are separate operations. Starting the video does not automatically start the observation loop, which can make users believe Codex is watching when it is not.
  - Pausing stops observation and reaction processing. watch_observe_next_moment fails while playback is paused, so the reaction workflow does not work properly on a paused frame.
  - Playback navigation controls are incomplete. The WebMCP interface supports play and pause, but not seeking, restarting, or jumping to a timestamp. We had to manipulate the YouTube controls directly to restart the video, and the first attempts failed.
  - Seek detection was unreliable. The playback position jumped from approximately 67 seconds to 20 seconds, but seekDetected was still reported as false. The most important issue is that the timestamp of the viewer’s question and the frame Codex actually receives may not match. The page should capture and preserve the frame immediately when ❓ is clicked, or automatically pause the video before capturing it.

- by [unknown](#) **&#x21C5; 1**
  <br/> appreciate feedback!

- by [unknown](#) **&#x21C5; 1**
  <br/> I watched that video.

The part you clipped is literally just repeating what the video is saying...

- by [unknown](#) **&#x21C5; 1**
  <br/> So it works?

- by [unknown](#) **&#x21C5; 1**
  <br/> I guess it depends on what you mean by "works".

Does it accurately get the content form the video? Sure. It looks that way

Does it add anything new or help the user understand and engage with the content more?

If the clip you posted is any indication... No. In fact it probably is worse for the user because they're wasting their subscription usage on it for no extra value.

- by [unknown](#) **&#x21C5; 1**
  <br/> Depends on user probably

Short summaries, accessibility reasons etc still makes sense for someone

The most practice case for regular users is to ask it to stay quiet until you click on ❓ if you need more details (if you’re watching lecture maybe)

- by [unknown](#) **&#x21C5; 1**
  <br/> Just wait for ads.
