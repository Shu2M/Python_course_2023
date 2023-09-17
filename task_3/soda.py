class Soda:
    def __init__(self, additive=None):
        self.additive = additive

    def show_my_drink(self):
        print(f'Soda with {self.additive}' if self.additive else 'Common soda')


common_soda = Soda()
soda_with_additive = Soda('lemon')

common_soda.show_my_drink()
soda_with_additive.show_my_drink()
