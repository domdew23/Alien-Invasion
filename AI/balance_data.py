import numpy as np 
import pandas as pd 
import cv2
import os
from collections import Counter
from random import shuffle

FILE_NAME = 'data/training_data.npy'
FINAL_FILE_NAME = 'data/final_training_data.npy'
train_data = np.load(FILE_NAME)

df = pd.DataFrame(train_data)
print(df.head)
print(Counter(df[1].apply(str)))

lefts = []
rights = []
spaces = []

# prevent neural network from being bias for specific movements

shuffle(train_data)

for data in train_data:
	img = data[0]
	choice = data[1]

	if choice == [1,0,0]:
		lefts.append([img, choice])
	elif choice == [0,1,0]:
		spaces.append([img, choice])
	elif choice == [0,0,1]:
		rights.append([img, choice])
	else:
		print("No mathces")

print(len(spaces))
print(len(lefts))
print(len(rights))
print()

spaces = spaces[:len(lefts)][:len(rights)]
lefts = lefts[:len(spaces)]
rights = rights[:len(spaces)]

print(len(spaces))
print(len(lefts))
print(len(rights))

final_data = spaces + lefts + rights
shuffle(final_data)

print("final data: {}".format(len(final_data)))
print("train data: {}".format(len(train_data)))


def save(final_data):
	if not os.path.isfile(FINAL_FILE_NAME):
		print("File does not exist, creating file...")
		with open(FINAL_FILE_NAME, 'wb') as file:
			np.save(file, final_data)
	else:
		print("File exists, appending data...")
		with open(FINAL_FILE_NAME, 'ab') as file:
			np.save(file, final_data)


save(final_data)