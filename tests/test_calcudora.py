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
        self.calc.subtract(4, 2)
        self.assertEqual(2, self.calc.valor)
    
    def test_metodo_multiplicacion(self)
        self.calc.multiply(3, 2)
        self.assertEqual(6, self.calc.valor)

    def test_metodo_division(self)
        self.calc.divide(10,2)
        self.assertEqual(5, self.calc.valor)
