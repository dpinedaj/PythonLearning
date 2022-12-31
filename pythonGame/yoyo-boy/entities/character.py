import pygame

IDLE_SUB_IMAGES = 5
ATTACK_SUB_IMAGES = 8
RUN_SUB_IMAGES = 8


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, images):
        super().__init__()
        self.player_clock = pygame.time.Clock()

        self.images = images
        self.image = self.images["base"]

        # Define Rect
        self.rect = self.image.get_rect()

        # Position
        self.rect.x = x
        self.rect.y = y

        # Velocity
        self.vy = 0
        self.vx = 0

        # Animations
        self.animation_images = {}
        self.idle_iter = 0
        self.attack_iter = 0
        self.run_iter = 0

        # States
        self.is_attack = False
        self.on_ground = False
        self.is_running = False
        self.facing_right = True
        self.can_move_left = True
        self.can_move_right = True

        # Constants
        self.jump_power = 50
        self.speed = 10

    def _load_animation(self, animation_type, sub_images):
        if self.animation_images.get(animation_type) is None:
            surface = self.images[animation_type].convert_alpha()
            width = surface.get_width()
            height = surface.get_height()
            sub_height = height / sub_images
            self.animation_images[animation_type] = {}
            self.animation_images[animation_type][1] = [
                surface.subsurface((0, x * sub_height, width, sub_height))
                for x in range(sub_images)
            ]
            self.animation_images[animation_type][0] = [
                pygame.transform.flip(img, True, False)
                for img in self.animation_images[animation_type][1]
            ]

    def idle_animation(self, canvas):
        self._load_animation("idle", IDLE_SUB_IMAGES)
        self.player_clock.tick(5)
        canvas.blit(
            self.animation_images["idle"][self.facing_right][self.idle_iter], self.rect
        )
        self.idle_iter = (self.idle_iter + 1) % IDLE_SUB_IMAGES

    def attack_animation(self, canvas):
        self._load_animation("attack", ATTACK_SUB_IMAGES)
        canvas.blit(
            self.animation_images["attack"][self.facing_right][self.attack_iter],
            self.rect,
        )
        self.attack_iter = (self.attack_iter + 1) % ATTACK_SUB_IMAGES
        if self.attack_iter == len(self.animation_images["attack"]) - 1:
            self.is_attack = False

    def run_animation(self, canvas):
        self._load_animation("run", RUN_SUB_IMAGES)
        canvas.blit(
            self.animation_images["run"][self.facing_right][self.run_iter], self.rect
        )
        self.run_iter = (self.run_iter + 1) % RUN_SUB_IMAGES
        if self.run_iter == len(self.animation_images["run"]) - 1:
            self.is_running = False

    def attack(self):
        self.is_attack = True

    def set_animation(self, canvas):
        if self.is_attack:
            self.attack_animation(canvas)
        elif self.is_running:
            self.run_animation(canvas)
        else:
            self.idle_animation(canvas)

    def jump(self):
        if self.on_ground:
            self.rect.y += 2  # Jump helps to smooth
            self.on_ground = False
            self.vy = -1 * self.jump_power
            self.rect.y -= 2  # Jump helps to smooth

    def apply_gravity(self, gravity):
        if not self.on_ground:
            self.vy += gravity

    def move(self, left=False):
        self.is_running = True
        if left:
            self.facing_right = False
            if self.can_move_left:
                self.vx = -self.speed

        else:
            self.facing_right = True
            if self.can_move_right:
                self.vx = self.speed

    def stop(self):
        self.vx = 0

    def horizontal_boundaries(self, canvas):
        # Detect canvas boundaries
        YOYO_GAP = 270  # TODO TESTING
        if self.rect.right - YOYO_GAP >= canvas.get_width():
            self.stop()
            self.can_move_right = False
        else:
            self.can_move_right = True

        if self.rect.left + YOYO_GAP <= 0:
            self.stop()
            self.can_move_left = False
        else:
            self.can_move_left = True

    def vertical_boundaries(self, canvas):
        # Detect floor
        if self.rect.bottom >= canvas.get_height():  # TODO CHECK RECT HEIGHT
            self.vy = 0
            self.on_ground = True

    def handle_movements(self, canvas):
        self.rect.y += self.vy
        self.rect.x += self.vx

        self.vertical_boundaries(canvas)
        self.horizontal_boundaries(canvas)

    def update(self, canvas):
        self.apply_gravity(5)
        self.handle_movements(canvas)
        self.set_animation(canvas)
