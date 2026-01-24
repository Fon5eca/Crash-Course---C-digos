from empleado import Employee
import unittest

class ProbarEmployeeClass(unittest.TestCase):
    def setUp(self):
        self.employee1 = Employee("Deisler", "Neftali", 40_000)
        self.employee2 = Employee("Adrián", "Roberto", 50_000)

    def test_default_salary(self):
        self.employee1.get_raise()
        self.assertEqual(self.employee1.salary, 45_000)

    def test_customized_salary(self):
        self.employee2.get_raise(10_000)
        self.assertEqual(self.employee2.salary, 60_000)

if __name__ == '__main__':
    unittest.main()