import numpy as np
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error as mse
import pickle

X_test, y_test = np.load('./test/X_test.npy'), np.load('./test/y_test.npy')

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

y_test_pred = model.predict(X_test)

print(f'r2: {r2_score(y_test, y_test_pred)}')
print(f'mse: {mse(y_test, y_test_pred, squared=False)}')