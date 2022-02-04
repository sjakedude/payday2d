import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("assets/player.png"), (50, 50))
        self.rect = self.image.get_rect(topleft = pos)


