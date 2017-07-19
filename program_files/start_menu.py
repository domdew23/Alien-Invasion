import pygame, pygame.font, pygame.event, pygame.draw, string
import sys

from pygame.locals import *


class StartMenu():
	# Display the start menu

	def __init__(self, screen):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.box_width, self.box_height = 320, 50
		self.box_x, self.box_y = (self.screen.get_width() / 2) - 158, (self.screen.get_height() / 2) - 50

		# Font settings
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

	def get_key(self):
		while 1:
			event = pygame.event.poll()
			if event.type == KEYDOWN:
				if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
					sys.exit()
				else:
					return event.key
			elif event.type == pygame.QUIT:
				sys.exit()
			else:
				pass

	def display_box(self, message):
	  # Print a message in a box in the middle of the screen 
	  fontobject = pygame.font.Font(None,18)
	  # Black background
	  pygame.draw.rect(self.screen, (0,0,0), (self.box_x, self.box_y, self.box_width, self.box_height))
	  # White border
	  pygame.draw.rect(self.screen, (255,255,255), (self.box_x - 2, self.box_y - 2, self.box_width + 4, self.box_height + 4), 1)

	  if len(message) != 0:
	    self.screen.blit(fontobject.render(message, 1, (255,255,255)), (self.box_x, self.box_y))
	  pygame.display.flip()

	def ask(self, question):
	  # ask(screen, question) -> answer
	  pygame.font.init()
	  current_string = []
	  string = ""
	  self.display_box(question + string.join(current_string))
	  while 1:
	    inkey = self.get_key()
	    if inkey == K_BACKSPACE:
	      current_string = current_string[0:-1]
	    elif inkey == K_RETURN:
	      break
	    elif inkey == K_MINUS:
	      current_string.append("_")
	    elif inkey <= 127:
	      current_string.append(chr(inkey))
	    self.display_box(question + string.join(current_string))
	  return string.join(current_string)