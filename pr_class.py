class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    @classmethod
    def crct_name(cls,var_1):
        return cls.fullname(var_1)

    


emp_1 = Employee('shiva', 'krishna', 7000)

print(emp_1.first)
print(emp_1.fullname())

emp_2 = Employee('Rao','Run',400)

print(Employee.crct_name(emp_2))

