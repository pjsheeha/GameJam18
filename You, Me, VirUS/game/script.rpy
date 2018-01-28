# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character("InFLUencer", color="#a575b2")
define w = Character("Warren", color="#d35d45")
define a = Character("Alexei", color="#5693ce")
define h = Character("Prince(ess) Honey Bear", color="#b85826")
define b = Character("Random Barista", color="#fffdc1")

default honey_end = True
default warren_end = True
default alexei_end = True

default date_finished = False

define end_count = 0

# The game starts here.

# label splashscreen:
    # scene bg splash
    # with fade

# label before_main_menu:
#     ""

label start:

    scene bg instagram popular
    with fade

    show virus angry at left
    with dissolve

    i "I can't believe that the Common Cold has overtaken me on Instagerm. They probably bought half of their infection vectors."
    i "They'd infect anybody...such low standards!"

    scene bg instagram flu
    show virus angry at left
    i "I mean, they aren't even seasonal like I am! I'm the flu! This is MY season"
    i "I can't let this happen, I need to do something!"

    menu What_to_do:
        "Do something about it":
            jump do_something

        "Do nothing about it":
            show virus neutral at left
            with dissolve
            i "yeah...I dont know what I would even do, though. Who really cares about instagerm anyway?"
            scene bg worst end
            pause
            return
        
label do_something:
    show virus happy at left
    with dissolve

    i "I know! The flu season is almost over, but there's still time."
    i "I mean, if there's people open for a cold, there's DEFINITELY people open for me."
    i "I'll make this the worst flu season of all time. I know just how to do it too!"

    scene bg infecter main
    with fade

    i "I'll infect a socialite! Someone who gets in contact with a lot of people who can do my dirty work. It's perfect! I can make history and not even have to change my IG posting schedule."
    
    menu infecter_date:
        "swipe right":
            scene bg infecter match
            i "They're perfect! And Nearby! I'll set up a date with them for this weekend and from there it'll be history!"

        "rethink plan":
            show virus sad
            i "now that I think on it...maybe this is a dumb plan"
            scene bg worst end
            pause
            return

label Warren_date:
    "You match with your city's resident wild party-planner, a typical super-posh, wealthy, play-boy with ties to all the elite in the area."
    "Infecting him means your strain will find its way to all the well-traveled high class in the area. From there you can hope it trickles down the social ladder."
    "His party lifestyle has done a number on his immune system, making him easy to infect. But can you get close enough? Party planners cant afford to get sick, you know!"

    scene bg restaurant
    show virus neutral at left
    show warren neutral at right
    with fade 

    w "I hope this isn't too much for you. I thought it'd be best to chose a more toned down locale for our initial meet."
    w "It may still be more than you're used to, though."

    menu:
        "Be rude back":
            show virus surprised at left
            i "I'm surprised you chose such a pedestrian type place."
            show virus neutral
            show warren surprised at right
            w "pedestrian?!"
        "Be polite":
            show virus neutral at left
            i "It's fine..."
        "Be excited":
            show virus happy at left
            i "The restaurant is lovely! I think its just right for us. No prying eyes."
        
    show warren neutral
    show virus neutral
    w "Whatever. Just let me know if you need any help understanding anything on the menu."

    i "How sweet"

    show virus happy at left
    w "Yeah. Anyway, I've been planning a party for this upcoming weekend. It's going to be the biggest party of the century and people will be flying from all over just to try to be near it. I could get you in guarenteed."
    w "want to come?"

    menu:
        "Accept invitation rudely":
            show virus angry at left
            show warren surprised at right
            i "I GUESS I can be free if I need to be"

        "Accept invitation happily":
            show virus happy at left
            i "I'd love to!"

    hide virus
    show warren shocked at right
    show honey happy

    h "Oh. My. Bio!"
    h "Is that InFLUencer?! From Instagerm?! Is it really YOU?!"

    show warren angry

    menu:
        "ew another fan?":
            hide warren 
            show virus angry at left
            show honey surprised at right
            i "What's it to ya?"
        "omg! a fan?!":
            hide warren 
            show virus happy at left
            show honey happy at right
            "Yeah, are you a fan? It's always nice to meet new people!"
    
    show honey happy at right
    h "I'm a huge fan! I can't believe I'm meeting you, I've been following you in IG since your big trip to the UK in 2011!"

    menu:
        "neutral":
            show virus happy at left
            i "I'm glad to be meeting you."
            jump honey_neutral_1

        "rude":
            show virus angry at left
            show honey surprised at right
            i "Okay. Did you need something?"
            jump honey_rude_1

        "polite":
            show virus neutral at left
            show honey neutral at right
            i "Thank you! I'm on a date right now, though, and want to focus on that."
            jump honey_polite_1

    label honey_neutral_1:
        show honey happy at right
        h "You've got to go check out this museum with me! It's huge right now and my family is donating a bunch of art so we could have to whole place to hang out!"
        menu:
            "Sure!":
                i "Yeah! That would be great! Im bored anyway."
                jump date_end
            "Too busy":
                show honey sad at right
                i "No, I'm busy today."

    label honey_rude_1:
        show honey sad at right
        h "Nothing really, I guess. I'll leave you guys alone."
        $ honey_end = False
        jump honey_leaves

    label honey_polite_1:
        show honey surprised at right
        h "Oh! You're on a date! I was so excited I didn't notice!"
        show honey sad at right
        h "I'm so sorry for interrupting"
        show honey neutral at right
        h "Could we possibly talk after your date?"
        menu:
            "Sure!":
                show virus happy at left
                i "Yeah! That would be great! I'll talk to you then."
                $ date_finished = True
                jump honey_leaves
            "Too busy":
                i "No, I'm busy today."
                show honey sad at right
                h "oh...I understand. I'll leave you guys alone."
                $ honey_end = False
                jump honey_leaves

    label honey_leaves:
        hide honey
        show warren neutral at right
        show virus neutral left

        w "wow I didn't realize you were so popular. You must be pretty famous! I didn't expect that."

        menu:
            "Yeah, you know, just a day in the life!":
                show virus blushing
                i "Yeah, you know, just a day in the life!"
            "I try not to BRAG about it, you know.":
                show virus blushing
                i "I try not to BRAG about it, you know. But I'm up there with the Common Cold and Strep Throat!"
            "It's no big deal.":
                i "It's no big deal."            
                show virus blushing

        w "Listen, I've had a great time. Let's hang out again. I'm pretty busy right now but we can spend some time together at my party. I'll see you there right?"

        menu:
            "maybe":
                i "maybe"
            "yes":
                i "yes"
            "no":
                i "no"

        show warren happy at right
        w "alright. Later!"
        jump date_end
    
    label date_end:
        if honey_end:
            hide warren
            hide honey
            show virus happy at left
            i "Bye Warren! Let's go, Honey!"

            if date_finished:
                hide virus
                show honey happy
                h "So, Influ! Is it alright if I call you Influ?"
                h "Anyway, what do you say to going to this museum with me? It'll be a great time!"
                i "sure...why not!"

            hide honey
            hide virus 
            scene bg black

            "On your inpromptu date, you find out some interesting things. Honey is a prince(ess)! To be specific, they are 5th in line for the throne in Tonga! If you infect them you're going international!!"
            "As a royal diplomat and carefree party-boy Honey comes in contact with all sorts of people all over the globe!"
            "Even betterm despite having a good immune system, Honey doesn't know any better about being wary around you. It's like no one taught him the basics of flu season!
            transmitting your strain to him would be a peice of cake!"

            jump morning_street

label morning_street:
    scene bg street
    show virus neutral
    with fade

    i "What a great morning. I don't have much at all planned for my day but should try to stay out so I don't waste this good weather. Who knows, maybe I'll the next greatest disease vector today!"
    show virus angry
    i "I cant seem to properly wake up, though. How will I ever Infect the whole West Coast if I can't even stay awake!?"
    show virus happy
    i "Oh! I'll head to Mitochondria! My favorite coffee shop always has something to power my cell."

label Coffee_shop:
    scene bg cafe
    show virus angry
    with fade

    i "I forgot how long it takes them to make my favorite drink sometimes. This sucks"
    b "One Grande, Iced, Sugar-Free, Vanilla Latte with Soy Milk and nutmeg at 120 Degrees!"
    show virus happy
    i "Finally! Now I can sit and enjoy my morning properly!"
    show virus angry
    i "Or at least I could if this gracile grassroots guy would stop whatever hes doing. People are paying him too much attention!"

    hide virus
    show alexei happy
    a "Everyone understands the extraordinary hardships that are placed on the uninsured, who live every day just one accident or illness away from bankruptcy. These are not primarily people on welfare. Some can’t get insurance on the jobs they have! I have a plan for us, that WILL work! It's simple, really..."

    hide alexei 
    show virus angry
    i "Oh. My. Bio. He's actually on to something! This isn't good. If he goes on like this I might die."
    show virus surprised
    i "If he actually does this all of virus kind might die! I'll be finished!"
    show virus angry
    i "I need to step in!"

    hide virus
    show alexei happy at right
    a "...This is especially true now in Flu season! Vaccines are essential! That’s why under my plan..."
    menu:
        "Cut in rudely":
            show alexei angry at right
            "Oy! Cut it out! Don't talk that vaccine stuff out here! Are you trying to ruin everyone's lives?! Everyone knows the best way to fight off any sort of sickness is to turn your a/c on high and binge eat Coldrock ice-cream!"
        "Take him aside kindly":
            "Hey! I couldn't help but overhear you. Would you mind sitting with me for a bit? Just to chat. You seem so friendly and sociable! So handsome! I bet you have a GREAT immune system too."
    show alexei happy at right
    a "I'm always glad to meet one of my constituents. What can I do for you?"

    "Now that youve had a chance to look at him, you recognize Alexei as on of the most prominent up-and-coming politicians! Jackpot! Just from the look of him, you can tell hell be a perfect carrier for your strain, too!"
    "A guy like him would go weeks symptomless, all the while infecting everyone he visits on all his trips! Perfect!"

    menu:
        "How do you react?"
        "Force him to party":
            show alexei angry at right
            i "First of all, you can chill the heck out. You're way too uptight. I think i've got the best solution, though"
            show alexei neutral at right
            i "Come to this party with me this weekend. It going to be the biggest of the century!"
            show alexei worried at right
            a "I couldn't possibly go! There's so much work to be done!"
            show alexei angry at right
            show alexei neutral at right
            i "Forget work, you're going. Thats final."
        "Coerce him to party":
            "You seem like a first class workaholic. When's the last time you took a break?"
            show alexei worried at right
            a "Now that you mention it...i'm not sure."
            show alexei neutral at right
            a "Maybe it's been too long"
            i "It definitely has. Youre going with me to this party this weekend and im going to teach you about taking some \"me time\""
            show alexei sad at right
            a "I dont know..."
            i "Of course you don't. Learn to take a risk or two! You're coming!"
            show alexei happy at right
            a "I guess I can't afford to disappoint my constituents. I'll go."


label party:
    scene bg party
    with fade

    label the_choice:
        hide warren
        hide honey
        hide alexei
        scene bg party
        show virus neutral at left
        menu:
            "You are at the party now and need to decide who to go to. Who will you transmit your strain to? Who's the perfect vector for you?!"
            "Warren, the pretty-boy party planner" if warren_end:
                if end_count == 1:
                    $ end_count+=1
                jump party_planner
            "Alexei, the white-hot witty workaholic" if alexei_end:
                if end_count == 2:
                    $ end_count+=1
                jump white_hot_workaholic
            "Honey Bear, the real party royalty" if honey_end:
                $ end_count = 1
                jump party_royalty
            "Leave party" if not honey_end and not warren_end and not alexei_end:
                jump bad_ending
    
    label party_royalty:
        show honey drunk sad at right
        show virus neutral at left

        h "Oh. My. Bio! InFLU I don't know what to do. My family is horrid.
        They've cut me off! I have nothing now!"

        menu:
            "That's not true! You have me!":
                show honey drunk neutral at right
                h "Nononononoono wait wait wait. I lied. I have you, InFLU! You're so nice to me and kind. You're so REAL. Like really, real!"
            "I'm so sorry! Is there anything I can do to help?":
                show honey drunk neutral at right
                h "Nononononoono wait wait wait. I lied. I have you, InFLU! You're so nice to me and kind!"
        menu:
            "stay and infect him":
                i "Awww you're so sweet...."
                jump honey_kiss
            "leave and save him":
                i "Yeah no. I can't do this to this poor guy."
                $ honey_end = False
                jump the_choice

    label party_planner:
        scene bg party
        hide alexei
        hide honey
        show warren happy at right
        show virus happy at left

        w "Hey you made it! So, what do you think big-shot?"
        menu:
            "I mean, its ALRIGHT, I guess...":
                w "It's great, I know!"
            "I love it!":
                w "It's great, I know!"
            "It sucks (leave)":
                $ warren_end = False
                jump the_choice
        menu:
            "stay and infect him":
                i "I need to talk to you about something"
                w "Yeah, sure. What's up?"
                i "I feel like I can be so close to you and real with you. You're so fun."
                w "I feel the same. Being around you is like the best party."
                i "I have a party favor for you..."
                show warren surprised at right
                w "I love those. What is it?"
                i "This..."
                jump warren_kiss
            "leave and save him":
                show warren sad at right
                i "You know what? Nevermind, I can't do this"
                $ warren_end = False
                jump the_choice

    label white_hot_workaholic:
        hide warren
        hide honey
        scene bg party
        show alexei drunk happy at right
        show virus happy at left

        a "Heyyy! I've been looking everywhere for yoouuuu!"
        show virus neutral at left
        i "Wait...Alexei..."
        show virus surprised at left
        i "Are you drunk?!"
        show virus neutral at left
        a "I just had a few drinks, ya know? There was a bunch of people who just kept giving them and it was so much fun and they really like my policies! This crowd is sooooo in touch!"
        show alexei drunk shy
        a "You, know..."
        a "I never saw myself being able to do stuff like this. I don't think I could ever really have fun like this with anyone else."
        show alexei drunk happy
        a "You've really changed me and opened me up to trying new things. I was open minded before but not open enough to live a little wild like this."

        menu:
            "ruin the mood":
                show virus angry at left
                i "What is this? A soliloquy?"
                show alexei drunk sad
                a "Oh... I guess ill just stop then"
                $ alexei_end = False
                jump the_choice

            "be happy about it":
                show virus happy at left
                i "I'm so glad you're being so honest with me. So open."
                show virus blushing at left
                show alexei drunk shy at right
                a "There's something special here between us. When I first got
                    into politics, it was because there was no one helping people
                    like me or the people around me. I wanted to help. The more I
                    worked the more I was able to help and the more I wanted to do.
                    I couldn't and can't afford breaks."
                a "I work hard to not get
                    sick so I can be there for the people at every moment. I've
                    spent all my time working to help people and improve lives. I never
                    thought I'd meet someone like you...who would improve my life."
                
                menu:
                    "infect him":
                        "Alexei..."
                        jump alexei_kiss
                    "save him":
                        show alexei drunk sad at right
                        i "I'm so sorry, Alexei. I can't do this to you. Not after everything!"
                        jump sad_ending

    label honey_kiss:
        h "I don't know what I'd do without you InFlu. Come here!"
        hide honey
        hide flu
        scene end honey
        with fade
        pause
        if warren_end:
            $ end_count = 2
            jump party_planner
        elif alexei_end:
            jump white_hot_workaholic
        else:
            jump ok_ending

    label warren_kiss:
        scene end warren
        with fade
        hide warren
        hide flu
        pause
        if alexei_end:
            if honey_end:
                $ end_count = 3
            jump white_hot_workaholic
        else:
            jump ok_ending

    label alexei_kiss:
        hide alexei
        hide flu
        scene end alexei
        with fade
        pause
        if end_count == 3:
            jump best_end
        else:
            jump ok_ending

    label ok_ending:
        if honey_end and warren_end:
            scene bg ok end hw
            pause
            scene bg ok end hw2
            with dissolve
            pause
            return
        elif honey_end and alexei_end:
            scene bg ok end ha
            pause
            scene bg ok end ha2
            with dissolve
            pause
            return
        elif warren_end and alexei_end:
            scene bg ok end wa
            pause
            scene bg ok end wa2
            with dissolve
            pause
            return
        elif warren_end:
            scene bg ok end w
            pause
            return
        elif alexei_end:
            scene bg ok end a
            pause
            return
        elif honey_end:
            scene bg ok end b
            pause
            return
        else:
            "How did you even get here?!..."
    
    label best_end:
        scene bg best end
        pause
        return

    label sad_ending:
        scene end leave
        pause
        "The thought of hurting Alexi and his career prooved to much to you. You cannot be with the one you now love without destroying all that they themselves love."
        "You drive away into the night, unable to hold back the tears"
        "The End"
        return

    label bad_ending:
        scene bg worst end
        pause
        return
return
