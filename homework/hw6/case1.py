from keras.models import Sequential
from keras.layers import Dense
import numpy as np


np.set_printoptions(precision=2, floatmode='fixed', suppress=True)
dataset = np.genfromtxt('data.txt', delimiter=',', dtype=float)

for i in range(len(dataset[0]) - 1):
    dataset = dataset[~np.isnan(dataset[:, i])]

dataset = np.around(dataset, 2)

Y = dataset[:, -1]
X = dataset[:, :-1]

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam')
model.fit(X, Y, epochs=15, batch_size=10, verbose=2)

print('предсказание')
prediction = model.predict(X[:3])
print('prediction:\n', prediction)
