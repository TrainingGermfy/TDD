from calculadora.calculadora import Calculadora
import unittest


class Test_MiCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def tearDown(self):
        del self.calc

    def test_inicial_valores(self):
        self.assertEqual(0, self.calc.valor)

    def test_metodo_suma(self):
        self.calc.add(1, 3)
        self.assertEqual(4, self.calc.valor)

    def test_divide(self):
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.divide(-1, -1), 1)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(8, 2), 4)

        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
            self.calc.divide(10, 0)

    def test_divide_int(self):
        self.assertEqual(self.calc.divide_int(11, 2), 5)
        self.assertEqual(self.calc.divide_int(-1, 1), -1)
        self.assertEqual(self.calc.divide_int(-1, -1), 1)
        self.assertEqual(self.calc.divide_int(8, 2), 4)

        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
            self.calc.divide(0, 0)
