import game_functions as gf
import pygame
import string
import colors

from pygame.locals import *
from button import Button

def get_input_key(settings, stats, screen, sb, ship, aliens, bullets, play_button):
	while True:
		event = pygame.event.poll()
		if event.type == KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()
			else:
				return event.key
		elif event.type == pygame.QUIT:
			sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			# guest
			return 4422
		else:
			pass


def display_box(settings, stats, screen, sb, lb, ship, aliens, bullets, play_button, message):
	# Print a message in a box in the middle of the screen 
	box_width, box_height = 320, 50
	box_x, box_y = (screen.get_width() / 2) - 158, (screen.get_height() / 2) - 50
	fontobject = pygame.font.Font(None,18)

	# Black background
	pygame.draw.rect(screen, colors.black, (box_x, box_y, box_width, box_height))
	# White border
	pygame.draw.rect(screen, colors.white, (box_x - 2, box_y - 2, box_width + 4, box_height + 4), 1)

	if len(message) != 0:
		screen.blit(fontobject.render(message, 1, colors.white), (box_x, box_y))
	gf.update_screen(settings, stats, screen, sb,lb, ship, aliens, bullets, play_button)

def get_username(settings, stats, screen, sb, lb, ship, aliens, bullets, play_button, message):
	# ask(screen, question) -> answer
	pygame.font.init()
	current_string = []
	string = ""
	display_box(settings, stats, screen, sb, lb, ship, aliens, bullets, play_button, message + string.join(current_string))

	while True:
		inkey = get_input_key(settings, stats, screen, sb, ship, aliens, bullets, play_button)
		if inkey == K_BACKSPACE:
		  current_string = current_string[0:-1]
		elif inkey == K_RETURN:
			break
		elif inkey == K_MINUS:
		  current_string.append("_")
		elif inkey == 4422 and not current_string:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			if gf.respond_play_button(settings, stats, screen, sb, lb, ship, aliens, bullets, play_button, mouse_x, mouse_y):
				return 'Guest'
			else:
				break
		elif inkey <= 127:
		  current_string.append(chr(inkey))
		if current_string:
			show_button(settings, screen)
		else:
			del_button(settings, stats, screen, sb, lb, ship, aliens, bullets, play_button, message)

		display_box(settings, stats, screen, sb, lb, ship, aliens, bullets, play_button, message + string.join(current_string))
	return string.join(current_string)


def show_button(settings, screen):
	press_enter_to_play = Button(settings, screen, "Press Enter to Play", adj_y=120)
	press_enter_to_play.draw()


def del_button(settings, stats, screen, sb, lb, ship, aliens, bullets, play_button, message):
	screen.fill(settings.bg_color)
	play_button.draw()
	display_box(settings, stats, screen, sb, lb, ship, aliens, bullets, play_button, message)


def no_username(settings, screen, play_button, message):
	font = pygame.font.SysFont(None, 48)
	text_image = font.render(message, True, colors.white, settings.bg_color)

	text_rect = text_image.get_rect()
	play_button_rect = play_button.get_rect()
	text_rect.centerx = play_button_rect.centerx
	text_rect.top = play_button_rect.top - 150
	screen.blit(text_image, text_rect)