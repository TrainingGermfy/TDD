class Calculadora:
    def __init__(self):
        self.valor = 0        

    def add(self, x, y):
        self.valor = x + y
        
    def substract(self, x, y):
        self.valor = x - y

    def divide(self, x, y):
        try:
            self.valor = x / y
        except ZeroDivisionError:
            print("Not possible operation, check divisor value.")
    
    def multiplication(self, x, y):
        self.valor = x * y
