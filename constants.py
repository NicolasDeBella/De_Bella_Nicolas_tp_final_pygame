import json

PATH_CURSOR = r"assets\graphics\setting_main_menu\cursor\cursor.png"
PATH_BACKGROUN_MENU = r"assets\graphics\setting_main_menu\background_menu\bakground_main_menu.png"
PATH_SCREEN_MAIN_MENU = r"assets\graphics\setting_main_menu\main_menu\screen_main_menu.png"
PATH_BUTTON_PLAY = r"assets\graphics\setting_main_menu\main_menu\button_play_game.png"
PATH_BUTTON_LEVEL_SELECT = r"assets\graphics\setting_main_menu\main_menu\button_level_select.png"
PATH_BUTTON_SCORE = r"assets\graphics\setting_main_menu\main_menu\button_score.png"
PATH_BUTTON_QUIT_GAME = r"assets\graphics\setting_main_menu\main_menu\button_quit_game.png"
PATCH_BUTTON_SOUND_ON = r"assets\graphics\setting_main_menu\setting_sound\button_sound_on.png"
PATCH_BUTTON_SOUND_OF = r"assets\graphics\setting_main_menu\setting_sound\button_sound_of.png"
PATCH_BUTTON_SETTING_VOLUME = r"assets\graphics\setting_main_menu\setting_sound\setting_volume.png"

PATH_SCREEN_LEVEL_SELECT = r"assets\graphics\setting_main_menu\levels\screen_levels.png"
PATCH_LEVEL_1 = r"assets\graphics\setting_main_menu\levels\button_level_1.png"
PATCH_LEVEL_2 = r"assets\graphics\setting_main_menu\levels\button_level_2.png"
PATCH_LEVEL_3 = r"assets\graphics\setting_main_menu\levels\button_level_3.png"

PATCH_SCREEN_SCORE = r"assets\graphics\setting_main_menu\score\screen_score.png"

PATCH_SCREEN_VOLUME = r"assets\graphics\setting_main_menu\setting_sound\screen_volume.png"
PATCH_BUTTON_LESS = r"assets\graphics\setting_main_menu\setting_sound\button_less.png"
PATCH_BUTTON_FURTHER = r"assets\graphics\setting_main_menu\setting_sound\button_further.png"

PATH_SCREEN_PAUSE = r"assets\graphics\setting_main_menu\pause\screen_pause.png"
PATH_BUTTON_CONTINUE = r"assets\graphics\setting_main_menu\pause\button_continue.png"
PATH_BUTTON_QUIT = r"assets\graphics\setting_main_menu\pause\button_quit.png"

PATH_IMAGE_MISION_COMPLETE = r"assets\graphics\game_state\mision_complete\mision_complete.png"
WIDTH_IMAGE_MISION_COMPLETE = 500
HIGH_IMAGE_MISION_COMPLETE = 500
PATH_MISSION_COMPLETE_SOUND = r"assets\sound\mission_complete\metal-slug-mission-complete.mp3"

PATH_BACKGROUND_SOUND = r"assets\sound\background_music\background_sound_metal_slug.mp3"
PATH_COLLISION_SOUND = r"assets\sound\object_collision_sound\object_collision_sound.mp3"
PATH_METAL_SLUG_SCREAM_SOUND = r"assets\sound\metal_slug_scream\metal-slug-scream.mp3"

PATH_VICTORY_SOUND = r"assets\sound\victory\victory.mp3"
PATH_VICTORY_IMAGE = r"assets\graphics\game_state\you_win\you_win.jpg"

PATH_GAME_OVER_SOUND = r"assets\sound\game_over\game_over.mp3"
PATH_GAME_OVER_IMAGE = r"assets\graphics\game_state\game_over\game_over.jpg"

PATH_DISPARO_SOUND = r"assets\sound\disparo\disparo.mp3"

FPS = 60
DIRECTION_L = -1
DIRECTION_R = 1
GROUND_RECT_H = 80
DEBUG = False

WIDTH_WINDOW = 1300
HIGH_WINDOW = 600

HIGH_PLAYER = 95
WIDTH_PLAYER = 80

HIGH_ENEMY = 120
WIDTH_ENEMY = 120

HIGH_SCORE = 45
WIDTH_SOCRE = 45

HIGH_LIFE = 45
WIDTH_LIFE = 45

HIGH_TRAP = 60
WIDTH_TRAP = 60

WIDTH_SCREEN_MAIN_MENU = 550
HIGH_SCREEN_MAIN_MENU = 550

WIDTH_SCREEN_PAUSE= 300
HIGH_SCREEN_PAUSE = 300

WIDTH_BUTTON_MAIN_MENU = 250
HIGH_BUTTON_MAIN_MENU = 65

WIDTH_BUTTON_NIVEL_SELECT = 150
HIGH_BUTTON_NIVEL_SELECT = 150

WIDTH_BUTTON_SOUND = 50
HIGH_BUTTON_SOUND = 50

NEGRO = (0,0,0)
BLANCO = (255,255,255)



def open_configs() -> dict:
        with open("setting.json", 'r', encoding='utf-8') as config:
            return json.load(config)



