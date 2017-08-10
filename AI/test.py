import numpy as np 
from sklearn.model_selection import train_test_split
import pandas as pd

FINAL_FILE_NAME = 'data/final_training_data.npy'
WIDTH, HEIGHT = 320, 180

train_data = np.load(FINAL_FILE_NAME)
df = pd.DataFrame(train_data)
X = np.array(train_data[0])
y = np.array(train_data[0])

train = train_data[:-100]
test = train_data[-100:]

X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 3)
y = [i[1] for i in train]

X_test = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 3)
y_test = [i[1] for i in test]


print(y[:6])
X_train, X_test, y_train, y_test = train_test_split(df, random_state=0)

print("{}".format(y_train[:6]))