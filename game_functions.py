import sys
import pygame
from bullet import Bullet

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
def update_screen(settings, screen, ship, bullets):
  """ Update images on the screen and flip to the new screen. """
  screen.fill(settings.bg_color)

  # Redraw all bullets behind ship and alients.
  for bullet in bullets.sprites():
    bullet.draw_bullet()

  ship.blitme()
  
def update_bullets(bullets):
  """ Update position of bullets and get rif of old bullets """
  # Update bullet positions
  bullets.update()

  # Get rid of bullets that have dissapeared
  for bullet in bullets.copy():
      if bullet.rect.top <= 0:
        bullets.remove(bullet)