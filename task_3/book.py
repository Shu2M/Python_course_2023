class Book:
    def __init__(self, title: str, author: str, checked_out: bool = False):
        self.title = title
        self.author = author
        self.checked_out = checked_out

    def check_out(self):
        if not self.checked_out:
            print('Выдаем книгу')
            self.checked_out = True
        else:
            print('Книга уже выдана')

    def check_in(self):
        if self.checked_out:
            print('Принимаем книгу в библиотеку')
            self.checked_out = False
        else:
            print('Книга в наличии')


book = Book('Документация Python', 'Гвидо ван Россум')
book.check_out()
book.check_out()

book.check_in()
book.check_in()
