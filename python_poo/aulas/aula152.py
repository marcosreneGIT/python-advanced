# membro = Classe(valor), Classe['chave']
# chave  = Classe.chave.name
# valor  = Classe.chave.value 

import enum

def mover(direcao):
    print(f'Movendo para {direcao}')

    # Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'Direita'])
    
mover('esquerda')
mover('direita')
mover('acima')
mover('abaixo')


class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()


print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)
print(Direcoes(1).name, Direcoes.ESQUERDA.value)


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')
    print(f'Movendo para {direcao.name} ({direcao.value})')
    
mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXOs)