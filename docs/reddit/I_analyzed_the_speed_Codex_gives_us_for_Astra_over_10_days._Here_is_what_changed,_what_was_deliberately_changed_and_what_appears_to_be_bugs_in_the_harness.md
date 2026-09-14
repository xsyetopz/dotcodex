#I analyzed the speed Codex gives us for Astra over 10 days. Here is what changed, what was deliberately changed and what appears to be bugs in the harness [Visit](https://www.reddit.com/r/codex/comments/1wf911a/i_analyzed_the_speed_codex_gives_us_for_astra/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Charming-Author4877](https://www.reddit.com/user/Charming-Author4877/)
### **Vote:** 10
---
[](https://preview.redd.it/i-analyzed-the-speed-codex-gives-us-for-astra-over-10-days-v0-17jlzqkdoaph1.png?width=800&format=png&auto=webp&s=c08c5707f0642d9a67ade6c309cef669e54afa71)
Codex performance statistics, nerfs and bugs
*Since Sep 10, parts of Astra usage are about 3x slower than in the first week.**Some parts have clearly been identified as deliberate nerfs (as they differ between slow and fast mode) and others appear to be bugs in Windows security layer from excessive codex session usage.*
The entire analysis is only related to Astra usage.
I show what OpenAI has done to reduce our performance, what their harness is causing inside Windows and partial corrections which gave me 3 times faster speed despite the ongoing nerf.
1. Token generation performanceWriting, thinking, editing, commenting.
Mode
Measured speed
Change
**Slow**
33.5 - 34.2 tok/s
None
**Fast**
49.4 - 65.2 tok/s
None
Slow mode has been extremely consistent every day.
Fast mode has also stayed inside the same range since day one.
So:
- Token generation is throttled to about 33 tok/s in slow mode
- Fast mode maxes out around 65 tok/s
- Generation itself has **NOT** been nerfed
- Fast mode is closer to 2x generation speed, not 1.5x
2. Delay between file-inspection callsThis is the delay around chunked reads, so whenever codex reads a file (or any other tool calls)
Date
Before read starts
After read / next tool call
Fast mode
**Launch**
1.75 sec
3.75 sec
No meaningful difference
**Sep 6**
2.5 sec
6.2 sec
About 20% faster
**Sep 10-now**
3.3 sec
5-8 sec
1.7 sec + about 4 sec
This is where OpenAI levers its performance nerf, and they did it selectively only for normal mode, not for fast mode. **So this is not a harness issue, it's deliberate slowdown.**
At launch, slow mode spent about: 1.75 sec + 3.75 sec = 5.5 sec
Now it spends roughly: 3.3 sec + 6.5 sec = 9.8 sec
And in fast mode on launch and now: 1.7sec + 4 sec = 5.7 sec
**Fast mode is unchanged since launch, slow mode half as fast**
There are two separate delays:
- The delay before a chunked read starts increased from about 1.7 sec to 3.3 sec in non-fast mode
- The delay after reading also increased heavily, from about 3.7 sec to roughly 5-8 sec
This started around Sep 5.
The stable gap between fast mode and normal mode is why I do not think this is random sandbox performance.
The harness is being made to wait.
This is the main lever currently slowing Astra down and increasing perceived usage time.
3. Time to apply a finished patchThis is not generation time. The patch is already finished - edits are being applied to files.
Date
Patch apply time
Sep 4-5
about 6 sec
Sep 6
about 10 sec
Sep 10-11
about 14 sec
Sep 12-13
18-19 sec
This is currently the strongest contribution to slow Astra usage.
A patch that took about 6 seconds now takes 18-19 seconds.
That is about 3x slower.
Unlike the tool-call delays, this is almost identical in slow and fast mode.
So I do NOT think this is the same deliberate throttling.
This looks like slop inside the Codex Windows harness.
4. The Windows harness slopEach patch / file edit makes the sandbox spawn 4 helper processes.
Those helper processes have become progressively slower.
The machine currently has:
Windows logon session
Count
CodexSandboxOffline
27,682
CodexSandboxOnline
2,644
All other accounts combined
21
Codex alone has created:
**30,326 logon sessions**
That is outside anything resembling normal Windows 11 usage.
The slowdown ends up ruining performance of lsass.exe, the Windows service responsible for authentication and credentials.
The longer Codex runs, the more the Windows authentication state affects helper-process startup.
That explains why patch application keeps getting slower even though generation speed stays exactly the same.
If you do not reboot frequently, this can seriously ruin Codex performance.
5. Fixing the harness slop and testing the fix**Test 1 - Change the sandbox to the unrecommended "unelevated" mode**
[windows]
sandbox = "unelevated"
Measurement
Time
Previous elevated-mode median
19.65 s
New test 1
5.82 s
New test 2
3.81 s
New test 3
4.89 s
**New median**
**4.89 s — 75% less time**
**4 times faster !!!**
**Test 2 - back to "elevated mode"**
Same scratch-edit test
Unelevated
Elevated
Edit 1
5.82 s
22.48 s
Edit 2
3.81 s
20.92 s
Edit 3
4.89 s
20.44 s
**Median**
**4.89 s**
**20.92 s**
This shows how badly damaged "lsass" is from the codex session spam, 33000 logon sessions and lsass is close from collapsing. This will make ALL of windows laggy and slow, logins, browser passwords, and so on.**The delay of 5 seconds is still horrible, why does Codex sandbox need 5 seconds to apply a tiny patch ?****That should take 5 milliseconds.**
**Update 3:**
icacls 'd:\devel\' /inheritance:eThis has moved the edits from 5 seconds down to 220 milliseconds.It stopped needless elevated edit requests to the compromised lsass service entirely after setting the sandbox to unelevated mode.
Summary
Finding
First week
Now
Result
Slow generation
33-34 tok/s
33-34 tok/s
Unchanged
Fast generation
49-65 tok/s
49-65 tok/s
Unchanged
Slow read delay
1.75 + 3.75 sec
3.3 + 5-8 sec
Almost 2x worse
Fast read delay
About same as slow
1.7 + about 4 sec
Much less affected
Patch application
about 6 sec
18-19 sec
About 3x worse
Codex logon sessions
-
30,326
Windows lsass service compromised
So the picture is pretty simple:
- Generation speed has NOT changed
- Fast mode generates about 2x faster than slow mode
- Tool-call latency has been nerfed in both modes, much harder in slow mode
- Patch application has gone from 4-6 sec to 18-19 sec  | BOTH is inacceptable. applying a small patch should be done in a millisecond.
- The Windows harness has created more than 30,000 Codex logon sessions
- The patch slowdown appears to be tied to Windows authentication / lsass.exe overhead
Astra itself did not become 3x slower.
The slowdown is in everything around Astra, partly nerfed by OpenAI deliberately and partly from sandbox slop.
---
## Comments 3

- by [unknown](#) **&#x21C5; 1**
  <br/> Something to note, this slowdown is also visible on web chat (including Work).

- by [unknown](#) **&#x21C5; 1**
  <br/> I tested ChatGPT Chat, Work, and the Codex Harness for output speed.


      
        
          
              Interface / Mode
            
              SOL
            
              Astra
            
        
        
      

      
        
            
                **ChatGPT Chat**
              
                **134 tok/s**
              
                **63 tok/s**
              
          
            
                **ChatGPT Work**
              
                **53 tok/s**
              
                **33 tok/s**
              
          
            
                **Codex Harness**
              
                **53 tok/s**
              
                **33 tok/s**
              
          
            
                **Fast Mode (Codex / Work)**
              
                **80 tok/s**
              
                **63 tok/s**
              
          
      
    Observations  - **ChatGPT Work and the Codex Harness have effectively identical output speeds** in my testing: 53 tok/s on SOL and 33 tok/s on Astra.
  - **Fast mode** increases SOL to around **80 tok/s** and Astra to **63 tok/s**.
  - **ChatGPT Chat appears to run Astra at roughly the same speed as Codex/Work Fast Mode**: 63 tok/s.
  - **ChatGPT Chat SOL is much faster at 134 tok/s**, roughly **1.7× Codex/Work Fast Mode SOL** and **2.5× regular Codex/Work SOL**.

So this seems to confirm the earlier findings: **ChatGPT Work is speed-limited in essentially the same way as the Codex Harness on PC.**

ChatGPT Chat seems to be using the faster configuration for Astra, while SOL in Chat is substantially faster than even Codex/Work Fast Mode. My guess is that Chat SOL may be running a different or more aggressively quantized serving configuration.

- by [unknown](#) **&#x21C5; 1**
  <br/> That's weird because since 2 days (I didn't tested today yet), **ChatGPT Chat** was really really slow, as much and sometimes slower than **Work**. Maybe it's because it's the weekend (Saturday here in EU) or something.

Overall, yes, it's definitively slower now for Codex and Work (regarding Astra, I didn't touched Sol since Astra release).
