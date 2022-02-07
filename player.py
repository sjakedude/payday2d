import pygame
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("assets/player.png"), (50, 50)
        )
        self.image_original = pygame.transform.scale(
            pygame.image.load("assets/player.png"), (50, 50)
        )
        self.rect = self.image.get_rect(center=pos)
        self.position = pos
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 3

    def get_input(self):
        keys = pygame.key.get_pressed()

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

    def get_mouse_pointer(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - (self.rect.x + (self.rect.width / 2)), mouse_y - (self.rect.y + (self.rect.height / 2))
        angle = math.atan2(rel_y, rel_x)
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.image_original, int(angle))
       #self.rect = self.image.get_rect(center=self.position)

    def update(self):
        self.get_input()
        self.get_mouse_pointer()
