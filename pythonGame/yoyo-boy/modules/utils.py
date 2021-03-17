import pygame


def load_image(path):
    img = pygame.image.load(path)
    h = img.get_height()
    w = img.get_width()
    img = pygame.transform.scale(img, (w*5, h*5))
    return img