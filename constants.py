import json
WIDTH_WINDOW = 1300
HIGH_WINDOW = 600

HIGH_PLAYER = 75
WIDTH_PLAYER = 75

HIGH_ENEMY = 100
WIDTH_ENEMY = 100

HIGH_SCORE = 45
WIDTH_SOCRE = 45

HIGH_LIFE = 45
WIDTH_LIFE = 45

FPS = 60
DIRECTION_L = -1
DIRECTION_R = 1
DEBUG = False


def open_configs() -> dict:
        with open("setting.json", 'r', encoding='utf-8') as config:
            return json.load(config)
        

