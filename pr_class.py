class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('shiva', 'krishna', 7000)

print(emp_1.first)
print(emp_1.fullname())


