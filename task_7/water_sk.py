from sklearn import datasets, svm
from sklearn.model_selection import train_test_split
import numpy as np

# np.set_printoptions(precision=2, floatmode='fixed', suppress=True)
dataset = np.genfromtxt('water_potability.csv', delimiter=',', dtype=float, skip_header=True)

for i in range(len(dataset[0]) - 1):
    dataset = dataset[~np.isnan(dataset[:, i])]

# dataset = np.around(dataset, 2)
target = dataset[:, -1]
data = dataset[:, :10]

model = svm.SVC(gamma=3)
x_train, x_test, y_train, y_test = train_test_split(
    data, target, test_size=0.2, shuffle=True
)
model.fit(x_train, y_train)
predicts = model.predict(x_test[0:10])
print(predicts)
print(y_test[:10])

predicts = model.predict(x_test)
print('% ', round((len(y_test) - sum(abs(predicts - y_test))) / len(y_test) * 100, 2))
