import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
  # Initialize game and create a screen object.
  pygame.init()
  stgs = Settings()
  pygame.display.set_caption("Alien Invasion")
  screen = pygame.display.set_mode((stgs.screen_width, stgs.screen_height))
  ship = Ship(screen)

  # Start the main loop for the game.
  while True:
    # Watch for keybaord and mouse events.
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

    # Redraw the screen during each pass through the loop.
    screen.fill(stgs.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

run_game()