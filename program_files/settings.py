'''
-Contains the Settings class
-Settings class contains only the __init__() method whihc initializes attributes controlling games apparance and ship's speed
'''


class Settings():
	# Class to store all settings for Alien Invasion

	def __init__(self):
		# Initialize game's static settings
		self.screen_x = 1310
		self.screen_y = 800
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_limit = 3

		# Bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3

		# Alien settings
		self.fleet_drop_speed = 10

		# How quickly the game speeds up
		self.speedup_scale = 1.2

		# Scale for increasing point values
		self.score_scale = 1.5

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		# Initialize settings that change throughout the game
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1

		# fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1

		# Scoring
		self.alien_points = 50


	def increase_speed(self):
		# Increase speed settings and point values
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
		print("ALIENS ARE NOW WORTH " + str(self.alien_points) + " POINTS EACH")



