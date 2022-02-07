import pygame
import os
from settings import *
from level import Level

# WIDTH AND HEIGHT MUST BE DIVISIBLE BY 6
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Payday2D")
clock = pygame.time.Clock()
level = Level(level_map, WIN)
FPS = 60


def main():
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        WIN.fill("black")
        level.run()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
