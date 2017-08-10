import numpy as np
training_data = []
screen = [5, 32 , 31]
output = [1, 0, 2]

training_data.append([screen, output])

#with open('teen.npy', 'wb') as file:
#	np.save(file, training_data)

with open('teen.npy', 'ab') as file:
	np.save(file, training_data)