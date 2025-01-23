# o módulo dataclasses fornece um decorador (@dataclasses)
# __init__, __repr__, __eq__...

# dataclasses são syntax sugar para classes de dados.
# descrito na PEP 557 e adicionado na versão 3.7 do Python.

# # doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    
if __name__ == '__main__':
    pessoa_0 = Pessoa('Renê', 21)
    pessoa_1 = Pessoa('Marcos', 21)
    
    
    print(pessoa_0.idade == pessoa_1.idade)