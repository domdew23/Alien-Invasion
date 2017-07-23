import json
import game_functions as gf
class GameStats():
	# Track statistics ffor Alien Invasion

	def __init__(self, settings):
		# Initialize settings
		self.settings = settings
		self.reset()

		# Start game in inactive state
		self.game_active = False
		self.game_over = False

		# High Score should never be reset
		self.high_score = 0

		self.user = ''
		self.top_scores = []
		self.score_rank = 0


	def reset(self):
		# Initialize statistics that can change during game
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1
		self.score_rank = 0
