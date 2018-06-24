import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class to represent a single alien in the fleet"""
    def __init__(self, settings, screen):
        """init alien and set starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings
        # load alien image and set its rect attr
        self.image = pygame.image.load('images/alien.gif')
        self.rect = self.image.get_rect()
        # start each new alien near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)