import unittest

from calculadora.calculadora import Calculadora


class Test_MiCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()
    
    def test_inicial_valores(self):
        self.assertEqual(0, self.calc.valor)

    def test_metodo_suma(self):
        self.calc.add(1, 3)
        self.assertEqual(4, self.calc.valor)
    
    def test_metodo_resta(self):
        self.calc.substract(7, 5)
        self.assertEqual(2, self.calc.valor)

    def test_metodo_division(self):
        self.calc.divide(13, 2)
        self.assertEqual(6.5, self.calc.valor)

    def test_metodo_multiplicacion(self):
        self.calc.multiplication(9, 4)
        self.assertEqual(36, self.calc.valor)
