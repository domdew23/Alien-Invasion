import pygame

class Button():

	def __init__(self, settings, screen, msg):
		# Initialize button attributes
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.settings = settings
		
		# Build the button's rect object and center it
		self.rect = pygame.Rect(0, 0, self.settings.button_width, self.settings.button_height)
		self.rect.center = self.screen_rect.center
		self.rect.centery = self.screen_rect.centery + 60

		# The button message needs to be prepped only once
		self.prep_msg(msg)


	def prep_msg(self, msg):
		# Turn msg into a rendered image and center text on the button
		self.msg_image = self.settings.button_font.render(msg, True, self.settings.button_text_color, self.settings.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center


	def draw(self):
		# Draw blank button and then draw message
		self.screen.fill(self.settings.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)