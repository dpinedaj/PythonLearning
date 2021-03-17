import pygame
import json
from .constants import Constants as Cts
from .utils import load_image
import sys
sys.path.append("..")
from entities.bear import Bear
from entities.coin import Coin
from entities.liveUp import OneUp
from entities.block import Block
from entities.heart import Heart
from entities.monster import Monster
from entities.flag import Flag


constants = Cts()


block_images = {"TL": load_image("assets/tiles/top_left.png"),
                "TM": load_image("assets/tiles/top_middle.png"),
                "TR": load_image("assets/tiles/top_right.png"),
                "ER": load_image("assets/tiles/end_right.png"),
                "EL": load_image("assets/tiles/end_left.png"),
                "TP": load_image("assets/tiles/top.png"),
                "CN": load_image("assets/tiles/center.png"),
                "LF": load_image("assets/tiles/lone_float.png"),
                "SP": load_image("assets/tiles/special.png")}

block_images = {"TL": load_image("assets/tiles/top_left.png"),
                "TM": load_image("assets/tiles/top_middle.png"),
                "TR": load_image("assets/tiles/top_right.png"),
                "ER": load_image("assets/tiles/end_right.png"),
                "EL": load_image("assets/tiles/end_left.png"),
                "TP": load_image("assets/tiles/top.png"),
                "CN": load_image("assets/tiles/center.png"),
                "LF": load_image("assets/tiles/lone_float.png"),
                "SP": load_image("assets/tiles/special.png")}

coin_img = load_image("assets/items/coin.png")
heart_img = load_image("assets/items/bandaid.png")
oneup_img = load_image("assets/items/first_aid.png")
flag_img = load_image("assets/items/flag.png")
flagpole_img = load_image("assets/items/flagpole.png")

monster_img1 = load_image("assets/enemies/monster-1.png")
monster_img2 = load_image("assets/enemies/monster-2.png")
monster_images = [monster_img1, monster_img2]

bear_img = load_image("assets/enemies/bear-1.png")
bear_images = [bear_img]


class Level:

    def __init__(self, file_path):
        self.starting_blocks = []
        self.starting_enemies = []
        self.starting_coins = []
        self.starting_powerups = []
        self.starting_flag = []

        self.blocks = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.flag = pygame.sprite.Group()

        self.active_sprites = pygame.sprite.Group()
        self.inactive_sprites = pygame.sprite.Group()

        with open(file_path, 'r') as f:
            data = f.read()

        map_data = json.loads(data)

        self.width = map_data['width'] * constants.GRID_SIZE
        self.height = map_data['height'] * constants.GRID_SIZE

        self.start_x = map_data['start'][0] * constants.GRID_SIZE
        self.start_y = map_data['start'][1] * constants.GRID_SIZE

        for item in map_data['blocks']:
            x, y = item[0] * constants.GRID_SIZE, item[1] * constants.GRID_SIZE
            img = block_images[item[2]]
            self.starting_blocks.append(Block(x, y, img))

        for item in map_data['bears']:
            x, y = item[0] * constants.GRID_SIZE, item[1] * constants.GRID_SIZE
            self.starting_enemies.append(Bear(x, y, bear_images))

        for item in map_data['monsters']:
            x, y = item[0] * constants.GRID_SIZE, item[1] * constants.GRID_SIZE
            self.starting_enemies.append(Monster(x, y, monster_images))

        for item in map_data['coins']:
            x, y = item[0] * constants.GRID_SIZE, item[1] * constants.GRID_SIZE
            self.starting_coins.append(Coin(x, y, coin_img))

        for item in map_data['oneups']:
            x, y = item[0] * constants.GRID_SIZE, item[1] * constants.GRID_SIZE
            self.starting_powerups.append(OneUp(x, y, oneup_img))

        for item in map_data['hearts']:
            x, y = item[0] * constants.GRID_SIZE, item[1] * constants.GRID_SIZE
            self.starting_powerups.append(Heart(x, y, heart_img))

        for i, item in enumerate(map_data['flag']):
            x, y = item[0] * constants.GRID_SIZE, item[1] * constants.GRID_SIZE

            if i == 0:
                img = flag_img
            else:
                img = flagpole_img

            self.starting_flag.append(Flag(x, y, img))

        self.background_layer = pygame.Surface([self.width, self.height], pygame.SRCALPHA, 32)
        self.scenery_layer = pygame.Surface([self.width, self.height], pygame.SRCALPHA, 32)
        self.inactive_layer = pygame.Surface([self.width, self.height], pygame.SRCALPHA, 32)
        self.active_layer = pygame.Surface([self.width, self.height], pygame.SRCALPHA, 32)

        if map_data['background-color'] != "":
            self.background_layer.fill(map_data['background-color'])

        if map_data['background-img'] != "":
            background_img = pygame.image.load(map_data['background-img']).convert_alpha()

            if map_data['background-fill-y']:
                h = background_img.get_height()
                w = int(background_img.get_width() * constants.HEIGHT / h)
                background_img = pygame.transform.scale(background_img, (w, constants.HEIGHT))

            if "top" in map_data['background-position']:
                start_y = 0
            elif "bottom" in map_data['background-position']:
                start_y = self.height - background_img.get_height()

            if map_data['background-repeat-x']:
                for x in range(0, self.width, background_img.get_width()):
                    self.background_layer.blit(background_img, [x, start_y])
            else:
                self.background_layer.blit(background_img, [0, start_y])

        if map_data['scenery-img'] != "":
            scenery_img = pygame.image.load(map_data['scenery-img']).convert_alpha()

            if map_data['scenery-fill-y']:
                h = scenery_img.get_height()
                w = int(scenery_img.get_width() * constants.HEIGHT / h)
                scenery_img = pygame.transform.scale(scenery_img, (w, constants.HEIGHT))

            if "top" in map_data['scenery-position']:
                start_y = 0
            elif "bottom" in map_data['scenery-position']:
                start_y = self.height - scenery_img.get_height()

            if map_data['scenery-repeat-x']:
                for x in range(0, self.width, scenery_img.get_width()):
                    self.scenery_layer.blit(scenery_img, [x, start_y])
            else:
                self.scenery_layer.blit(scenery_img, [0, start_y])

        pygame.mixer.music.load(map_data['music'])

        self.gravity = map_data['gravity']
        self.terminal_velocity = map_data['terminal-velocity']

        self.completed = False

        self.blocks.add(self.starting_blocks)
        self.enemies.add(self.starting_enemies)
        self.coins.add(self.starting_coins)
        self.powerups.add(self.starting_powerups)
        self.flag.add(self.starting_flag)

        self.active_sprites.add(self.coins, self.enemies, self.powerups)
        self.inactive_sprites.add(self.blocks, self.flag)

        # with this speed up blitting on slower computers?
        for s in self.active_sprites:
            s.image.convert()

        for s in self.inactive_sprites:
            s.image.convert()

        self.inactive_sprites.draw(self.inactive_layer)

        # is converting layers helpful at all?
        self.background_layer.convert()
        self.scenery_layer.convert()
        self.inactive_layer.convert()
        self.active_layer.convert()

    def reset(self):
        self.enemies.add(self.starting_enemies)
        self.coins.add(self.starting_coins)
        self.powerups.add(self.starting_powerups)

        self.active_sprites.add(self.coins, self.enemies, self.powerups)

        for e in self.enemies:
            e.reset()
