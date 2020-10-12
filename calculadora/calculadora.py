class Calculadora:
    def __init__(self):
        self.valor = 0

    def add(self, x=0, y=0):
        try:
            self.valor = float(x) + float(y)
        except ValueError as e:
            self.valor = e

    def div(self, numerador=0, denominador=1):
        try:
            self.valor = float(numerador) / float(denominador)
        except ValueError as e:
            self.valor = e
        except ZeroDivisionError as e:
            self.valor = e

    def mult(self, x=0, y=0):
        try:
            self.valor = float(x) * float(y)
        except ValueError as e:
            self.valor = e

    def resta(self, x=0, y=0):
        try:
            self.valor = float(x) - float(y)
        except ValueError as e:
            self.valor = e