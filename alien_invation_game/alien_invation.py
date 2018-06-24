import sys

import pygame

def run_game():
    # init game and create a screen
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invation")

    # start the main loop for the game
    while True:
        # watch for keyboard event and mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

run_game()