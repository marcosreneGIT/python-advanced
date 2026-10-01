class Pessoas:
    def __init__(self, nome, idade):
        self.nome  = nome
        self.idade = idade


pessoa = Pessoas('Marcos', 21)

print(pessoa.nome)