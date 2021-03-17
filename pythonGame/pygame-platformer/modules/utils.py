import pygame
from .constants import Constants as Cts

constants = Cts()


# Helper functions
def load_image(file_path, width=constants.GRID_SIZE, height=constants.GRID_SIZE):
    img = pygame.image.load(file_path)
    img = pygame.transform.scale(img, (width, height))

    return img


def play_sound(sound_file, loops=0, maxtime=0, fade_ms=0):
    if constants.SOUND_ON:
        sound = pygame.mixer.Sound(sound_file)
        sound.play(loops, maxtime, fade_ms)


def play_music():
    if constants.SOUND_ON:
        pygame.mixer.music.play(-1)
