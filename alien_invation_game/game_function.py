import sys
import pygame
from settings import Settings
from bullet import Bullet
from alien import Alien

def check_events(settings, screen, ship, bullets):
    """response to game event: mouse/key event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(settings, screen, ship, bullets):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(settings, screen, ship, aliens, bullets):
    # redraw the screen 
    screen.fill(settings.bg_color)
    # refresh the ship
    ship.blitme()
    aliens.draw(screen)
    # redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_fleet(settings, screen, aliens):
    number_aliens_x = get_number_aliens_x(settings, screen)
    # create the first row of aliens
    for alien_number in range(number_aliens_x):
        create_alien(settings, screen, alien_number, aliens)

def create_alien(settings, screen, alien_number, aliens):
    alien = Alien(settings, screen)
    alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

def get_number_aliens_x(settings, screen):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    avaliable_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(avaliable_space_x / (2 * alien_width))
    return number_aliens_x