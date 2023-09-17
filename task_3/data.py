class Data:
    def __new__(cls, *args, **kwargs):
        print('state fetching')
        return super().__new__(cls)

    def __init__(self, lst: list):
        print(f'data processing: {lst}')


d1 = Data([1, 2, 3])
d2 = Data([4, 5, 6])
