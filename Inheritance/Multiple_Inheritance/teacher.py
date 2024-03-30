from Multiple_Inheritance.employee import Employee
from Multiple_Inheritance.person import Person


class Teacher(Person, Employee):

    def teach(self):
        return 'teaching...'