#Codex can chat with other tasks. [Visit](https://www.reddit.com/r/codex/comments/1wa0zrf/codex_can_chat_with_other_tasks/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [CommentDebate](https://www.reddit.com/user/CommentDebate/)
### **Vote:** 19
---
You can handover tasks from other chat.
---
![Codex can chat with other tasks.](https://preview.redd.it/codex-can-chat-with-other-tasks-v0-to59czjka5oh1.png?width=640&crop=smart&auto=webp&s=ebcf03a54db350c64367ba65c34d57524c75caea)
---
## Comments 19

- by [unknown](#) **&#x21C5; 5**
  <br/> yeah i didn't realize this until a few days ago myself apparently its been a feature for a while, definetly saves some effort of coordinating things mysellf

- by [unknown](#) **&#x21C5; 3**
  <br/> This only works with the ChatGPT app, right? I tried it from the browser and it didn't work

- by [unknown](#) **&#x21C5; 2**
  <br/> Yeah the app or cli (personally I think that the codex app is *better* for this)

- by [unknown](#) **&#x21C5; 2**
  <br/> [](https://preview.redd.it/codex-can-chat-with-other-tasks-v0-guxebz9db5oh1.png?width=909&format=png&auto=webp&s=d1d9c05540e85076ea294af6666e07c765f6c81d)
      
    They are chatting with each other

- by [unknown](#) **&#x21C5; 2**
  <br/> oh wow didnt know i could do this, how?

- by [unknown](#) **&#x21C5; 3**
  <br/> Just ask it.

- by [unknown](#) **&#x21C5; 1**
  <br/> Ask it what though? "Talk to the other task" how does it index the tasks? Do I give it an id? I need to know what tooling the model has so I know what it can do

- by [unknown](#) **&#x21C5; 1**
  <br/> You can use the task name that shows under the project for reference. I did not even do that; I just said to check the other task that is running.

- by [unknown](#) **&#x21C5; 2**
  <br/> Yes, I've been considering using this instead of using subagents, considering that the main / expensive thread can simply end its turn and stop using tokens altogether until further instructions (by another thread) are received, while I feel an active orchestrator waiting for subagents sometimes seems to burn a lot of unneccessary tokens.

I experimented with this a little bit earlier today and it worked pretty well for my use case; I had a really dumb Luna thread actively monitor whether processes were still properly running, and then have it poke the Astra low thread if anything needed fixing. The only things I noticed were that ownership of tasks needed to be very clearly defined because sometimes the Astra thread refused to address an issue, and the Luna thread sometimes fizzled out for seemingly no reason, so I had to use a periodic scheduled task to ensure that the heartbeat kept going (in hindsight perhaps this could have simply been resolved with setting a goal).

- by [unknown](#) **&#x21C5; 2**
  <br/> You can also schedule a task after another task is completed, after which the timer icon should appear.

So just ask - run a code review after this (name or link) chat completes its task.

- by [unknown](#) **&#x21C5; 2**
  <br/> I've been doing this instead of subagents for months now. I assumed it was common knowledge, but I guess not.

- by [unknown](#) **&#x21C5; 1**
  <br/> Finally. Claude could do it already and its useful for merge stuff when two chats are working on the same project.

- by [unknown](#) **&#x21C5; 1**
  <br/> Codex has been doing this for a while now. It just most people don’t need to have AI to orchestrate tasks for them.

- by [unknown](#) **&#x21C5; -8**
  <br/> Wait you’re JUST learning this? Do you guys not stress test your ai or something? 😂

- by [unknown](#) **&#x21C5; 6**
  <br/> Don't be THAT guy. No ones likes THAT guy. People learn new things all day every day and thats ok!

- by [unknown](#) **&#x21C5; -5**
  <br/> What guy? The one that queries getting the most of your money by using your noggin and spending more than 30 seconds on google? 👀🤷🏻‍♂️ or are you too used to being offended on reddit that you need to involve yourself mr arbiter sir? Lmao

- by [unknown](#) **&#x21C5; 5**
  <br/> Yup. You are THAT guy. Sucks to be you dude lol.

- by [unknown](#) **&#x21C5; -3**
  <br/> Damn, I never considered it like that, you're absolutely right, it DOES suck to be me, I'll be sure to give myself a long look in the mirror my guy, you've really done a great thing here, you've SAVED me<3 lmao, touch grass fella, not everything has to be a battle ;)

- by [unknown](#) **&#x21C5; 2**
  <br/> You are welcome. #dobetter
