class Employee():
    def __init__(self, f_name, s_name, salary):
        self.first_name = f_name
        self.second_name = s_name
        self.salary = salary

    def get_raise(self, plus=5000):
        self.salary += plus
