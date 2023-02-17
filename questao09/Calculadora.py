class Calculadora:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def soma(self):
        return self.valor1 + self.valor2

    def subtracao(self):
        return self.valor1 - self.valor2

    def multiplicacao(self):
        return self.valor1 * self.valor2

    def divisao(self):
        return self.valor1 / self.valor2