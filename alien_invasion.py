import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_functions import check_events, update_screen, update_bullets, create_fleet

def run_game():
  # Initialize game and create a screen object.
  pygame.init()
  settings = Settings()
  pygame.display.set_caption("Alien Invasion")
  screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
  
  # Make a ship, a group of bullets, and a group of aliens.
  ship = Ship(screen, settings)
  bullets = Group()
  aliens = Group()

  # Create the fleet of aliens
  create_fleet(settings, screen, ship, aliens)

  # Start the main loop for the game.
  while True:
    # Check events from game_functions module
    check_events(settings, screen, ship, bullets)

    # Update the location of the ship
    ship.update()

    # Update bullets
    update_bullets(bullets)

    # Redraw the screen during each pass through the loop.
    update_screen(settings, screen, ship, aliens, bullets)

run_game()
