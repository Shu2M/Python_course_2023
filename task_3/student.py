class Student:
    def __new__(cls, *args, **kwargs):
        print('new')
        return super().__new__(cls)

    def __init__(self, first_name, last_name, age, profession='Developer'):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession

    def check_profession(self):
        print(self.profession)

    @staticmethod
    def print_location():
        print('Saint-Petersburg')


new_student = Student('Chernomor', 'Peresvetovich', 49)
Student.print_location()
new_student.print_location()

