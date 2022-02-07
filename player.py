import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("assets/player.png"), (50, 50)
        )
        self.rect = self.image.get_rect(topleft=pos)
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

    def update(self):
        self.get_input()
