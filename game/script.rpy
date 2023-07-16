# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")

define m = Character("Mama Squirrel")
define s = Character("Squirrel")
define t = Character("Turtle")
define f = Character("Finch")

image squirrel happy:
    "Sprites/Squirrel/squirrel happy.png"
    zoom 0.35
    yalign 0.25

image squirrel neutral:
    "Sprites/Squirrel/squirrel neutral.png"
    zoom 0.35
    yalign 0.25

image squirrel nervous:
    "Sprites/Squirrel/squirrel nervous.png"
    zoom 0.35
    yalign 0.25

image squirrel crying:
    "Sprites/Squirrel/squirrel sad.png"
    zoom 0.35
    yalign 0.25

image mama neutral:
    "Sprites/Mama Squirrel/Mama_Squirrel.png"
    zoom 0.35
    yalign 0.25

image turtle neutral:
    "Sprites/Turtle/Turtle_neutral.png"
    zoom 0.35
    yalign 0.25

image turtle happy:
    "Sprites/Turtle/Turtle_happy.png"
    zoom 0.35
    yalign 0.25

image finch neutral:
    "Sprites/Mr. Finch/Finch_neutral.png"
    zoom 0.35
    yalign 0.25

image finch thinking:
    "Sprites/Mr. Finch/Finch_Thinking.png"
    zoom 0.35
    yalign 0.25

transform move_left:
    #zoom 0.35
    yalign 0.25
    xalign -0.005

transform move_right:
    yalign 0.4
    xalign 1.0

transform middle:
    yalign 1.0
    xalign 0.5


default optionTurtle = 1
default optionFinch = 1
#default optionOwl = 1

# The game starts here.
# random edit

label start:

    define config.default_music_volume = 0.6
    define config.default_sfx_volume = 0.6
    define config.default_voice_volume = 0.6

    scene bg forestfall with fade
    play music "audio/Act1toMidAct2.mp3" volume 0.25 loop

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    "Squirrel woke from the morning light coming through the window, but it was darker than usual."

    "For the first time, he noticed the leaves changed colors and made piles on the ground."

    "Squirrel felt the chill from the window and shivered. His breath left the shape of his tiny nostrils on the glass."
    play sound "audio/SFX/pagesfx.mp3" volume 0.5

    show bg squirrelhome with wipeleft
    
    "Squirrel climbed down the ladder to meet his mother."   

    show squirrel happy at left

    s "Winter is coming! Winter is coming!" 

    hide squirrel

    "Mama Squirrel set her broom down and turned to her son."

    show squirrel happy at left
    show mama neutral at right

    m "That's right my dear! Your first winter. Are you excited?"

    s "Yes! I can't wait to play in the snow and sled with my friends, Turtle and Finch!"

    "Mama Squirrel took Squirrel's hands and wrapped them in her own."

    m "Oh my dear, you won't be able to see your friends until winter is over."

    show squirrel nervous

    "Squirrel paused and stared at his mother."

    s "Why not?"

    m "Turtle must store her food and sleep. Finch must fly south to find food when it gets too cold."

    show squirrel crying
    
    "Squirrel began to cry."

    s "Then I won't let them go. Who will take me across the lake? Who will fly me to the tops of the trees? I can't do this on my own. I don't want to be alone all winter."

    show squirrel nervous
    
    "Mama Squirrel wiped away Squirrel's tears and wrapped him in a tight hug."

    m "It will be alright, Squirrel. You are smarter and braver than you think you are. Why don't you go spend time with your friends before winter comes?"

    hide squirrel 
    hide mama

    "Squirrel decided he must speak to his friends at once and tell them to stay through winter."

label friendChoice:

    menu choose_friend1:
        "Squirrel went to see Turtle" if optionTurtle == 1:
            $optionTurtle = 0
            jump turtleSection
        "Squirrel went to see Finch" if optionFinch == 1:
            $optionFinch = 0
            jump finchSection
        
    if optionTurtle == 0 and optionFinch == 0:
        jump act2

label turtleSection:
    play sound "audio/SFX/pagesfx.mp3" volume 0.5

    show bg forestfall with wipeleft
    show squirrel nervous at left
    show turtle neutral at right

    s "Turtle! Turtle! You can't sleep through the winter. I will be all alone in the woods with no one to play with."

    t "Calm down, my Squirrely friend. It will be okay."

    show squirrel neutral

    t "When winter comes, I have to sleep and breathe under water so I don't freeze in the cold."

    show squirrel crying

    "Squirrel tried to hold back his tears."

    hide squirrel
    hide turtle
    show bg turtlesquirrelcg with wiperight
    

    s "But who will carry me across the pond to get acorns?"

    t "You can take a little raft to get across. It will be just like you are on my back."

    s "What if I fall in? Who will keep me safe?"

    show bg forestfall with wipeleft
    show squirrel nervous at left
    show turtle neutral at right

    "Turtle nudged Squirrel with the tip of her nose."

    t "You will keep yourself safe. If you fall from your raft, you can swim to safety. Squirrels are swimmers like turtles. You just have to believe in yourself."

    hide squirrel
    hide turtle

    jump friendChoice

label finchSection:
    play sound "audio/SFX/pagesfx.mp3" volume 0.5

    show bg finchhome with wipeleft
    show squirrel nervous at left
    
    s "Finch! Finch! Please don't go away for winter. I want you to stay and play. I don't want to be alone in the woods everyday."

    show finch neutral at right

    f "I know it will be hard for you, but I have to migrate dear Squirrel."

    "Squirrel took a deep breath."

    s "But who will help me fly to the top of the trees?"

    "Finch opened his wing and wrapped it around Squirrel."

    show finch thinking

    f "Ah, you are already getting too big for me to carry you. Besides, you are a Squirrel. You were born to climb. You can get to the top of the trees by yourself."

    show finch neutral

    s "What if I fall?"

    show finch thinking

    f "You get up and try again."

    hide squirrel 
    hide finch
    
    jump friendChoice

label act2:
    play sound "audio/SFX/pagesfx.mp3" volume 0.5

    show bg forestfall with wipeleft

    "Squirrel spent all of his time with his friends. Despite his wishes, the days grew shorter and colder."

    stop music fadeout 0.5

    play music "audio/Act2toEnd.mp3" volume 0.25 loop
    show bg forestwinter with fade
    play sound "audio/SFX/windsfx.mp3" volume 0.5 loop

    "Squirrel woke one bright morning to a forest covered in white snow."

    "The wind whipped past Squirrel's window and howled through the bare trees."

    stop sound

    "Squirrel felt a pit in his stomach. He knew winter had come and his friends would be gone until spring."

    play sound "audio/SFX/pagesfx.mp3" volume 0.5

    show bg squirrelhome with wipeleft

    "Squirrel pulled his blankets over his head."

    show squirrel nervous at left

    s "I will just sleep through the winter like turtle. I won't have to miss my friends or go to the woods by myself if I just sleep."

    hide squirrel

    "Squirrel's plan didn't last long."

    #show squirrel nervous at left
    show mama neutral at right

    m "Squirrel! Come downstairs. I have a chore for you."

    hide mama

    "Squirrel found his mother counting ingredients in the kitchen."

    show squirrel neutral at left
    show mama neutral at right

    m "I need you to get the rest of the acorns from the other side of the pond. We need a few more to make it through winter and the snow will cover them soon."

    "Squirrel held his hands to his chest."

    show squirrel nervous

    s "But I have never crossed the pond without help."

    "Mama Squirrel crouched next to Squirrel and held his face in her hands."

    m "You do things without help all the time. I would not put my little Squirrel in danger. I promise you can do this."

    hide squirrel 
    hide mama

    "Squirrel promised his mother he would try his best."

    play sound "audio/SFX/pagesfx.mp3" volume 0.5
    show bg frozenpond with wipeleft

    "Once Squirrel reached the pond, he searched for a raft."

    "He found a large, crunchy brown leaf poking out of the snow."

    play sound "audio/rustle01.flac"

    "Squirrel pulled it out and dusted off the snow."

    show squirrel happy at middle
    
    s "This leaf will work."

    hide squirrel

    "Squirrel gently set the leaf on the water. He felt his hands shake and his heart pound."

    show squirrel nervous at middle

    s "What if the wind tips the leaf over? What if I fall off and I forget how to swim? What if the water is so cold I freeze up?"

    hide squirrel

    "Squirrel took a deep breath and remembered everyone believed in him. He could do it, he just had to believe he could."

    "Squirrel carefully stepped onto the leaf and sat down. With his tiny fingers, he pushed off the edge of the pond."

    "As the little raft floated on the water, Squirrel felt his heart beat slow down. He felt the soft rock of the leaf under him and wind brush against his fur."

    "Squirrel laughed and squealed with joy."

    show squirrel happy at middle

    s "I did it! It was scary and I did it! And it's fun!"

    hide squirrel


    "Squirrel made it to the other side and pulled the last acorns from the snow."

    "He decided he would come back tomorrow to explore the rest of the pond alone."

    play sound "audio/SFX/pagesfx.mp3" volume 0.5
    show bg forestwinter with wipeleft

    "On his walk home, arms full of acorns, Squirrel heard the call of a Finch."

    show squirrel neutral at middle

    s "Could it be Finch about to leave for the winter?"

    hide squirrel


    "Squirrel placed his acorns in a neat pile under a birch tree."

    show squirrel happy at middle

    s "Maybe if I can reach the top of the trees, I can wave goodbye to my friend."
    hide squirrel

    "Squirrel looked up at the towering tree in front of him. He could barely see the top. His heart raced once again."

    show squirrel nervous at middle

    s "Maybe it's not worth it. What if I fall?"
    hide squirrel

    "Squirrel closed his eyes and took a deep breath, remembering that Finch believed in him."
    
    "He placed one hand on the bark of the tree and began to climb, putting one hand above the other."
    
    stop music fadeout 0.5
    play music "audio/ClimbingTreeandTurtleCG.mp3" volume 0.15 loop
    play sound "audio/SFX/windsfx.mp3" volume 0.75 loop

    "He climbed higher and higher."

    "Squirrel felt the wind whistle by his ears. He looked down and saw how far the ground was from him. He began to panic."

    "Squirrel paused, took another deep breath, and continued to climb higher."

    show squirrel neutral at middle

    s "I'm already this far. I can do this."
    hide squirrel

label act3:
    "Squirrel climbed to the highest branch he could find and sat with his back against the tree."

    "He looked around the sky for his feathered friend Finch and saw him sailing far off through the air. Finch was headed south to a different place, a warmer place."

    "Squirrel smiled, his heart swelled with pride."

    show squirrel happy at middle

    s "I did it! It was scary and I did it! And it's fun!"
    hide squirrel

    "Squirrel closed his eyes and felt the wind through his fur. He loved the thrill of being so high above the ground."

    show squirrel crying at middle
    stop music fadeout 0.5
    stop sound fadeout 0.5

    s "No matter how scary and no matter how hard, from now on, I will always believe in myself."

    hide squirrel

    "Squirrel kept his promise through winter."

    "And onwards."

    #play sound "audio/SFX/pagesfx.mp3" volume 0.5
    #scene bg endcard with wipeleft
    #pause
    return
