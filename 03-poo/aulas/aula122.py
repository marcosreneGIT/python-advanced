# métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja, ao invés de receber a instância no primeiro parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2024

    def __init__(self, idade, nome, sexo):
        self.idade = idade
        self.nome = nome
        self.sexo = sexo


    @classmethod
    def metodo_classe(cls):
        return f'Metodo de classe. {cls.ano}' # acesso apenas a valores pertecentes a classe
    

    @classmethod
    def criar_pessoa_masculina(cls, nome, idade):
        return cls(idade, nome, sexo='Masculino')
    

    @classmethod
    def criar_pessoa_feminina(cls, nome, idade):
        return cls(idade, nome, sexo='Feminino')


print(Pessoa.ano)
print(Pessoa.metodo_classe())

pessoa_0 = Pessoa.criar_pessoa_masculina('Marcos', 21)
pessoa_1 = Pessoa.criar_pessoa_feminina ('Maria', 33)

print(pessoa_0.nome)
print(pessoa_0.sexo)

print(pessoa_1.sexo)

