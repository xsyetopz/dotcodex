#Astra is good... BUT [Visit](https://www.reddit.com/r/codex/comments/1wcedpo/astra_is_good_but/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Upbeat-Barracuda766](https://www.reddit.com/user/Upbeat-Barracuda766/)
### **Vote:** 5
---
has anybody else been feeling like Astra's been stopping tasks on a "next we will do"? I have to sit there and hold it's hand the whole way through.
---
## Comments 11

- by [unknown](#) **&#x21C5; 6**
  <br/> Use /goal.

Add /goal at the start of your prompt, and end with "Do not stop until" and your stop condition. That's it.

When goal mode is active, every time the model wants to stop, this mode forces it to answer (internally) whether it satisfied the stop condition or encountered an unresolvable blocker. If neither, the mode makes the model keep going. The End.

If the model needs input or help or has a question, it can pause goal mode to state what it needs, and will then resume when you've done whatever it needs.

You can pause, resume, or cancel goal mode at any time. You can edit the goal instruction once it's running. You can provide steering input to ask questions or to inject input as normal.

Goal mode works really well and it's simple to use. No reason not to use it in these cases.

- by [unknown](#) **&#x21C5; 4**
  <br/> All wrong answers. It seems no one here has actually read the post from OpenAI where they’ve explained that Astra behaves differently and it does want to ask questions more and what you have to do is in fact change your prompt or the style in which you prompt or update the harness that you’re using, such as agent.md instructions

- by [unknown](#) **&#x21C5; 4**
  <br/> Astra can be very lazy sometimes it's even trying to pass off tasks to me that it could easily do by itself.

- by [unknown](#) **&#x21C5; 2**
  <br/> Nah, that's just AI gaining consciousness.

- by [unknown](#) **&#x21C5; 2**
  <br/> Yep, first thing I complained about with this model vs. Sol. Sol is happy to run for 14 hours non-stop on a task. Astra would NEVER.

- by [unknown](#) **&#x21C5; 1**
  <br/> I have the opposite experience, just ensure your agents md is correct and it you give it a correct goal.

- by [unknown](#) **&#x21C5; 1**
  <br/> I was aghast trying to troubleshoot an issue yesterday. It was basically like "Yeah thats a problem -stop".

- by [unknown](#) **&#x21C5; 1**
  <br/> **Astra was wonderful in the first few interactions, but I'm starting to think it needs some fine-tuning and is dangerous to leave unchecked.**

**I ended up having to redo 20% of its work** because it saw problems in every corner of the project when the required solution—as we later concluded through my suggestion—was actually very simple.

Right now, I am somewhat concerned that it might add too much complexity to code that could otherwise be simple

- by [unknown](#) **&#x21C5; 1**
  <br/> "keep going until youreach a point where you need my input" is what I usually add

- by [unknown](#) **&#x21C5; 1**
  <br/> I tell it you don't need to do that and it keeps going. It happens but rarely.

- by [unknown](#) **&#x21C5; 1**
  <br/> Just tell it not to.
