import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

X_train, y_train = np.load('./train/X_train.npy'), np.load('./train/y_train.npy')

model = LinearRegression()

model.fit(X_train, y_train)

with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

