import pygame.font

from pygame.sprite import Group
import colors
from ship import Ship

class LeaderBoard():
	# Class to report scoring information

	def __init__(self, settings, screen):
		# Initialize scorekeeping attributes
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.settings = settings
		self.stats = None

		# Font settings for leaderboard
		self.font = pygame.font.SysFont(None, 48)

	def prep(self):
		i = 1
		move = 0
		for d in self.stats.top_scores:
			for name, score in d.items():
				if i <= 10:
					move += 50
					self.check_current_score(score)
					self.prep_scores(score, move)
					self.prep_names(name, move)
				i += 1


	def check_current_score(self, score):
		# Check if the latest score was a high score
		if self.stats.score == score:
			self.text_color = colors.yellow
		else:
			self.text_color = colors.white


	def prep_scores(self, score, move):
		# Turn the scores into a rendered image
		rounded_score = int(round(score, -1))
		score_str = "{:,}".format(rounded_score)
		score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
		score_image_rect = score_image.get_rect()
		score_image_rect.y =  self.score_header_rect.y + move
		score_image_rect.right = self.score_header_rect.right
		return score_image, score_image_rect


	def prep_names(self, name, move):
		# Turn the names into a rendered image
		name_image = self.font.render(name.title(), True, self.text_color, self.settings.bg_color)
		name_image_rect = name_image.get_rect()
		name_image_rect.y =  self.name_header_rect.y + move
		name_image_rect.right =  self.name_header_rect.right
		return name_image, name_image_rect


	def prep_ranks(self, rank, move):
		# Turn the place rankings into a rendered image
		if rank == 1:
			rank_str = str(rank) + "st"
		elif rank == 2:
			rank_str = str(rank) + "nd"
		elif rank == 3:
			rank_str = str(rank) + "rd"
		else:
			rank_str = str(rank) + "th"

		rank_image = self.font.render(rank_str, True, self.text_color, self.settings.bg_color)
		rank_image_rect = rank_image.get_rect()
		rank_image_rect.y = self.rank_header_rect.y + move
		rank_image_rect.right = self.rank_header_rect.right
		return rank_image, rank_image_rect


	def draw_header(self):
		# Draw the header of the leaderboard to the screen
		score_header_image = self.font.render("Score", True, colors.cyan, self.settings.bg_color)
		name_header_image = self.font.render("Name", True, colors.cyan, self.settings.bg_color)
		rank_header_image = self.font.render("Rank", True, colors.cyan, self.settings.bg_color)

		self.score_header_rect = score_header_image.get_rect()
		self.name_header_rect = name_header_image.get_rect()
		self.rank_header_rect = rank_header_image.get_rect()

		self.score_header_rect.x = (self.screen_rect.left + 300)
		self.score_header_rect.y = (self.screen_rect.top + 100)

		self.name_header_rect.x = (self.screen_rect.right - 150)
		self.name_header_rect.y = (self.screen_rect.top + 100)

		self.rank_header_rect.x = self.score_header_rect.x - 200
		self.rank_header_rect.y = self.score_header_rect.y

		self.screen.blit(score_header_image, self.score_header_rect)
		self.screen.blit(name_header_image, self.name_header_rect)
		self.screen.blit(rank_header_image, self.rank_header_rect)


	def draw_game_over(self):
		# Draw 'Game Over' at the top of the screen
		game_over_image = self.font.render("Game Over.", True, colors.red, self.settings.bg_color)
		game_over_image_rect = game_over_image.get_rect()
		game_over_image_rect.centerx = self.screen_rect.centerx
		game_over_image_rect.top = self.screen_rect.top + 20
		self.screen.blit(game_over_image, game_over_image_rect)


	def draw_leaderboard(self):
		# Draw the leaderboard
		self.draw_header()
		self.draw_game_over()
		rank = 1
		move = 20
		for d in self.stats.top_scores:
			for name, score in d.items():
				if rank <= 10:
					move += 50
					self.check_current_score(score)
					score_image, score_rect = self.prep_scores(score, move)
					name_image, name_rect = self.prep_names(name, move)
					rank_image, rank_rect = self.prep_ranks(rank, move)
					self.screen.blit(name_image, name_rect)
					self.screen.blit(rank_image, rank_rect)
					self.screen.blit(score_image, score_rect)
				rank += 1
