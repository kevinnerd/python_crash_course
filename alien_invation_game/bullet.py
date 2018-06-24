import pygame
from pygame.sprite import Sprite
from settings import Settings

class Bullet(Sprite):
    """a class to manage bullets fired from the ship"""

    def __init__(self, settings, screen, ship):
        """create a bullet obj at the ship's current location"""
        super(Bullet, self).__init__()
        self.screen = screen
        # create a bullet rect at (0, 0) and set correct position
        self.rect = pygame.Rect(0, 0, settings.bullet_width, 
            settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor
    
    def update(self):
        """move the bullet up to screen"""
        # update bullet position
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)