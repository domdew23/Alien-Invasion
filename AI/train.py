import numpy as np 

from models import inception_v3 as googlenet

WIDTH, HEIGHT = 320, 180
LEARNING_RATE = 1e-3
EPOCHS = 10
MODEL_NAME = 'models/alien_invasion_googlenet_model_{}_{}_epochs_v1.model'.format(LEARNING_RATE, EPOCHS)
FINAL_FILE_NAME = 'data/final_training_data.npy'

model = googlenet(WIDTH, HEIGHT, 3, LEARNING_RATE, output=9, MODEL_NAME=MODEL_NAME)

train_data = np.load(FINAL_FILE_NAME)

train = train_data[:-100]
test = train_data[-100:]

X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 3)
y = [i[1] for i in train]

X_test = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 3)
y_test = [i[1] for i in test]

model.fit(X, y, n_epoch=EPOCHS, validation_set=(X_test, y_test), 
	snapshot_step=2500, show_metric=True, run_id=MODEL_NAME)

# tensorboard --logdir=foo:D:/Coding Projects/Python/gtav_self_driving_car

model.save(MODEL_NAME)
