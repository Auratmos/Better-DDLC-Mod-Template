# options.rpy
# This file is for defining basic information about your mod.

# This defines the name of the mod.
# Replace the string below with the name of your mod.
define config.name = "DDLC Mod"

# This determines whether or not the mod name should be shown on the main menu.
# By default, this is True.
# It's best to keep this on to prevent confusion between the vanilla game and your mod.
define gui.show_name = True

# This defines the version number string.
# You should use Semver Versioning to version your mod.
# https://semver.org
define config.version = "1.0.0"

# This defines the text in the about menu.
# DDLC hides the about menu by default, so this can remain blank.
define gui.about = _("")

# This defines the build name of your mod.
# This is used for internally naming distributions of your mod.
# The string MUST be ASCII, so no spaces, colons, or semicolons.
# Replace the string below with the build name of your mod.
define build.name = "DDLC-Mod"

# These determine whether the sound, music and voice sliders should be visible in the game's Settings menu or not.
# By default, these are...
define config.has_sound = True # True
define config.has_music = True # True
define config.has_voice = False # False

# This defines what audio definition to play at the main menu.
# By default, this is audio.t1.
# t1 (or audio.t1) is the audio definition of the Doki Doki Literature Club main menu theme song.
define config.main_menu_music = audio.t1


define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)

# This defines what transition to use when loading a save file.
# By default, this is None.
define config.after_load_transition = None

# This defines what transition to use to go to the main menu after a return action is called.
# By default, this is Dissolve(.5).
define config.end_game_transition = Dissolve(.5)

# This defines the behavior of the textbox's appearance.
# By default, this is "auto", meaning the textbox will only appear while dialogue is displayed.
# This can be changed in-game with window show, window hide, and window auto.
define config.window = "auto"

# This defines what the transition to use in showing and hiding the textbox.
# By default, these are Dissolve(.2).
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

# This defines the default speed of characters appearing in the textbox.
# It is measured in characters per second.
# By default, this is 50.
default preferences.text_cps = 50

# This defines the default time (in seconds) to wait before jumping to the next line while Auto-Forward mode is enabled.
# By default, this is 15 (seconds).
default preferences.afm_time = 15

# These defines the default volume of music and sound on a scale of 0 to 1.
# By default, these are 0.75.
default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75

# This defines the name of the folder to put save data in.
# Replace the string below with the name of the folder for your mod's save data.
# Be sure to keep the name within allowed lengths and character parameters for Windows, macOS and Linux.
define config.save_directory = "DDLC Mod"

# This defines where the icon for your game's window is located in your game directory.
# By default, this is "gui/window_icon.png". However, this location is inaccessible normally due to Team Salvato's choice to keep the game closed-source, so you should replace this with the location of a custom logo.
define config.window_icon = "gui/window_icon.png"


define config.allow_skipping = True
define config.has_autosave = False
define config.autosave_on_quit = False
define config.autosave_slots = 0
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]
define config.image_cache_size = 64
define config.predict_statements = 50
define config.rollback_enabled = config.developer
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"


init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)






init python:




















    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("audio", "all")
    build.archive("fonts", "all")

    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")

    build.classify("game/**.rpyc", "scripts")
    build.classify("game/**.txt", "scripts")
    build.classify("game/**.chr", "scripts")
    build.classify("game/**.wav", "audio")
    build.classify("game/**.mp3", "audio")
    build.classify("game/**.ogg", "audio")
    build.classify("game/**.ttf", "fonts")
    build.classify("game/**.otf", "fonts")

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)









    build.documentation('*.html')
    build.documentation('*.txt')

    build.include_old_themes = False











define build.itch_project = "teamsalvato/ddlc"