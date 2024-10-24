# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome  = nome
        self.idade = idade


    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

dados_pessoais =[{'nome': 'Marcos', 'idade': 21}, 
                 {'nome': 'Ana', 'idade': 19},
                 {'nome': 'Caio', 'idade': 33}
                 ]

pessoa_0 = Pessoa(**dados_pessoais[0])
pessoa_1 = Pessoa(**dados_pessoais[1])
pessoa_2 = Pessoa(**dados_pessoais[2])

print(pessoa_0.__dict__)
print(vars(pessoa_1))
print(vars(pessoa_2))

print(pessoa_0.ano_nascimento())
