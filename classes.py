"""
a class
an instance of a class

attribute -> variable
    emp1.first = "Kieron"
    emp1.first
    >>>> "Kieron"

method ->    function
"""


class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def full_name(self, middle_name):
        if middle_name:
            print(self.first, middle_name, self.last)

    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday >= 5:
            return False
        else:
            return True

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(
            self.first, self.last, self.pay)

    def __str__(self):
        return "{}, {})".format(
            self.full_name, self.email)

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)

    @full_name.setter
    def full_name(self, new_name):
        first, last = new_name.split(" ")
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        print("Name deleted!")
        self.first = None
        self.last = None


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, progr_lang):
        super().__init__(first, last, pay)
        self.progr_lang = progr_lang


class Manager(Employee):
    def __init__(self, first, last, pay, managed_emps=None):
        super().__init__(first, last, pay)
        if managed_emps is None:
            self.managed_emps = []
        else:
            self.managed_emps = managed_emps

    def add_emp(self, emp):
        if emp not in self.managed_emps:
            self.managed_emps.append(emp)

    def remove_emp(self, emp):
        if emp in self.managed_emps:
            self.managed_emps.remove(emp)

    def print_emps(self):
        for emp in self.managed_emps:
            print("-->", emp.full_name())