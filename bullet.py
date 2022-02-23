import pygame


class Bullet:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def get_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and not self.shooting:
            print(self.shooting)
            self.shooting = True
            b = Bullet(self.rect.x, self.rect.y, 7, "Green", 1)
            b.shoot_bullet()

    def shoot_bullet(self):
        pygame.draw.circle(
            pygame.display.get_surface(), self.color, (self.x, self.y), self.radius
        )

    def update(self):
        self.get_input()
        self.get_player_orientation()
