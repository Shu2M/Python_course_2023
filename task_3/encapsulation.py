class Encapsulation:
    def __init__(self):
        self.open_param = 1
        self.__private_param = 2


o = Encapsulation()
print(o.open_param)
print(o._Encapsulation__private_param)