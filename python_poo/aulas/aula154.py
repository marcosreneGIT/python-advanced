# o módulo dataclasses fornece um decorador (@dataclasses)
# __init__, __repr__, __eq__...

# dataclasses são syntax sugar para classes de dados.
# descrito na PEP 557 e adicionado na versão 3.7 do Python.

# # doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass

@dataclass(init=False) # possíbilidade de criar meu próprio __init__ 
class Pessoa:
    _nome: str
    _idade: int
    
    def __init__(self, nome, idade) -> None:
        self._nome = nome
        self._idade = idade
    
    # def __post_init__(self): # execulta após o "__init__" da dataclass.
    #     print('__post_init__')
        
    @property
    def nome(self):
        return self._nome
    
    
if __name__ == '__main__':
    pessoa_0 = Pessoa('Renê', 21)
    pessoa_1 = Pessoa('Marcos', 21)
    
    print(pessoa_0.nome)
    print(pessoa_0._idade == pessoa_1._idade)