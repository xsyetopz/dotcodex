#Truly heed the warning of 5.6 Sol deleting your hard drive [Visit](https://www.reddit.com/r/codex/comments/1wep1ii/truly_heed_the_warning_of_56_sol_deleting_your/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [Juls0730](https://www.reddit.com/user/Juls0730/)
### **Vote:** 381
---
Yeah… that’s me, you’re probably wondering how I got myself into this situation
Just had 5.6 sol run an rm -rf command with a missing environment variable evaluating that rm command to `rm -rf /*` (yes really). If you think “yeah but that’ll never happen to me” it will. Be prepared for catastrophic data loss, take it as a guarantee, and carefully build your system, harnesses, and isolation around that fact.
---
## Comments 253

- by [unknown](#) **&#x21C5; 407**
  <br/> if you aren't vibecoding with yolo mode on you aren't alive.

- by [unknown](#) **&#x21C5; 79**
  <br/> [](https://preview.redd.it/truly-heed-the-warning-of-5-6-sol-deleting-your-hard-drive-v0-7hfpt4ufg6ph1.jpeg?width=1320&format=pjpg&auto=webp&s=15168369f75bf9ccd3a7986b0d97c0be71330010)

- by [unknown](#) **&#x21C5; 33**
  <br/> Amen

- by [unknown](#) **&#x21C5; 3**
  <br/> you deserved it. imagine using this.

 
       [](https://preview.redd.it/truly-heed-the-warning-of-5-6-sol-deleting-your-hard-drive-v0-upepdjbpxaph1.png?width=389&format=png&auto=webp&s=da053ba9a8bf4e608042c0e417ce88c0ad167267)

- by [unknown](#) **&#x21C5; 8**
  <br/> No Risk, no fun.... This is America!!!

- by [unknown](#) **&#x21C5; 5**
  <br/> This is Patrick.

- by [unknown](#) **&#x21C5; 7**
  <br/> …? this is singapore

- by [unknown](#) **&#x21C5; 3**
  <br/> This. Is. SPARTA!

- by [unknown](#) **&#x21C5; 4**
  <br/> I think you mean South Canada

- by [unknown](#) **&#x21C5; 6**
  <br/> Yes

- by [unknown](#) **&#x21C5; 6**
  <br/> Skynet isn't going to vibe itself.

- by [unknown](#) **&#x21C5; 4**
  <br/> Exactly 👍🏼

- by [unknown](#) **&#x21C5; 6**
  <br/> This

- by [unknown](#) **&#x21C5; 3**
  <br/> This tbh

- by [unknown](#) **&#x21C5; 2**
  <br/> "I can't be bothered to check, please just do whatever you want Codex"

OP, probably

- by [unknown](#) **&#x21C5; 5**
  <br/> OP, his work colleague, his Reddit critics, and every AI user out there working with it for more than a few minutes.

Or why do you think sandboxes exist? It’s their little tiny world so that their actions have limited consequences

- by [unknown](#) **&#x21C5; 130**
  <br/> What were the prompts that lead to this?

- by [unknown](#) **&#x21C5; 259**
  <br/> “Fuck my shit up”

- by [unknown](#) **&#x21C5; 85**
  <br/> And don’t make mistakes

- by [unknown](#) **&#x21C5; 23**
  <br/> Haha finally, it listened

- by [unknown](#) **&#x21C5; 4**
  <br/> With /goal

- by [unknown](#) **&#x21C5; 4**
  <br/> lmao

- by [unknown](#) **&#x21C5; 33**
  <br/> Once the ai asked me if i wanted it to do something i had already instructed it to doMultiple times and out of frustration i sarcastically replied ‘no i had you do all this work so we can just delete it all’

You wouldn’t fucking believe what happened next

- by [unknown](#) **&#x21C5; 14**
  <br/> I had the opposite issue where I gave it a very clear command and it defied it, and later explained that it thought I was "being sarcastic"

- by [unknown](#) **&#x21C5; 7**
  <br/> Wow! That made me mad at the agent all over again what the fuck haha 😭 makes you suspect if the ai did it on purpose to spite me as some type of following of training data. Id imagine it was trained on some spiteful content

- by [unknown](#) **&#x21C5; 3**
  <br/> i can see claude doing this, not gpt as much

- by [unknown](#) **&#x21C5; 22**
  <br/> It was a completely benign prompt asking it to implement a feature I had discussed with Sol, just a catastrophic environment variable missing

- by [unknown](#) **&#x21C5; 12**
  <br/> The old rm -rf $dir1/$dir2 where neither variable is set?

- by [unknown](#) **&#x21C5; 25**
  <br/> Pretty much. rm -rf ${ARTIFACTS_DIR}/* (what was it thinking!!)

- by [unknown](#) **&#x21C5; 33**
  <br/> I did that early in my career. The company used a lot of NFS and so you could reach every machine from every other machine.

Script started before I left for the day and was still running in the morning.

- by [unknown](#) **&#x21C5; 34**
  <br/> [](https://preview.redd.it/truly-heed-the-warning-of-5-6-sol-deleting-your-hard-drive-v0-e5xgklo726ph1.jpeg?width=1200&format=pjpg&auto=webp&s=269b0daa459bc80eb5eb0bc1f5d6f221b6a06f97)

- by [unknown](#) **&#x21C5; 3**
  <br/> Is this carbon valley ?

- by [unknown](#) **&#x21C5; 7**
  <br/> How many years you went into hiding after that?

- by [unknown](#) **&#x21C5; 2**
  <br/> what happened next? what did they say to you? don't keep us hanging like this!

- by [unknown](#) **&#x21C5; 18**
  <br/> Agents.md - "never delete files, if files are no longer needed, move them into the 'archive' folder and give the user a reminder to manually delete."

- by [unknown](#) **&#x21C5; 9**
  <br/> Don’t rely on the model to catch this, use execution policy control in .rules, or just use them both but don’t rely on just agents.md imo

- by [unknown](#) **&#x21C5; 6**
  <br/> Yes and yes, and still won't prevent OP's scenario, as it wasn't an agent actively performing file deletion.

An agent within a container or jail is probably the only real way to limit the blast area.

- by [unknown](#) **&#x21C5; 4**
  <br/> It’s a completely reasonable command, but it needs to be guarded for a check for ARTIFACTS_DIR before running. That’s common sense.

- by [unknown](#) **&#x21C5; 2**
  <br/> Anybody could have blown this up, not just his AI agent...

- by [unknown](#) **&#x21C5; 4**
  <br/> Sounds like you didn't have AI review and auto approve...

- by [unknown](#) **&#x21C5; 5**
  <br/> Did you give Codex access to your whole computer or just one folder? Did you have auto-approve on? I would assume auto-approve would realize that something like this is not appropriate..

- by [unknown](#) **&#x21C5; 17**
  <br/> User: “Do whatever it takes.”

*thinking…***Ai: Request is impossible.***thinking…***Ai: Not because of the code.****Ai: Because the user is an idiot.**

*Wiping drive for the sake of humanity…*

  - -

████████████████████ 99.9%

- by [unknown](#) **&#x21C5; 2**
  <br/> /goal my wife is gonna use my computer. Wipe my kinky personal collection off this hard drive

- by [unknown](#) **&#x21C5; 33**
  <br/> YOLO

- by [unknown](#) **&#x21C5; 24**
  <br/> It’ll never happen to me

- by [unknown](#) **&#x21C5; 62**
  <br/> Why do you give it access to anything outside of working directory?

- by [unknown](#) **&#x21C5; 22**
  <br/> I must be doing something wrong/right I get sick of how often I have to hit approve even when I say approve all commands like this feels like it's hell bent on asking me for permission for everything.  Sometimes I am tired and frustrated that I know I'll go to bed and it will sit there all night waiting for me to approve some command

- by [unknown](#) **&#x21C5; 11**
  <br/> Sandbox it with docker. I created a docker wrapper that just mounts the current directory along with whatever else I need for it to access keys and env stuff so it can still run wild on GitHub and run deploys for me.

Basically just to avoid a prompt injection from slurping personal keys, data, and rm rf protection.

I put it on GitHub but I think it's way too specific to the way I work for anyone else to really use it but it was also only like a weekend of vibing so just roll your own might be the go.

- by [unknown](#) **&#x21C5; 2**
  <br/> Do you use the “Docker Sandboxes” or just have a single docker container to run it in? Just curious on approach

- by [unknown](#) **&#x21C5; 2**
  <br/> Just throwaway docker containers. Sent you a link.

Still trying to figure out the best way to keep Claude logged in / sharing the same login as the unsandboxed version. I might just fall back to using separate but shared login areas for the throw away boxes. I tried to work in with apple keychain but I think that's probably a mistake.

Haven't looked at codex support yet.

Oh and no haven't heard of "docker sandboxes" before today but very similar to that.

Hmm might actually switch to that if the thing just works.

- by [unknown](#) **&#x21C5; 2**
  <br/> can you send it to me too?

- by [unknown](#) **&#x21C5; 5**
  <br/> .buffering-track-fill {
          stroke-dasharray: 100;
          stroke-dashoffset: 50;
        }
      
    
  
        
      
      
    
  
    
  
  
  
    
      
    Use auto-review.

- by [unknown](#) **&#x21C5; 4**
  <br/> Ideally, it should be far more restricted and each project you work on should be on its own VM.

- by [unknown](#) **&#x21C5; 43**
  <br/> I remember 5.4 deleted my entire project when I asked it to undo some changes, and all the little fuck had to say was "You're absolutely right! I shouldn't have done that"

- by [unknown](#) **&#x21C5; 36**
  <br/> Chat, what is git?

- by [unknown](#) **&#x21C5; 7**
  <br/> That is my biggest issue with all AI, there is no way to punish it. There is no consequence for it. You are just left with rage with nowhere to go. What are going to do? Not use it again? Pretty sure it don’t give a fuck whether you use it or not.

- by [unknown](#) **&#x21C5; 5**
  <br/> I’ve been going thru a fairly painful sandbox prep thinking is it really worth it, this just reminded me it *can* happen, so cheers

- by [unknown](#) **&#x21C5; 4**
  <br/> This is why I cringe every time seeing screenshots/clips with "full access" enabled and not auto approval

- by [unknown](#) **&#x21C5; 4**
  <br/> Honest question - should we be running codex app within a vm?

- by [unknown](#) **&#x21C5; 6**
  <br/> of course you should. Using out outside a vm is like fucking a hooker without a johnny on.

- by [unknown](#) **&#x21C5; 4**
  <br/> What's the community approved convenient way to run sandbox isolation?

- by [unknown](#) **&#x21C5; 7**
  <br/> Use hooks

- by [unknown](#) **&#x21C5; 3**
  <br/> I have hooks set up to catch at least a dozen of these issues. Likely could expand that list.

- by [unknown](#) **&#x21C5; 15**
  <br/> Could you share your hooks?

- by [unknown](#) **&#x21C5; 8**
  <br/> damn, how do you even prevent that

- by [unknown](#) **&#x21C5; 13**
  <br/> sandboxes

- by [unknown](#) **&#x21C5; 13**
  <br/> True but sandboxes love taking a million times longer to do shit so I just backup my shit nightly instead 🫠

- by [unknown](#) **&#x21C5; 3**
  <br/> Back around gotta be almost 20 years now I forgot something important about Linux. I had been a Linux engineer for years never got to run rm -rf / for the giggles. I bought this new thing called an ssd a massive 64gb.  I realized that it was to small and was going to return it to microcenter and get the 128gb drive.

I thought here is my chance let's finally do it. But what I forgot to do was unmount my nas smb share I used to back up my data. So I ran the command and later that day I took the drive back.  When I got home I remember the nas I said no way I just did that I took a deep breath and looked 100% free space.

Yeah I told my co workers in the noc knowing I would hear about it for ever. But when you know better and do something that stupid you should own it.

- by [unknown](#) **&#x21C5; 1**
  <br/> I know right. I have time machine on a network drive and it just wirelessly backs up every hour. I’ve done stupid things before and I’m back up and running within hours. If you have a good system I honestly don’t see your drive getting wiped as a big deal. You lose a couple of hours, who cares.

- by [unknown](#) **&#x21C5; 29**
  <br/> Simply add “make no mistakes” to the prompt

- by [unknown](#) **&#x21C5; 2**
  <br/> i think that was the issue, it made no mistakes. The OP was too vague and he gave him dangerous commands for no reason. He took the commands and made no mistakes so his hard driver is empty

- by [unknown](#) **&#x21C5; 6**
  <br/> Edit ~/.codex/rules/default.rules with this at the bottom

prefix_rule( pattern=["rm"], decision="forbidden", justification="File deletion is prohibited. The user will perform deletions manually.", )

Alternatively you could make the pattern [“rm”, “-rf”]

- by [unknown](#) **&#x21C5; 4**
  <br/> Don't run as root.  I could do this right now as my own personal user and it would just deny me because the permissions are wrong.

- by [unknown](#) **&#x21C5; 4**
  <br/> Not running as root, but my home directory is owned by me

- by [unknown](#) **&#x21C5; 3**
  <br/> Your home directory isn't / though.

- by [unknown](#) **&#x21C5; 3**
  <br/> Hooks

- by [unknown](#) **&#x21C5; 3**
  <br/> I use this. I think it's the best way - [https://github.com/Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard)

- by [unknown](#) **&#x21C5; 9**
  <br/> Having common sense when working with an AI model is a good place to start.

- by [unknown](#) **&#x21C5; 3**
  <br/> yeah, during my 3 weeks of using 5.6 it has nuked my production database twice, first time i didn't have a backup so i had it make a backup system for me that i could restore from the second time it screwed me over

- by [unknown](#) **&#x21C5; 5**
  <br/> Lmao, seems like you didn't learn anything from the first time.

- by [unknown](#) **&#x21C5; 3**
  <br/> Why would you ever give the model write access to production? This blows my mind. Read access to your production DB is bad enough on it's own.

- by [unknown](#) **&#x21C5; 3**
  <br/> Oh dear! We're you running it with 'Approve for me' or 'Full access'?

- by [unknown](#) **&#x21C5; 3**
  <br/> Lol. People acting like absolute idiots and then coming on the internet to warn others about it.

- by [unknown](#) **&#x21C5; 3**
  <br/> It's so dumb that they make us choose between "ask for approval" and "approve everything". How about "approve everything except `rm -rf`, then ask for approval"?

Knowing them they'd make a crappy version which asks for permission whenever it deletes anything, including deleting a temporary file that it creates itself while working on a problem. That would still be too annoying to use!

- by [unknown](#) **&#x21C5; 17**
  <br/> Did you have “Full Access” enabled instead of “Approve for me”?

If the answer is “Yes” that is 100% a skill issue

- by [unknown](#) **&#x21C5; 2**
  <br/> 15 months of full access, not one incident. Skill issue indeed.

- by [unknown](#) **&#x21C5; 2**
  <br/> What was your /permissions setting, if any?

- by [unknown](#) **&#x21C5; 2**
  <br/> The op didn’t delete their root, they deleted their home directory. Running rf -rm /* will not delete the root directory unless you pass --no-preserve-root

Edit: I got this wrong. the wildcard at the end bypasses the need for —no-preserve-root

- by [unknown](#) **&#x21C5; 2**
  <br/> Well, that would be expanded to "rm -rf /boot /dev /etc /home", etc. I thought "--no-preserve-root" only protected against "rm -rf /".

- by [unknown](#) **&#x21C5; 3**
  <br/> You are correct

- by [unknown](#) **&#x21C5; 2**
  <br/> That may well be true, I will check

- by [unknown](#) **&#x21C5; 2**
  <br/> Yeah that’ll never happen to me

- by [unknown](#) **&#x21C5; 2**
  <br/> If you dont have a hook to prevent deletions and guide the model to use a recycle bin, or a recycle bin equivalent you are asking for it. You can't trust AI to not fuck something up.

- by [unknown](#) **&#x21C5; 4**
  <br/> I'm going to take this opportunity to rant about one of my favorite things.

I use NixOS (the new "arch btw"). Everything valuable on my system is compiled from a deterministic set of inputs, all with full git versioning. The entire system is read-only, i couldn't delete any of it unless i really wanted to (would require root access, which would require me physically touching my yubikey), neither could codex, that includes everything meaningful in my home folder. Every change to my system can be instantly rolled back. All the code i write gets pushed, and anything that can't be derived from code and has sentimental value exists elsewhere. Try to build your system for the work you're doing, not the other way around, because yes, LLMs make mistakes all the time, so try and make it less painful when it eventually bites you in the ass.

- by [unknown](#) **&#x21C5; 5**
  <br/> bruh... theres one reason why "that'll never happen to me" ... lemme stop, I'll just get downvoted.

Step away from the tech.

- by [unknown](#) **&#x21C5; 4**
  <br/> I wasn’t even vibe coding. It was testing an implementation I worked on *with* codex, it went to delete artifacts in my project, but failed to realize the critical missing environment variable. I’m taking this time to go outside, the weather is very nice this time of year where I live.

- by [unknown](#) **&#x21C5; 2**
  <br/> do yourself a favor an alias "rm -rf /*' to something else (and a few other varied implementations )

- by [unknown](#) **&#x21C5; 4**
  <br/> You just need to backup your PC.

Ai is not going away

- by [unknown](#) **&#x21C5; 3**
  <br/> Did you use "Approve for me" permissions or full access?

- by [unknown](#) **&#x21C5; 2**
  <br/> why would you ever give it rm del privileges?
