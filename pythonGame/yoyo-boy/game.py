import pygame
import os
from entities.character import Character
from modules.utils import load_image

pygame.init()
screen = pygame.display.set_mode((800,640))
asset_path = "assets"
char_path = os.path.join(asset_path,"character")

idle_img = load_image(os.path.join(char_path,'idle.png'))
base_img = load_image(os.path.join(char_path,'base.png'))
attack_img = load_image(os.path.join(char_path, 'attack.png'))
run_img = load_image(os.path.join(char_path, 'run.png'))
images = {'idle': idle_img,
          'base': base_img,
          'attack': attack_img,
          'run': run_img}

char = Character(-20, 200, images)

# clock - FPS
clock = pygame.time.Clock()

# mainloop 
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_x:
                char.attack()
            elif event.key == pygame.K_z:
                char.jump()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        char.move(left=True)
    elif pressed[pygame.K_RIGHT]:
        char.move()
    else:
        char.stop()

    screen.fill( (0,0,0) )
    char.update(screen)
    pygame.display.flip()

    clock.tick(15)

pygame.quit()