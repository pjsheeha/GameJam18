# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character("InFLUencer", color="#7e7935")
define w = Character("Warren", color="#7a3396")
define a = Character("Alexey", color="#5693ce")
define h = Character("Honey Bear", color="#b85826")
define b = Character("Random Barista", color="#fffdc1")

# The game starts here.

label splashscreen:
    # scene bg splash
    # with fade

label before_main_menu:
    ""

label start:

    # scene bg instagram popular
    # with fade

    # show flu angry at left
    # with dissolve

    i "I can't believe that the Common Cold has overtaken me on Instagram. They probably bought half of their infection vectors."
    i "They'd infect anybody...such low standards!"
    i "I mean, they aren't even seasonal! I'm the flu."
    pause 0.5
    i "THE"
    pause 0.5
    i "FLU"
    pause 0.5
    i "I can't let this happen, I need to do something!"

    menu What_to_do:
        "Say Statement"
        "Do something about it":
            jump do_something
        "Do nothing about it":
            # show flu sad at left
            # with dissolve

            i "yeah...I dont know what I would even do, though. Who really cares about instagram anyway?"
            ".:. you have infected 0 people this Flu season and failed as a virus. You lose all your followers and delete your Instagerm account."
            return
        
label do_something:
    # show flu angry at left
    # with dissolve

    # show flu happy at left
    # with dissolve

    i "I know! The flu season is almost over, but there's still time."
    i "I mean, if there's people open for a cold, there's DEFINITELY people open for me."
    i "I'll make this the worst flu season of all time. I know just how to do it too!"

    # scene bg infecter main
    # with fade

    i "I'll infect a socialite! Someone who gets in contact with a lot of people who can do my dirty work. It's perfect! I can make history and not even have to change my IG posting schedule."
    
    menu infecter_date:
        "swipe right"
            scene bg infecter match
            i "They're perfect! And Nearby! I'll set up a date with them for this weekend and from there it'll be history!"
        "rethink plan"
            show flu sad
            i "now that I think on it...maybe this is a dumb plan"
            ".:. you have infected 0 people this Flu season and failed as a virus. You lose all your followers and delete your Instagerm account."
            return
            
    jump Warren_date

label Warren_date:
    "You match with your city's resident wild party-planner, a typical super-posh, wealthy, play-boy with ties to all the elite in the area."
    "Infecting him means your strain will find its way to all the well-traveled high class in the area. From there you can hope it trickles down the social ladder."
    "His extravagant and wild party lifestyle has done a number on his immune system, making him easy to infect. But can you get close enough? Party planners cant afford to get sick, you know!"

    scene bg restaurant
    show flu neutral at left
    show Warren neutral at right
    with fade 

    w ""

    return
