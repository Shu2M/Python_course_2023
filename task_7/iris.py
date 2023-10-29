from sklearn import datasets, svm
from sklearn.model_selection import train_test_split

irises = datasets.load_iris()

data = irises.data


model = svm.SVC()
x_train, x_test, y_train, y_test = train_test_split(
    data, irises.target, shuffle=True
)
model.fit(x_train, y_train)
predicts = model.predict(x_test[0:3])
print(predicts)
print(y_test[:3])