import unittest
from calculadora.calculadora import Calculadora


class TestMiCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_inicial_valores(self):
        self.assertEqual(0, self.calc.valor)

    def test_metodo_division_entre_cero(self):
        self.calc.div(0, 0)
        self.assertIsInstance(self.calc.valor, ZeroDivisionError)

    def test_metodo_division_enteros(self):
        self.calc.div(1, 3)
        self.assertEqual(1 / 3, self.calc.valor)

    def test_metodo_division_floats(self):
        self.calc.div(10, 2.5)
        self.assertEqual(4.0, self.calc.valor)

    def test_metodo_division_strings_validos(self):
        self.calc.div('1', '3')
        self.assertEqual(1 / 3, self.calc.valor)

    def test_metodo_division_strings_invalidos(self):
        self.calc.div('2', 'a')
        self.assertIsInstance(self.calc.valor, ValueError)

    def test_metodo_mult_enteros(self):
        self.calc.mult(1, 3)
        self.assertEqual(3, self.calc.valor)

    def test_metodo_mult_floats(self):
        self.calc.mult(1.0, 3.0)
        self.assertEqual(3.0, self.calc.valor)

    def test_metodo_mult_strings_validos(self):
        self.calc.mult('1', '3')
        self.assertEqual(3, self.calc.valor)

    def test_metodo_mult_string_invalidos(self):
        self.calc.mult('a', '1')
        self.assertIsInstance(self.calc.valor, ValueError)

    def test_metodo_resta_enteros(self):
        self.calc.resta(3, 1)
        self.assertEqual(2, self.calc.valor)

    def test_metodo_resta_floats(self):
        self.calc.resta(3.0, 1.0)
        self.assertEqual(2.0, self.calc.valor)

    def test_metodo_resta_strings_validos(self):
        self.calc.resta('1', '3')
        self.assertEqual(-2, self.calc.valor)

    def test_metodo_resta_string_invalidos(self):
        self.calc.add('a', '1')
        self.assertIsInstance(self.calc.valor, ValueError)

    def test_metodo_suma_enteros(self):
        self.calc.add(1, 3)
        self.assertEqual(4, self.calc.valor)

    def test_metodo_suma_floats(self):
        self.calc.add(1.0, 3.0)
        self.assertEqual(4.0, self.calc.valor)

    def test_metodo_suma_strings_validos(self):
        self.calc.add('1', '3')
        self.assertEqual(4, self.calc.valor)

    def test_metodo_suma_string_invalidos(self):
        self.calc.add('a', '1')
        self.assertIsInstance(self.calc.valor, ValueError)
