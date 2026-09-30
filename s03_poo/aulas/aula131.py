# herança simples - relações entre classes

# associação - usa
# agregação - tem  
# composição - é dono de  

# herança - é um 

# herança vs composição

# casse principal (Pessoa)
# super class, base class    , parent class

# classes filhas (Cliente)
# sub class  , derived class , child class

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def informar_classe(self):
        return f'{self.nome} {self.sobrenome} é da classe {self.__class__.__name__}'


class Professor(Pessoa):
    pass


class Aluno(Pessoa):
    pass


professor_0 = Professor('Luiz', 'Otávio')
aluno_0 = Aluno('Marcos', 'Renê')

print(professor_0.informar_classe())
print(aluno_0.informar_classe())
print('Porém ambos são da classe Pessoa.')