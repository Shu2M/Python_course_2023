class DataBase:
    __instance = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = True
            return super().__new__(cls)
        else:
            raise Exception(f'Попытка создания второго объекта {cls.__name__}')

    def __init__(self, user='', password='', port=''):
        self.user = user
        self.password = password
        self.port = port

    def __del__(self):
        self.__class__.__instance = False

    def connect(self):
        print(f'Соединение с БД: {self.user}, {self.password}, {self.port}')

    @staticmethod
    def close():
        print('Закрытие соединения с БД')


db = DataBase('Misha', '12345', '54671516431')
# db2 = DataBase('Peter', '6546', '9851654987')
db.connect()
# db.__del__()
del db

db2 = DataBase('Peter', '6546', '9851654987')
db2.connect()
