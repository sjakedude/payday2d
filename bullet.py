import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color, facing, pos):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        self.shooting = False
        self.image = pygame.transform.scale(
            pygame.image.load("assets/bullet.png"), (10, 10)
        )
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(1, 0)
        self.speed = 3

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.shooting:
            print(self.shooting)
            self.shooting = True

    def update(self):
        self.get_input()
        # self.get_player_orientation()
