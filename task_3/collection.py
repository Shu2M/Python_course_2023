class Collection:
    def __init__(self, my_list: list):
        self.my_list = my_list

    def __len__(self):
        return len(self.my_list)

    def __del__(self):
        print('Удаляется объект класса Collection')


obj = Collection([1, 2, 3, 4, 5])
print(len(obj))
del obj
