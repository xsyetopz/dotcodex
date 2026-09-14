#Astra adding tons of unnecessary guards in code [Visit](https://www.reddit.com/r/codex/comments/1wddj0t/astra_adding_tons_of_unnecessary_guards_in_code/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [evrimfeyyaz](https://www.reddit.com/user/evrimfeyyaz/)
### **Vote:** 1
---
I've noticed that when I'm coding with Astra, it adds guards for cases that are impossible or extremely unlikely to happen. For example:
- There's a check on screen A that needs to happen that isn't even mission critical.
- Screen B is only reachable through screen A.
- Astra still adds the same check on screen B to account for the theoretical possibility that the user might somehow end up on B without going through A, even though there's no path in the app that allows that.
I've been removing things like this from my code a lot since I started using Astra. I care about readability and maintainability so I pretty much always reviewed the code and asked the agent to refactor it since I started using coding agents, but I've only noticed this particular problem with Astra.
Have you noticed this too, or is it just my codebase?
---
## Comments 3

- by [unknown](#) **&#x21C5; 2**
  <br/> happens with all other models

- by [unknown](#) **&#x21C5; 1**
  <br/> Sure, but I've definitely been noticing it more on Astra. Might be a coincidence but I wanted to see if there are others out there experiencing this.
