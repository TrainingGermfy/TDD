class Calculadora:
    def __init__(self):
        self.valor = 0        

    def add(self, x, y):
        self.valor = x + y
        

    def substract(self, x, y):
        self.valor = x - y

    def multiply(self, x, y):
        self.valor = x * y
        
    def divide(self, x, y):
        try:
            self.valor = x / y
        except:
            self.valor = NULL
