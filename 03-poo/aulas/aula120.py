# atributos de classe

class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome  = nome
        self.idade = idade


    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

pessoa_0 = Pessoa('Marcos', 21)
pessoa_1 = Pessoa('Ana', 19)

print(Pessoa.ano_atual)
print(pessoa_0.ano_nascimento())
print(pessoa_1.ano_nascimento())
