import cv2
import win32api as wapi 
import numpy as np
import time
import os

from functions import countdown, grab_screen
from key_codes import LEFT, RIGHT, SPACE

l = [1,0,0]
r = [0,0,1]
s = [0,1,0]

left_key = 0x25
right_key = 0x27
space_key = 0x20
P = 0x50

KEY_LIST = [left_key, right_key, space_key, P]
FILE_NAME = 'data/training_data.npy'

def keys_to_output(keys):

	output = [0,0,0]

	if left_key in keys:
		output[0] = 1
	elif right_key in keys:
		output[2] = 1
	else:
		output[1] = 1
	return output


def key_check():
    keys = []
    for key in KEY_LIST:
        if wapi.GetAsyncKeyState(key):
            keys.append(key)
    return keys

def save(length, training_data):
	save_time = time.time()
	print("Saving... || training_data length: {}".format(length))
	if not os.path.isfile(FILE_NAME):
		print("File does not exist, creating file...")
		with open(FILE_NAME, 'wb') as file:
			np.save(file, training_data)
	else:
		print("File exists, appending data...")
		with open(FILE_NAME, 'ab') as file:
			np.save(file, training_data)

	print("Took || {}{:.2f}{} minutes to save".format('{', (time.time()- save_time) / 60, '}'))
	print("Saved")
	time.sleep(1)


def get_screen():
	screen = grab_screen(region=(0, 40, 1310, 835))
	screen = cv2.resize(screen, (320, 180))
	screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
	return screen


def show_screen(screen):
	cv2.imshow('window', cv2.resize(screen, (640, 360)))
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()


def main():		
	countdown(4)
	PAUSED = False
	training_data = []
	while True:
		if not PAUSED:
			start_time = time.time()
			screen = get_screen()
			# show_screen(screen)

			keys = key_check()
			output = keys_to_output(keys)
			training_data.append([screen,output])
			length = len(training_data)

			if length == 1000:
				save(length, training_data)
				training_data = []
			print("Not Paused Loop took: {}{:.3f}{} seconds || training_data length: {}".format('{', time.time()- start_time, '}', length))

		keys = key_check()

		if P in keys:
			if not PAUSED:
				PAUSED = True
				print("Paused training")
				time.sleep(3)
			else:
				PAUSED = False
				print("Unpausing training")


main()