import sys
import pygame
from settings import Settings
from ship import Ship
from game_functions import check_events, update_screen

def run_game():
  # Initialize game and create a screen object.
  pygame.init()
  settings = Settings()
  pygame.display.set_caption("Alien Invasion")
  screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
  ship = Ship(screen, settings)

  # Start the main loop for the game.
  while True:
    # Check events from game_functions module
    check_events(ship)

    # Update the location of the ship
    ship.update()

    # Redraw the screen during each pass through the loop.
    
    update_screen(settings, screen, ship)

    # Make the most recently drawn screen visible.
    pygame.display.flip()

run_game()