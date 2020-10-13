class Calculadora:

    def __init__(self):
        self.valor = 0

    def add(self, x, y):
        self.valor = x + y

    def divide_int(self, x, y):
        if y == 0:
            raise ZeroDivisionError
        return x//y

    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError
        return x/y
