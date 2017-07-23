import pygame.font
import colors

from pygame.sprite import Group
from ship import Ship

class Scoreboard():
	# Class to report scoring information

	def __init__(self, settings, screen, stats):
		# Initialize scorekeeping attributes
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.settings = settings
		self.stats = stats

		# Font settings for scoreboard
		self.text_color = colors.white
		self.font = pygame.font.SysFont(None, 48)
		

	def draw_score(self):
		# Turn the score into a rendered image
		your_score_image = self.font.render("Your Score", True, colors.red, self.settings.bg_color)
		your_score_rect = your_score_image.get_rect()
		your_score_rect.right = self.screen_rect.right - 20
		your_score_rect.top = self.screen_rect.top + 3

		rounded_score = int(round(self.stats.score, -1))
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)


		# Display score at the top right of the screen
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = your_score_rect.right
		self.score_rect.y = your_score_rect.bottom + 15

		self.screen.blit(your_score_image, your_score_rect)
		self.screen.blit(self.score_image, self.score_rect)


	def draw_high_score(self):
		# Turn the high score into a rendered image
		high_score = int(round(self.stats.high_score, -1))
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

		# Center high score at the top of the screen
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.screen_rect.top + 45
		self.screen.blit(self.high_score_image, self.high_score_rect)


	def draw_level(self):
		# Turn the level into a rendered image
		level = "Level: " + str(self.stats.level)
		self.level_image = self.font.render(level, True, colors.red, self.settings.bg_color)

		# Position the level below the score
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.high_score_rect.left - 300
		self.level_rect.top = self.screen_rect.top + 13
		self.screen.blit(self.level_image, self.level_rect)



	def draw_ships(self):
		# Show how many ships are left
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.screen, self.settings, False)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)


	def draw_text(self):
		self.high_score_text_image = self.font.render("High Score", True, colors.red, self.settings.bg_color)
		self.high_score_text_rect = self.high_score_text_image.get_rect()
		self.high_score_text_rect.centerx = self.screen_rect.centerx
		self.high_score_text_rect.top = self.screen_rect.top + 3
		self.screen.blit(self.high_score_text_image, self.high_score_text_rect)


	def show_score(self):
		# Draw score to screen
		self.draw_score()
		self.draw_high_score()
		self.draw_level()
		self.draw_ships()
		self.draw_text()

		# Draw ships
		self.ships.draw(self.screen)