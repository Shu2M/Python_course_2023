class Transport:
    def __init__(self, brent, model, data, cost):
        self.brent = brent
        self.model = model
        self.data = data
        self.cost = cost

    def print_info(self):
        print(self.__dict__)


class Sedan(Transport):
    def __init__(self, door_num, style, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.door_num = door_num
        self.style = style


car1 = Sedan(2, 'future', 'tesla', 's type', '2020', 45)
car1.print_info()
