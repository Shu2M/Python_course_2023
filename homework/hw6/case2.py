from keras.models import Sequential
from keras.layers import Dense
import numpy as np


class Neural:
    def __init__(
            self,
            path_dataset: str = 'data.txt',
            input_dim: int = 8,
            output_dim: int = 1,
            num_epochs: int = 15,
            batch_size: int = 10,
    ):
        self.INPUT_DIM = input_dim
        self.OUTPUT_DIM = output_dim
        self.NUM_EPOCHS = num_epochs
        self.BATCH_SIZE = batch_size

        self.dataset = list()
        self.path_dataset = path_dataset
        self.model = None

    def data_preparation(self):
        dataset = np.genfromtxt(self.path_dataset, delimiter=',', dtype=float)
        for i in range(len(dataset[0]) - 1):
            dataset = dataset[~np.isnan(dataset[:, i])]
        self.dataset = np.around(dataset, 2)

    def training(self):
        self.data_preparation()
        y = self.dataset[:, -1]
        x = self.dataset[:, :-1]

        model = Sequential()
        model.add(Dense(12, input_dim=self.INPUT_DIM, activation='relu'))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(self.OUTPUT_DIM, activation='sigmoid'))

        model.compile(loss='binary_crossentropy', optimizer='adam')
        model.fit(x, y, epochs=self.NUM_EPOCHS, batch_size=self.BATCH_SIZE, verbose=2)

        self.model = model

    def inference(self, x):
        return self.model.predict(x)


dataset = np.genfromtxt('data.txt', delimiter=',', dtype=float)
x = dataset[:, :-1][:1]
print(x)

neural = Neural()
neural.training()
predict = neural.inference(x)
print(predict)
