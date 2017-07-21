'''

'''
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	# Class  to manage bullets fired from the ship

	def __init__(self, settings, screen, ship):
		# Create bullet object at ships current position
		super().__init__()
		self.screen = screen

		# Create a bullet rect at (0,0) and then set correct position
		self.image = pygame.image.load('../images/game_images/bullet.bmp')
		self.image = pygame.transform.scale(self.image, (settings.bullet_width, settings.bullet_height))

		self.rect = self.image.get_rect()
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# Store bullets position as a decimal value
		self.y = float(self.rect.y)
		self.speed_factor = settings.bullet_speed_factor


	def update(self):
		# Move the bullet up  the screen
		# Update the decimal position of the bullet
		self.y -= self.speed_factor
		# Update rect position
		self.rect.y = self.y
	def draw(self):
		# Draw bullet to the screen
		self.screen.blit(self.image, self.rect)