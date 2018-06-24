import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
    # init game and create a screen
    pygame.init()
    # create game settings object
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invation")
    # create a ship object
    ship = Ship(settings, screen)
    # create group of bullets
    bullets = Group()
    # start the main loop for the game
    while True:
        # watch for keyboard event and mouse event
        gf.check_events(settings, screen, ship, bullets)
        # update ship position
        ship.update()
        # update bullets
        gf.update_bullets(bullets)
        # update screen
        gf.update_screen(settings, screen, ship, bullets)

run_game()