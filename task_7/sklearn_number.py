from sklearn import datasets, svm
from sklearn.model_selection import train_test_split


digits = datasets.load_digits()

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))


model = svm.SVC()
x_train, x_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False
)
model.fit(x_train, y_train)
predicts = model.predict(x_test[0:5])