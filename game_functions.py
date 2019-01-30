import sys
import pygame

def check_events():
  """ Respond to keypresses and mouse events. """
  
  # Watch for keybaord and mouse events.
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
  
# Redraw the screen during each pass through the loop.
def update_screen(settings, screen, ship):
  """ Update images on the screen and flip to the new screen. """
  screen.fill(settings.bg_color)
  ship.blitme()
