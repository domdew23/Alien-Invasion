'''
-Contains the Ship class
-update() method manage's the ships position
-blitme() mehtod draws the ship to the screen
-image of the ship is stored in ship.bmp which is in the images folder
'''
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

	def __init__(self, screen, settings, big=True):
		# Initialize the ship and set its starting position
		super().__init__()
		self.screen = screen
		self.settings = settings

		# Load the ship image and get its rect.
		if big:
			self.image = pygame.image.load('../images/game_images/ship_big.bmp')
		else:
			self.image = pygame.image.load('../images/game_images/ship_small.bmp')

		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start each new ship at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Store a decimal value for the ship's center
		self.center = float(self.rect.centerx)

		# Movement flags
		self.moving_right = False
		self.moving_left = False


	def update(self):
		# Update the ship's position based on the movement flag
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.settings.ship_speed_factor
			# print("Ship Moving Right : X-Position: " + str(self.center))

		if self.moving_left and self.rect.left > 0:
			self.center -= self.settings.ship_speed_factor
			# print("Ship Moving Left : X-Position: " + str(self.center))

		# Update rect object from self.center
		self.rect.centerx = self.center


	def center_ship(self):
		# Center ship on the screen
		self.center = self.screen_rect.centerx


	def blitme(self):
		# Draw the ship at it's current location
		self.screen.blit(self.image, self.rect)