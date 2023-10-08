import pandas as pd

flights = pd.DataFrame({
    'id': [0, 1, 2, 3],
    'year': [2013, 2013, 2013, 2013],
    'month': [1, 9, 3, 1],
    'dep_time': [517, 533, 542, 544],
    'sched_dep_time': [515, 529, 540, 545],
}).set_index('id')

flights.to_csv('flights.csv')
# flights.to_csv('flights.csv', index=False, header=False)

flights_2 = pd.read_csv('flights.csv')
print(flights_2)

