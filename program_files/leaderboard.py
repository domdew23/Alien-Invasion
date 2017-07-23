import pygame.font
import colors

from pygame.sprite import Group
from ship import Ship

class LeaderBoard():
	# Class to report the all time score

	def __init__(self, settings, screen):
		# Initialize attributes
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.settings = settings
		self.stats = None

		# Font settings for leaderboard
		self.font = pygame.font.SysFont(None, 48)


	def check_current_score(self, score, rank):
		# Check if the latest score was a high score
		if self.stats.score == score:
			if self.stats.score_rank == 0:
				self.stats.score_rank = rank
			elif self.stats.score_rank == rank:
				self.text_color = colors.yellow
			else:
				self.text_color = colors.white
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
		self.score_header_rect.y = (self.screen_rect.top + 130)

		self.name_header_rect.x = (self.screen_rect.right - 150)
		self.name_header_rect.y = self.score_header_rect.y

		self.rank_header_rect.x = self.score_header_rect.x - 200
		self.rank_header_rect.y = self.score_header_rect.y

		self.screen.blit(score_header_image, self.score_header_rect)
		self.screen.blit(name_header_image, self.name_header_rect)
		self.screen.blit(rank_header_image, self.rank_header_rect)


	def draw_your_score(self):
		your_score_image = self.font.render("Your Score", True, colors.red, self.settings.bg_color)
		rounded_score = int(round(self.stats.score, -1))
		score_str = "{:,}".format(rounded_score)
		score_image = self.font.render(score_str, True, colors.white, self.settings.bg_color)
		your_score_rect = your_score_image.get_rect()
		score_rect = score_image.get_rect()

		your_score_rect.right = self.name_header_rect.right
		your_score_rect.top = self.screen_rect.top + 3

		score_rect.right = your_score_rect.right
		score_rect.y = your_score_rect.bottom + 15

		self.screen.blit(your_score_image, your_score_rect)
		self.screen.blit(score_image, score_rect)


	def draw_game_over(self):
		# Draw 'Game Over' at the top of the screen
		game_over_image = self.font.render("Game Over.", True, colors.red, self.settings.bg_color)
		game_over_image_rect = game_over_image.get_rect()
		game_over_image_rect.centerx = self.screen_rect.centerx - 350
		game_over_image_rect.top = self.screen_rect.top + 3
		self.screen.blit(game_over_image, game_over_image_rect)



	def draw_scores(self, score, name, rank, move):
		score_image, score_rect = self.prep_scores(score, move)
		name_image, name_rect = self.prep_names(name, move)
		rank_image, rank_rect = self.prep_ranks(rank, move)
		self.screen.blit(name_image, name_rect)
		self.screen.blit(rank_image, rank_rect)
		self.screen.blit(score_image, score_rect)


	def draw_leaderboard(self):
		# Draw the leaderboard
		self.draw_header()
		self.draw_game_over()
		self.draw_your_score()
		rank = 1
		move = 20
		for d in self.stats.top_scores:
			for name, score in d.items():
				if rank <= 10:
					move += 50
					self.check_current_score(score, rank)
					self.draw_scores(score, name, rank, move)
				rank += 1
