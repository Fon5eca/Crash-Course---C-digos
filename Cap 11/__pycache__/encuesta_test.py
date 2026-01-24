from testing_classes import Survey
import unittest

class TestSurveys(unittest.TestCase):
    def setUp(self):     #Es como una caja de herramientas que podemos crear en el que hay código y posibles respuestas.
        '''Crear una encuesta y respuestas que pueden ser usadas en las pruebas.'''
        self.q = Survey("How old are you?")
        self.responses_to_add = [9, 16, 38, 56]     #Es como cuando se crean variables en la función __init__()

    def test_response_storaging(self):
        self.q.store_answer(self.responses_to_add[1])
        self.assertIn(self.responses_to_add[1], self.q.responses)

    def test_storaging_many_responses(self):
        for response in self.responses_to_add:
            self.q.store_answer(response)
        
        for response in self.responses_to_add:
            self.assertIn(response, self.q.responses)     #En cada método podemos correr los asserts cuantas veces queramos.


if __name__ == '__main__':
    unittest.main()