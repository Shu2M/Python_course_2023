from sklearn import datasets, svm
from sklearn.model_selection import train_test_split
import numpy as np


dataset = np.genfromtxt('data.txt', delimiter=',', dtype=float)
dataset = np.around(dataset, 2)
target = dataset[:, -1]
data = dataset[:, :9]

model = svm.SVC()
x_train, x_test, y_train, y_test = train_test_split(
    data, target, test_size=0.10
)
model.fit(x_train, y_train)
predicts = model.predict(x_test[0:10])
print(predicts)
print(y_test[:10])

predicts = model.predict(x_test)
print('% ', (len(y_test) - sum(abs(predicts - y_test))) / len(y_test) * 100)


