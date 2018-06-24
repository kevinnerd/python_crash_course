import pygame
from settings import Settings

class Ship():
    def __init__(self, settings, screen):
        """init the ship and set its starting position"""
        self.screen = screen
        self.settings = settings
        # load the ship image and get its rect
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # store the decimal value for the ship's center
        self.center = float(self.rect.centerx)
        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.settings.ship_speed_factor

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)