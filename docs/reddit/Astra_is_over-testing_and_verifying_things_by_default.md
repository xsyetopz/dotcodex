#Astra is over-testing and verifying things by default [Visit](https://www.reddit.com/r/codex/comments/1wasgkc/astra_is_overtesting_and_verifying_things_by/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [HotLion7](https://www.reddit.com/user/HotLion7/)
### **Vote:** 31
---
In one instance I gave it two sql files containing dev and prod databases schema and asked it to create migration script to add the new things to the prod database,
it did all of that:
- Create the script
- Create MariaDB docker instance
- Verified the database health
- Loaded the dev database
- Ran the script
- Exported the db
- Verified the export
- Ran an instance of the API connected to the test docker prod db
- Ran a bunch of automated tests it wrote itself without me asking
- Stopped the docker instance
that was not necessary at all for just adding few extra columns to some tables.
In another instance, I asked it to add an fadeout animation to a button in a Flutter app,
- It added the animation code
- Created a new test app with one screen containing the exact same layout that button is in with buttons to test animation
- it launched an emulator in the background and launched the test app on it
- it triggered the animation and kept taking screenshot every few milliseconds
- then it reviewed the screenshots.
That was also unnecessary at all, I've got the app running in an emulator already with hot reload just ask me to test it
---
## Comments 38

- by [unknown](#) **&#x21C5; 30**
  <br/> 765 tests passed....

Cool, I just said print hello world.

- by [unknown](#) **&#x21C5; 18**
  <br/> just try sol , it's like 3x of that

- by [unknown](#) **&#x21C5; 3**
  <br/> And still climbing.

- by [unknown](#) **&#x21C5; 13**
  <br/> Yeah. For me it decided that just git pushing isn’t enough, so it used computer use, and went to GitHub to verify the push

- by [unknown](#) **&#x21C5; 1**
  <br/> Lmao bro why didn’t you take a picture of that. That’s fucking hilarious 😆

- by [unknown](#) **&#x21C5; 1**
  <br/> Not exactly git, but something synced to git(that was said in an Md file)

- by [unknown](#) **&#x21C5; 3**
  <br/> Haven't used Astra yet, but this sounds exactly like GPT-5.6.  It will mock everything to the lowest depths of hell, and then assert against the fabricated data.  I was building a unified error code system for an application (think Stripe [error codes](https://docs.stripe.com/error-codes)).  I have explicit instructions to test behavior, not implementation details, and it used these relevant skills while building out the solution.

Most of the time, it creates useless tests like these:

const errorExample = {
  code: "example_code",
  description: "example description",
}

test("error", () => {
  expect(errorExample.description).toBe("example description")
})The problem is that it was defaulting to this kind of testing approach for every implementation, regardless of my instructions.  I eventually banned testing, unless explicitly requested, in my AGENTS.md.  I can guide it much better in a dedicated session.

- by [unknown](#) **&#x21C5; 3**
  <br/> Yeah this is why so many people have bugs it will mock some shit then claim shit is properly implemented when not even actually looking at what’s being done across the code it’s infuriating I think OpenAI is really missing on how proper testing is done in software dev or expecting devs like us to guide it. I can’t stand how it does tests and considered things green off some dumbass shit like what you just said

- by [unknown](#) **&#x21C5; 3**
  <br/> Noticed it wanted to retest everything every time i ran it. You need to tell it to only test things relevant to your feature. Then run regular full tests. I tried one thing with astra and it uses my entire 5 hour limit every query but doing this saved me quite a bit of tokens

- by [unknown](#) **&#x21C5; 3**
  <br/> same issue here except i'm working with stripe gifts vs subs issue on my live platform, i asked it to fix a small bug in how gifts display and it rewrote the whole thing to make gifts a subscription-based and recurring instead of like every single other crud platform on earth

- by [unknown](#) **&#x21C5; 2**
  <br/> I was able to tell Sol and Astra to back of the profiling and testing a bit. Seems to have worked.

- by [unknown](#) **&#x21C5; 4**
  <br/> my steak is too juicy, my lobster is too buttery

- by [unknown](#) **&#x21C5; 9**
  <br/> it's a problem when a too juicy stake costs 3x as much as a normal one

- by [unknown](#) **&#x21C5; 3**
  <br/> oh yes this old bs.whats going on is, I  try to buy a steak. The chief runs to the kitchen then decides he needs to make a steak 90 times and never gets around to doing the thing you paid him to do, which was make YOU a steak.

- by [unknown](#) **&#x21C5; 1**
  <br/> It is when the chef is paid by the token then refuses to cook for rest of the week because he spent all the budget on one meal

- by [unknown](#) **&#x21C5; 2**
  <br/> Because you’re using high intelligence frontier models for tasks that are far too simple for it.

More specifically you’re likely using too high a level of reasoning or too frontier a model for your basic tasks. The model will always use the reasoning level/reasoning token allotment you put, so if you put it on “xhigh” which might allot 4 turns of reasoning when called for. If the model fully scopes, maps, and reasons your task in turn 1 because it’s a simple problem what do you think it’s spending the rest of its reasoning turns on?

The only thing it can do for the task. It writes an insane amount of completely unnecessary tests and over engineers the problem into the ground. Because it had too many reasoning turns for the given problem.

- by [unknown](#) **&#x21C5; 2**
  <br/> in both cases it was Astra low

- by [unknown](#) **&#x21C5; 4**
  <br/> As I said, you’re using Astra for what sounds like a Terra High task at most. Honestly sounds like something I’d send to Luna.

You’re driving the Ferrari to the gas station for a Big Gulp

- by [unknown](#) **&#x21C5; 6**
  <br/> If it's so smart, maybe it should figure out how to not be so dumb.

- by [unknown](#) **&#x21C5; 2**
  <br/> Its not smart, its just deep and relentless.

It doesnt care about time, tokens, cost.

- by [unknown](#) **&#x21C5; 2**
  <br/> Thank you, I was being facetious

- by [unknown](#) **&#x21C5; 2**
  <br/> Internet hides intentions well...

- by [unknown](#) **&#x21C5; 1**
  <br/> 💯Have a nice day brotha!

- by [unknown](#) **&#x21C5; 1**
  <br/> Do you have a configured Agents.MD file with instructions on what Astra should be doing for any given task

- by [unknown](#) **&#x21C5; 1**
  <br/> I have [Agents.MD](http://Agents.MD), but it doesn't cover testing, only coding style and structure

- by [unknown](#) **&#x21C5; -1**
  <br/> Not how it works at all

- by [unknown](#) **&#x21C5; 3**
  <br/> [https://developers.openai.com/api/docs/guides/reasoning?api-mode=responses](https://developers.openai.com/api/docs/guides/reasoning?api-mode=responses)

It absolutely is. The reasoning setting is you directly setting how many turns the model will take for reasoning opportunities.

I can only assume that’s what you’re disputing, as surely you’re not disputing that Astra will overengineer and overtest when presented with a problem that doesn’t require even a full turn of reasoning to handle? Genuinely, what do you think it’s going to do with your task during its reasoning turns when it finishes thinking through such a simple task as the ones presented? It’s not going to fill that time with its favorite rendition of Beethoven. It’s going to spend that time over engineering the task into the ground, usually by planning to throw tests at anything it can think of until its reasoning turns are exhausted.

- by [unknown](#) **&#x21C5; 0**
  <br/> Not how it works at all

- by [unknown](#) **&#x21C5; 1**
  <br/> Oh lol. I guess the direct OpenAI documentation is incorrect. You should email them the corrections or something.

What even is “it”?

- by [unknown](#) **&#x21C5; 0**
  <br/> Not how it works at all

- by [unknown](#) **&#x21C5; 1**
  <br/> Keep trying buddy. One day you’ll formulate a response or argument.

- by [unknown](#) **&#x21C5; 1**
  <br/> Why wouldn’t you tell it that isn’t necessary then or tell it you have some type of backup somewhere? I’m also confused why you would want an AI to do it a shittier way like not take screenshots to confirm or possibly fuck up your database cause you didn’t instruct it to follow a different process? This is a bizzare take just tell it not to do that in your instructions or agents md.

- by [unknown](#) **&#x21C5; 1**
  <br/> I usually run multiple things at once, the check on them once done, I can't always predict that it is going to over-test everything

- by [unknown](#) **&#x21C5; 1**
  <br/> It does this because every serious agent benchmark grades the final repo state, not what the model says it did. The over-verifying that annoys you is what makes it score.

So the fix isn't less verification, it's a budget. If you have simple tasks, use simple models; if you have complex tasks - use complex models that cost a lot.

- by [unknown](#) **&#x21C5; 1**
  <br/> "Hey, I'm using this artifact that has been here for 10 years, SHA was verified a couple of hours ago. You know what? Time to verify the SHA" - Open AI models for some reason.

- by [unknown](#) **&#x21C5; 1**
  <br/> I dont know i am loving the way it verifies everything. Running tests meh, but what i have been loving is it running playwright and verifying UI, UX and responsiveness and other workflows.. It even created a directory, had screenshots when it identified errors and started referencing those screenshots for fixing those exact bugs

- by [unknown](#) **&#x21C5; 1**
  <br/> user error
