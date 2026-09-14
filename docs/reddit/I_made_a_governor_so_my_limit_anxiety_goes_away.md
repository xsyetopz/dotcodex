#I made a governor so my limit anxiety goes away [Visit](https://www.reddit.com/r/codex/comments/1wb01g1/i_made_a_governor_so_my_limit_anxiety_goes_away/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [TheRobotCluster](https://www.reddit.com/user/TheRobotCluster/)
### **Vote:** 0
---
Now I can just send messages willy nilly of arbitrary complexity and they’ll queue up, get paced, and I’ll always run out of usage basically the minute my weekly reset hits. It applies to all agent and subagent calls/messages and tool calls within a turn, not just delaying when to start a turn. And I can set prioritization and allow some threads to bypass the governor altogether if I want.
No more wondering if I’m gonna make it through the week.
---
## Comments 20

- by [unknown](#) **&#x21C5; 2**
  <br/> What I want is to limit a particular thread to only use an allocated amount of tokens.

- by [unknown](#) **&#x21C5; 1**
  <br/> It could do that

- by [unknown](#) **&#x21C5; 1**
  <br/> It can or does?

- by [unknown](#) **&#x21C5; 1**
  <br/> Kinda both. Not exactly that but close and I could just tell it to and it would

- by [unknown](#) **&#x21C5; 1**
  <br/> Maybe if your pipeline detects that there are a few prompts queued up for the same agent session then it could chain them together and save a little bit on cache to make your usage stretch that little bit further?

- by [unknown](#) **&#x21C5; 3**
  <br/> I've just read the description again and this tool will even pace tool calls within a response? Do you know how caching works? This tool seems to trade off too much in caching advantages for the usage availability for my judgement. The overall token per week reduction that is incurred as a result of this must be significant, right?

- by [unknown](#) **&#x21C5; 1**
  <br/> I don’t know the ins and outs of how caching works. How would you improve it to address what you’re talking about? And from what I understand I don’t think it reduces weekly tokens, just lets me pace the tokens so that “background non-urgent ongoing tasks that can work indefinitely or in no rush” don’t drain the usage prematurely, so then I have what I need for things I want immediately. And the pace readjusts always

- by [unknown](#) **&#x21C5; 1**
  <br/> If I put into Astra "Does caching affect chatgpt subscriber's weekly usage?" the answer is yes, good cache reuse can substantially reduce the amount of metered compute/credits consumed. As non-cached input tokens consume 10x more usage than non-cached. [https://help.openai.com/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu-credit-based-pricing](https://help.openai.com/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu-credit-based-pricing)

- by [unknown](#) **&#x21C5; 1**
  <br/> From what I can gather the cache retention period or time to live (TTL) for OpenAI is 30 minutes. So if the tool detects multiple prompts for the same agent session it could enforce that there's no longer than 30 minutes between the end of one response and the next prompt being submitted. In practice you'd use a number less than 30 minutes to allow some margin. The bit where the gets complicated is if you decide to allow the tool to re-order prompts the enforce this goal then you run the risk of thread starvation.

- by [unknown](#) **&#x21C5; 1**
  <br/> Or I guess more accurately prompt starvation. As it's the prompt that's starved of threads rather than it being the thread that is starved of prompts. To demonstrate this say you have 200 minutes left to your next reset and you submit a prompt to thread A and a prompt in thread B and then 8 more prompts in thread A. I assume the currently the first prompt in thread A would be submitted, then the thread B prompt and then the rest of the thread A prompts. But if you were to implement changes to make better use of the cache then it might submit all 9 thread A prompts and then submit the thread B prompt. But whereas before the thread B prompt might have been submitted in 20 minutes time it's not going to be submitted in 180 minutes time.

- by [unknown](#) **&#x21C5; 1**
  <br/> The trouble I’m having is that I want to allow tool calls through since they don’t really use tokens, but when tool calls are done processing and finishing, their result comes back and automatically gets fed into the next model request (which is what I’m actually trying to meter). Now there IS a step between tools finishing and their results being sent to the model for continuation, but PostToolUse isn’t available on every tool. And tools can conjure other tools with no model in between.

- So if I governed all tool use, then tools that should run in parallel or sequentially can be delayed enormously with no good reason.- But if I allow all tool use, the model basically only gets governed at how fast it receives MY messages, but can otherwise loop endlessly and ungoverned. This just melts usage limits- if I govern the tool call results so models don’t get the results til schedule says so, that also stalls sequential tool calls unnecessarily where a tool calls another tool without model tokens. Again just adding unnecessary delay.- also not every tool can be governed in this way, so there will still be usage slipping through and still making me run out of usage early, though still much better i suppose. So progress lol

Now there is a way to control the local relay that codex sends every model request through, but then we can have time-out and retry issues with artificially pausing requests for long periods of time. Then tasks and their progress can just go stale without me realizing it. But solving the local relay would really be the sweetest solution

- by [unknown](#) **&#x21C5; 1**
  <br/> Yeah I’ve actually been looking into this to understand and build around it since you left your first comment hours ago lol this has become my night now

- by [unknown](#) **&#x21C5; 1**
  <br/> Does OpenAI offer better price-per-usage with caching on consumer subscriptions too or just API? I’m not doing credit based usage.

- by [unknown](#) **&#x21C5; 1**
  <br/> But honestly the way I'd implement these improvements is to just prompt codex "brainstorm ideas for how to change this tool to make it take advantage of input token caching" then evaluate the ideas that pop out and then if any sound good enough then let it implement the improvements itself.

- by [unknown](#) **&#x21C5; 1**
  <br/> I like that idea

- by [unknown](#) **&#x21C5; 1**
  <br/> Lol why the dislikes people? I don’t wanna run out of usage or even have to think about it. I’ve offended 60% of you with that? Weird

- by [unknown](#) **&#x21C5; 1**
  <br/> Reinventing the 5-hour limit. Nice.

- by [unknown](#) **&#x21C5; 1**
  <br/> Not exactly. Just 132s delay (currently. It would’ve been 84s if I had this going since the reset) between tool/agent calls. And I can give myself back instant access again whenever I want, no restriction to when I want something now. But for stuff that I’m cool with taking an indefinite amount of time, it gets paced to not chew up all my usage for things I do want immediately

- by [unknown](#) **&#x21C5; -14**
  <br/> Get this AI slop out of my sight

- by [unknown](#) **&#x21C5; 11**
  <br/> ...you DO see what sub you're on, right?
