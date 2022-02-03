import pygame
import os
from parse_level import LevelParser

# WIDTH AND HEIGHT MUST BE DIVISIBLE BY 6
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Payday2D")

# Colors
GREEN = (0, 99, 0)
BLACK = (0, 0, 0)

# Settings
VELOCITY = 2
FPS = 60

# Player sprite setup
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
PLAYER_IMAGE = pygame.image.load("assets/player.png")
PLAYER = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))

# Level generation
level_parser = LevelParser(WIDTH, HEIGHT)


def draw_window(player_rect, barriers):
    WIN.fill(GREEN)
    WIN.blit(PLAYER, (player_rect.x, player_rect.y))
    for wall in barriers:
        pygame.draw.rect(WIN, BLACK, wall)
    pygame.display.update()


def move_player_within_bounds(player, barriers, direction):
    movement_is_within_bounds = True
    
    for barrier in barriers:
        if player.colliderect(barrier):
            if (
                direction == "up"
                and abs(player.top - barrier.bottom) < collision_tolerance
            ):
                player.y = barrier.bottom + collision_tolerance
            if (
                direction == "down"
                and abs(player.bottom - barrier.top) < collision_tolerance
            ):
                player.y = barrier.top - collision_tolerance
            if (
                direction == "right"
                and abs(player.right - barrier.left) < collision_tolerance
            ):
                player.x = barrier.left - collision_tolerance
            if (
                direction == "left"
                and abs(player.left - barrier.right) < collision_tolerance
            ):
                player.x = barrier.right + collision_tolerance

    return movement_is_within_bounds


def handle_player_movement(keys_pressed, player, barriers):
    collision_tolerance = 5
    if keys_pressed[pygame.K_w] and player.y + VELOCITY > 0:
        for barrier in barriers:
            if player.colliderect(barrier) and abs(player.top - barrier.bottom) < collision_tolerance:
                player.y = barrier.bottom
                return
        player.y -= VELOCITY
    if keys_pressed[pygame.K_a] and player.x + VELOCITY > 0:
        for barrier in barriers:
            if player.colliderect(barrier) and abs(player.left - barrier.right) < collision_tolerance:
                player.x = barrier.right
                return
        player.x -= VELOCITY    
    if keys_pressed[pygame.K_s] and player.y + PLAYER_HEIGHT - VELOCITY < HEIGHT:
        for barrier in barriers:
            if player.colliderect(barrier) and abs(player.bottom - barrier.top) < collision_tolerance:
                player.y = barrier.top - PLAYER_HEIGHT
                return
        player.y += VELOCITY 
    if keys_pressed[pygame.K_d] and player.x + PLAYER_WIDTH - VELOCITY < WIDTH:
        for barrier in barriers:
            if player.colliderect(barrier) and abs(player.right - barrier.left) < collision_tolerance:
                player.x = barrier.left - PLAYER_WIDTH
                return
        player.x += VELOCITY 

def main():
    player_rect = pygame.Rect(100, 100, PLAYER_WIDTH, PLAYER_HEIGHT)
    barriers = level_parser.load_level(WIN)
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys_pressed = pygame.key.get_pressed()
        handle_player_movement(keys_pressed, player_rect, barriers)
        draw_window(player_rect, barriers)
    pygame.quit()


if __name__ == "__main__":
    main()
