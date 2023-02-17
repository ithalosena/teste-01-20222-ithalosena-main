
from Funcionario import Funcionario

class FolhaDePagamento:
    def __init__(self, funcionarios):
        self.__funcionarios = funcionarios

    def calcularFolha(self):
        total = 0
        for funcionario in self.__funcionarios:
            total += total+funcionario.calcularSalario()
        return total