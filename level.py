import pygame
from tiles import Tile
from settings import tile_size
from player import Player
from police import Police


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.police = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == "1":
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "2":
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                if cell == "3":
                    police_sprite = Police((x, y))
                    self.police.add(police_sprite)

    def horizontal_movement_collision(self):
        player = self.player.sprite

        player.rect.x += player.direction.x * player.speed
        player.rect.y += player.direction.y * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top

    def police_movement(self):
        police = self.police.sprite
        police.rect.x += police.direction.x * police.speed

    def run(self):

        # level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        # player
        self.player.update()
        self.horizontal_movement_collision()
        self.player.draw(self.display_surface)

        # police
        self.police.update()
        self.police_movement()
        self.police.draw(self.display_surface)
