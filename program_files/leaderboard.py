import pygame.font

from pygame.sprite import Group
from ship import Ship

class LeaderBoard():
	# Class to report scoring information

	def __init__(self, settings, screen, stats):
		# Initialize scorekeeping attributes
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.settings = settings
		self.stats = stats

		self.score_images = []
		self.name_images = []
		self.score_rects = []
		self.name_rects = []


		# Font settings for leaderboard
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		self.prep()

		print(str(len(self.name_images)))
		for im in self.name_images:
			print(im)
			r = im.get_rect()
			print(str(r.centerx))

	def prep(self):
		i = 0
		move = 0
		for d in self.stats.top_scores:
			for name, score in d.items():
				if i < 10:
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
		score_image_rect.y = (self.screen_rect.top + 10) + move
		score_image_rect.x = (self.screen_rect.right - 100)
		self.score_images.append(score_image)
		self.score_rects.append(score_image_rect)


	def prep_names(self, name, move):
		# Display score at the top right of the screen
		name_image = self.font.render(name.title(), True, self.text_color, self.settings.bg_color)
		name_image_rect = name_image.get_rect()
		name_image_rect.y = (self.screen_rect.top + 10) + move
		name_image_rect.x = (self.screen_rect.left + 100)
		self.name_images.append(name_image)
		self.name_rects.append(name_image_rect)


	def draw_leaderboard(self):
		for name_image,name_rect in zip(self.name_images, self.name_rects):
			self.screen.blit(name_image, name_rect)
		for score_image,score_rect in zip(self.score_images, self.score_rects):
			self.screen.blit(score_image, score_rect)
