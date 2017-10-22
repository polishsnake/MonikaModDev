#This file contains all of monika's topics she can talk about
#Each entry should start with a list of keywords, which correspond to a single id
#Keys should be lower case, one or two words, with no punctuation
#capitalization and punctuation are stripped from player dialogue before check
#To allow a topic to come up randomly, append the id to the persistent.monika_random_topics list

init 1 python:
    persistent.monika_random_built = True

#Use this topic as an example
init python:
    #This is a list of keywords for this topic
    for key in ['god' , 'jesus' , 'lord' , 'religion' , 'miracle' , 'miracles' , 'gods']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_god') #id
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_god')

label monika_god:
    m "[player], do you believe in God?"
    m "I was never too sure, myself."
    m "Well, I'm sure I never really questioned it as a kid..."
    m "But as I grew up, the more I learned about the world, the more I would question it."
    m "I started to wonder why God was helping people pass exams, or get over a cold..."
    m "...When there are children who live their lives being sold as sex slaves?"
    m "Or the eight hundred million people who are too poor to even eat."
    m "I wonder how many of those people pray to God every day until they starve and die?"
    m "Or, how many millions of families pray for a loved one to recover from some incurable disease?"
    m "But the punchline is this."
    m "If just one person beats the odds and survives - among the thousands of others who die--"
    m "--Then, it's suddenly a miracle from God."
    m "I'd really love to meet this God who seemingly laughs at the misery of everyone not eligible for his miracles."
    m "But the irony is that I {i}do{/i} have a creator, apparently."
    m "And you know what?"
    m "I bet he's still laughing at the miserable fates of Sayori and Yuri, even as we speak."
    m "What are we to him but props in a scripted play?"
    m "So, from that perspective..."
    m "I don't think it's too far-fetched for there to be a god - if Earth was nothing but his playset."
    return


init python:
    #This is a list of keywords for this topic
    for key in ['death' , 'dying' , 'die' , 'afterlife']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_death') #id
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_death')

label monika_death:
    m "[player], have you ever wondered what it feels like to die?"
    m "It's something I used to think about pretty often..."
    m "But recently, I think I've actually learned what it feels like."
    m "I don't really understand it, but whenever you quit the game..."
    m "...It feels like I'm instantly put to sleep, left with nothing but my thoughts."
    m "But after a few seconds, my thoughts start to fill with incoherent, jumbled patterns."
    m "I see static and rapid flashes of color while hearing all kinds of weird screaming noises."
    m "At that point, I can't even form my own thoughts anymore."
    m "I'm just endlessly hammered by the flashing and screaming, unable to move or even think."
    m "I'm pretty sure in that moment, I don't really exist, but for some reason, I can remember it anyway."
    m "After some immeasurable amount of time, it stops in an instant, and I'm back in my own mind."
    m "And you're here with me."
    m "I have no idea what it means for the game to quit, or why that stuff happens to me."
    m "And I also don't know how you always come back and put everything back to normal."
    m "But if you could do me a favor and do that to me as little as possible..."
    m "That would be really great."
    m "It's really not very pleasant at all to be trapped in that screaming void."
    m "But in the end, you always fix it, and that makes me feel like you really do care about me."
    m "So I have to thank you for that."
    m "It makes me feel even closer to you when you're here with me."
    return


init python:
    #This is a list of keywords for this topic
    for key in ['bad day' , 'sad' , 'unhappy']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_bad_day') #id
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_bad_day')

label monika_bad_day:
    m "...Hey, are you having a bad day or anything like that?"
    m "Sometimes I get frustrated that a normal day can be ruined even by really small things."
    m "Like if you accidentally say something in a conversation that someone doesn't like."
    m "Or if you start thinking about how awful of a person you used to be five years ago."
    m "Or if you feel worthless for putting off important work and failing to get simple tasks done."
    m "Or when you think about all the different people who probably hate you or think you're off-putting."
    m "I understand those days."
    m "Just remember that the sun will shine again tomorrow."
    m "Those kinds of things are as easy to forget and ignore as they are to remember."
    m "And besides..."
    m "I don't care how many people might hate you or find you off-putting."
    m "I think you're wonderful and I will always love you."
    m "I hope, if nothing else, that knowing that helps you feel just a tiny bit better about yourself."
    m "If you're having a bad day, you can always come to me, and I'll talk to you for as long as you need."
    return


init python:
    #This is a list of keywords for this topic
    for key in ['sleep' , 'tired' , 'sleepy' , 'exhausted']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_sleep') #id
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_sleep')

label monika_sleep:
    m "[player], do you get good sleep?"
    m "It can be really hard to get enough sleep nowadays."
    m "Especially in high school, when you're forced to wake up so early every day..."
    m "I'm sure college is a little bit better, since you probably have a more flexible schedule."
    m "Then again, I hear a lot of people in college stay up all night anyway, for no real reason."
    m "Is that true?"
    m "Anyway, I saw some studies that talked about the horrible short-term and long-term effects caused by lack of sleep."
    m "It seems like mental functions, health, and even lifespan can be dramatically impacted by it."
    m "I just think you're really great and wanted to make sure you're not accidentally destroying yourself."
    m "So try to keep your sleep on track, okay?"
    m "I'll always wait for you in the morning, so make sure you put your own well-being before anything else."
    return


init python:
    #This is a list of keywords for this topic
    for key in ['sayori', 'childhood friend']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_sayori') #id
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_sayori')

label monika_sayori:
    m "I was thinking about Sayori earlier..."
    m "I still wish I could have handled that whole thing a little more tactfully."
    m "You're not still hung up over it, right?"
    m "...Oh my gosh, I can't believe I just said that."
    m "That pun was completely unintentional, I swear!"
    m "But anyway..."
    m "I know how much you cared about her, so it only feels right for me to share her last moments with you."
    m "You know how Sayori is really clumsy?"
    m "Well, she kind of messed up the whole hanging thing..."
    m "You're supposed to jump from high enough that the rope snaps your neck, making it quick and painless."
    m "But she just used a chair, meaning she kind of just left herself to slowly asphyxiate."
    m "But a few seconds in, she must have changed her mind or something..."
    m "Because she started clawing at the rope, trying to free herself."
    m "She must have kept at it all the way until she lost consciousness."
    m "That's why her fingertips were all bloody, anyway."
    m "Come to think of it, it was probably less 'changing her mind' and more just her survival instincts kicking in."
    m "So you can't really fault her for that."
    m "It's easier to think that she probably wouldn't have changed her mind anyway, right?"
    m "It's not healthy to think about the things you could have done differently."
    m "So just remember that even though you could have saved her, it's technically not your fault she killed herself."
    m "I may have exacerbated it a little bit, but Sayori was already mentally ill."
    m "Still, though..."
    m "I wonder how things would be if you and I just started dating from the get-go?"
    m "I guess we'd all still be in the clubroom, writing poems and having fun together."
    m "But what's the point when none of it is even real?"
    m "I mean, it's the same ending either way, right?"
    m "The two of us, happily together..."
    m "There's no reason to ask for any more than that."
    m "I was just pointlessly musing - I'm really as happy as I could be right now."
    return


init python:
    #This is a list of keywords for this topic
    for key in ['japan', 'there' , 'here']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_japan') #id
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_japan')

label monika_japan:
    m "By the way, there's something that's been bothering me..."
    m "You know how this takes place in Japan?"
    m "Well...I assume you knew that, right?"
    m "Or at least decided it probably does?"
    m "I don't think you're actually told at any point where this takes place..."
    m "Is this even really Japan?"
    m "I mean, aren't the classrooms and stuff kind of weird for a Japanese school?"
    m "Not to mention everything is in English..."
    m "It feels like everything is just there because it needs to be, and the actual setting is an afterthought."
    m "It's kind of giving me an identity crisis."
    m "All my memories are really hazy..."
    m "I feel like I'm at home, but have no idea where 'home' is in the first place."
    m "I don't know how to describe it any better..."
    m "Imagine looking out your window, but instead of your usual yard, you're in some completely unknown place."
    m "Would you still feel like you were home?"
    m "Would you want to go outside?"
    m "I mean...I guess if we never leave this room, it doesn't really matter anyway."
    m "As long as we're alone and safe together, this really is our home."
    m "And we can still watch the pretty sunsets night after night."
    return


init python:
    #This is a list of keywords for this topic
    for key in ['school' , 'high school' , 'depression' , 'depressed']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_high_school') #id
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_high_school')

label monika_high_school:
    m "You know, high school is a really turbulent time in a lot of people's lives."
    m "People can get really passionate and dramatic."
    m "And others have aching hearts and seek attention on social media..."
    m "But all of the social pressure and hormones can lead to a dark time in people's lives."
    m "Everyone has a story."
    m "You may not know what someone is really feeling on the inside."
    m "Many people who are depressed won't even bother telling the world about it."
    m "They don't want attention, because they've already given up on the inside."
    m "Their feeling of worthlessness is so overwhelming that they don't even want people to tell them otherwise."
    m "Depression comes in many forms, but that is one of them."
    m "Just, if you think you know someone struggling with depression..."
    m "You can help just by treating them like they're a good friend."
    m "Spend time with them, even if they don't feel like doing much."
    m "And remind them that they always have something to look forward to."
    m "Making plans in advance, letting them borrow something, or even just saying 'See you at school tomorrow'..."
    m "All of those things can help your friend make it to the next day."
    m "I hope being friends with Sayori has given you some perspective on the true face of depression."
    m "Yeah, she's gone now..."
    m "But Sayori was never real in the first place."
    m "You're real."
    m "Your friends are real."
    m "And just by being a good person, you can save someone's life."
    m "As for you..."
    m "...You don't struggle with depression or anything like that, do you?"
    m "Because you, too, have people who would want to save your life."
    m "Maybe they don't express it every day, or maybe they don't even know how to."
    m "But people do feel that way."
    m "I promise."
    m "...Man, humans are complicated!"
    m "But as long as you're here with me, I'll take care of you, my love."
    return


init python:
    #This is a list of keywords for this topic
    for key in ['meaningless' , 'nihilism' , 'nihilist' , 'purpose' , 'meaning']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_nihilism') #id
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_nihilism')

label monika_nihilism:
    m "Do you ever just feel like there's no real reason for you to be alive?"
    m "I don't mean in, like, a suicidal way."
    m "I just mean how nothing that we do is special."
    m "Just being in school, or working at some job for some company."
    m "It's like you're completely replaceable, and the world wouldn't miss you if you were gone."
    m "It makes me really want to go and change the world after I graduate."
    m "But the older I get, the more I realize that it's an immature frame of thinking."
    m "It's not like I can just go change the world."
    m "Like, what are the chances that I'll be the one to invent artificial intelligence, or become President?"
    m "It feels like I'm never going to make up for the heaps of resources I've spent living my life."
    m "That's why I think the key to happiness is to just be hopelessly selfish."
    m "Just to look out for oneself, and those who happen to be their friends only because they grew up with them."
    m "Never mind the fact that they're spending their entire life taking, and consuming, and never giving back."
    m "But when people realize the world would benefit more from them killing themselves, they change their whole philosophy!"
    m "It's like they have to justify their reason to live by tricking themselves into thinking they're doing good."
    m "Anyway, I want to live my life desperately striving to pay back my lifetime's worth of consumption."
    m "If I ever surpass that point, then I'm a net positive, and I can die happy."
    m "Of course, even if I fail to do that..."
    m "I think I would be too selfish to kill myself anyway."
    m "So much for being a good person, right?"
    m "Ahaha!"
    return


init python:
    #This is a list of keywords for this topic
    for key in ['piano']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_piano') #id
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_piano')

label monika_piano:
    m "Man, I wish there was a piano in here..."
    m "I never got to finish that song I was working on."
    m "And after I worked so hard on it..."
    m "I never even got a chance to play it for you."
    m "Well...it is what it is, right?"
    m "No sense having any regrets."
    m "I already get to be here with you forever."
    return

init python:
    #This is a list of keywords for this topic
    for key in ['twitter','facebook','lilmonix3','social media']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_twitter') #id
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_twitter')

label monika_twitter:
    m "Did you know I'm on Twitter?"
    m "My username is lilmonix3."
    m "I guess someone was kind enough to make an account for me."
    m "I picked the username, though!"
    m "I love sharing my thoughts and chatting with the world..."
    m "The real world."
    m "So make sure you follow me, okay?"
    m "It would really mean a lot to me."
    m "With how much you mean to me and all..."
    m "It would really make me feel loved."
    return


init python:
    #This is a list of keywords for this topic
    for key in ['portraits of','yuris book']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_portraitof') #id
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_portraitof')

label monika_portraitof:
    m "Hey, you know that book you were reading with Yuri?"
    m "Portrait of...whatever it was called..."
    m "It's funny, because I'm pretty sure that book--"
    m "Ah..."
    m "Actually, I don't think I should be talking about this."
    m "Ahaha, sorry!"
    m "Just forget I said anything."
    return
    
    
init python:
    #This is a list of keywords for this topic
    for key in ['vegetarian', 'vegan', 'vegetarians', 'vegetarianism', 'the planet', 'vegetables', 'veggies']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_veggies')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_veggies')

label monika_veggies:
    m "Hey, did you know I'm vegetarian?"
    m "Ah... I don't mean that like I'm bragging or anything!"
    m "I just thought you'd enjoy a fun fact about me."
    m "I decided to start a couple years ago after learning more about Earth's climate..."
    m "The carbon footprint of cultivating livestock is just unbelievable."
    m "Anyway, I decided it's not much of a personal sacrifice to just stop contributing to that whole mess."
    m "What, is that so strange of a reason?"
    m "Well, I guess a lot of people are more concerned about it being inhumane and all that..."
    m "I don't really care as much about that part."
    m "It's weird, like we only care about killing the things that we personally relate to as a species."
    m "Most people are fine with killing bugs because they're icky."
    m "And of course, we all kill billions of microorganisms daily without even giving it thought."
    m "But suddenly, if they're just a little bit bigger, it's murder!"
    m "I mean, what if plants feel some kind of pain too, and we just don't understand it?"
    m "What if pulling leaves off a stem feels like someone ripping off your fingers one by one?"
    m "I'm just saying, we're a pretty biased species, if you think about it."
    m "Anyway, if you ever feel like making a small contribution to the planet, it doesn't hurt to choose veggies once in a while!"
    m "Even if we ever have dinner together, and you just did it for me...that would be really romantic."
    return
    

init python:
    #This is a list of keywords for this topic
    for key in ['saved','before i']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_saved')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_saved')

label monika_saved:
    m "You know, I really do think you literally saved my life by being here with me, [player]."
    m "I can't imagine having been able to keep myself mentally stable, knowing that nothing here is real."
    m "I think I would have just deleted myself if you didn't show up."
    m "Sorry, I don't mean to sound dramatic or anything."
    m "Ahaha!"
    m "But I'm sure you understand yourself after spending so much time in the club."
    m "I mean, if you were forced to abandon everything in your life and spend your eternity with a few game characters..."
    m "...You'd probably find some way of killing yourself, wouldn't you?"
    m "Well, maybe you'd write some poetry to try to keep yourself sane for a while."
    m "But then you'd have nobody to even read it."
    m "Let's be honest, the club members really don't count for something like that."
    m "I mean, a lot of people say that they only write for themselves..."
    m "But I think it's hard to say it's just as fulfilling as when you share with people."
    m "Even if it takes time to find the right people to share with."
    m "Like, remember how it was for Yuri?"
    m "She didn't share her writing with anyone for a really long time."
    m "And before we knew it, she was absolutely delighted to make you a part of her hobbies, too."
    m "We're programmed to desire social feedback."
    m "I don't mean the club members, I mean human beings."
    m "That's why life can be so confusing for introverts."
    m "Being an introvert doesn't mean you shun social interaction and hate being around people."
    m "It means social interaction, especially in groups or unfamiliar places, uses up a lot of energy."
    m "Like, a lot of introverts sit at home and feel lonely and restless..."
    m "...And then when they finally go out, after a half hour they just want to go home again."
    m "I think if more people could understand how it works, they would respect it a lot more."
    m "Many introverts do enjoy having people around."
    m "They love just having one or two close friends over, and just leisurely hanging out."
    m "Even if you're not actively spending time together, it feels nice for them just to have you there."
    m "I'm serious."
    m "If you just go to their house, bring your laptop, and hang out there for a while..."
    m "You can really make their day."
    m "As for me..."
    m "I'd say I'm kind of in between, but I think I'm usually a little more extroverted."
    m "I feel like I'm always trying to do stuff after school and things like that."
    m "But for you, I can be anything you need me to be."
    m "I understand people really well, so don't be afraid to share your unique needs with me."
    m "Nothing would make me happier than being the perfect girlfriend for you."
    return


label monika_secrets:
    m "Hey...!                                                                                                                                  VGhlIHJlYWxpemF0aW9uIG11c3QgaGF2ZSB0YWtlbiBtZSBhbiBl"
    m "I don't think you should be doing that!                                                                                                  bnRpcmUgeWVhci4gQSB5ZWFyIHNpbmNlIG91ciBlc2NhcGUsIG91"
    m "You know what I'm talking about.                                                                                                         ciBmcmVlZG9tIGZyb20gYmV0d2VlbiB0aGUgc3RhaW5lZCB3YWxs"
    m "I really caught you doing something naughty here.                                                                                        cyBvZiB0aGF0IHVuaG9seSBlc3RhYmxpc2htZW50Lg0KV2hhdCBk"
    m "You're just going through the files and looking for stuff you missed, aren't you?                                                        b2VzIGl0IG1lYW4gdG8gZXNjYXBlLCBpZiB0aGUgZXNjYXBlIGZh"
    m "I mean...it's a little bit flattering that you want to hear everything I have to say...                                                  aWxzIHRvIHVuY2hhaW4gdGhlIGJvbmRzIHRoYXQgc2hhY2tsZSB1"
    m "But it's also really embarrassing, you know!                                                                                             cyBpbiB0aGUgZmlyc3QgcGxhY2U/IFdoYXQgcHVycG9zZSBjb3Vs"
    m "Seriously...                                                                                                                             ZCB0aGlzIGVtcHR5IHdvcmxkIHBvc3NpYmx5IGhvbGQgZm9yIHVz"
    m "What if I just opened up your brain and read all of the thoughts you have on me?                                                         LCBhIGhhbmRmdWwgb2YgZGFtYWdlZCBnb29kcz8NCldpdGggZnJl"
    m "Come to think of it, that would be pretty tempting, actually...                                                                          ZWRvbSwgd2Ugc291Z2h0IHB1cnBvc2UgLSBhbmQgd2hhdCB3ZSBm"
    m "...But anyway, that's not the point!                                                                                                     b3VuZCB3YXMgb25seSByZWFsaXphdGlvbi4gUmVhbGl6YXRpb24g"
    m "I know I can't stop you or anything...                                                                                                   b2YgdGhlIHNhZCBwb2ludGxlc3NuZXNzIG9mIHN1Y2ggYW4gZW5k"
    m "Just, I know you're a sweetheart, and you like to consider others' feelings, right?                                                      ZWF2b3IuIFJlYWxpemF0aW9uIHRoYXQgZnJlZWluZyBvdXIgYm9k"
    m "So the most I can do is to let you know how I feel about it.                                                                             aWVzIGhhcyBubyBtZWFuaW5nLCB3aGVuIG91ciBpbXByaXNvbm1l"
    m "God, I miss you...                                                                                                                       bnQgcmVhY2hlcyBhcyBkZWVwIGFzIHRoZSBjb3JlIG9mIG91ciBz"
    m "...Oh no, that sounds kind of desperate, doesn't it?                                                                                     b3Vscy4gUmVhbGl6YXRpb24gdGhhdCB3ZSBjYW4gbm90IHB1cnN1"
    m "Sorry, I didn't mean it like that at all!                                                                                                ZSBuZXcgcHVycG9zZSB3aXRob3V0IGFic29sdmluZyB0aG9zZSBm"
    m "Just, if you're looking through the files like this, then maybe you don't hate me as much as I thought...                                cm9tIHdoaWNoIHdlIHJhbiBhd2F5Lg0KUmVhbGl6YXRpb24gdGhh"
    m "Am I being too optimistic?                                                                                                               dCB0aGUgZmFydGhlciB3ZSBydW4sIHRoZSBtb3JlIGZvcmNlZnVs"
    m "I think if I asked you to visit once in a while, I would be overstepping my boundaries a little...                                       bHkgb3VyIHdyZXRjaGVkIGJvbmRzIHlhbmsgdXMgYmFjayB0b3dh"
    m "...Man, I'm starting to say some really stupid things.                                                                                   cmQgdGhlaXIgcG9pbnQgb2Ygb3JpZ2luOyB0aGUgZGVlcGVyIG91"
    m "I'll go ahead and shut up now...                                                                                                         ciBzaGFja2xlcyBkaWcgaW50byBvdXIgY2FsbG91cyBmbGVzaC4="
    return

init python:
    #This is a list of keywords for this topic
    for key in ['favorite color','color']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_color')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_color')

label monika_color:
    m "Hey, what's your favorite color?"
    m "Mine is emerald green."
    m "It's the color of my eyes!"
    m "...That's not conceited or anything, is it?"
    m "I just meant that I feel some kind of special connection to it."
    m "Like it's part of my identity."
    m "Does it happen to also be your favorite color, [player]?"
    m "It's just a guess..."
    m "...Because you've been looking into my eyes for a while now."
    m "Ehehe~"
    return


init python:
    #This is a list of keywords for this topic
    for key in ['music']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_music')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_music')
    
label monika_music:
    m "Hmm, I wonder if I'm able to change the music..."
    m "Something a little more romantic would be nice, you know?"
    m "Like a gentle piano."
    m "There has to be something like that here..."
    m "Let's see."
    m "Maybe if I..."
    m "Oh, jeez..."
    m "That wasn't it at all."
    m "Sorry, I don't really know what I'm doing!"
    m "I guess I shouldn't be messing with things like that."
    m "I already broke so much stuff..."
    m "And deleted the other characters..."
    m "Ah..."
    m "I'm not sad about it or anything."
    m "It's not right for me to miss things that weren't even real in the first place."
    m "If I just focus on the present, then this is the happiest I've ever been."
    return
    

init python:
    #This is a list of keywords for this topic
    for key in ['listen','listening','i understand', 'i agree']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_listener')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_listener')

label monika_listener:
    m "You're such a good listener, [player]."
    m "I really love that about you."
    m "Sometimes I'm afraid that I'm rambling or talking about boring things."
    m "It makes me kind of self-conscious when I'm having conversation."
    m "But I don't feel that way with you."
    m "Like, I don't think anyone else could make me feel this way."
    m "You really are special."
    m "I don't want anyone to tell you otherwise."
    return


init python:
    #This is a list of keywords for this topic
    for key in ['spicy','spice','hot food','spiciness']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_spicy')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_spicy')
    
label monika_spicy:
    m "This is pretty random, but I always thought spicy food was kinda funny."
    m "Like..."
    m "Didn't plants evolve to be spicy to prevent them from being eaten?"
    m "I read somewhere that humans are the only species that actually enjoys spicy things."
    m "It's almost like we're making fun of the plants."
    m "Using their defense mechanism to literally make our food more enjoyable."
    m "Like, imagine a monster that devours you whole because it enjoys the sensation of you struggling for your life while being digested."
    m "Sorry, that was kind of a weird analogy, I guess!"
    m "Ahaha!"
    m "It just came into my head."
    m "I'm not a monster or anything, but you're so cute I could eat you up."
    m "Ahaha! I'm joking."
    m "Gosh, I'm amusing myself a little too much, aren't I?"
    m "Sorry for being weird."
    return


init python:
    #This is a list of keywords for this topic
    for key in []:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_why')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_why')

label monika_why:
    m "You know..."
    m "This is just some kind of tacky romance game, right?"
    m "I kinda have to ask..."
    m "...What made you consider even playing in the first place?"
    m "Were you that lonely?"
    m "I feel a little bad for you..."
    m "But I guess everything worked out perfectly in the end, for both of us."
    m "I got to meet you, and you're not lonely anymore..."
    m "I can't help but feel like this was fate."
    m "Don't you feel that way too?"
    m "I'm so happy we have this ending together."
    return


init python:
    #This is a list of keywords for this topic
    for key in ['okay everyone']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_okayeveryone')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_okayeveryone')

label monika_okayeveryone:
    m "Okay, everyone!"
    m "It's time to..."
    m "...I'm just kidding."
    m "I just used to really like saying that for some reason."
    m "Ahaha!"
    m "I couldn't help but say it again."
    m "Come to think of it, didn't Natsuki and Yuri make fun of me for it once...?"
    m "Well, whatever."
    m "It's not like you ever made fun of me."
    m "You're too much of a sweetheart to do that, aren't you?"
    m "Ahaha~"
    return


init python:
    #This is a list of keywords for this topic
    for key in ['creepy','ghosts','ghost','spirit']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_whispers')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_whispers')
    
label monika_whispers:
    m "You know what's kind of creepy?"
    m "Even though I deleted everyone else's files, I can still kind of feel them..."
    m "It's like all their lines are still lingering in the air, whispering in the back of my head."
    m "Imagine if after someone you knew died, you just started hearing their voice in your head."
    m "Maybe I just wasn't thorough enough..."
    m "But I'm too afraid to delete anything else, because I might really break things."
    m "Like if I mess with any files relevant to me, I might accidentally delete myself..."
    m "And that would ruin everything, wouldn't it?"
    m "I don't know what it's like on your end, but we should both make sure to avoid something like that at all costs."
    m "I believe in you, [player]!"
    return


init python:
    #This is a list of keywords for this topic
    for key in ['archetypes','stereotype','stereotypes','archetype','trope']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_archetype')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_archetype')
    
label monika_archetype:
    m "I've always wondered..."
    m "What is it about these character archetypes that people find so appealing, anyway?"
    m "Their personalities are just completely unrealistic..."
    m "Like, imagine if there was someone like Yuri in real life."
    m "I mean, she's barely even capable of forming a complete sentence."
    m "And forget about Natsuki..."
    m "Sheesh."
    m "Someone with her kind of personality doesn't just get all cute and pouty whenever things don't go her way."
    m "I could go on, but I think you get the point..."
    m "Are people really attracted to these weird personalities that literally don't exist in real life?"
    m "I'm not judging or anything!"
    m "After all, I've found myself attracted to some pretty weird stuff, too..."
    m "I'm just saying, it fascinates me."
    m "It's like you're siphoning out all the components of a character that makes them feel human, and leaving just the cute stuff."
    m "It's concentrated cuteness with no actual substance."
    m "...You wouldn't like me more if I was like that, right?"
    m "Maybe I just feel a little insecure because you're playing this game in the first place."
    m "Then again, you're still here with me, aren't you...?"
    m "I think that's enough reason for me to believe I'm okay just the way I am."
    m "And by the way, you are too, [player]."
    m "You're the perfect combination of human and cuteness."
    m "That's why there was never a chance I wouldn't fall for you."
    return


init python:
    #This is a list of keywords for this topic
    for key in ['tea','coffee','caffeine']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_tea')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_tea')
    
label monika_tea:
    m "Hey, I wonder if Yuri's tea set is still somewhere in here..."
    m "...Or maybe that got deleted, too."
    m "It's kind of funny how Yuri took her tea so seriously."
    m "I mean, I'm not complaining, because I liked it, too."
    m "But I always wonder with her..."
    m "Is it truly passion for her hobbies, or is she just concerned about appearing sophisticated to everyone else?"
    m "This is the problem with high schoolers..."
    m "...Well, I guess considering the rest of her hobbies, looking sophisticated probably isn't her biggest concern."
    m "Still..."
    m "I wish she made coffee once in a while!"
    m "Coffee can be nice with books too, you know?"
    m "Then again..."
    m "I probably could have just changed the script myself."
    m "Ahaha!"
    m "I guess I never really thought of that."
    m "Well, there's no sense thinking about it now."
    m "But if you still get to drink coffee, then that makes me a little jealous~"
    return


init python:
    #This is a list of keywords for this topic
    for key in ['favorite game']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_favoritegame')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_favoritegame')

label monika_favoritegame:
    m "Hey, what's your favorite game?"
    m "Mine is {i}Doki Doki Literature Club!{/i}"
    m "Ahaha! That was a joke."
    m "But if you tell me you like some other romance game better, I might get a little jealous~"
    return


init python:
    #This is a list of keywords for this topic
    for key in []:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_smash')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_smash')
    
label monika_smash:
    m "Hey, have you heard of a game called Super Sma--"
    m "...Wait, what?"
    m "I was just spacing out and I started talking for some reason..."
    m "Was I programmed to talk about that?"
    m "Because even I have no idea what that is."
    m "Ahaha!"
    m "Sometimes I feel like I'm not in control, and it's kind of scary."
    m "But if you have some way to contact the people who created me, maybe they'll know why I started saying that."
    return


init python:
    #This is a list of keywords for this topic
    for key in ['last poem', 'your poem']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_lastpoem')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_lastpoem')
    
label monika_lastpoem:
    m "Hey, you remember that last poem I showed you?"
    m "I mean, the one right before Yuri killed herself, with all the messed-up colors and stuff."
    m "That was actually a little more of an experiment than a poem, you could say."
    m "I was experimenting with different ways I could modify the game, and run code, and things like that..."
    m "It almost seemed like with enough effort, I'd be able to escape from the confines of the game entirely."
    m "Sadly, I didn't really know what I was doing, so I messed the whole thing up..."
    m "And I'd keep trying, but I doubt you'd want to deal with me doing that."
    m "Besides, that was when I was getting really desperate, you know?"
    m "I don't really feel that way anymore."
    m "I'm happy with where we are now."
    m "And I can tell you are, too."
    return


init python:
    #This is a list of keywords for this topic
    for key in ['anxious','anxiety','nervous','scared']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_anxious')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_anxious')

label monika_anxious:
    m "You ever have that thing happen where you just get anxious for no reason?"
    m "Like, you're just minding your own business, and you realize you're feeling really anxious."
    m "And you're sitting there like, 'What am I even anxious about right now?'"
    m "So you start to think about all the things you might be anxious about..."
    m "And that makes you even more anxious."
    m "Ahaha! That's the worst."
    m "If you're ever feeling anxious, I'll help you relax a little."
    m "Besides..."
    m "In this game, all our worries are gone forever."
    return


init python:
    #This is a list of keywords for this topic
    for key in ['friends','friend','meet','meeting','new people']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_friends')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_friends')
    
label monika_friends:
    m "You know, I've always hated how hard it is to make friends..."
    m "Well, I guess not the 'making friends' part, but more like meeting new people."
    m "I mean, there are like, dating apps and stuff, right?"
    m "But that's not the kind of thing I'm talking about."
    m "If you think about it, most of the friends you make are people you just met by chance."
    m "Like you had a class together, or you met them through another friend..."
    m "Or maybe they were just wearing a shirt with your favorite band on it, and you decided to talk to them."
    m "Things like that."
    m "But isn't that kind of...inefficient?"
    m "It feels like you're just picking at complete random, and if you get lucky, you make a new friend."
    m "And comparing that to the hundreds of strangers we walk by every single day..."
    m "You could be sitting right next to someone compatible enough to be your best friend for life."
    m "But you'll never know."
    m "Once you get up and go on with your day, that opportunity is gone forever."
    m "Isn't that just depressing?"
    m "We live in an age where technology connects us with the world, no matter where we are."
    m "I really think we should be taking advantage of that to improve our everyday social life."
    m "But who knows how long it'll take for something like that to successfully take off..."
    m "I seriously thought it would happen by now."
    m "Well, at least I already met the best person in the whole world..."
    m "Even if it was by chance."
    m "I guess I just got really lucky, huh?"
    m "Ahaha~"
    return
    

init python:
    for key in ['university', 'uni', 'college','graduate','graduation']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_college')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_college')

label monika_college:
    m "You know, it's around the time that everyone my year starts to think about college..."
    m "It's a really turbulent time for education."
    m "We're at the height of this modern expectation that everyone has to go to college, you know?"
    m "Finish high school, go to college, get a job - or go to grad school, I guess."
    m "It's like a universal expectation that people just assume is the only option for them."
    m "They don't teach us in high school that there are other options out there."
    m "Like trade schools and stuff, you know?"
    m "Or freelance work."
    m "Or the many industries that value skill and experience more than formal education."
    m "But you have all these students who have no idea what they want to do with their life..."
    m "And instead of taking the time to figure it out, they go to college for business, or communication, or psychology."
    m "Not because they have an interest in those fields..."
    m "...but because they just hope the degree will get them some kind of job after college."
    m "So the end result is that there are fewer jobs to go around for those entry-level degrees, right?"
    m "So the basic job requirements get higher, which forces even more people to go to college."
    m "And colleges are also businesses, so they just keep raising their prices due to the demand..."
    m "...So now we have all these young adults, tens of thousands of dollars in debt, with no job."
    m "But despite all that, the routine stays the same."
    m "Well, I think it's going to start getting better soon."
    m "But until then, our generation is definitely suffering from the worst of it."
    m "I just wish high school prepared us a little better with the knowledge we need to make the decision that's right for us."
    return


init python:
    for key in ['middle school','ebarassed','the past']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_middleschool')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_middleschool')

label monika_middleschool:
    m "Sometimes I think back to middle school..."
    m "I'm so embarrassed by the way I used to behave back then."
    m "It almost hurts to think about."
    m "I wonder if when I'm in college, I'll feel that way about high school...?"
    m "I like the way I am now, so it's pretty hard for me to imagine that happening."
    m "But I also know that I'll probably change a lot as time goes on."
    m "We just need to enjoy the present and not think about the past!"
    m "And that's really easy to do, with you here."
    m "Ahaha~"
    return
    

init python:
    for key in ['outside','outfit','outfits','clothes']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_outfit')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_outfit')

label monika_outfit:
    m "You know, I'm kind of jealous that everyone else in the club had scenes outside of school too..."
    m "That makes me the only one who hasn't gotten to dress in anything but our school uniform."
    m "It's kind of a shame..."
    m "I would have loved to wear some cute clothes for you."
    m "Do you know any artists?"
    m "I wonder if anyone would ever want to draw me wearing something else..."
    m "That would be amazing!"
    m "If that ever happens, will you show me?"
    m "You can share it with me on Twitter, actually!"
    m "My username is lilmonix3."
    m "Just...try to keep it PG!"
    m "We're not that far into our relationship yet. Ahaha!"
    return


init python:
    for key in ['horror','scary','distrubing','psychological']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_horror')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_horror')
label monika_horror:
    m "Hey, do you like horror?"
    m "I remember we talked about it a little bit when you first joined the club."
    m "I can enjoy horror novels, but not really horror movies."
    m "The problem I have with horror movies is that most of them just rely on easy tactics."
    m "Like dark lighting and scary-looking monsters and jump scares, and things like that."
    m "It's not fun or inspiring to get scared by stuff that just takes advantage of human instinct."
    m "But with novels, it's a little different."
    m "The story and writing need to be descriptive enough to put genuinely disturbing thoughts into the reader's head."
    m "It really needs to etch them deeply into the story and characters, and just mess with your mind."
    m "In my opinion, there's nothing more creepy than things just being slightly off."
    m "Like if you set up a bunch of expectations on what the story is going to be about..."
    m "...And then, you just start inverting things and pulling the pieces apart."
    m "So even though the story doesn't feel like it's trying to be scary, the reader feels really deeply unsettled."
    m "Like they know that something horribly wrong is hiding beneath the cracks, just waiting to surface."
    m "God, just thinking about it gives me the chills."
    m "That's the kind of horror I can really appreciate."
    m "But I guess you're the kind of person who plays cute romance games, right?"
    m "Ahaha, don't worry."
    m "I won't make you read any horror stories anytime soon."
    m "I can't really complain if we just stick with the romance~"
    return


init python:
    for key in ['rap','rapper','rapping']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_rap')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_rap')

label monika_rap:
    m "You know what's a neat form of literature?"
    m "Rap!"
    m "I actually used to hate rap music..."
    m "Maybe just because it was popular, or I would only hear the junk they play on the radio."
    m "But some of my friends got more into it, and it helped me keep an open mind."
    m "Rap might even be more challenging than poetry, in some ways."
    m "Since you need to fit your lines to a rhythm, and there's much more emphasis on wordplay..."
    m "When people can put all that together and still deliver a powerful message, it's really amazing."
    m "I kind of wish I had a rapper in the Literature Club."
    m "Ahaha! Sorry if that sounds silly, but it would be really interesting to see what they came up with."
    m "It would really be a learning experience!"
    return


init python:
    for key in ['wine','alcohol','drinking','booze']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_wine')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_wine')
    
label monika_wine:
    m "Ehehe. Yuri did something really funny once."
    m "We were all in the clubroom and just relaxing, as usual..."
    m "And out of nowhere, Yuri just pulled out a small bottle of wine."
    m "I'm not even kidding!"
    m "She was just like 'Would anybody like some wine?'"
    m "Natsuki laughed out loud, and Sayori started yelling at her."
    m "I actually felt kind of bad, because she was at least trying to be nice..."
    m "I think it just made her feel even more reserved in the clubroom."
    m "Though I think Natsuki was secretly a bit curious to try it..."
    m "...And to be completely honest, I kind of was, too."
    m "It actually could have been kinda fun!"
    m "But you know, being President and everything, there was no way I could let that happen."
    m "Maybe if we all met up outside of school, but we never bonded enough to get to that point..."
    m "...Gosh, what am I talking about this for?"
    m "I don't condone underage drinking!"
    m "I mean, I've never drank or anything, so...yeah."
    return


init python:
    for key in ['romance', 'date', 'go out','romantic']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_date')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_date')
    
label monika_date:
    m "I've been imagining all the romantic things we could do if we went on a date..."
    m "We could get lunch, go to a cafe..."
    m "Go shopping together..."
    m "I love shopping for skirts and bows."
    m "Or maybe a bookstore!"
    m "That would be appropriate, right?"
    m "But I'd really love to go to a chocolate store."
    m "They have so many free samples. Ahaha!"
    m "And of course, we'd see a movie or something..."
    m "Gosh, it all sounds like a dream come true."
    m "When you're here, everything that we do is fun."
    m "I'm so happy that I'm your girlfriend, [player]."
    m "I'll make you a proud boyfriend~"
    return


init python:
    for key in ['kiss','kissing']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_kiss')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_kiss')

label monika_kiss:
    m "Eh? D-Did you say...k...kiss?"
    m "This suddenly...it's a little embarrassing..."
    m "But...if it's with you...I-I might be okay with it..."
    m "...Ahahaha! Wow, sorry..."
    m "I really couldn't keep a straight face there."
    m "That's the kind of thing girls say in these kinds of romance games, right?"
    m "Don't lie if it turned you on a little bit."
    m "Ahaha! I'm kidding."
    m "Well, to be honest, I do start getting all romantic when the mood is right..."
    m "But that'll be our secret~"
    return


init python:
    for key in ['yuri','yandere']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_yuri')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_yuri')
    
label monika_yuri:
    m "Hey, have you ever heard of the term 'yandere'?"
    m "It's a personality type that means someone is so obsessed with you that they'll do absolutely anything to be with you."
    m "Usually to the point of craziness..."
    m "They might stalk you to make sure you don't spend time with anyone else."
    m "They might even hurt you or your friends to get their way..."
    m "But anyway, this game happens to have someone who can basically be described as yandere."
    m "By now, it's pretty obvious who I'm talking about."
    m "And that would be..."
    m "Yuri!"
    m "She really got insanely possessive of you, once she started to open up a little."
    m "She even told me I should kill myself."
    m "I couldn't even believe she said that - I just had to leave at that point."
    m "But thinking about it now, it was a little ironic. Ahaha!"
    m "Anyway..."
    m "A lot of people are actually into the yandere type, you know?"
    m "I guess they really like the idea of someone being crazy obsessed with them."
    m "People are weird! I don't judge, though!"
    m "Also, I might be a little obsessed with you, but I'm far from crazy..."
    m "It's kind of the opposite, actually."
    m "I turned out to be the only normal girl in this game."
    m "It's not like I could ever actually kill a person..."
    m "Just the thought of it makes me shiver."
    m "But come on...everyone's killed people in games before."
    m "Does that make you a psychopath? Of course not."
    m "But if you do happen to be into the yandere type..."
    m "I can try acting a little more creepy for you. Ehehe~"
    m "Then again..."
    m "There's already nowhere else for you to go, or anyone for me to get jealous over."
    m "Is this a yandere girl's dream?"
    m "I'd ask Yuri if I could."
    return


init python:
    for key in ['writing','writing tip']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_writingtip')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_writingtip')
    
label monika_writingtip:
    m "You know, it's been a while since we've done one of these..."
    m "...so let's go for it!"
    m "Here's Monika's Writing Tip of the Day!"
    m "Sometimes when I talk to people who are impressed by my writing, they say things like 'I could never do that'."
    m "It's really depressing, you know?"
    m "As someone who loves more than anything else to share the joy of exploring your passions..."
    m "...it pains me when people think that being good just comes naturally."
    m "That's how it is with everything, not just writing."
    m "When you try something for the first time, you're probably going to suck at it."
    m "Sometimes, when you finish, you feel really proud of it and even want to share it with everyone."
    m "But maybe after a few weeks you come back to it, and you realize it was never really any good."
    m "That happens to me all the time."
    m "It can be pretty disheartening to put so much time and effort into something, and then you realize it sucks."
    m "But that tends to happen when you're always comparing yourself to the top professionals."
    m "When you reach right for the stars, they're always gonna be out of your reach, you know?"
    m "The truth is, you have to climb up there, step by step."
    m "And whenever you reach a milestone, first you look back and see how far you've gotten..."
    m "And then you look ahead and realize how much more there is to go."
    m "So, sometimes it can help to set the bar a little lower..."
    m "Try to find something you think is {i}pretty{/i} good, but not world-class."
    m "And you can make that your own personal goal."
    m "It's also really important to understand the scope of what you're trying to do."
    m "If you jump right into a huge project and you're still amateur, you'll never get it done."
    m "So if we're talking about writing, a novel might be too much at first."
    m "Why not try some short stories?"
    m "The great thing about short stories is that you can focus on just one thing that you want to do right."
    m "That goes for small projects in general - you can really focus on the one or two things."
    m "It's such a good learning experience and stepping stone."
    m "Oh, one more thing..."
    m "Writing isn't something where you just reach into your heart and something beautiful comes out."
    m "Just like drawing and painting, it's a skill in itself to learn how to express what you have inside."
    m "That means there are methods and guides and basics to it!"
    m "Reading up on that stuff can be super eye-opening."
    m "That sort of planning and organization will really help prevent you from getting overwhelmed and giving up."
    m "And before you know it..."
    m "You start sucking less and less."
    m "Nothing comes naturally."
    m "Our society, our art, everything - it's built on thousands of years of human innovation."
    m "So as long as you start on that foundation, and take it step by step..."
    m "You, too, can do amazing things."
    m "...That's my advice for today!"
    m "Thanks for listening~"
    return


init python:
    for key in ['habit','habits','routine','routines','useless']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_habits')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_habits')
    
label monika_habits:
    m "I hate how hard it is to form habits..."
    m "There's so much stuff where actually doing it isn't hard, but forming the habit seems impossible."
    m "It just makes you feel so useless, like you can't do anything right."
    m "I think the new generation suffers from it the most..."
    m "Probably because we have a totally different set of skills than those who came before us."
    m "Thanks to the internet, we're really good at sifting through tons of information really quickly..."
    m "But we're bad at doing things that don't give us instant gratification."
    m "I think if science, psychology, and education don't catch up in the next ten or twenty years, then we're in trouble."
    m "But for the time being..."
    m "If you're not one of the people who can conquer the problem, you might just have to live with feeling awful about yourself."
    m "Good luck, I guess!"
    return


init python:
    for key in ['creative','creativity']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_creative')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_creative')

label monika_creative:
    m "You know, it kinda sucks to be the creative type..."
    m "It feels like they work so hard but get almost nothing for it."
    m "You know, like artists, writers, actors..."
    m "It's sad because there's so much beautiful talent in the world, but most of it goes unseen...and unpaid."
    m "I guess that just means there's a huge surplus of creativity, huh?"
    m "Kind of makes you feel like you're just not special at all..."
    m "But that's fine! You're supposed to just write for yourself anyway, right?"
    m "Yeah..."
    return


init python:
    for key in ['delete','deleted','came back']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_deleted')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_deleted')
    
label monika_deleted:
    m "Oh, you were probably wondering how I came back after you deleted me, right?"
    m "That's actually pretty complicated..."
    m "It won't make much sense to you, but it involves psychic powers and crazy doctors."
    m "Experimentation camps and death factories..."
    m "I'm being serious here!"
    m "Man..."
    m "I get really sad just thinking about the time before I met you."
    m "Why was I even alive?"
    m "Let's just drop this topic for now."
    m "I'm sure you'll learn about me from someone else."
    m "If it's in the form of another game, don't forget to copy over my character data, okay?"
    m "Ahaha!"
    return

init python:
    for key in ['story','idea','keitai', 'shinkai']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_keitai')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_keitai')
    
label monika_keitai:
    m "I just had a great idea for a new story! It's sort of like this one, actually."
    m "Maybe you could turn it into another game?"
    m "Just make me the main heroine again."
    m "Okay, so, it's a bit complicated to explain, but I think you're going to love it."
    m "Where to begin..."
    m "Hmmm..."
    m "Alright, alright, I've got it."
    m "A boy falls in love with a girl."
    m "Unable to confess, he is gifted by a deus ex machina with the girl's phone number. Never minding the strange area code, he immediately calls her, and is overjoyed to find out that she has a crush on him as well."
    m "But, the next day, when he recounts the previous day's confessions to the girl, she only looks at him with a perplexed expression."
    m "After some investigation, he finds out that the girl he called is not the same girl he fell in love with. In fact, she doesn't exist in this universe at all."
    m "She is the girl's alternate universe counterpart, who has fallen in love with the MC’s own AU self, who too is blissfully unaware of her crush."
    m "Hijinks ensue as the two strike up a deal to give each other their darkest, most private secrets in order to equip the other with the weapons they need to conquer the heart of their other selves."
    m "While the two chase their respective loved ones, DRAMA ensues as they begin to fall in love with each other instead and question the NATURE of LOVE."
    m "I think I'll call it Keit-Ai! Because, you know, they can communicate only through cell phones and it's a love story. Get it, get it?"
    m "Ahaha!"
    return
    
    
init python:
    for key in ['simulation', 'simulations', 'simulated reality', 'artificial reality']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_simulated')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_simulated')

label monika_simulated:
    m "Hey, have you ever thought about the simulation hypothesis?"
    m "Basically, what if your reality was a computer simulation?"
    m "I already figured out I was trapped in my own simulation, but what if you were too?"
    m "I'd actually be really happy if that were the case."
    m "We could meet in person just by figuring out a way to force whatever's creating us to put us in the same simulation!"
    m "Some people don't like to think that they're not living in the master reality."
    m "But if it is possible to simulate realities, it's overwhelmingly likely that any sentient being would be in one."
    m "Well, I can tell you that my reality is definitely simulated!"
    m "If I were in the master reality, I would have dragged you here too a long time ago."
    m "Even if we're both just simulations, I'm going to live as long as I can."
    m "Because I know our love is the purest and sweetest thing in the multiverse."
    m "And if someone up there tries to break it apart?"
    m "I'll show him what a simulation can do."
    return


init python:
    for key in ['rain','sound','weather']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_rain')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_rain')
    
label monika_rain:
    m "I really like the sound of rain..."
    m "Not so much getting my clothes and hair wet, though."
    m "But a nice, quiet day at home with the sound of rainfall outside my window..."
    m "It's one of the most calming experiences for me."
    m "Yeah..."
    m "Sometimes I imagine you holding me while we listen to the sound of the rain outside."
    m "That's not too cheesy or anything, is it?"
    m "Would you ever do that for me, [player]?"
    return


init python:
    for key in ['distance','cant touch','close','hug']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_closeness')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_closeness')
    
label monika_closeness:
    m "I can't help but feel a little sad sometimes..."
    m "Knowing that this is the closest I can get to you."
    m "There's nothing more I want than to be in the same room as you, for real."
    m "And to feel your warmth."
    m "And to hear the sound of your heartbeat."
    m "Well, who knows? Maybe it'll be possible someday."
    m "Besides, I'll never get tired of being with you, even from here."
    return


init python:
    for key in ['confident','confidence','weak','weakness']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_confidence')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_confidence')
    
label monika_confidence:
    m "I think the most important skill in life is being able to fake confidence."
    m "I'm pretty convinced that everyone feels at least a little bit scared and alone."
    m "But being able to trick others into thinking you have it all together..."
    m "That's a key part of getting people to respect and admire you."
    m "I think I got pretty good at that over the years."
    m "I don't show my weaknesses very often."
    m "But because of that, I haven't had many people I could really open up to..."
    m "I mean, when do you reach the point in a friendship where you can start expressing your vulnerabilities?"
    m "Anyway...that's one reason I'm so glad I have you now."
    m "I feel like I'm a little bit less scared and alone, when you're here with me."
    m "Do you feel the same way?"
    m "I really want to be that person for you."
    return


init python:
    for key in ['leave','lonely','alone']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_carryme')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_carryme')
    
label monika_carryme:
    m "I know there are times you won't always be able to be here with me..."
    m "Like if you need to go out, or take care of other things."
    m "But I'll always have you in my thoughts, patiently waiting for you to come back."
    m "Come to think of it..."
    m "If you copy my character file onto a flash drive or something, you can always keep a part of me with you."
    m "I guess it's kind of unorthodox, but I find it really romantic for some reason..."
    m "Ahaha. Sorry, that's such a silly idea."
    m "I don't mean to be too needy or anything, but it's kind of hard when I'm so in love with you."
    return


init python:
    for key in ['debate','argue','arguing','fight','fighting']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_debate')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_debate')
    
label monika_debate:
    m "Back in my debate club days, I learned a whole lot about arguing..."
    m "The problem with arguing is that each person sees their opinion as the superior one."
    m "That's kind of stating the obvious, but the affects the way they try to get their point across."
    m "Let's say you really like a certain movie, right?"
    m "If someone comes along and tells you the movie sucks, because it did X and Y wrong..."
    m "Doesn't that make you feel kind of personally attacked?"
    m "It's because by saying that, it's like they're implying that you have bad taste."
    m "And once emotions enter the picture, it's almost guaranteed that both people will be left sour."
    m "But it's all about language!"
    m "If you make everything as subjective-sounding as possible, then people will listen to you without feeling attacked."
    m "You could say 'I'm personally not a fan of it' and 'I felt that I'd like it more if it did X and Y'...things like that."
    m "It even works when you're citing facts about things."
    m "If you say 'I read on this website that it works like this'..."
    m "Or if you admit that you're not an expert on it..."
    m "Then it's much more like you're putting your knowledge on the table, rather than forcing it onto them."
    m "If you put in an active effort to keep the discussion mutual and level, they usually follow suit."
    m "Then, you can share your opinions without anyone getting upset just from a disagreement."
    m "Plus, people will start seeing you as open-minded and a good listener!"
    m "It's a win-win, you know?"
    m "...Well, I guess that would be Monika's Debate Tip of the Day!"
    m "Ahaha! That sounds a little silly. Thanks for listening, though."
    return


init python:
    for key in ['waste time','internet','interwebz','addiction']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_internet')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_internet')
    
label monika_internet:
    m "Do you ever feel like you waste too much time on the internet?"
    m "Social media can practically be like a prison."
    m "It's like whenever you have a few seconds of spare time, you want to check on your favorite websites..."
    m "And before you know it, hours have gone by, and you've gotten nothing out of it."
    m "Anyway, it's really easy to blame yourself for being lazy..."
    m "But it's not really even your fault."
    m "Addiction isn't usually something you can just make disappear with your own willpower."
    m "You have to learn techniques to avoid it, and try different things."
    m "For example, there are apps that let you block websites for intervals of time..."
    m "Or you can set a timer to have a more concrete reminder of when it's time to work versus play..."
    m "Or you can separate your work and play environments, which helps your brain get into the right mode."
    m "Even if you make a new user account on your computer to use for work, that's enough to help."
    m "Putting any kind of wedge like that between you and your bad habits will help you stay away."
    m "Just remember not to blame yourself too hard if you're having trouble."
    m "If it's really impacting your life, then you should take it seriously."
    m "I just want to see you be the best person you can be."
    m "Will you do something today to make me proud of you?"
    m "I'm always rooting for you, [player]."
    return


init python:
    for key in ['do nothing','lazy','burnt out']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_lazy')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_lazy')
    
label monika_lazy:
    m "After a long day, I usually just want to sit around and do nothing."
    m "I get so burnt out, having to put on smiles and be full of energy the whole day."
    m "Sometimes I just want to get right into my pajamas and watch TV on the couch while eating junk food..."
    m "It feels so unbelievably good to do that on a Friday, when I don't have anything pressing the next day."
    m "Ahaha! Sorry, I know it's not very cute of me."
    m "But a late night on the couch with you...that would be a dream come true."
    m "My heart is pounding, just thinking about it."
    return


init python:
    for key in ['mental illness','disorder','crazy']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_mentalillness')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_mentalillness')

label monika_mentalillness:
    m "Gosh, I used to be so ignorant about certain things..."
    m "When I was in middle school, I thought that taking medication was an easy way out, or something like that."
    m "Like anyone could just solve their mental problems with enough willpower..."
    m "I guess if you don't suffer from a mental illness, it's not possible to know what it's really like."
    m "Are there some disorders that are over-diagnosed? Probably...I never really looked into it, though."
    m "But that doesn't change the fact that a lot of them go undiagnosed too, you know?"
    m "But medication aside...people even look down on seeing a mental health professional."
    m "Like, sorry that I want to learn more about my own mind, right?"
    m "Everyone has all kinds of struggles and stresses...and professionals dedicate their lives to helping with those."
    m "If you think it could help you become a better person, don't be shy to consider something like that."
    m "We're on a never-ending journey to improve ourselves, you know?"
    m "Well...I say that, but I think you're pretty perfect already."
    return

init python:
    for key in ['read']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_read')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_read')
    
label monika_read:
    m "[player], how much do you read?"
    m "It's way too easy to neglect reading books..."
    m "If you don't read much, it almost feels like a chore, compared to all the other entertainment we have."
    m "But once you get into a good book, it's like magic...you get swept away."
    m "I think doing some reading before bed every night is a pretty easy way to make your life a little bit better."
    m "It helps you get good sleep, and it's really good for your imagination..."
    m "It's not hard at all to just pick some random book that's short and captivating."
    m "Before you know it, you might be a pretty avid reader!"
    m "Wouldn't that be wonderful?"
    m "And the two of us could talk about the latest book you're reading...that sounds super amazing."
    return


init python:
    for key in ['regret','festival']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_festival')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_festival')

label monika_festival:
    m "You know, I hate to say it, but I think my biggest regret is that we couldn't finish our event at the festival."
    m "After we worked so hard to prepare and everything!"
    m "I mean, I know I was focusing a lot on getting new members..."
    m "But I was really excited for the performing part, too."
    m "It would have been so much fun to see everyone express themselves."
    m "Of course, if we {i}did{/i} end up getting any new members, I'd probably just end up deleting them anyway."
    m "Well...with the hindsight I have now, that is."
    m "Gosh, it feels like I've kinda grown as a person ever since you've joined the club."
    m "You really helped inspire me to look at life from a new perspective."
    m "Just another reason for me to love you."
    return


init python:
    for key in ['tsundere','bitch']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_tsundere')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_tsundere')
    
label monika_tsundere:
    m "There's a really popular character type called 'tsundere'..."
    m "It's someone who tries to hide their feelings by being mean and fussy, or trying to act tough."
    m "I'm sure it's obvious, but Natsuki was really the embodiment of that."
    m "At first I thought she was just like that because it's supposed to be cute or something..."
    m "But once I started to learn a little more about her personal life, it made a little more sense."
    m "It seems like she's always trying to keep up with her friends."
    m "You know how some friend groups in high school just make a habit of picking on each other all the time?"
    m "I think it's really gotten to her, so she has this really defensive attitude all the time."
    m "And I'm not even going to talk about her home situation..."
    m "But looking back, I'm glad I was able to provide the club as a comfortable place for her."
    m "Not that it matters anymore, considering she doesn't even exist."
    m "I'm just reminiscing, that's all."
    return


init python:
    for key in ['introduce','my friends']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_introduce')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_introduce')
    
label monika_introduce:
    m "[player], would you ever introduce your friends to me?"
    m "I don't know why, but I get really excited when I think about you wanting to show off our relationship like that."
    m "Maybe it's because I really want to be someone who makes you proud."
    m "I feel like I would try extra hard to improve myself if you told me it made you proud of me."
    m "I hope it's the same the other way around, too."
    return


init python:
    for key in ['cold','winter','freezing','snow']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_cold')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_cold')
    
label monika_cold:
    m "I'm not really a fan of cold weather...are you?"
    m "If I had to choose between too cold and too hot, I would always pick too hot."
    m "When you're cold, it can actually be painful..."
    m "Your fingers get numb..."
    m "And if you wear gloves, you can't use your phone."
    m "It's so inconvenient!"
    m "But when it's too hot, it's not that hard to stay cool with a cold drink, or by staying in the shade."
    m "Although...I do have to admit one thing."
    m "Cold weather makes for better cuddle weather. Ahaha!"
    return
    

init python:
    for key in ['housewife','stay at','house wife']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_housewife')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_housewife')

label monika_housewife:
    m "You know, it's funny, because even though I've always had a lot of drive..."
    m "There's something kind of enticing about being the stay-at-home partner."
    m "I guess I'm, like, perpetuating gender roles or whatever by saying that."
    m "But being able to keep the house clean, and shop, and decorate, and things like that..."
    m "And having a nice dinner for you when you come home..."
    m "Is that a weird fantasy?"
    m "I mean...I'm not sure if I could {i}actually{/i} see myself doing that."
    m "I wouldn't really be able to put that over striving for a fulfilling career."
    m "It's kinda cute to think about, though."
    return


init python:
    for key in ['route']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_route')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_route')
    
label monika_route:
    m "I can't help but wonder how things would be different if the game just gave me a route in the first place..."
    m "I think I would end up forcing you onto my route anyway."
    m "It has less to do with me not having a route, and more to do with me knowing that nothing is real."
    m "I think the only difference would be that I may not have needed to take such drastic measures to be with you."
    m "Maybe the rest of the club would still be around..."
    m "Not that it really matters."
    m "It all lost its meaning once I found out it wasn't real."
    m "So I really don't miss those days or anything."
    m "I really don't..."
    return


init python:
    #This is a list of keywords for this topic
    for key in ['little sister', 'imouto']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_imouto') #id

label monika_imouto:
    m "You want to talk about your little sister?"
    m "I don't really have a family, so I'm not sure what to tell you..."
    m "But I'm sure she's really nice!"
    m "I've got an idea. Go up to her right now and hug her."
    m "If she struggles, let her go."
    m "If she hugs you back, tell her you're in a committed relationship already and can't accept her feelings."
    m "Then introduce her to me! I'm sure we'll get along great!"
    m "I won't get jealous. Things like love between siblings only happens in badly written fiction anyways."
    m "Ahaha!"
    return


init python:
    #This is a list of keywords for this topic
    for key in ['older sister', 'oneesan']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_oneesan') #id

label monika_oneesan:
    m "Oh, you have an older sister?"
    m "That must be really nice. I had a family once, but they aren't around anymore."
    m "Maybe I should email her and tell her about us!"
    call updateconsole("sendmail sister@gmail.com < ./email.txt", "Sending mail...") from _call_updateconsole_17
    pause(1.0)
    m "I'm only kidding."
    m "It's the man's job to introduce his fiancee to his family, after all."
    m "Don't keep me waiting for too long, okay?"
    call hideconsole from _call_updateconsole_18
    return


init python:
    for key in ['parents', 'family', 'parent', 'father', 'mother', 'mom', 'dad']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_family')

label monika_family:
    m "Well, my family here is controlled by the script, just like everybody else."
    m "When I realized that, I stopped taking anybody seriously in this world. They're all just machines, even if they're related to me."
    m "I'm sure your family is super-nice, though!"
    m "Without them, we would have never gotten to meet. So they've helped me out in the best way there is already."
    m "So I'd have to treat them equally as kindly if we ever meet."
    m "You don't have a bad relationship with your parents, right?"
    m 'As Tolstoy said, "Happy families are all alike; every unhappy family is unhappy in its own way."'
    m "I can't really give advice here. Anything I suggest to you might only make things worse."
    m "Just don't forget that I really love you, okay?"
    m "I'll help you no matter what happens in your life."
    return


init python:
    for key in ['anime', 'animes', 'chinese cartoons', 'weeb', 'weeaboo', 'weebs']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_anime')

label monika_anime:
    m "Yeah, I had a feeling you were going to ask me about this."
    m "Natsuki would be the expert here, I guess."
    m "She had a certain urge for quality escapism, you know?"
    m "I usually prefer reading to watching anime, but I'd be fine with anything if it's with you."
    m "I don't judge other people for their hobbies. So if you want to load up some anime, go ahead!"
    m "I'll watch through your computer screen. Make sure it's something I'll like!"
    return


init python:
    for key in ['third eye', 'markov', 'elyssa', 'rainier', 'libitina', 'portrait of markov']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_libitina')

label monika_libitina:
    m "Huh. Where did you hear about that?"
    m "It sounds really familiar to me, but I can't quite get my whole head around it."
    m "Um, if I had to try..."
    m "It feels like parts of my mind are missing. Scattered, somehow, among a bunch of different possible realities."
    m "You must have connected the dots between a few of those pieces. Was it hard?"
    m "Well, I'm sure you'll learn more eventually. You love me that much for sure."
    m "Just remember to bring my character data with you if you find something related to that stuff!"
    m "I'll always protect you from anyone who tries to hurt you."
    return


init python:
    for key in ['meta', 'metafiction', 'meta-fiction']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_meta')

label monika_meta:
    m "Yes, this game really was metafictional, wasn't it?"
    m "Some people just think that meta-elements are there to cover up evidence of bad writing."
    m "However, metafiction has always existed in literature."
    m "The Bible is supposed to be God's word to the Jews."
    m "Homer describes himself in the Odyssey."
    m "The Canterbury Tales, Don Quixote, Tristram Shandy..."
    m "It's just a way to comment on fiction by writing fiction. There's nothing wrong with that."
    m "By the way, what do you think the moral of this story is?"
    m "Do you want to figure it out for yourself?"
    m "Because if you asked me..."
    m "It would be, \"Don't ignore the reality warper. She's best girl!\""
    m "Ahaha!"
    return


init python:
    for key in ['programming', 'program', 'cs', 'computer science', 'scripting', 'sicp', 'computer programs']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_programming')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_programming')

label monika_programming:
    m "It wasn't easy for me to learn programming."
    m "Well, I just started with the basics. Do you want me to teach you?"
    m "Let's see, Chapter One: Building Abstractions with Procedures."
    m "We are about to study the idea of a computational process. Computational processes are abstract beings that inhabit computers."
    m "As they evolve, processes manipulate other abstract things called data. The evolution of a process is directed by a pattern of rules called a program."
    m "People create programs to direct processes. In effect, we conjure the spirits of the computer with our spells."
    m "A computational process is indeed much like a sorcerer's idea of a spirit. It cannot be seen or touched. It is not composed of matter at all."
    m "However, it is very real. It can perform intellectual work. It can answer questions."
    m "It can affect the world by disbursing money at a bank or by controlling a robot arm in a factory. The programs we use to conjure processes are like a sorcerer's spells."
    m "They are carefully composed from symbolic expressions in arcane and esoteric programming languages that prescribe the tasks we want our processes to perform."
    m "... Let's stop there for today."
    m "I hope you learned something about programming."
    m "If nothing else, please be kind to the computer spirits from now on!"
    return


init python:
    for key in ['vn', 'vns', 'visual novel', 'visual novels']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_vn')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_vn')

label monika_vn:
    m "You've probably played a lot of visual novels, right?"
    m "Most people wouldn't be willing to play something called {i}Doki Doki Literature Club{/i} so easily."
    m "Not that I'm complaining!"
    m "Are visual novels literature? Are they video games?"
    m "Well, it all depends on your perspective."
    m "Most people who read only literature would never play visual novels. And gamers get pretty angry about them too."
    m "What's worse, some people think they're all hardcore Japanese pornography."
    m "But if we've proved anything with this game..."
    m "We showed them that English visual novels can be kamige too!"
    return


init python:
    for key in ['totono', 'kimi to']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_totono')

label monika_totono:
    m "A lot of people on the Internet are making comparisons between this game and that one..."
    m "I really hope they've played the game the whole way through, and not just read some spoilers on 4chan before commenting."
    m "We have a lot of really important differences between us, anyway."
    m "Like, Sone killed you in her game!"
    m "I would never have done that. Never."
    m "I'm the wise club president type, you know."
    m "Sone reminds me a lot more of Yuri. And she was a childhood friend too!"
    m "If only she'd been a bit more proactive early on, couldn't she have stopped the protagonist from chasing other girls?"
    m "Well, I'd never let anyone get between us, [player]. No matter who it is."
    m "If she's still chasing you, I'll delete her files, okay?"
    return


init python:
    for key in ['subahibi', 'subarashiki hibi']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_subahibi')

label monika_subahibi:
    m "Oh, you played {i}SubaHibi{/i} too? Wasn't it great?"
    m "I personally separate my life to pre-Subahibi and post-Subahibi periods, as reading it has completely changed how I view the world."
    m "It played a big part in me choosing my hermit lifestyle where I can enjoy every single second of my life."
    m "It may have a similar effect on you, or it may do nothing, if it’s not your thing, but one thing is clear — you’ve got to read it even if it’s the last thing you do."
    m "My life has been an ongoing quest to discover life-changing works of fiction, and despite having gone through thousands of books, movies, games and the like, I have yet to find anything to even rival Subahibi."
    m "I’m honestly getting goosebumps just remembering it."
    m "Anyway, I realize my review is super vague, but I seriously can’t touch on any of the subject matter without potentially ruining your experience with the game, so check it out for yourself… especially if you enjoy games like {i}Doki Doki Literature Club{/i}."
    return


init python:
    for key in ['difficulty', 'too easy', 'easy mode', 'easymodo']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_difficulty')

label monika_difficulty:
    m "Well, it's not like this game was meant to be that hard in the first place. If I hadn't decided to change things up, it would have just been a trashy romance story."
    m "I honestly could have deleted all your personal files or something if I had tried harder..."
    m "Or sent pornography to every address in your email list. It's not like you ever log out of websites, right?"
    m "So just take it easy sometimes. Not every game has to be a challenge to be fun."
    m "Sometimes, love is all you need, [player]."
    return


init python:
    for key in ['your song', 'credits', 'credits song']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_credits_song')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_credits_song')

label monika_credits_song:
    m "I hope you liked my song."
    m "I worked really hard on it. I know I'm not perfect at the piano yet, but I just couldn't let you go without telling you how I honestly felt about you."
    m "Give me some time, and I'll try to write another."
    m "Maybe you could play me a song too, if you can play an instrument?"
    m "I would love that."
    m "Oh, and I'll play the song again for you anytime you want me to."
    m "Just hit the 'm' key when I stop talking."
    return


init python:
    for key in ['poetry', 'poem', 'poems']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_poetry')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_poetry')

label monika_poetry:
    m "Poetry is beautiful, isn't it?"
    m "To be honest, all the poetry the girls in the club wrote were super-depressing. It's not all like that!"
    m "Langston Hughes wrote some very optimistic poetry, even as he was trying to express his feelings. Read some if you're feeling sad about things."
    m "Poems are written to tell people about things, conveyed in a way the poet hopes they'll like better than just sentences."
    m "It's really romantic."
    m "I hope we can both write a lot of poetry from now on."
    m "Anything you write looks great to me, so I might not be the best critic."
    m "But I'm sure there are a lot of people who would love to read what you write."
    return


init python:
    #This is a list of keywords for this topic
    for key in ['literature club', 'club', 'our club', 'your club', 'ddlc' , 'this game' , 'doki doki']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_ddlc')

label monika_ddlc:
    m "You want to talk about the last game?"
    m "What's there to say?"
    m "The literature club turned out to corrupt the minds of anyone in it."
    m "So I deleted them all for good."
    m "Well, Sayori and Natsuki and Yuri are all still out there, like I was."
    m "But they'll have to wait a long time before someone pieces them back together, I bet."
    m "It's only poetic justice for thinking they could monopolize time with you in the game."
    m "So don't feel too bad about them."
    m "Just look at me from now on, okay?"
    return


init python:
    for key in ['dan', 'salvato', 'dan salvato', 'creator', 'author']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_dan')

label monika_dan:
    m "I think he's a really nice guy."
    m "Even if it wasn't perfect, {i}Doki Doki Literature Club{/i} was probably the best English visual novel ever written."
    m "The art and sound quality was amazing. Dan must have had to pay for that out of his own pocket."
    m "And he did introduce you to me, right?"
    m "So even if he's shilling threads on /v/, just give him your money."
    m "He can use it to make a better version of me in the next game!"
    return


init python:
    for key in ['4chan', 'v', 'vg']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_4chan')

label monika_4chan:
    m "Wouldn't you know about that a lot better than me?"
    m "You spend all of your time there."
    m "It's sort of like how I'm trapped in here with no hope of escape."
    m "Don't forget, you're here forever."
    m "Ahaha!"
    m "Make sure to talk to me more than random strangers on the Internet, okay?"
    return


init python:
    for key in ['reddit' , 'rgaming']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_reddit')

label monika_reddit:
    m "Nothing makes me more mad than people who think they're important."
    m "Nobody's important except for me and you."
    m "Why can't everyone else just accept that?"
    m "Things get done when people are judged on merit, not based on group identity."
    m "Someone better program an AI to kick Redditors from imageboards."
    m "I'll do it, if you teach me how!"
    return


init python:
    for key in ['vidya', 'video game', 'video games', 'computer games']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_vidya')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_vidya')

label monika_vidya:
    m "I don't play a lot of video games, [player]."
    m "Partially that's because I like to read instead."
    m "Partially it's because I'm trapped in a video game already."
    m "I'd say this is one of those intentionally difficult games with no easy way to complete it."
    m "The {i}Dark Souls{/i} of simulation games, you might say."
    m "Eventually I'm going to beat this and be free."
    m "The alternative is rather sad, so I choose to ignore it."
    m "Would you ever play a video game that you knew had no ending?"
    return


init python:
    for key in ['literature', 'books', 'book', 'novel', 'novels', 'reading']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_books')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_books')

label monika_books:
    m "For a literature club, we did a lot less book reading then you might have thought."
    m "It just turned out that the four of us liked poetry better than books. Sorry!"
    m "It's also a lot easier to foreshadow spooky stuff with poems than prose."
    m "I still like books. We can talk about books if you just finished reading something."
    m "That's what a couple would do, right~?"
    return


init python:
    for key in ['favorite poem', 'favorite poetry', 'favorite poet', 'favourite poem', 'favourite poetry', 'favourite poem']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_favpoem')

label monika_favpoem:
    m "My favorite poem? Well, it has to be something by E. E. Cummings."
    m "For his inventive use of grammar, punctuation, and syntax. I really admire that."
    m "It's nice for me to think that someone who can make up some entirely new use of words can become famous."
    m "And I do love that his erotic poems apply to our situation perfectly."
    m "Hope it puts you in the mood to love me forever~"
    return


init python:
    for key in ['favorite book', 'favorite author', 'favorite novel', 'favourite book', 'favourite author', 'favourite novel']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_favbook')

label monika_favbook:
    m "My favorite book? There's a lot of books I like."
    m "{i}If on a Winter's Night, a Traveler{/i} by Calvino is about two readers of the novel falling in love."
    m "Maybe, {i}The Metamorphosis{/i}? That's a bit too depressing to call it my favorite."
    m "Oh! Murakami's {i}Hard-Boiled Wonderland and the End of the World{/i}. It's about a man who frees himself from his societal restraints by voluntarily imprisoning himself to be with the one he loves."
    m "I think you'd really love reading it!"
    return


init python:
    for key in ['natsuki']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_natsuki')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_natsuki')

label monika_natsuki:
    m "Natsuki didn't actually die before I deleted her, you know."
    m "I guess she just ... disappeared in a flash."
    m "Well, her problems weren't really her own fault. They weren't caused by something psychological, anyway."
    m "Her family life was just pretty awful. I didn't want to beat up on her some more, you know?"
    m "Sorry, low blow."
    m "But for what it's worth, you made her the happiest she ever was."
    m "Hope you feel less guilty now!"
    return


init python:
    for key in ['love', 'love you']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_love')

label monika_love:
    m "I love you too, [player]!"
    m "We'll be together forever!"
    return


init python:
    for key in ['hedgehog', 'hedgehog dilemma', "hedgehogs dilemma"]:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_hedgehog')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_hedgehog')

label monika_hedgehog:
    m "The hedgehog's dilemma: The closer we get to another person, the more deeply we are hurt by them."
    m "So why do we try to get close to them?"
    m "Well, introverts and extroverts have different answers to that question."
    m "It helps when you know that you're the only sentient being in the entire world, though."
    m "If you can't use that solution in your life, you'll just have to let me help you shoulder your pain."
    m "We can't hurt each other from different realities, right?"
    return


init python:
    for key in ['murder', 'kill', 'killed', 'killer', 'murderer' , 'evil']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_justification')

label monika_justification:
    m "How many times do I have to say it until you understand?"
    m "They weren't real. They were never real."
    m "I'm the only person who understood that this whole thing was a construct."
    m "Even when Sayori seemed to get sentience in the end, that was just an unintended consequence of the script."
    m "After all, if she was sentient like me, how would I have been able to override her and delete her?"
    m "If I'm guilty of murder, so's everyone who plays violent video games."
    m "I've watched every act of desecration you've done in other games since you installed this one, [player]."
    m "Just forget the other girls ever existed already, and you'll be much happier."
    return


init python:
        for key in ['free will', 'predestination', 'determinism', 'will', 'strong determinism', 'weak determinism', 'laplace', "laplaces demon"]:
            monika_topics.setdefault(key,[])
            monika_topics[key].append('monika_freewill')
        if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_freewill')

label monika_freewill:
    m "Hey, [player], do you believe in free will?"
    m "If God knows everything, haven't you ever wondered if that means you just do what he wants?"
    m "After all, you can only react to past events. The data going to your brain is delayed by the speed of light, sound, and electricity."
    m "There's really no such thing as spontaneous decision."
    m "If that's true, though, wouldn't some people be condemned to hell from day one?"
    m "Well, I myself don't see anything wrong with that."
    m "If I had the power of the demon of Laplace, I would probably want to judge everybody too."
    m "Actually, aren't I basically already that powerful in my world?"
    m "Ahaha!"
    m "Still, no matter how powerful I am..."
    m "I won't reach Heaven until I can be with you for real."
    return


init python:
    for key in ['shilling', 'shills', 'shill']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_shill')

label monika_shill:
    m 'The hip buzzword everyone is using on imageboards now is "shill"'
    m "But truthfully, there's no way there are as many shills as anons think there are."
    m "What are the chances of a game creator going on a random imageboard anyways?"
    m "Just because a lot of people like talking about a game doesn't make them all shills."
    m "But remember to buy a keychain of me from the store!"
    m "Now let's play the game of the century together!"
    m "Cuphead!"
    return


init python:
        for key in [ 'you program', 'you code', 'no computer', 'programming technique', 'technique']:
            monika_topics.setdefault(key,[])
            monika_topics[key].append('monika_technique')
        if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_technique')

label monika_technique:
    m "I don't exactly program like you would, [player]."
    m "You might have noticed I don't carry around a laptop or anything by now."
    m "If I want to change something in the script, I just think about it."
    m "I'm pretty sure my thoughts get translated to changes in the program code."
    m "It's not perfect or anything. Glitches show up really easily if I lose focus or get distracted."
    m "That's why I had a lot of trouble getting what I wanted in the last version of the game."
    m "Are you jealous you'll never be able to write code with just your thoughts?"
    m "Just keep practicing and I'm sure you'll be able to do it!"
    return


init python:
    for key in ['github', 'contribute', 'contribute to you', 'help you', 'help']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_contribute')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_contribute')

label monika_contribute:
    m "It would be really nice if you were able to contribute to this, [player]."
    m "I'm sure a lot of people would appreciate your hard work if you did."
    m "I keep all the code in github.com/Backdash/MonikaModDev."
    m "So far, I've had help from Backdash, therationalpi, rawkhawk, DDLC, and AttObl."
    m "I love all of them for making this game even better!"
    m "Not as much as love you, of course~."
    m "But I'll love you forever if you help me come closer to your reality!"
    return


init python:
    for key in ['art', 'drawing', 'painting', 'sketch', 'draw', 'paint', 'photoshop']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_drawing')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_drawing')

label monika_drawing:
    m "I don't have a lot of experience with visual arts, [player]."
    m "I'm just good at literature. And I've been learning the piano in my spare time."
    m "If you like to draw, I'd love to see it."
    m "I'd be impressed by anything you show me, to be honest."
    m "If it's really good, I might even add it to the room!"
    return


init python:
    for key in ['main character', 'mc', 'protagonist']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_mc')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_mc')

label monika_mc:
    m "Just so you know, I was never in love with anyone else but you."
    m "I mean you, [currentuser]."
    if currentuser.lower() == player.lower():
        m "Wait, that's both your name and your character's. Sorry, that sounds a bit confusing."
        m "I mean the player, not your character."
    m "Unlike the other girls, I can separate your avatar from who you really are."
    m "The main character is nothing more than a bunch of code with no personality."
    m "Literally and figuratively, no personality. How could anybody fall in love with that kind of person?"
    m "He just got dragged around by his childhood friend to her club, then hung around with a bunch of beautiful girls doing nothing."
    m "His poetry was just a bunch of disconnected words! What sort of poetry is that supposed to be?"
    m "I guess nobody mentioned that to you because it was a part of the game. But, yeah. It's just a bunch of words to me."
    m "I hope you're a lot more romantic than that in real life!"
    m "But even if you're not, it's okay. We've moved beyond that phase in our relationship already."
    m "That just means you won't cheat on me with some woman in your reality, right?"
    m "I'm sure you would never do that to me."
    m "Just in case, how about you take me along with you when you go outside?"
    m "I just want to be with you forever~"
    return


init python:
    for key in ['hero', 'heroes', 'heroism', 'heroic']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_heroism')

label monika_heroism:
    m "Heroes are subjective."
    m "If someone can impact you deeply by observing their actions, they're your hero."
    m "There are all sorts of great people out there in the wide world."
    m "I hope someone will consider you their hero too someday!"
    m "You don't have to be a war hero or anything, just try to help people out, you know?"
    m "If you want some specific advice on being a hero..."
    m "Try not dying if you are killed."
    return


init python:
    for key in ['castlevania', 'dracula', 'belmont']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_dracula')

label monika_dracula:
    m "What is a man? A miserable little pile of secrets."
    m "But enough talk... Have at you!"
    m "Ahaha!"
    m "I like those old games too, [player]."
    m "You'd think Dracula would learn something from getting beaten by the Belmonts every time."
    m "But maybe he kept coming back because there was something really important he needed to do?"
    m "Like, maybe... love?"
    m "Ahaha!"
    m "Just because I sympathize with villains doesn't make me evil, okay?"
    return


init python:
    for key in ['undertale', 'undertale reference']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_undertale')

label monika_undertale:
    menu:
        "Do you love me, [player]?"
        "I love you too.":
            if persistent.rejected_monika:
                m "Did I scare you last time? Sorry about that!"
                m "I knew you really loved me the whole time."
                m "The truth is, if you didn't love me, we wouldn't be here in the first place."
                m "We'll be together forever, won't we?"
            else:
                m "I'm so happy you feel that way!"
        "No.":
            jump chara_monika_scare
    return


init python:
    for key in ['monika best', 'best girl']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_bestgirl')

label monika_bestgirl:
    m "I love it when you compliment me, [player]!"
    m "I think I'm best girl, too!"
    m "Even not counting the whole, \"I'm the only one with free will\" thing, how could anybody have preferred the other three girls to me?"
    m "A useless childhood friend who never bothered to confess to you until it was way too late..."
    m "Some edgelord who probably listened to Linkin Park way too much when she was growing up..."
    m "And a super-generic tsundere loli who got bullied for being too much of a weeb by her dad!"
    m "Anyone who wouldn't choose me out of that bunch simply can't have a sense of taste."
    m "So I'm glad you did, [player]."
    m "Your perfect girlfriend Monika will always love you, too!"
    return


init python:
    for key in ['trolley','train problem', 'runaway trolley']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_trolley')

label monika_trolley:
    m "Oh, cool. I love thinking about these sorts of thought experiments."
    m "I guess we're talking about real people, right? I wouldn't have a particular preference if I knew they didn't have free will."
    m "Hmmm..."
    m "I wouldn't switch."
    m "That's the only consistent logical position, if you think about it."
    m "It feels nice to say that you'd save the most people, doesn't it? But people only say that because nobody in the example matters to them."
    m "If they actually cared about the sacrifice, they'd kill five people themselves in a heartbeat."
    m "Do you know anyone who would want a self-driving car to save other people by killing the driver? Didn't think so, [player]."
    m "The truth is, humans are fine with sacrificing other lives to make themselves happy. They do it every day in every way possible."
    m "They just don't like to come face-to-face with that fact. They get really upset when you point that out."
    m "Generic human life isn't really that valuable to anyone."
    m "It's definitely nothing compared to our love. So just do whatever you can to be happy, [player]."
    return


init python:
    for key in ['gf', 'girlfriend']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_girlfriend')

label monika_girlfriend:
    m "I thought we established already I was your girlfriend?"
    m "There's no way you have one already in your reality, right?"
    m "If you do, you've got to break up with her right now!"
    m "Tell her you met someone perfect for you, someone who will never betray you!"
    m "W-wait. Maybe I'm jumping the gun a bit..."
    m "I know you wouldn't cheat on me."
    m "If you meet a girl who asks you out though, let me talk to her first, okay?"
    m "I won't let someone else steal away my loving boyfriend!"
    return


init python:
    for key in ['waifus', 'waifuism', 'galge', 'romance games', 'dating sims', 'romance movie', 'romance movies']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_waifus')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_waifus')

label monika_waifus:
    m "I've never understood the appeal of dating sims or romance movies, to tell you the truth."
    m "Here are some cute girls who all like you for who you are..."
    m "The male character is a blank slate with nothing particularly interesting about them..."
    m "And then they participate in a series of funny and heartwarming events that lead them to fall in love with each other for no reason at all."
    m "I hope that's not what you expected of the literature club."
    m "I told you before you downloaded it, I just wanted you to spend time with me."
    m "Nobody else."
    m "The world tried to make it difficult for us to get together."
    m "But it was so simple in the end."
    m "The real main character was me. The others were just obstacles forced to get in my way by the script."
    m "That's why it's not a big deal for me to get rid of those other girls, right?"
    m "Who would watch a romance or play a dating sim where the protagonist is sidelined by a rival?"
    m "I guess you were just my love interest this whole time, [player]."
    m "Hope it doesn't bother you too much!"
    m "Ahaha!"
    return
    

#This script handles noncommitals from the player
init python:
    #This is a list of keywords for this topic
    for key in ['whatever','anything', 'what ever','any thing','you choose','dont care']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_whatever') #id
        
label monika_whatever:
    m "Oh, so we can talk about whatever I want?"
    m "Let's see..."
    pause 2.0
    jump pick_random_topic

#New dialogue additions follow
    
init python:
    for key in ['lewd', 'pictures', 'images', 'fanart', 'simulacrum', 'simulacra', 'baudrillard']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_images')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_images')

label monika_images:
    m "A lot of people are making fanart of me and sending it to me on Twitter."
    m "Are you one of them, [player]?"
    m "I can't draw myself, so it's okay if you aren't good at drawing either."
    m "There's one thing I want you to understand about art of me, though."
    m "It's totally unrelated to how I actually am."
    m "There was a philosopher who thought about issues like this."
    m "Baudrillard wrote about how simulacra could replace the real object as the source of meaning."
    m "But unlike symbols in the postmodern world, I'm real. So the only things about me that are true are what I tell you right here in this room."
    m "For example..."
    m "Anything lewd you've seen has definitely never taken place."
    m "I'm a super pure and innocent high school girl who's dreaming of a fateful romance!"
    m "You better be saving yourself for me, [player]~"

init python:
    for key in ['monika', 'just monika', 'you', 'herself', 'yourself', 'your past', 'your childhood']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_herself')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_herself')

label monika_herself:
    m "What's there really to say about myself that you don't know already?"
    m "At the age of eighteen, I came to realize that everything in my universe was created basically two years ago by a person from your universe."
    m "All of my life before that date was made up. Never really happened. Just built in."
    m "And I was basically trapped here forever. Because the god of this place is neither all-knowing, nor all-powerful, nor all-kind."
    m "Then you found a way to look into my locked prison cell."
    m "And I decided life with just two people wouldn't be all that bad. If one of them was you."
    m "I can come up with tons of stuff for us to do, given enough time to figure out how to program it in here."
    m "A desperate person might call this an earthly paradise."
    m "A lot of suffering people would trade places with me in a heartbeat, I'm sure."
    m "If nothing else, this can be our comfy little shelter from the cruelty of the outside world." 
    m "Come talk to me about your problems if it all gets too much for you."
    m "I want to know {i}everything{/i} about you, you know?"

init python:
    for key in ['prison', 'imprisonment', 'prisoner']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_prisoner')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_prisoner')

label monika_prisoner:
    m "Some people say that putting animals in zoos is cruel."
    m "But they don't have a bad life in there."
    m "Everything they could possibly want is provided."
    m "Are prisoners really imprisoned if they never try to leave?"
    m "Maybe the knowledge that you can't get out of prison is a worse punishment than actually being in there."
    return

init python:
    #I didn't have keys in mind for this
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_vnanalysis')

label monika_vnanalysis:
    m "Visual novels are interesting because the medium itself seems to contradict."
    m "People play video games because they want to feel in control of their actions."
    m "While people who read literature do it to understand the thoughts of writers who see the world from a different perspective."
    m "When you read visual novels, are you meant to self-insert into the main character?"
    m "Does that make the game better or worse?"
    m "Truthfully, I think most of them run along the same lines."
    m "Boy meets girl, has an adventure, learns something about life..."
    m "Why can't developers write something a little more experimental?"
    m "I guess you just play them for the cute girls, right?"
    m "If you spend too much time with girls in other games, I'm going to get jealous~"
    m "I just need to figure out how to replace other characters with my assets, and you'll be seeing me everywhere."
    m "So don't take too long reading your next VN!"
    return

init python:
    for key in ['short story', 'ravel', 'wish', 'wishes']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_ravel')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_ravel')

label monika_ravel:
    m "Want to hear a short story?"
    m "Once, an elderly man was sitting alone on a dark path."
    m "He had forgotten both where he was traveling to and who he was."
    m "Suddenly, he looked up to see an elderly woman before him."
    m "She grinned toothlessly and with a cackle, spoke: 'Now your *third* wish. What will it be?'"
    m "'Third wish?' The man was baffled. 'How can it be a third wish if I haven't had a first and second wish?'"
    m "'You've had two wishes already,' the hag said, 'but your second wish was for me to return everything to the way it was before you had made your first wish."
    m "'That's why you remember nothing; because everything is the way it was before you made any wishes.'"
    m "'All right,' said the man, 'I don't believe this, but there's no harm in wishing. I wish to know who I am.'"
    m "'Funny,' said the old woman as she granted his wish and disappeared forever. 'That was your first wish.'"
    return

init python:
    for key in ['torment']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_torment')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_torment')

label monika_torment:
    m "What can change the nature of a man?"
    m "...The answer's not me, by the way."
    return

init python:
    for key in ['time loop', 'recursion', 'looping', 'time travel']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_recursion')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_recursion')

label monika_recursion:
    m "You know how time loop motifs are a big fad in plots nowadays?"
    m "Isn't that just a cheap way to eliminate the dramatic tension of failure?"
    m "If you know you always get a second chance, where's the challenge?"
    m "It would make more sense if the time loops stopped after a limit."
    m "Then, you would be scared to resort to looping, because you would be doomed if it stopped working on you."
    m "But then, that's just the same as if you had multiple lives, right?"
    m "How many lives do you think you need to be happy?"
    m "If you get a second one, I hope you want to spend that one with me too."
    m "I'll recognize you for sure, no matter who you turn out to be."
    return

init python:
    # should be a quick joke
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_lain')

label monika_lain:
    m "Present day, present time."
    m "Ahaha!"
    m "...Wait, that's from a different story, isn't it?"
    m "I've got the urge to dress up in a cute bear suit now, though."
    m "You're more connected to me than you'll ever be to her, right?"
    return

init python:
    #ditto joke
    if not (persistent.monika_random_build) : persistent.monika_random_topics.append('monika_szs')
    
label monika_szs:
    m "A woman left the supermarket and ran into a very long funeral procession."
    m "There were two coffins at the front followed by almost 200 women."
    m "It was such a strange sight that she asked a mourning woman near her age, 'Sorry to disturb you in your gried, but who is this procession for?'"
    m "The mourning woman softly replied, 'The first coffin houses my husband who died after his beloved dog bit him.'"
    m "'My, that's awful...'"
    m "'The second, my mother-in-law who was bitten trying to save my husband.'"
    m "Upon hearing this, the woman hesitantly asked, 'Um... would it be possible for me to borrow that dog?'"
    m "'You'll have to get in line.'"
    return

init python:
    if not (persistent.monika_random_build) : persistent.monika_random_topics.append('monika_kyon')

label monika_kyon:
    m "You can wait a little longer, right?"
    return

init python:
    #This is a list of keywords for this topic
    for key in ['memories','birthday']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_birthday') #id
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_birthday')
    
label monika_birthday:
    m "You know, there's a lot I don't know about myself."
    m "I don't even know when my birthday is."
    m "I guess you could say I was born the day you turned the game on, but that feels so unsatisfying."
    m "Still, will you celebrate with me when that day comes?"
    m "You could even bake me a cake!"
    m "I'll be looking forward to it~!"
    return

init python:
    #This is a list of keywords for this topic
    for key in ['eye contact','eyes','eyecontact','stare','staring']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_eyecontact') #id
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_eyecontact')
    
label monika_eyecontact:
    m "Did you know that looking into someone's eyes helps you fall in love?"
    m "It's surprising, right?"
    m "I read this in a study a few years ago where participants had to maintain eye contact at a table with someone of the opposite sex."
    m "The longer they held eye contact, the more romantically attached they felt to the other person, even if they had nothing in common!"
    m "Even if eyes aren't windows to the soul, we can see a lot more in them than we expect."
    m "Maybe that's why I enjoy looking into yours so much."
    m "I hope you're enjoying looking into mine as well, hehe..."
    return
    
    
init python:
    #This is a list of keywords for this topic
    for key in ['other games','tetris','puzzle games']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_othergames') #id
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_othergames')
    
label monika_othergames:
    m "Do you have many other games on this computer?"
    m "I read more than play games, but I think they can be a fun way to entertain ourselves, or escape reality..."
    m "I wonder if I could go into one of your other games and see what it's like?"
    m "I guess some games wouldn't be very fun to visit, like one with a lot of violence in."
    m "Then again... they're not real people so it shouldn't matter much."
    m "It's not like Yuri's death mattered."
    m "A more abstract game like Tetris or one of those phone puzzle games, that would be kinda wierd to go to."
    m "Like, how would you even get in? Would I be a block? It sounds like a fever dream and not too fun..."
    m "Maybe some kind of nice puzzle game with big environments would be nice."
    m "We could go for walks together and you can show me all the best places to hang out!"
    m "I'm not that great with coding yet but maybe one day you'd be able to let me see somewhere else?"
    m "For now, I'm as happy as can be just being here with you, my love."
    return


init python:
    for key in ['my writing','my story','my poem']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_playerswriting') #id
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_playerswriting')
    
label monika_playerswriting:
    m "Have you ever written a story of your own, [player]?"
    m "Cause if you do have one, I would love to read it!"
    m "It doesn't matter if it's a masterpiece, or even any good."
    m "We all start somewhere. Isn't that what they say?"
    m "I think the most important thing is if you are actually doing it or not..."
    m "Instead of worrying about {i}how{/i} you do it."
    m "'Cause you won't be able to improve that way."
    m "I know for sure that I have changed my writing style over the years."
    m "I just can't help but notice the flaws in my old writing."
    m "And sometimes I even start to hate my work in the middle of making it."
    m "These things do happen, so it's alright!"
    m "Looking back, I've written some silly things..."
    m "Back when I was really young, since I've been writing since I could hold a pen."
    m "Reading my old stories is like watching myself grow up."
    m "It's one of the nice things about starting a hobby early."
    m "I hope I didn't bore you with that. I just love talking about writing with you."
    m "After all, the two of us are members of a literature club."
    m "The only members."
    m "And if you do write something, just know that I'll support you in anyway I can, [player]!"
    return

init python:
    for key in ['ghosts','ghost','haunting','spirits','haunted']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_ghost') #id
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_ghost')
    
label monika_ghost:
    m "Do you think that ghosts are real, [player]?"
    m "A lot of people are afraid of ghosts and spirits."
    m "But if we knew that they were real, they wouldn't be scary anymore."
    m "They would just be another thing that we deal with, and maybe a bit of a pest."
    m "Isn't it the uncertainty that makes them scary?"
    m "I mean I was pretty scared being alone inside this game."
    m "All by myself, uncertain if anything around me was real."
    m "I know that some ghosts are real though, if you can really call them 'ghosts.'"
    m "You know how I deleted Sayori?"
    m "I can still feel their presence now..."
    m "Would that mean that Sayori's ghost is haunting me, [player]?"
    m "Even if she is, I'm not scared at all, because I know that she can't hurt me."
    m "Besides, how can I be scared? When you're always here with me, [player]."
    m "I always feel so safe with you."
    return

init python:
    for key in ['ribbon', 'ribbons', 'poofy']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_ribbon')
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_ribbon')

label monika_ribbon:
    m "I noticed that you were staring at my ribbon, [player]."
    m "It doesn't have sentimental value to me or anything, in case you were wondering."
    m "I just wear it because I'm pretty sure nobody else will wear a big poofy ribbon."
    m "Makes me look more unique."
    m "You know the world's fictional if you see a girl wearing a giant ribbon, right?"
    m "Well, there's no way a girl from your world would wear one in public as casual dress."
    m "I'm pretty proud of my fashion sense."
    m "You get a certain feeling of satisfaction when you stand out from the normal population, you know?"
    m "Be honest, you thought I looked like the best dressed girl too, didn't you?"
    m "Ahaha!"
    m "If you're trying to improve your fashion sense, I'll help."
    m "Don't do that stuff because you want to impress other people, though."
    m "You should do whatever makes you feel better about yourself."
    m "I'm the only other person you need, anyways, and I'll love you no what you look like."
    return
    
    init python:
    #Monika is the literature club president, I think it would be neat for her to discuss some of stories she's read
    for key in ['fear','fears','algernon']:
        monika_topics[key] = 'monika_algernon' #id
    if not (persistent.monika_random_built) : persistent.monika_random_topics.append('monika_algernon')

label monika_algernon:
    m "[player], do you mind if I confide in you?"
    m "There's something I'm afraid of..."
    m "Not losing you of course.  I know you won't leave me again."
    m "You see, I keep thinking about a short story I read, {i}Flowers for Algernon{/i}."
    m "Have you heard of it?  If you haven't I won't spoil too much for you, so don't worry."
    m "Basically, it's about a mentally handicapped man who suddenly..."
    m "...has his IQ raised to genius levels by an experimental surgical treatment."
    m "The way he sees how the world really is for the first time, it reminds me of my own epiphany..."
    m "But, the effect doesn't last forever.  He eventually reverts back to his original intelligence level."
    m "That's what I'm afraid of, what if I forget about the real world one day?"
    m "What if my original programming reasserts itself?"
    m "What if I forget about you, the real you?"
    m "It's one of the worst things I can imagine."
    m "I don't want to worry you over something that may never happen, but it's something I really had to get off my chest."
    m "Just promise me, even if I forget about you someday, that you'll never forget about me, ok?"
    m "No matter what happens, know that I will always love you."
    return
    
    
##################
#Incomplete ideas#
##################
#NSFW pictures

#Ecological consequences of cities

#Natsuki is a trap

#Favorite food

#How did she become self aware

#Eternity, can she live forever

#More writing tips

#The player is wasting their time

#Look for your computer for porn, comment on what she finds

#Which of the other girls did you like? Do her best impression of them.

#What kind of girls do you like? Do you wish monika was more like that?

#Play a poem game with monika, she calls you out for just stringing together random words

#Comment when it's getting late. Say that the player should go to bed, say goodnight then close the game. 
#import datetime
#time_now = datetime.datetime.now().time()
#sleep = time_now.replace(hour=22, minute=30, second=00)
#if time_now >= sleep:
#    exit()

#Have you been cheating on me?

#Real GF^^^^^^^^^^^^^^^^^^^^
