# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character("InFLUencer", color="#7e7935")
define w = Character("Warren", color="#7a3396")
define a = Character("Alexei", color="#5693ce")
define h = Character("Honey Bear", color="#b85826")
define b = Character("Random Barista", color="#fffdc1")

default honey_end = True

# The game starts here.

# label splashscreen:
    # scene bg splash
    # with fade

# label before_main_menu:
#     ""

label start:

    scene bg instagram popular
    with fade

    show flu angry at left
    with dissolve

    i "I can't believe that the Common Cold has overtaken me on Instagram. They probably bought half of their infection vectors."
    i "They'd infect anybody...such low standards!"
    i "I mean, they aren't even seasonal! I'm the flu!"
    i "I can't let this happen, I need to do something!"

    menu What_to_do:
        "Do something about it":
            jump do_something

        "Do nothing about it":
            show flu sad at left
            with dissolve
            i "yeah...I dont know what I would even do, though. Who really cares about instagram anyway?"
            ".:. you have infected 0 people this Flu season and failed as a virus. You lose all your followers and delete your Instagerm account."
            return
        
label do_something:
    show flu angry at left
    with dissolve

    show flu happy at left
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
            show flu sad
            i "now that I think on it...maybe this is a dumb plan"
            ".:. you have infected 0 people this Flu season and failed as a virus. You lose all your followers and delete your Instagerm account."
            return
            
    jump Warren_date
return

label Warren_date:
    "You match with your city's resident wild party-planner, a typical super-posh, wealthy, play-boy with ties to all the elite in the area."
    "Infecting him means your strain will find its way to all the well-traveled high class in the area. From there you can hope it trickles down the social ladder."
    "His extravagant and wild party lifestyle has done a number on his immune system, making him easy to infect. But can you get close enough? Party planners cant afford to get sick, you know!"

    scene bg restaurant
    show flu neutral at left
    show warren neutral at right
    with fade 

    w "I hope this isn't too much for you. I thought it'd be best to chose a more toned down locale for our initial meet."
    w "It may still be more than you're used to, though."

    menu:
        "Be rude back":
            show flu surprised at left
            i "I'm surprised you chose such a pedestrian type place."
            show warren surprised at right
            w "pedestrian?!"
        "Be polite":
            show flu neutral at left
            i "It's fine..."
        "Be excited":
            show flu happy at left
            i "The restaurant is lovely! I think its just right for us. No prying eyes."
        
    show warren neutral
    w "Whatever. Just let me know if you need any help understanding anything on the menu."

    i "How sweet"

    w "Yeah. Anyway, I've been planning a party for this upcoming weekend. It's going to be the biggest party of the century and people will be flying from all over just to try to be near it. I could get you in guarenteed."
    w "want to come?"

    menu:
        "Accept invitation rudely":
            i "I GUESS I can be free if I need to be"
            show warren surprised

        "Accept invitation happily":
            show flu happy at left
            i "I'd love to!"

    hide flu
    show warren shocked at right
    show honey happy

    h "Oh. My. Bio!"
    h "Is that InFLUencer?! Is it really YOU?!"

    show warren angry

    menu:
        "ew another fan?":
            hide warren 
            show flu angry at left
            show honey surprised at right
            i "What's it to ya?"
        "omg! a fan?!":
            hide warren 
            show flu happy at left
            show honey happy at right
            "Yeah, are you a fan? It's always nice to meet new people!"
    
    show honey happy at right
    h "I'm a huge fan! I can't believe I'm meeting you, I've been following you in IG since your big trip to the UK in 2011!"

    menu:
        "neutral":
            show flu happy at left
            i "I'm glad to be meeting you."
            jump honey_neutral_1

        "rude":
            show flu angry at left
            show honey surprised at right
            i "Okay. Did you need something?"
            jump honey_rude_1

        "polite":
            show flu neutral at left
            show honey neutral at right
            i "Thank you! I'm on a date right now, though, and want to focus on that."
            jump honey_polite_1

    label honey_neutral_1:
        show honey happy at right
        h "You've got to go check out this museum with me! It's huge right now and my family is donating a bunch of art so we could have to whole place to hang out!"
        menu:
            "Sure!":
                show flu happy at left
                i "Yeah! That would be great! Im bored anyway."
                i "Bye Warren! Let's go!"
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
                show flu happy at left
                i "Yeah! That would be great! I'll talk to you then."
                jump date_end
            "Too busy":
                i "No, I'm busy today."
                show honey sad at right
                h "oh...I understand. I'll leave you guys alone."
                $ honey_end = False
                jump honey_leaves

    label honey_leaves:
        hide honey
        show warren neutral at right
        show flu neutral left

        w "wow I didn't realize you were so popular. You must be pretty famous! I didn't expect that."

        menu:
            "Yeah, you know, just a day in the life!":
                show flu blush
                i "Yeah, you know, just a day in the life!"
            "I try not to BRAG about it, you know.":
                show flu blush
                i "I try not to BRAG about it, you know. But I'm up there with the Common Cold and Strep Throat!"
            "It's no big deal.":
                i "It's no big deal."            
                show flu blush

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
            show flu happy at left
            i "Bye Warren!"

            hide flu
            show honey happy
            h "Hey again Influ! Is it alright if I call you Influ?"
            h "Anyway, what do you say to going to this museum with me? It'll be a great time!"

            i "sure...why not!"

            hide honey
            hide flu 
            scene bg black

            "On your inpromptu date, you find out some interesting things. Honey is a prince(ess)! 5th in line for the throne in Tonga! If you infect them you're going international"
            "As a royal diplomat and carefree party-boy Honey comes in contact with all sorts of people all over the globe!"
            "Even betterm despite having a good immune system, Honey doesn't know any better about being wary around you. It's like no one taught him the basics of flu season!
            transmitting your strain to him would be a peice of cake!"

            jump morning_street

label morning_street:
    scene bg street
    with fade

    show flu neutral
    with fade

    i "What a great morning. I don't have much at all planned for my day but should try to stay out so I don't waste this good weather. Who knows, maybe I'll the next greatest disease vector today!"
    show flu angry
    i "I cant seem to properly wake up, though. How will I ever Infect the whole West Coast if I can't even stay awake!?"
    show flu happy
    i "Oh! I'll head to Mitochondria! My favorite coffee shop always has something to power my cell."

label Coffee_shop:
    scene bg cafe
    show flu angry
    with fade

    i "I forgot how long it takes them to make my favorite drink sometimes. This sucks"
    b "One Grande, Iced, Sugar-Free, Vanilla Latte with Soy Milk and nutmeg at 120 Degrees!"
    show flu happy
    i "Finally! Now I can sit and enjoy my morning properly!"
    show flu angry
    i "Or at least I could if this gracile grassroots guy would stop whatever hes doing. People are paying him too much attention!"

    hide flu
    show alexei happy
    a "Everyone understands the extraordinary hardships that are placed on the uninsured, who live every day just one accident or illness away from bankruptcy. These are not primarily people on welfare. Some can’t get insurance on the jobs they have! I have a plan for us, that WILL work! It's simple, really..."

    hide alexei 
    show flu angry
    i "Oh. My. Bio. He's actually on to something! This isn't good. If he goes on like this I might die."
    show flu surprised
    i "If he actually does this all of virus kind might die! I'll be finished!"
    show flu angry
    i "I need to step in!"

    hide flu
    show alexei happy at right
    a "...This is especially true now in Flu season! Vaccines are essential! That’s why under my plan..."
    menu:
        "Cut in rudely":
            "Oy! Cut it out! Don't talk that vaccine stuff out here! Are you trying to ruin everyone's lives?! Everyone knows the best way to fight off any sort of sickness is to turn your a/c on high and binge eat Coldrock ice-cream!"
        "Take him aside kindly":
            "Hey! I couldn't help but overhear you. Would you mind sitting with me for a bit? Just to chat. You seem so friendly and sociable! So handsome! I bet you have a GREAT immune system too."
    
return
