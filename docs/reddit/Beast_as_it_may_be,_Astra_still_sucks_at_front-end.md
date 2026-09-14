#Beast as it may be, Astra still sucks at front-end [Visit](https://www.reddit.com/r/codex/comments/1war4wh/beast_as_it_may_be_astra_still_sucks_at_frontend/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [aivampires](https://www.reddit.com/user/aivampires/)
### **Vote:** 1
---
Perhaps it's better, but still fundamentally I'm seeing that it just doesn't understand front-end logic. It will not produce dedicated layouts, it will stack override on top of override to try and make some existing component match a mockup instead of actually understanding how to build layout structures.
If you notice it procrastinates, check if its procrastinating on UI work because I notice it doing so. It doesn't know how to handle complex front end tasks so it stalls by running tests and writing elaborate notes to itself about said tests.
After all the blender magic I'm seeing where it demonstrates an understanding of the visual world, I was hoping that it would have also gained a better understanding of the world of visuals. Sadly, it has not.
Would love to know what the problem is there. Why can't the model ever get this intuitively right?
---
## Comments 20

- by [unknown](#) **&#x21C5; 4**
  <br/> front end is a layered problem.

  1. ui goal
  2. initial mocks
  3. revised mocks
  4. ux refinement
  5. ui refinement
  6. another layer of ux refinement

it's a very hard concept for a model to understand in one shot even on a per-feature basis.

what i suggest is breaking it down.

the list above translates to these things you can do to get there

  1. this is your prompt for the goals of the feature
  2. ask it to use imagegen but not implement things yet
  3. ask it to critique the generated mocks and generate a new set based on that
  4. this is a subjective thing that you do. you eat your own dog food
  5. this is a browser pass the model does (ask it to actually run through the thing. even better if you ask it to come up with "user journeys"
  6. this is your final pass for a manual review where you highlight any remaining problems.

- by [unknown](#) **&#x21C5; 4**
  <br/> Not my experience at all! It’s definitely much better. My workflow is to always have it make the UI in Figma or Magicpath then create the frontend from it.

If you’re just raw digging a frontend then it’s gonna struggle but the frontend skill tends to be better if you’re doing that

- by [unknown](#) **&#x21C5; 3**
  <br/> I've always believed that frontend is wildly more complicated than backend, there are of course many people who disagree with me on that, but its my personal observation. Obviously the human interface has more nuance and edge cases than a system that's basically a fancy calculator.

- by [unknown](#) **&#x21C5; 1**
  <br/> Bcz front-end is more flexible approach wise, while backend is just a boilerplate CRUD most of the time.

- by [unknown](#) **&#x21C5; 1**
  <br/> How are you structuring your projects and what difficult frontend tasks do you mean?

Using next or astro, I've not seen the behavior you mentioned on stacking with any frontier models for probably 8 months. Astra didn't blow me away or anything, though. It feels like Sol but able to do more general computer work.

- by [unknown](#) **&#x21C5; 1**
  <br/> I wouldn't go that far, but it's definitely a weak point. Hopefully the next version brings a big improvement there.

You should focus more on building and remaining positive though, and less on complaining.

You'll live a better life that way.

- by [unknown](#) **&#x21C5; 1**
  <br/> I felt the same way until I realized it was a skill issue on my end using the CLI. Switch to the desktop codex for your UI. It's god mode.

- by [unknown](#) **&#x21C5; 1**
  <br/> "BUILD ME A BEAUTIFUL CLEAN APP" - gets surprised how the MACHINEE didnt read his mind and built a generic app....

- by [unknown](#) **&#x21C5; 1**
  <br/> I used to have a problem with AI UIs, then i realised AI wasn't magic, and took steps to make it better. There is a trove of information about getting decent UIs using Codex, and most are just a search away. For the most part Codex generally get's it right immediately 90% of the time, and when it doesn't it's usually my fault.

- by [unknown](#) **&#x21C5; 1**
  <br/> UI is a pain in the ass when it’s 100% humans. Adding AI is not going to change that. If you’re expecting AI to do it all, you probably need to look into Canva or one of the UI tools. Those can generate foo mockups that you can pass to Codex. Otherwise you need to be very explicit in what you want, just like you would be with a human.

- by [unknown](#) **&#x21C5; 1**
  <br/> I'm gonna push back here. I almost agreed with you but this weekend I sat down and built an entire website around a job application. The first go because like you I was curious what GPT-6 offered in terms of front end UI and UX capability and the first prompt I gave it resulted literally in crap. I told her to give me five designs unique designs but admittedly my prompt wasn't super great. All five designs were just trash. So that I had a little back-and-forth with it and I told it I wanted to give it full creative license I needed it to reread the job description reread my résumé and I wanted it to go crazy with creating unique brilliant graphic interface user experience etc. etc. and it freaking went ballistic it was amazing and I wound up spending five hours just having it do these website graphics and I went up with like 50 of them and every single one was brilliant. This was like I said a webpage not a full website but a single long webpage scrolling long webpage specific to a job application. So maybe in terms of creating full websites it still sucks and I'm I'm not gonna disagree because I haven't tested it but they really did a good job much better than what Claude did because I actually also had Claude do this same exercise in parallel. So I'm I'm impressed. I'm I'm not going to disagree with you like I said I didn't give it the full test but for my current needs it actually blue 5.6 and every previous GPT version out of the water.

- by [unknown](#) **&#x21C5; 1**
  <br/> I’m actually quite impressed with the ui capabilities.  I built some cool ui components that  I haven’t seen in the wild.

Like an option selector where the center label is colored and when clicked opens to swatch options

 
       [](https://preview.redd.it/beast-as-it-may-be-astra-still-sucks-at-front-end-v0-y5h2605cqboh1.jpeg?width=1206&format=pjpg&auto=webp&s=94a6dabea27d285369069da51dc100301c322616)

- by [unknown](#) **&#x21C5; 1**
  <br/> Astra and the rest of the family do really well on the backend, but really sucks on frontend, zero taste, negative amount of taste/eye for design "design clean dark mode UI" yeah here's 10 buttons no reasonable person will ever need and just so much nonsensical design choices, I tried "impeccable" I'm not quite certain but it might have made things worse. Idk what to do about this.

- by [unknown](#) **&#x21C5; 2**
  <br/> Skill issue. Not trolling. Try doing a proper handoff and it'll do better.

Try looking for samples of websites/components/apps/UI you like, or maybe do a proper moodboard. You can also try with Google Stitch until you like something. Once the model can understand what you want, you can create a proper design system and then it'll go smoothly. But you can't just tell it "do a cool UI" and expect it to deliver anything other than AI slop.

- by [unknown](#) **&#x21C5; 2**
  <br/> Skill issue? totally, just like how its a skill issue I can't write backend to save my life, that's what the AI is for, you do have an excellent point about making a proper moodboard with examples of what I like and I'll do that going forward. But telling Astra to make an UI should at least come out reasonable, I made a video catalog application and the top bar took 30% of the screen for nothing, bottom bar another 20%, the UI was reminiscent of win98 with buttons that make no sense at all, so there's skill issue both ways. Anyways, off to craft a moodboard/design preferences folder! :)

- by [unknown](#) **&#x21C5; 2**
  <br/> Now, that's a real issue and not from skill. I wasn't talking about broken interfaces but about lackluster design. The model should deliver a usable UI. My advice is to avoid the AI slop feel.

- by [unknown](#) **&#x21C5; 1**
  <br/> If it is a "skill issue" with Astra and yet Claude nails it every time given the same limitations; then the "skill" is just working around Astra's limitations/weakness.

So "skill issue," maybe, but perhaps a skill that shouldn't be needed. It certainly isn't a "skill" I need when I use Claude Design.

PS - I think it is very telling that you're telling him to use multiple other resources/products to babysit how Astra should do UI work, while calling it a "skill issue," without a hint of irony. Did you even read that back and reflect?

- by [unknown](#) **&#x21C5; 1**
  <br/> Claude Design spits the same UIs every time. I was so embarrassed when I discovered another website looking *exactly* like mine even after I spent an afternoon going back and forth with different ideas. I assure you whatever CD did for you, you'll find a clone out there.

You avoid this by doing the actual work. Then the model is not relevant for the task. Even Gemini could get it done.

- by [unknown](#) **&#x21C5; 0**
  <br/> Claude Design spits the same UIs every time.


    Skill issue - see how that works? Claude Design is, as the name implies, a design framework. You set up the visual standards, which Claude will help you construct through a series of questions/opinions, and then reuse that framework for future designs. It will then work within the framework you've created, and generate additional assets.

In essence, it does what you're saying people should go do, but all within a single very powerful tool. Ultimately what you get at the back end is a bespoke, unique, purpose built design using design language you yourself have constructed.

To quote:


      But you can't just tell it "do a cool UI"
