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
		self.font = pygame.font.Font(settings.text_font, 24)


	def check_current_score(self, score, rank):
		# Check if the latest score was a high score
		self.text_color = colors.white
		if self.stats.score == score:
			if self.stats.score_rank == 0:
				self.stats.score_rank = rank
			elif self.stats.score_rank == rank:
				self.text_color = colors.yellow


	def prep_score(self, score, move):
		# Turn the scores into a rendered image
		rounded_score = int(round(score, -1))
		score_str = "{:,}".format(rounded_score)
		score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
		score_image_rect = score_image.get_rect()
		score_image_rect.y =  self.score_header_rect.y + move
		score_image_rect.right = self.score_header_rect.right
		return score_image, score_image_rect


	def prep_name(self, name, move):
		# Turn the names into a rendered image
		name_image = self.font.render(name.title(), True, self.text_color, self.settings.bg_color)
		name_image_rect = name_image.get_rect()
		name_image_rect.y =  self.name_header_rect.y + move
		name_image_rect.right =  self.name_header_rect.right
		return name_image, name_image_rect


	def prep_level(self, level, move):
		# Turn the names into a rendered image
		level_image = self.font.render(str(level), True, self.text_color, self.settings.bg_color)
		level_image_rect = level_image.get_rect()
		level_image_rect.y =  self.level_header_rect.y + move
		level_image_rect.right =  self.level_header_rect.right
		return level_image, level_image_rect


	def prep_rank(self, rank, move):
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
		level_header_image = self.font.render("Level", True, colors.cyan, self.settings.bg_color)


		self.score_header_rect = score_header_image.get_rect()
		self.name_header_rect = name_header_image.get_rect()
		self.rank_header_rect = rank_header_image.get_rect()
		self.level_header_rect = level_header_image.get_rect()

		self.score_header_rect.x = (self.screen_rect.left + 400)
		self.score_header_rect.y = (self.screen_rect.top + 130)

		self.name_header_rect.x = (self.screen_rect.right - 150)
		self.name_header_rect.y = self.score_header_rect.y

		self.rank_header_rect.x = self.score_header_rect.x - 300
		self.rank_header_rect.y = self.score_header_rect.y

		self.level_header_rect.x = self.name_header_rect.x - 200
		self.level_header_rect.y = self.score_header_rect.y

		self.screen.blit(score_header_image, self.score_header_rect)
		self.screen.blit(name_header_image, self.name_header_rect)
		self.screen.blit(rank_header_image, self.rank_header_rect)
		self.screen.blit(level_header_image, self.level_header_rect)


	def draw_game_over(self):
		# Draw 'Game Over' at the top of the screen
		game_over_image = self.font.render("Game Over.", True, colors.red, self.settings.bg_color)
		game_over_image_rect = game_over_image.get_rect()
		game_over_image_rect.centerx = self.screen_rect.centerx - 350
		game_over_image_rect.top = self.screen_rect.top + 3
		self.screen.blit(game_over_image, game_over_image_rect)


	def draw_score(self):
		self.screen.blit(self.name_image, self.name_rect)
		self.screen.blit(self.rank_image, self.rank_rect)
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.level_image, self.level_rect)


	def draw_leaderboard(self):
		# Draw the leaderboard
		self.draw_header()
		#self.draw_game_over()
		rank = 1
		move = 20
		for d in self.stats.top_scores:
			if rank <= 10:
				move += 50
				self.check_current_score(d['score'], rank) 
				for key, value in d.items():
						if key == 'username':
							self.name_image, self.name_rect = self.prep_name(value, move)
						elif key == 'score':
							score = value
							self.score_image, self.score_rect = self.prep_score(value, move)
						elif key == 'level':
							self.level_image, self.level_rect = self.prep_level(value, move)
				self.rank_image, self.rank_rect = self.prep_rank(rank, move)
				self.draw_score()
				rank += 1