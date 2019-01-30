import sys
import pygame
from bullet import Bullet
from alien import Alien

def get_number_aliens_x(settings, alien_width):
  """ Determine the number of aliens that fit into a row. """
  available_space_x = settings.screen_width - 2 * alien_width
  number_aliens_x = int(available_space_x / (2 * alien_width))
  return number_aliens_x

def get_number_rows(settings, ship_height, alien_height):
  """ Determine the number of rows of aliens that fit on the screen. """
  available_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
  number_rows = int(available_space_y / (2 * alien_height))
  return number_rows

def create_alien(settings, screen, aliens, alien_number, row_number):
  """ Create an alien and place it in the row. """
  alien = Alien(settings, screen)
  alien_width = alien.rect.width
  alien.x = (alien_width + 1.7 * alien_width * alien_number)
  alien.rect.x = alien.x
  alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
  aliens.add(alien)

def create_fleet(settings, screen, ship, aliens):
  """ Create a full fleet of aliens. """
  # Create an alien and find the number of aliens in a row.
  alien = Alien(settings, screen)
  number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
  number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)
  # Create the first row of aliens.
  for number_rows in range(number_rows):
    for alien_number in range(number_aliens_x):
      create_alien(settings, screen, aliens, alien_number, number_rows)

def check_keydown_events(event, settings, screen, ship, bullets):
  # Move the  ship to the right
  if event.key == pygame.K_RIGHT:
    ship.moving_right = True
  # Move the ship to the left
  if event.key == pygame.K_LEFT:
    ship.moving_left = True
  # Create a bullet
  if event.key == pygame.K_SPACE:
    # Create a new bullet and add it to the bullet group
    if len(bullets) < settings.bullets_allowed:
      new_bullet = Bullet(settings, screen, ship)
      bullets.add(new_bullet)

def check_keyup_events(event, ship):  
  # Stop movement to the right
  if event.key == pygame.K_RIGHT:
    ship.moving_right = False
  # Stop movement to the right
  if event.key == pygame.K_LEFT:
    ship.moving_left = False

def check_events(settings, screen, ship, bullets):
  """ Respond to keypresses and mouse events. """
  # Watch for keybaord and mouse events.
  for event in pygame.event.get():
    # Close the screen when the X button is pressed
    if event.type == pygame.QUIT:
      sys.exit()
    # Check for keydown events
    if event.type == pygame.KEYDOWN:
      check_keydown_events(event, settings, screen, ship, bullets)
    # Check for keyup events
    if event.type == pygame.KEYUP:
      check_keyup_events(event, ship)
  
# Redraw the screen during each pass through the loop.
def update_screen(settings, screen, ship, aliens, bullets):
  """ Update images on the screen and flip to the new screen. """
  screen.fill(settings.bg_color)
  # Redraw all bullets behind ship and alients.
  for bullet in bullets.sprites():
    bullet.draw_bullet()
  ship.blitme()
  aliens.draw(screen)
  # Make the most recently drawn screen visible.
  pygame.display.flip()
  
  
def update_bullets(aliens, bullets):
  """ Update position of bullets and get rif of old bullets """
  # Update bullet positions
  bullets.update()
  # Get rid of bullets that have dissapeared
  for bullet in bullets.copy():
      if bullet.rect.top <= 0:
        bullets.remove(bullet)
  # Check for any bullets that have hit aliens. If so, get rid of the bullet and the alien.
  collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

def change_fleet_direction(settings, aliens):
  """ Drop the entire fleet and change the fleet's direction. """
  for alien in aliens.sprites():
    alien.rect.y += settings.fleet_drop_speed
  settings.fleet_direction *= -1

def check_fleet_edges(settings, aliens):
  """ Respond appropriately if any aliens have reached an edge. """
  for alien in aliens.sprites():
    if alien.check_edges():
      change_fleet_direction(settings, aliens)
      break

def update_aliens(settings, aliens):
  """ Update the positions of all aliens in the fleet. """
  check_fleet_edges(settings, aliens)
  aliens.update()
