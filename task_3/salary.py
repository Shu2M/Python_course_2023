class Salary:
    def __init__(self, pay):
        self.pay = pay

    def total(self):
        return self.pay * 12


class Employee:
    def __init__(self, pay, bonus):
        self.salary = Salary(pay)
        self.bonus = bonus

    def annual_salary(self):
        return self.salary.total() + self.bonus


a = Employee(pay=12, bonus=55)
print(a.annual_salary())
