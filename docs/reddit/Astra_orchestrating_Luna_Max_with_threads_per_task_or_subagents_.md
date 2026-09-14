#Astra orchestrating Luna Max with threads per task or subagents? [Visit](https://www.reddit.com/r/codex/comments/1wcwqlz/astra_orchestrating_luna_max_with_threads_per/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [tavenger5](https://www.reddit.com/user/tavenger5/)
### **Vote:** 2
---
Ive read a lot about this, and know how to do both, but its unclear which would be more efficient as far as token usage over time. I know Luna is pretty slow in comparison to Sol/Astra.
---
## Comments 11

- by [unknown](#) **&#x21C5; 4**
  <br/> if you're using luna max workers, use threads per task, astra likes to poll subagents too often. i would recommend you ask it to set it up where astra gives the prompt to the luna max workers, once it has, it actually goes idle, and waits for the luna max worker to send it's receipt/blocker and then it wakes back up and processes it and then dispatches more luna workers or back to the same one.

- by [unknown](#) **&#x21C5; 1**
  <br/> Thanks. That is what I'm currently doing with a new task.

- by [unknown](#) **&#x21C5; 4**
  <br/> Luna is absolute garbage, I don't understand why people insist on using it.

- by [unknown](#) **&#x21C5; 0**
  <br/> Its cheap. If the coordinator catches its errors its fine. The only problem is, could Sol or Astra do the job with less tokens by itself rather then reviewing the code over and over

- by [unknown](#) **&#x21C5; 3**
  <br/> That's the conclusion many have come to after actually comparing the two approaches. The orchestration itself burns a ton of tokens that could have just been used to actually implement it directly. I've also seen several people say Sol and Astra suggested to switch from Luna subagents to something else because the Luna agents kept making mistakes and getting stuck. Every time I've personally tried using Luna I've regretted it and have had to do the work all over with a better model.

- by [unknown](#) **&#x21C5; 1**
  <br/> I’ve benchmarked this and found that there is a case when you have sufficiently scoped and large enough multi-task effort, that Sol controlling Luna is cheaper than Sol solo.

For most straightforward stuff though, Sol by itself came back cheaper every time for exactly the reasons you describe.

The majority of the experiments I ran found Sol by itself to be cheaper.

But I’m also not convinced the case has been cracked yet, and that there may be a way to optimize this further so that a Luna agent approach is superior in more cases than not.

- by [unknown](#) **&#x21C5; 1**
  <br/> I like this idea and I want to test it out. This a concept I’m exploring now too. Although my idea was to work with an Astra session that will spawn a sol session that can use Luna max subagents. Astra just waits, doesn’t ask for updates, but sol will push updates as necessary to Astra. I can send instructions to Astra if necessary. My hope was that I can still watch the sol session and subagents work just for awareness. But ultimately Astra is just the project manager watching from his fancy corner office waiting for an update

I did try having sol as an orchestrator in the same session previously and while the work got done well, it burned crazy tokens. So maybe new sessions are better. ¯_(ツ)_/¯

- by [unknown](#) **&#x21C5; 1**
  <br/> That's my setup but be careful Luna Max would require highly detailed specs and you can expect implementation gaps and bit amount of back and forth.

- by [unknown](#) **&#x21C5; 1**
  <br/> I had regular ChatGPT Pro 6 write a detailed implementation plan, then fed that to Astra medium, which is opening threads with Luna Max agents.

- by [unknown](#) **&#x21C5; 1**
  <br/> How to tell Astra to create a thread and not a sub agent?  That sounds like exactly what I want. Does it know what a thread is? Do I ask for a fork? Can I specify that I don’t want to carry over the context to the new thread?

- by [unknown](#) **&#x21C5; 1**
  <br/> Say don’t use subagents create top level threads
