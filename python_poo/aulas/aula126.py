# @property + @setter - getter e setter no modo Pythônico
# Atributos que começar com um ou dois underlines não devem ser usados fora da classe.

 # ------------------------------------------ 

# seu codigo

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade 


    @property
    def nome(self):
        print('@property')
        return self._nome
    

    @property
    def idade(self):
        print('@property')
        return self._idade
    
    
    @nome.setter
    def nome(self, nome):
        print('@nome.setter')

        if not isinstance(nome, str):
            raise ValueError('nome deve ser uma "str".')
        
        self._nome = nome 

    
    @idade.setter
    def idade(self, idade):
        print('@idade.setter')

        if not isinstance(idade, int):
            raise ValueError('idade deve ser um "int".')
        
        self._idade = idade
    
    
# ------------------------------------------ 

# codigo do cliente

pessoa_0 = Pessoa('Marcos', 21)

print(pessoa_0.nome)

pessoa_0.nome = 'Maria'
pessoa_0.idade = 55

print(f'Nome: {pessoa_0.nome}\nIdade: {pessoa_0.idade}')


