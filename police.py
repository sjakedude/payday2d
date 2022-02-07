import pygame
import time

class Police(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("assets/police.png"), (50, 50)
        )
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(1, 0)
        self.speed = 3

    def walking_route(self):
        if self.rect.x > 600 - self.rect.width or self.rect.x < 0:
            self.direction.x *= -1        


    def update(self):
        self.walking_route()
