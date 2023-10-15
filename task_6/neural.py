import random
import numpy as np
import matplotlib.pyplot as plt


class Neural:
    def __init__(
            self,
            path_dataset: str = 'data.txt',
            input_dim: int = 9,
            output_dim: int = 2,
            h_dim: int = 25,
            alpha: float = 1e-5,
            num_epochs: int = 1000,
            batch_size: int = 30,
    ):
        self.INPUT_DIM = input_dim
        self.OUTPUT_DIM = output_dim
        self.H_DIM = h_dim
        self.ALPHA = alpha
        self.NUM_EPOCHS = num_epochs
        self.BATCH_SIZE = batch_size

        self.dataset = list()
        self.nn_weights = dict()
        self.path_dataset = path_dataset

    @staticmethod
    def softmax_batch(matrix):
        out = np.exp(matrix)
        out /= np.sum(out, axis=1, keepdims=True)
        return out

    @staticmethod
    def sparse_cross_entropy_batch(z, y):
        return -np.log(np.array([z[j, y[j]] for j in range(len(y))]))

    @staticmethod
    def to_full_batch(y, num_classes):
        y_full = np.zeros((len(y), num_classes))

        for j, yj in enumerate(y):
            y_full[j, yj] = 1

        return y_full

    @staticmethod
    def relu(matrix):
        return np.maximum(matrix, 0)

    @staticmethod
    def relu_deriv(matrix):
        return (matrix >= 0).astype(float)

    def data_preparation(self):
        dataset = np.genfromtxt(self.path_dataset, dtype=float, skip_header=True, delimiter=',')

        # row_ind_to_delete = []
        # for i, line in enumerate(dataset):
        #     if any(np.isnan(line)):
        #         row_ind_to_delete.append(i)
        # dataset = np.delete(dataset, obj=row_ind_to_delete, axis=0)
        for i in range(len(dataset[0]) - 1):
            dataset = dataset[~np.isnan(dataset[:, i])]

        dataset[:, 2] *= 0.001
        dataset[:, 4] *= 0.01
        dataset[:, 5] *= 0.01

        dataset = np.around(dataset, 2)

        target = dataset[:, -1]
        dataset = dataset[:, :9]

        if len(target) != len(dataset):
            raise Exception('Кол-во строк dataset не совпадает c кол-вом строк target')

        self.dataset = [(dataset[i][None, ...], int(target[i])) for i in range(len(target))]

    def inference(self, x):
        if not self.nn_weights:
            raise Exception('Сеть не обучена')

        t1 = x @ self.nn_weights['W1'] + self.nn_weights['b1']
        h1 = self.relu(t1)

        t2 = h1 @ self.nn_weights['W2'] + self.nn_weights['b2']
        z = self.softmax_batch(t2)

        return np.argmax(z)

    def calc_accuracy(self):
        correct = 0
        for x, y in self.dataset:
            y_pred = self.inference(x)
            if y_pred == y:
                correct += 1
        return correct / len(self.dataset)

    def training(self):
        self.data_preparation()

        self.nn_weights['W1'] = np.random.rand(self.INPUT_DIM, self.H_DIM)
        self.nn_weights['b1'] = np.random.rand(1, self.H_DIM)
        self.nn_weights['W2'] = np.random.rand(self.H_DIM, self.OUTPUT_DIM)
        self.nn_weights['b2'] = np.random.rand(1, self.OUTPUT_DIM)

        self.nn_weights['W1'] = (self.nn_weights['W1'] - 0.5) * 2 * np.sqrt(1 / self.INPUT_DIM)
        self.nn_weights['b1'] = (self.nn_weights['b1'] - 0.5) * 2 * np.sqrt(1 / self.INPUT_DIM)
        self.nn_weights['W2'] = (self.nn_weights['W2'] - 0.5) * 2 * np.sqrt(1 / self.H_DIM)
        self.nn_weights['b2'] = (self.nn_weights['b2'] - 0.5) * 2 * np.sqrt(1 / self.H_DIM)

        loss_arr = []

        for ep in range(self.NUM_EPOCHS):
            random.shuffle(self.dataset)
            for i in range(len(self.dataset) // self.BATCH_SIZE):
                batch_x, batch_y = zip(*self.dataset[i * self.BATCH_SIZE: i * self.BATCH_SIZE + self.BATCH_SIZE])
                x = np.concatenate(batch_x, axis=0)
                y = np.array(batch_y)

                # Forward
                t1 = x @ self.nn_weights['W1'] + self.nn_weights['b1']
                h1 = self.relu(t1)
                t2 = h1 @ self.nn_weights['W2'] + self.nn_weights['b2']
                z = self.softmax_batch(t2)
                E = np.sum(self.sparse_cross_entropy_batch(z, y))

                # Backward
                y_full = self.to_full_batch(y, self.OUTPUT_DIM)
                dE_dt2 = z - y_full
                dE_dW2 = h1.T @ dE_dt2
                dE_db2 = np.sum(dE_dt2, axis=0, keepdims=True)
                dE_dh1 = dE_dt2 @ self.nn_weights['W2'].T
                dE_dt1 = dE_dh1 * self.relu_deriv(t1)
                dE_dW1 = x.T @ dE_dt1
                dE_db1 = np.sum(dE_dt1, axis=0, keepdims=True)

                # Update
                self.nn_weights['W1'] -= self.ALPHA * dE_dW1
                self.nn_weights['b1'] -= self.ALPHA * dE_db1
                self.nn_weights['W2'] -= self.ALPHA * dE_dW2
                self.nn_weights['b2'] -= self.ALPHA * dE_db2

                loss_arr.append(E)

        print('accuracy: ', self.calc_accuracy())
        plt.plot(loss_arr)
        plt.savefig('loss_arr.png')
