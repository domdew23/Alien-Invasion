import pygame.font

from pygame.sprite import Group
from ship import Ship

class LeaderBoard():
	# Class to report scoring information

	def __init__(self, settings, screen):
		# Initialize scorekeeping attributes
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.settings = settings
		#self.stats = stats
		self.stats = None

		self.score_images = []
		self.name_images = []
		self.score_rects = []
		self.name_rects = []
		self.places = []
		self.place_rects = []

		# Font settings for leaderboard
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		#self.prep()

		print("made new leadeboard")
		print(self.score_images)

	def prep(self):
		i = 1
		move = 0
		for d in self.stats.top_scores:
			for name, score in d.items():
				if i <= 10:
					move += 50
					self.prep_scores(score, move)
					self.prep_names(name, move)
				i += 1


	def prep_scores(self, score, move):
		# Turn the scores into a rendered image
		rounded_score = int(round(score, -1))
		score_str = "{:,}".format(rounded_score)
		score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
		score_image_rect = score_image.get_rect()
		score_image_rect.y = (self.screen_rect.top + 100) + move
		score_image_rect.x = (self.screen_rect.right - 150)
		self.score_images.append(score_image)
		self.score_rects.append(score_image_rect)


	def prep_names(self, name, move):
		# Display score at the top right of the screen
		name_image = self.font.render(name.title(), True, self.text_color, self.settings.bg_color)
		name_image_rect = name_image.get_rect()
		name_image_rect.y = (self.screen_rect.top + 100) + move
		name_image_rect.x = (self.screen_rect.left + 300)
		self.name_images.append(name_image)
		self.name_rects.append(name_image_rect)


	def prep_places(self, place, name_rect):
		if place == 1:
			place_str = str(place) + "st"
		elif place == 2:
			place_str = str(place) + "nd"
		elif place == 3:
			place_str = str(place) + "rd"
		else:
			place_str = str(place) + "th"

		place_image = self.font.render(place_str, True, self.text_color, self.settings.bg_color)
		place_image_rect = place_image.get_rect()
		place_image_rect.centery = name_rect.centery
		place_image_rect.centerx = name_rect.centerx - 100
		return place_image, place_image_rect


	def draw_header(self):
		score_header_image = self.font.render("Score", True, self.text_color, self.settings.bg_color)
		name_header_image = self.font.render("Name", True, self.text_color, self.settings.bg_color)
		#level_header_image = self.font.render("Level", True, self.text_color, self.settings.bg_color)

		score_header_rect = score_header_image.get_rect()
		name_header_rect = name_header_image.get_rect()
		#level_header_rect = level_header_image.get_rect()

		score_header_rect.right = self.score_rects[0].right
		score_header_rect.centery = self.score_rects[0].centery - 50

		name_header_rect.right = self.name_rects[0].right
		name_header_rect.centery = self.name_rects[0].centery - 50

		self.screen.blit(score_header_image, score_header_rect)
		self.screen.blit(name_header_image, name_header_rect)


	def draw_game_over(self):
		game_over_image = self.font.render("Game Over.", True, self.text_color, self.settings.bg_color)
		game_over_image_rect = game_over_image.get_rect()
		game_over_image_rect.centerx = self.screen_rect.centerx
		game_over_image_rect.top = self.screen_rect.top + 20
		self.screen.blit(game_over_image, game_over_image_rect)

	def draw_leaderboard(self):
		i = 1
		for name_image,name_rect in zip(self.name_images, self.name_rects):
			place_image, place_image_rect = self.prep_places(i, name_rect)
			self.screen.blit(name_image, name_rect)
			self.screen.blit(place_image, place_image_rect)
			i += 1
		for score_image,score_rect in zip(self.score_images, self.score_rects):
			self.screen.blit(score_image, score_rect)

		self.draw_header()
		self.draw_game_over()

