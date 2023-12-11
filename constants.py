import json
WIDTH_MAIN_MENU = 550
HIGH_MAIN_MENU = 550

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

WIDTH_BUTTON = 200
HIGH_BUTTON = 100

FPS = 60
DIRECTION_L = -1
DIRECTION_R = 1
GROUND_RECT_H = 80
DEBUG = False


def open_configs() -> dict:
        with open("setting.json", 'r', encoding='utf-8') as config:
            return json.load(config)
        

