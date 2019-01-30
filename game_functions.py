import sys
import pygame

def check_events(ship):
  """ Respond to keypresses and mouse events. """
  
  # Watch for keybaord and mouse events.
  for event in pygame.event.get():
    
    # Close the screen when the X button is pressed
    if event.type == pygame.QUIT:
      sys.exit()
    
    # Move left and right when the left and right arrow keys are pressed
    elif event.type == pygame.KEYDOWN:
      # Move the  ship to the right
      if event.key == pygame.K_RIGHT:
        ship.moving_right = True
      
      # Move the ship to the left
      elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.type == pygame.KEYUP:
      # Stop movement to the right
      if event.key == pygame.K_RIGHT:
        ship.moving_right = False
      
      # Stop movement to the right
      elif event.key == pygame.K_LEFT:
        ship.moving_left = False
  
# Redraw the screen during each pass through the loop.
def update_screen(settings, screen, ship):
  """ Update images on the screen and flip to the new screen. """
  screen.fill(settings.bg_color)
  ship.blitme()
