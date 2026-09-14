#Astra token spending is low, while usage % is very high. [Visit](https://www.reddit.com/r/codex/comments/1waamo3/astra_token_spending_is_low_while_usage_is_very/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [spike-spiegel92](https://www.reddit.com/user/spike-spiegel92/)
### **Vote:** 84
---
I have been tracking my token spending for months, and today, since I got a reset this morning and Tibo announced a reset. I have used 100% of my x20 Pro weekly allowance, in the very same day.
However, token-wise and COST-wise, I have spent about as much as I would on a very normal day before Astra. ~200-300$ dollar for a full week of usage, before I was able to spend thousands.
You can see it in the screenshot. In the past, I managed to spend $1–3K in “cost” in a single day without using 100% of my weekly allowance.
How the fuck did I use 100% with less than $400 spent (at equivalent API pricing)?
I have never seen this before with any other model. The dollar-to-percentage burn rate has always been relatively constant.
But if this is correct, then the monthly allowance in terms of dollar value has now been reduced insanely.
Tool used: [https://github.com/junhoyeo/tokscale](https://github.com/junhoyeo/tokscale)
---
![Astra token spending is low, while usage % is very high.](https://preview.redd.it/astra-token-spending-is-low-while-usage-is-very-high-v0-pew4aoso87oh1.png?width=640&crop=smart&auto=webp&s=dbaac2faf3523a28406c0cbfccf869fbe61b5ff7)
---
## Comments 52

- by [unknown](#) **&#x21C5; 29**
  <br/> I think they're shrinking the quota and using resets to smooth out the load.

- by [unknown](#) **&#x21C5; 19**
  <br/> That's it. It always happens. Remember what the limits were six months ago? I didn't even know they existed. I could have used hundreds of millions of tokens on the best models at the time.

- by [unknown](#) **&#x21C5; 2**
  <br/> Totally agree, I used 30% today, when couldn't do that even with /goal active a few weeks ago!

- by [unknown](#) **&#x21C5; 2**
  <br/> For now, nothing has changed. The quota has remained the same since at least July. I've got some logs here for August:

[https://codex-quota.manetli.com/?model=gpt-5.6-sol&plan=pro_x20&unit=tokens#capacity](https://codex-quota.manetli.com/?model=gpt-5.6-sol&plan=pro_x20&unit=tokens#capacity)

- by [unknown](#) **&#x21C5; 3**
  <br/> Your own data shows 4x burn rate when astra costs 2.5 times more (less than twice if we take launch price which we should)

- by [unknown](#) **&#x21C5; 5**
  <br/> You're mixing two different measurements.

Yes, the current data shows roughly 4x quota consumption **per observed token** for Astra vs Sol. I'm not disputing that.

What I'm talking about is whether the underlying Codex allowance itself has been reduced over time. If you compare Sol with Sol, the observed capacity is basically in the same range as it was in August. There is no 4x drop there.

The 4x is a model-specific Astra/Sol weighting, not evidence that the account's overall quota was cut by 4x.

And even for Astra, 4x/token isn't the same as 4x/task. In my current MAX samples Astra uses ~56% fewer tokens per completed task, which puts the estimated quota cost at ~1.77x Sol per task, not 4x.

- by [unknown](#) **&#x21C5; 2**
  <br/> The thing is that API pricing and plan usage were coupled before, now they apparently give you less of a discount for astra? Thats whats surprising to me.

- by [unknown](#) **&#x21C5; 1**
  <br/> They cut the usage by 4/2.5 .Astra costs per token 4 times or even more than sol on subscription. According to API usage it should cost 2.5 times (2 times if we take launch price).Notwithstanding that Astra completes a task in less tokens, they have reduced the value in dollars the subscription provided if we use Astra.

Also, 56% fewer tokens is only in the ideal case on benchmarks in real world i find that its a little more token efficient but not by 50%.These models have been trained on tasks similar to benchmark which is why they can be so efficient on them. In real world, they see a lot of novel things and have to think explore to decide what to do.

If you don’t  believe, paste this into astra and see who is correct.

Anthropic also did something similar but they actually disclosed it by saying 50% of the weekly is the fable limit

- by [unknown](#) **&#x21C5; 1**
  <br/> There is no need to use Astra.

That's not even what I was responding to.

The original claim was that OpenAI is shrinking the subscription quota over time. I replied that my historical data doesn't show that: Sol capacity today is still essentially in the same range as it was in August.

You're now talking about Astra's quota weighting relative to its API price. That's a different discussion.

Astra can be worse value per API-equivalent dollar while the underlying subscription allowance remains unchanged. Those two things are not contradictory.

- by [unknown](#) **&#x21C5; 3**
  <br/> Why would Sol be the relevant benchmark once Astra is available and is the better model for most use cases?

When we moved from 5.4 → 5.5 → 5.6 Sol, users didn’t suddenly get dramatically lower usage if we calculate it by equivalent API usage in $.


      
    This is not true in any meaningful sense. They give you the option to buy credits in Codex when your included usage is exhausted. Astra costs 2.5× as many credits as Sol (2x more if we consider Sol launch pricing), not 4×.

The Codex pricing page itself says Astra gives you roughly half as many messages as Sol.

You cannot simply hide behind technical distinctions in how the quota is defined when the practical effect for users is different. That is misleading advertising; what technical accounting is being used in the backend isn't relevant as that is not exposed to us.

- by [unknown](#) **&#x21C5; 1**
  <br/> I think the setup you have is great for collecting the data. The interpretations offered are very uncompelling and have the weird kind of nitpick quality that Astra provides as well.

- by [unknown](#) **&#x21C5; 1**
  <br/> I think it would be really interesting to install [tibotattle.com](http://tibotattle.com) and compare the two allowance measurements.

- by [unknown](#) **&#x21C5; 16**
  <br/> I noticed this too, even Astra low demolishes my usage limits for my 20X plan for unexplainable reasons. I switched back to luna xhigh builders and have my Astras build stronger plans to compensate

- by [unknown](#) **&#x21C5; 5**
  <br/> I'm on plus plan I've saying the same things but people always say "pay more" to me, (earlier I could spend 250 million tokens in a day now it's not even 30 million even at best) and anything I was saying was invalid because I'm on plus plan.

- by [unknown](#) **&#x21C5; 5**
  <br/> At this point, the reset Tibo is given only to avoid this usage problem to make users happy. I don't give a fuck about the reset if my usage can only be used for only one day

- by [unknown](#) **&#x21C5; 3**
  <br/> I've used three weeks worth of codex usage on Astra in just three days.

- by [unknown](#) **&#x21C5; 3**
  <br/> i could use 1000$ of api before this every single day....

- by [unknown](#) **&#x21C5; 2**
  <br/> Where can you track spending usage like that, external tool? looks nice.

- by [unknown](#) **&#x21C5; 2**
  <br/> [https://github.com/junhoyeo/tokscale](https://github.com/junhoyeo/tokscale)

- by [unknown](#) **&#x21C5; 3**
  <br/> With all the resets they might as well introduce a 3 day usage instead of a week

- by [unknown](#) **&#x21C5; 7**
  <br/> It is apparently time to say it again: Subscription usage is not measured in tokens.

- by [unknown](#) **&#x21C5; 16**
  <br/> And this is what i am trying to say here.

It is not measured in the value of those tokens either.

I spent 200$ dollar in tokens in the last 8h, and that was 80% of my weekly.

With sol 5.6 or with gpt 5.5  or 5.4 some days i have spent 2K$ in tokens value and it was not even 100%, i mean back then we did not even have the 5h window removed.

So even if it is less tokens, they have an "api value" and what I am saying is ... we are getting way way way less $$$ per account if you use astra. Which honestly i find weird.

- by [unknown](#) **&#x21C5; 4**
  <br/> This is also the case with fable. The api pricing ratios dont track with subscription usage amongst the models.

- by [unknown](#) **&#x21C5; 1**
  <br/> This was my usage today, which ended up totalling 60% of my weekly limit. I spent 800+$ in token, and somehow still allegedly used 20% less than you spending 200$.

Something dont add up.

 
       [](https://preview.redd.it/astra-token-spending-is-low-while-usage-is-very-high-v0-2pkugv5ed8oh1.png?width=2048&format=png&auto=webp&s=59dc0c344ee019495b5c76409ba28fb328e74999)

- by [unknown](#) **&#x21C5; 1**
  <br/> true, wtf something has to be wrong in my tool or i dont get it

- by [unknown](#) **&#x21C5; 1**
  <br/> It's about 2x Sol. I haven't felt the efficiency benefits of Astra although results are marginally better

- by [unknown](#) **&#x21C5; -6**
  <br/> > I spent 200$ dollar in tokens

No, you didn't, because there is no direct association between dollars and tokens.

> with gpt 5.5 or 5.4 some days i have spent 2K$ in tokens

There was no direct association between dollars and tokens then either.

The newer models have, however, become more efficient and now require shorter reasoning and fewer tokens to accomplish the same job.

Stop trying to associate dollars with tokens. It was never valid. Start trying to associate dollars with productivity, because that's how you're being billed.

I mean come on, think about it, even if we ignored "productivity" for a moment and focused solely on how much water and electricity you're burning in the data centers that everyone loves to hate on these days, should these two things cost the user the same amount of money?- thinking for one second and generating x tokens- thinking for ten seconds and generating x tokens

And should a smart model that generates x tokens cost the same as a smarter model that generates x _better_ tokens?

Of course not, so stop misleading yourself.

- by [unknown](#) **&#x21C5; 3**
  <br/> There very much a correlation between dollars a tokens, it just not clear how much of it is involved in monthly plans.

The API cost is literally priced per million token.

GPT-6 Astra, $10 input / $50 output per million tokens.

GPT-5.6 Sol, $5/$30,

GPT-5.6 Terra, $2/$12,

GPT-5.6 Luna, $0.20/$1.20.

Cached input at 10% of standard rate

- by [unknown](#) **&#x21C5; 2**
  <br/> Idiot.  Dollar is associated with token. Check api price.

- by [unknown](#) **&#x21C5; 0**
  <br/> Idiot. We're talking about subscriptions. Check your head.

- by [unknown](#) **&#x21C5; 1**
  <br/> There just needs to be some transparency in how the billing works - even if it’s a different token rate for every model (they already do this for the API).

Being able to quietly jerk around usage and limits whenever they want isn’t fair to the consumer.

Anthropic has done this same shell game over and over again.

I useAPI access for work, even there it’s not super transparent, but it’s a lot better.

To be honest, I’m not not even sure tokens are the best representation of their costs, to your point. This would be akin to basing your vehicle registration charge on the number of times your spark plugs fire.

It’s kind of a meaningless derivative of consumption.

- by [unknown](#) **&#x21C5; 1**
  <br/> Thanks for a thoughtful reply instead of just a knee-jerk downvote because I didn't support the thoughtless hivemind.

I totally agree with you! Almost every time I reply these days it's about shit takes. Tokens this, data that, math this, "evidence" that. Perhaps I need to go out of my way to make clear that I also want more transparency to the pricing, and to not feel like unknown things are shifting under my feet, but I honestly don't want to spend too much time here (it really seems like most OPs and most replies are either trolls for money, trolls for fun, or idiots) and so I focus on people's obsession with tokens, bad statistics, and poor logic. There's sadly a lot of it.

- by [unknown](#) **&#x21C5; 1**
  <br/> Usage for the same tasks about 2 to 2.5x sol.

- by [unknown](#) **&#x21C5; 1**
  <br/> Cache read is expensive. 1$/1M

- by [unknown](#) **&#x21C5; 2**
  <br/> could the tool be wrong 🤔

- by [unknown](#) **&#x21C5; 1**
  <br/> [https://developers.openai.com/api/docs/pricing](https://developers.openai.com/api/docs/pricing)

Yes

- by [unknown](#) **&#x21C5; 1**
  <br/> Is this also including other models for the last days? Because the cost column doesn't seem to make much sense for Astra. Fresh input = $12.5 and cached = $1. So the input alone would be way more expensive than the cost column suggests.

- by [unknown](#) **&#x21C5; 1**
  <br/> [](https://preview.redd.it/astra-token-spending-is-low-while-usage-is-very-high-v0-ymeeilvpfaoh1.png?width=1241&format=png&auto=webp&s=053c239c8c3e968ec46e6bdd62b9c1322a676005)
      
    only astra.

however, i dont know why the tool is not counting cache writes.

- by [unknown](#) **&#x21C5; 1**
  <br/> 12.8M input * $12.50 = $160

336.5M cache input * $1 = $336.50

0.8M output * $50 = $40

Sum: $536.50

Not sure what this tool its doing, but that´s pretty basic math.

- by [unknown](#) **&#x21C5; 1**
  <br/> yes clearly something is wrong, yes yes. Weird it is a big project.

- by [unknown](#) **&#x21C5; 1**
  <br/> So first of all how your Cache write is 0?, second what is this? I mean did you made this yourself or what?, i would love to use this, i was actually thinking about this as how we measured tokens input output with codex, as Claude give us /cost where you can see details but not codex, i also love the design, if you made this make it public n share repo, I'll use it

- by [unknown](#) **&#x21C5; 2**
  <br/> its this: [https://github.com/junhoyeo/tokscale](https://github.com/junhoyeo/tokscale)

- by [unknown](#) **&#x21C5; 1**
  <br/> Yeah, I used to be able to go an entire week of using Sol medium - xhigh on the x20 plan.

I just blew through an entire week's quota in a single morning using astra, which is insane.

- by [unknown](#) **&#x21C5; 1**
  <br/> Now that they achieved AGI, it's time to turn that 200$ into profit by giving you 150$ usage instead

- by [unknown](#) **&#x21C5; 0**
  <br/> has anyone else gotten the reset tibo promised yet? nothing for me

- by [unknown](#) **&#x21C5; 2**
  <br/> thats not related to my post at all....

- by [unknown](#) **&#x21C5; 1**
  <br/> my bad, you had mentioned that tibo had just reset yours, and I noticed mine hadn't, so I wanted to check

- by [unknown](#) **&#x21C5; -1**
  <br/> everybody got it an hour ago, probably a problem with your account !

- by [unknown](#) **&#x21C5; 1**
  <br/> same issue here then. I did already use two tests recently though.

- by [unknown](#) **&#x21C5; 0**
  <br/> If you compare it on the new artificialanalysis bench, Astra low is about the same cost as Sol high per task, in API pricing. Meaning, at half the cost, Sol burns about double the amount of tokens. So if Astra in the subscription gives you 1/4 of the tokens you would get with Sol, this comes out to about to being able to run half as many tasks as with Sol, which would track with Astra being twice as expensive. Just guessing here, but maybe that's their logic?

- by [unknown](#) **&#x21C5; 1**
  <br/> This is extremely depending on the task. Astra low has almost no thinking, so it will save some expensive output tokens there. It might also arrive quicker at the solution with less turns. But if there is not much to think to begin with and simply a lot of context to read, the doubled input price comes into effect. Or the ~doubled output price, if you expect it to write a lot. You can´t generalize that it´s cheaper or the same just based on benchmarks.

- by [unknown](#) **&#x21C5; 1**
  <br/> problem is, that the API pricing is not matching the % usage of our accounts.

I could spend thousands of the API equivalent before, but now one entire week window was consumed by only 300$ in API equiivalent. This is weird as fuck.
