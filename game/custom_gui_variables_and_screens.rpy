#
#
#
#
#
### ------------------------- ##

## Custom GUI Variables -- Do Not Change ------------------------- ##
## GUI Variables ------------------------- ##
default extra_menu = "none"

## CG GALLERY CODE ------------------------- ##
## this tells the gallery which CG to show
default cg = "1"

## This tells the screen whether or not the CG was unlocked in the game
default cg_1_unlocked = False
default cg_2_unlocked = False


## Extras screens ##################################################################
##
## This is the code for the extras screens (CG Gallery, Achievements, and Endings)
##
##

screen extras():
    tag menu
    style_prefix "extras"

    add "gui/extras_bg.png"

    hbox:
        yalign 0.5
        yoffset 100
        xpos 50
        ## extras menu navigation
        vbox:
            imagebutton auto "gui/button/gallery_%s.png" action SetScreenVariable("extra_menu", "gallery") alt "Gallery"
            imagebutton auto "gui/button/endings_%s.png" action SetScreenVariable("extra_menu", "endings") alt "Endings"
            imagebutton auto "gui/button/ach_%s.png" action SetScreenVariable("extra_menu", "achievements") alt "Achievements"
            imagebutton auto "gui/button/return_%s.png" action Return() alt "Return"

    if extra_menu == "none":
        text "Extras"
    elif extra_menu == "gallery":
        use gallery
        text "Gallery"
    elif extra_menu == "endings":
        use endings
        text "Endings"
    elif extra_menu == "achievements":
        use achievements
        text "Achievements"
    else:
        text ""
        text "Extras"


style extras_label is gui_label
style extras_vbox is gui_vbox
style extras_button is gui_button
style extras_button_text is gui_button_text

style extras_vbox:
    spacing 25
    xpos 50

style extras_text:
    size 100
    color gui.accent_color
    font "font/Forum_Regular.ttf"
    xalign .70
    ypos 70

style extras_button_text:
    size 75
    xpos 300
    xalign 0.5
    yoffset 15


## Endings Screen ##################################################################
##
## This is code for the Ending screen
##
##
screen endings():

    style_prefix "endings"
    vbox:
        ## Sample Ending Code

        if persistent.ending_1_unlocked:
            text "Ending One!" color "#ff3a50"
        else:
            text "Ending: ????"

        if persistent.ending_2_unlocked:
            text "Ending Two!" color "#ff3a50"
        else:
            text "Ending: ????"

        if persistent.ending_3_unlocked:
            text "Ending Three!" color "#ff3a50"
        else:
            text "Ending: ????"

        if persistent.ending_4_unlocked:
            text "Ending Four!" color "#ff3a50"
        else:
            text "Ending: ???? "


style endings_vbox is vbox

style endings_vbox:
    xpos 725
    ypos 225
    spacing 25

style endings_text:
    color "#2d1509"
    font "font/Forum_Regular.ttf"
    size 50

## Achievements Screen ##################################################################
##
## This is code for the Achievements screen
##
##

screen achievements():
    style_prefix "ach"

    vbox:
        if persistent.ach_1_unlocked:
            text "Achievements One" color "#ff3a50"
        else:
            text "Achievement: ????"

        if persistent.ach_2_unlocked:
            text "Achievements Two" color "#ff3a50"
        else:
            text "Achievement: ????"

        if persistent.ach_3_unlocked:
            text "Achievements Three" color "#ff3a50"
        else:
            text "Achievement: ????"

        if persistent.ach_4_unlocked:
            text "Achievements Four" color "#ff3a50"
        else:
            text "Achievement: ????"


style ach_vbox is vbox

style ach_vbox:
    xpos 725
    ypos 225
    spacing 25

style ach_text:
    color "#2d1509"
    font "font/Forum_Regular.ttf"
    size 50


## Gallery Screen ##################################################################
##
## This is code for the gallery screens
##
##
screen gallery():

    style_prefix "extras"

    grid 3 3:

        ### Sample Gallery Code!!
        if persistent.cg_1_unlocked:
            ## Show Transient Menu + Set Variable to tell it which CG to show
            imagebutton auto "gui/gallery/cg1_preview_%s.png" action [ShowTransient('illustration'), SetVariable("cg", "1")] alt "Illustration One"
        else:
            image "gui/gallery/cg_locked.png"

        image "gui/gallery/cg_locked.png"
        image "gui/gallery/cg_locked.png"

        image "gui/gallery/cg_locked.png"
        image "gui/gallery/cg_locked.png"
        image "gui/gallery/cg_locked.png"

        image "gui/gallery/cg_locked.png"
        image "gui/gallery/cg_locked.png"
        image "gui/gallery/cg_locked.png"

style extras_grid is gui_grid

style extras_grid:
    spacing 25
    xpos 725
    ypos 225


#### CG IMAGES CODE GO HERE
screen illustration():

    ## add numbered CGs below!
    if cg == "1":
        ## This is where the CG goes
        add "gui/gallery/cg_1.png"
    elif cg == "2":
        ## This is another sample
        add "gui/gallery/cg_1.png"
    else:
        text "Error: No Illustration Found"

    ## Return Button
    vbox:
        style_prefix "illustration"
        textbutton "Return" action Hide('illustration')

style illustration_button is button
style illustration_button_text is button_text

style illustration_button:
    xpos 1660
    ypos 960

style illustration_button_text:
    idle_color "#2d1509"
    hover_color "#b8a68e"
    size 75
