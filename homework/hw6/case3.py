from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import itertools
from random import randrange


INPUT_DIM = 8
OUTPUT_DIM = 1
H_DIM_1 = [i for i in range(5, 16, 1)]
H_DIM_2 = [i for i in range(4, 10, 1)]
NUM_EPOCHS = [i for i in range(10, 50, 5)]
BATCH_SIZE = [i for i in range(10, 50, 5)]


def model_report(idim, odim, hdim1, hdim2, nepochs, batchsize) -> str:
    return f'INPUT_DIM: {idim}\n' \
           f'OUTPUT_DIM: {odim}\n' \
           f'H_DIM_1: {hdim1}\n' \
           f'H_DIM_2: {hdim2}\n' \
           f'NUM_EPOCHS: {nepochs}\n' \
           f'BATCH_SIZE: {batchsize}\n' \
           f'\n'


def prediction_report(prediction_num, input_data, answer, model_prediction) -> str:
    return f'prediction {prediction_num}\n' \
           f'input data: {input_data}\n' \
           f'answer: {answer}\n' \
           f'model prediction: {model_prediction}\n' \
           f'\n'


np.set_printoptions(precision=2, floatmode='fixed', suppress=True)
dataset = np.genfromtxt('data.txt', delimiter=',', dtype=float)
for i in range(len(dataset[0]) - 1):
    dataset = dataset[~np.isnan(dataset[:, i])]
dataset = np.around(dataset, 2)
Y = dataset[:, -1]
X = dataset[:, :-1]

for h_dim_1, h_dim_2, num_epochs, batch_size in itertools.product(H_DIM_1, H_DIM_2, NUM_EPOCHS, BATCH_SIZE):
    model = Sequential()
    model.add(Dense(h_dim_1, input_dim=INPUT_DIM, activation='relu'))
    model.add(Dense(h_dim_2, activation='relu'))
    model.add(Dense(OUTPUT_DIM, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam')
    model.fit(X, Y, epochs=num_epochs, batch_size=batch_size, verbose=2)

    report = model_report(INPUT_DIM, OUTPUT_DIM, h_dim_1, h_dim_2, num_epochs, batch_size)

    for i in range(3):
        row_ind = randrange(len(dataset))
        input_data = X[row_ind:row_ind + 1]
        answer = Y[row_ind]
        model_prediction = model.predict(input_data)
        report += prediction_report(i + 1, input_data, answer, model_prediction)

    with open(f'model_{h_dim_1}_{h_dim_2}_{num_epochs}_{batch_size}.txt', 'w') as file:
        file.write(report)


