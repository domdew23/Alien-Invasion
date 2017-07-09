'''
'''
import pygame

from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
	# Class to represent a single alien in the fleet

	def __init__(self, settings, screen):
		# Initialize alien and set its starting position
		super().__init__()
		self.screen = screen
		self.settings = settings

		possible_images = []
		path = '../images/game_images/'
		for x in range(1,5):
			possible_images.append(path + 'alien' + str(x) + '.bmp')

		rand_int = randint(0, len(possible_images) - 1)
		rand_image = possible_images[rand_int]

		# Load alien image and set its rect attribut
		self.image = pygame.image.load(rand_image)
		self.rect = self.image.get_rect()

		# Start each new alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store alein's exact position
		self.x = float(self.rect.x)


	def check_edges(self):
		# Return true if alien is at the edge of the screen
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True


	def update(self):
		# Move alien right
		self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
		self.rect.x = self.x


	def blitme(self):
		# Draw the alien at it's current location
		self.screen.blit(self.image, self.rect)


