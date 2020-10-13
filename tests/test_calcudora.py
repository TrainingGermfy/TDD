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
        self.calc.substract(10, 5)
        self.assertEqual(5, self.calc.valor)
        
    def test_metodo_multiplicacion(self):
        self.calc.multiply(6, 3)
        self.assertEqual(18, self.calc.valor)
        
    def test_metodo_division(self):
        self.calc.divide(15, 3)
        self.assertEqual(5, self.calc.valor)
   
    def test_metodo_divisioncero(self):
        self.calc.divide(15, 0)
        self.assertEqual(NULL, self.calc.valor)

