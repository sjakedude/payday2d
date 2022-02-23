import pygame
import math
from bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("assets/player.png"), (31, 31)
        )
        self.image_original = pygame.transform.scale(
            pygame.image.load("assets/player.png"), (31, 31)
        )
        self.rect = self.image.get_rect(topleft=pos)
        self.position = pos
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 3
        self.shooting = False

    def get_input(self):
        keys = pygame.key.get_pressed()

        # Movement
        if keys[pygame.K_d]:
            self.direction.y = 0
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.y = 0
            self.direction.x = -1
        elif keys[pygame.K_w]:
            self.direction.x = 0
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.x = 0
            self.direction.y = 1
        else:
            self.direction.x = 0
            self.direction.y = 0


    def get_player_orientation(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.image = pygame.transform.rotate(self.image_original, 90)
        elif keys[pygame.K_DOWN]:
            self.image = pygame.transform.rotate(self.image_original, -90)
        elif keys[pygame.K_LEFT]:
            self.image = pygame.transform.rotate(self.image_original, 180)
        elif keys[pygame.K_RIGHT]:
            self.image = pygame.transform.rotate(self.image_original, 0)


    def update(self):
        self.get_input()
        self.get_player_orientation()
