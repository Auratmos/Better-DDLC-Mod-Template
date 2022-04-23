# script.rpy
# This file is for the label that is called when the Start() action is given, like with the "New Game" button.

# This is the start label.
# It is required for all Ren'Py games.
label start:

    # This determines the anti-cheat ID.
    # This is used in Act 2, to keep players from using saves that aren't their own.
    $ anticheat = persistent.anticheat

    # This determines the game's chapter.
    # This is used for the poem game, to determine the initial poem game message and scares in Act 2.
    $ chapter = 0

    # This determines whether or not the player can skip through pauses and transitions.
    # By default, this is config.developer. If a variable = variable, like in this, the first variable will copy the value of the second variable.
    $ _dismiss_pause = config.developer

    # This defines the initial names of the four girls.
    # By default, these are...
    $ s_name = "???" # "???" - (Sayori)
    $ m_name = "Girl 3" # "Girl 3" - (Monika)
    $ n_name = "Girl 2" # "Girl 2" - Natsuki
    $ y_name = "Girl 1" # "Girl 1" - Yuri

    # This determines whether or not the buttons at the bottom of the textbox are visible and the escape button works.
    $ quick_menu = True

    # This determines the style of speech used in dialogue.
    # If you wish to change it to the glitched dialogue style, use "$ style.say_dialogue = style.edited"
    $ style.say_dialogue = style.normal

    # This determines whether or not the player is in the Sayori kill cutscene.
    $ in_sayori_kill = None

    # These determine whether or not the player is allowed to use the skip option, no matter their current settings.
    $ allow_skipping = True
    $ config.allow_skipping = True

    # Place your code here, or call/jump to another label (recommended).
    
    
    # This returns the user to the previous label.
    # If start is the first label to run in a sequence, then this here return action will return to the main menu.
    return

# This is the endgame label.
# It is used for the Sayori kill scene, where the screen fades to black and says "END" before returning to the main menu.
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return