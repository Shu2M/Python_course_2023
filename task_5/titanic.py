import pandas as pd

titanic = pd.DataFrame({
    'PClass': ['1st', '1st', '1st', '1st', '1st', '1st', '1st'],
    'Age': [12,231,564,54,54,54,4],
    'Sex': ['male', 'female','male','female','male','female','male'],
    'Survived': [1,1,1,1,0,0,0],
    'SexCode': [1,0,1,0,1,0,1]
})

print(titanic.groupby('Survived')['Survived'].count())
print(titanic.groupby(['Survived', 'Sex'])['Survived'].count())

