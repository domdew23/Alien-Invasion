'''
-The main file, creates a number of important objects used throughout the game:
-the settings are stored in settings
-the main display surface is stored in screen
-a ship instance is created as well
-also contains the main loop of the game which is a while loops that calls: check_events, ship.update() and update_screen()
-run this file to play Alien Invasion
'''
import pygame
import game_functions as gf
import sys

from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from leaderboard import LeaderBoard
from  pygame.sprite import Group

def run_game():
	# Initialize pygame, settings and create a screen object 
	pygame.init()
	settings = Settings()

	screen = pygame.display.set_mode((settings.screen_x, settings.screen_y))
	pygame.display.set_caption("Alien Invasion")

	# Make the Play as Guest Button
	play_button = Button(settings, screen, "Play as Guest", adj_y=60)

	# Create a instance to store game stats and create a scoreboard, leaderboard
	stats = GameStats(settings)
	sb = Scoreboard(settings, screen, stats)
	lb = LeaderBoard(settings, screen)

	# Create a ship, alien, and groups to store bullets and alien fleet
	ship = Ship(screen, settings)
	alien = Alien(settings, screen)
	bullets = Group()
	aliens = Group()

	# Create the fleet of aliens
	gf.create_fleet(settings, screen, ship, aliens)

	# Load in all time scores
	gf.all_time_scores(stats,settings)

	# Start the main loop for the game
	while True:
		gf.check_events(settings, stats, screen, sb, lb, ship, aliens, bullets, play_button)
		if stats.game_active:
			ship.update()
			gf.update_bullets(settings, stats, screen, sb, ship, aliens, bullets)
			gf.update_aliens(settings, stats, screen, sb, lb, ship, aliens, bullets)
		gf.update_screen(settings, stats, screen, sb, lb, ship, aliens, bullets, play_button, True)
		
run_game()



