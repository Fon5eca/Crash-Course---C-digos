import city_function
import unittest

class Cities_function_test(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(city_function.formated_name("santiago", "chile", population=500_000), "Santiago, Chile - Population: 500000")

if __name__ == '__main__':
    unittest.main()