'''
-Contains a number of functions that carry out the bulk of the work in the game

-check_events() function detects relevant events, such as keypresses and releases
-respond_keydown() and respond_keyup() carry out action for specified methods
-update_screen() redraws the escreen on each pass through the main loop
-respond_play_button() starts the game when the play button is pressed
-create_alien() creates a single instance of an Alien
-create_fleet() creates a fleet of Alien objects
-get_number_aliens() get the number of aliens allowed in one row on the screen
-get_number_rows() get maximum number of rows allowed in one screen
-fire_bullet() repsonse when users clicks spacebar
-update_bullets() updates the bullets
-update_aliens() updates the aliens
-ship_hit() responds to the users ship being hits
-check_bullet_alien_collisions() check and respond to alien being shot down
-check_fleet_edges() make sure the fleet does not go off the edge of the screen
-change_fleet_direction() change fleet direction when they reach the edge of the  screen
-check_aliens_bottom() check and respond to aliens reaching the bottom of the screen
-check_high_score() check and respond to new high scores
'''
import sys
import pygame
import json
import colors
import string
import textbox as tb

from bullets import Bullet
from alien import Alien
from button import Button
from leaderboard import LeaderBoard
from time import sleep
from pygame.locals import *


def respond_keydown(event, settings, screen, ship, bullets):
	# Respond to keydown events
	if event.key == pygame.K_RIGHT:
		# Move ship to the right
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(settings, screen, ship, bullets)
	elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
		print("GAME QUIT")
		sys.exit()
	else:
		pass


def respond_keyup(event, ship):
	# Respond to keyup events
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False


def respond_play_button(settings, stats, screen, sb, lb, ship, aliens, bullets, play_button, mouse_x, mouse_y):
	# Start a new game when the player clicks play
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

	if button_clicked and not stats.game_active:
		# Hide the mouse curser
		pygame.mouse.set_visible(False)

		# Reset game stats and scoreboard
		stats.reset()
		stats.game_active = True
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_ships()

		# Empty the list of aliens and bullets
		aliens.empty()
		bullets.empty()

		# Reset game's settings
		settings.initialize_dynamic_settings()

		# Create a new fleet and center the ship
		create_fleet(settings, screen, ship, aliens)
		ship.center_ship()
		
		update_screen(settings, stats, screen, sb, lb, ship, aliens, bullets, play_button)
		return True

def fire_bullet(settings, screen, ship, bullets):
	# Fire a bullet if limit is not reached yet
	# Create a new bullet and add it to bullets group
	if len(bullets) < settings.bullets_allowed:
		new_bullet = Bullet(settings, screen, ship)
		bullets.add(new_bullet)
		# print("***BULLET FIRED***")


def get_number_aliens(settings, aliens, alien_width):
	# Find the number of aliens in a row
	# Spacing between each alien is equal to one alien width
	available_space_x = settings.screen_x - (2 * alien_width)
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x


def get_number_rows(settings, ship_height, alien_height):
	# Determine the number of rows of aliens that fit on the screen
	available_space_y = (settings.screen_y - (3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows


def create_alien(settings, screen, aliens, alien_number, row_number):
	# Create an alien
	alien = Alien(settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)


def create_fleet(settings, screen, ship, aliens):
	# Create a full fleet of aliens
	alien = Alien(settings, screen)
	number_aliens_x = get_number_aliens(settings, aliens, alien.rect.width)
	number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

	# Create first row of aliens
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(settings, screen, aliens, alien_number, row_number)


def check_events(settings, stats, screen, sb, lb, ship, aliens, bullets, play_button):
	# Listen and respond to keypresses and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			respond_keydown(event, settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			respond_keyup(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			respond_play_button(settings, stats, screen, sb, lb, ship, aliens, bullets, play_button, mouse_x, mouse_y)


def update_screen(settings, stats, screen, sb, lb, ship, aliens, bullets, play_button, playing=False):
	if playing:
		# Redraw the screen during each pass through the loop
		screen.fill(settings.bg_color)
		if stats.game_active:
			# Redraw bullets behind ship and aliens
			for bullet in bullets.sprites():
				bullet.draw()

			# Draw ship to the screen
			ship.blitme()

			# Draw aliens to the screen
			aliens.draw(screen)

			# Draw the scoreboard
			sb.show_score()
		else:
			if stats.game_over:
				lb.draw_leaderboard()
				play_button.edit_pos(adj_y=300)
				play_button.edit_msg("Play Again")
				play_button.draw()
			else:
				# Draw the play button if the game is inactive
				play_button.draw()
				stats.user = tb.get_username(settings, stats, screen, sb, lb, ship, aliens, bullets, play_button, "Username: ")
				while stats.user == '':
					tb.no_username(settings, screen, play_button, "Please enter a username or click play as guest")
					stats.user = tb.get_username(settings, stats, screen, sb, lb, ship, aliens, bullets, play_button, "Username: ")
				if check_user(stats.user):
					get_user(stats.user)
				else:
					save_user(stats.user, stats.data)
				stats.game_active = True
	# Make the most recently drawn screen visible
	pygame.display.flip()


def update_bullets(settings, stats, screen, sb, ship, aliens, bullets):
	# Update bullet position and remove old bullets
	bullets.update()
	# Get rid of bullets that have disappeared
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	check_bullet_alien_collisions(settings, stats, screen, sb, ship, aliens, bullets)


def update_aliens(settings, stats, screen, sb, lb, ship, aliens, bullets):
	# Update the positions of all aliens in the fleet
	check_fleet_edges(settings, aliens)
	aliens.update()

	# Look for alien-ship collisions
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(settings, stats, screen, sb, lb, ship, aliens, bullets)

	check_aliens_bottom(settings, stats, screen, sb, lb, ship, aliens, bullets)



def ship_hit(settings, stats, screen, sb, lb, ship, aliens, bullets):
	# Respond to ship being hit by alien
	if stats.ships_left > 0:
		# Decrement ships left
		stats.ships_left -= 1
		print("SHIP HIT!!! ---- SHIPS LEFT: " + str(stats.ships_left))

		# Update scoreboard
		sb.prep_ships()

		# Empty list of alien and bullets
		aliens.empty()
		bullets.empty()

		# Create a new fleet and center ship
		create_fleet(settings, screen, ship, aliens)
		ship.center_ship()

		# Pause
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)
		save_score(stats.score, stats.user)
		all_time_scores(stats)
		stats.game_over = True
		lb.stats = stats
		print("GAME OVER")


def check_bullet_alien_collisions(settings, stats, screen, sb, ship, aliens, bullets):
	# Respond to bullet-alien collisions
	# Check for any bullets that have hit aliens
	# If so get rid of the bullet and alien
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	
	if collisions:
		for aliens in collisions.values():
			stats.score += settings.alien_points * len(aliens)
			sb.prep_score()
			print("ALIEN HIT --- PLUS " + str(settings.alien_points) + " POINTS!!")
		check_high_score(stats, sb)

	if len(aliens) == 0:
		# Destroy existing bullets, create new fleet and increase level
		bullets.empty()
		settings.increase_speed()

		# Increase level
		stats.level += 1
		sb.prep_level()
		print("FLEET DESTROYED -- NEW LEVEL")

		create_fleet(settings, screen, ship, aliens)


def check_fleet_edges(settings, aliens):
	# Respond appropriatley if any aliens have reached an edge
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(settings, aliens)
			break


def change_fleet_direction(settings, aliens):
	# Drop entire fleet and change the fleet's direction
	for alien in aliens.sprites():
		alien.rect.y += settings.fleet_drop_speed
	settings.fleet_direction *= -1


def check_aliens_bottom(settings, stats, screen, sb, lb, ship, aliens, bullets):
	# Check if any aliens have reached the bottom of the screen
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# Treat the same way as if a ship got hit
			ship_hit(settings, stats, screen, sb, lb, ship, aliens, bullets)
			break


def check_high_score(stats, sb):
	# Check to see if there's a new high score
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()
		save_score(stats.score)


def save_score(score, user):
	with open('../data_files/test.json') as file:
		data = json.load(file)
		saved_user = find_user(user, data)
		saved_user['scores'].append(score)
	save(data)


def find_user(user, data):
	for saved_user in data['users']:
		if saved_user['username'] == user:
			return saved_user
	return None


def check_user(user):
	try:
		with open('../data_files/test.json') as file:
			data = json.load(file)
			if find_user(user, data) != None:
				return True
			else:
				return False
	except FileNotFoundError:
		return False

def save_user(user, data):
	data = {}
	with open('../data_files/test.json', 'r+') as file:
		data = json.load(file)
		data['users'].append({
			'username': user,
			'scores': []
		})
	save(data)


def save(data):
	with open('../data_files/test.json', 'w') as file:
		json.dump(data, file, indent=4)


def get_user(user):
	print('getting user')
	pass


def all_time_scores(stats):
	dicts = []
	with open('../data_files/test.json') as file:
		data = json.load(file)
		for user in data['users']:
			user['scores'].sort(reverse=True)
		tmp_list = sorted(data['users'], key=lambda k: max(k['scores']), reverse=True)
		for item in tmp_list:
			for k,v in item.items():
				for score in v:
					try:
						score = int(score)
					except ValueError:
						continue
					tmp = {}
					tmp[item['username']] = score
					dicts.append(tmp)

	stats.top_scores = sorted(dicts, key=lambda k: list(k.values()), reverse=True)

