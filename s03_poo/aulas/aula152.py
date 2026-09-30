# membro = Classe(valor), Classe['chave']
# chave  = Classe.chave.name 
# valor  = Classe.chave.value 

import enum


class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA  = enum.auto()
    

print(Direcoes(1),'\n', # membro
      Direcoes['ESQUERDA'], '\n',  # membro
      Direcoes.DIREITA.name, '\n', # chave 
      Direcoes.ESQUERDA.value,'\n' # valor
      ) 

def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada.')
    
    print(f'Movendo para {direcao.name}')
    

mover(Direcoes.ESQUERDA)