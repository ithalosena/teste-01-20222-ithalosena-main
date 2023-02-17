class FormaDePagamento:
    def __init__(self, nome, desconto, acrescimo):
        self.nome = nome
        self.desconto = desconto
        self.acrescimo = acrescimo
    
    def calcular_preco(self, preco):
        return preco - (preco * (self.desconto / 100)) + (preco * (self.acrescimo / 100))
        