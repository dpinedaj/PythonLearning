import os


class Constants:
    def __init__(self):
        # Paths
        self.__ASSETS_PATH = "assets"
        self.__LEVELS_PATH = "levels"

        # Levels
        self.__LEVELS = [os.path.join(self.__LEVELS_PATH, p) for p in os.listdir(self.__LEVELS_PATH)]

        # Window settings
        self.__TITLE = "DANIEL's GAME"
        self.__WIDTH = 960
        self.__HEIGHT = 640
        self.__FPS = 60
        self.__GRID_SIZE = 64

        # Options
        self.__SOUND_ON = True


        # Sounds
        self.__SOUNDS_PATH = os.path.join(self.__ASSETS_PATH, "sounds")
        self.__JUMP_SOUND_FILE = os.path.join(self.__SOUNDS_PATH, "jump.wav")
        self.__COIN_SOUND_FILE = os.path.join(self.__SOUNDS_PATH, "pickup_coin.wav")
        self.__POWERUP_SOUND_FILE = os.path.join(self.__SOUNDS_PATH, "powerup.wav")
        self.__HURT_SOUND_FILE = os.path.join(self.__SOUNDS_PATH, "hurt.ogg")
        self.__DIE_SOUND_FILE = os.path.join(self.__SOUNDS_PATH, "death.wav")
        self.__LEVELUP_SOUND_FILE = os.path.join(self.__SOUNDS_PATH, "level_up.wav")
        self.__GAMEOVER_SOUND_FILE = os.path.join(self.__SOUNDS_PATH, "game_over.wav")



    @property
    def ASSETS_PATH(self):
        return self.__ASSETS_PATH

    @property
    def LEVELS_PATH(self):
        return self.__LEVELS_PATH

    @property
    def LEVELS(self):
        return self.__LEVELS

    @property
    def TITLE(self):
        return self.__TITLE

    @property
    def WIDTH(self):
        return self.__WIDTH

    @property
    def HEIGHT(self):
        return self.__HEIGHT

    @property
    def FPS(self):
        return self.__FPS

    @property
    def GRID_SIZE(self):
        return self.__GRID_SIZE

    @property
    def SOUND_ON(self):
        return self.__SOUND_ON

    @property
    def SOUNDS_PATH(self):
        return self.__SOUNDS_PATH

    @property
    def JUMP_SOUND_FILE(self):
        return self.__JUMP_SOUND_FILE

    @property
    def COIN_SOUND_FILE(self):
        return self.__COIN_SOUND_FILE

    @property
    def POWERUP_SOUND_FILE(self):
        return self.__POWERUP_SOUND_FILE

    @property
    def HURT_SOUND_FILE(self):
        return self.__HURT_SOUND_FILE

    @property
    def DIE_SOUND_FILE(self):
        return self.__DIE_SOUND_FILE

    @property
    def LEVELUP_SOUND_FILE(self):
        return self.__LEVELUP_SOUND_FILE

    @property
    def GAMEOVER_SOUND_FILE(self):
        return self.__GAMEOVER_SOUND_FILE