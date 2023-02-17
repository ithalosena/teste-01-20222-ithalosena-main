class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def setSalario(self, salario):
        self.salario = salario

    def aumentaSalario(self, percentual):
        self.salario = self.salario + (self.salario * percentual / 100)