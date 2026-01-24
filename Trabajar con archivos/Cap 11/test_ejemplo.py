import unittest
import ejemplo

class Prueba_ej(unittest.TestCase):     #Crear una clase heredada de la clase TestCase de unittest
    def test_primer_apellido(self):     #No se pone el init, solamente ponemos las funciones que queremos probar.
        '''Probar si sirve poner solamente primer nombre y apellido'''
        self.assertEqual(ejemplo.nombre("Juan", "Pérez"), "Juan Pérez")     #Una función que determina la igualdad entre ambos parámetros.
    def test_segundo(self):
        '''Probrar si la función sirve al introducir segundo nombre'''
        self.assertEqual(ejemplo.nombre("Deisler", "Fonseca", "Neftali"), "Deisler Neftali Fonseca")

if __name__ == '__main__':
    unittest.main()