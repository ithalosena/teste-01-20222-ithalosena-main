class Produto:
    def __init__(self, nome, preco, desconto=0):
        self.nome = nome
        self.preco = preco
        self.desconto = desconto
    
    def aplicar_desconto(self, desconto):
        self.desconto = desconto
    
    def calcular_preco(self):
        return self.preco - (self.preco * (self.desconto / 100))

    