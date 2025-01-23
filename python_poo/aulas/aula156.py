# namedtuples: tuplas imutáveis com nomes para valores

# é ultilizado para criar classes de agrupamento de atributos
# classes normais sem métodos, ou registros de bases de dados, etc.

# as namedtuples são imutáveis assim como as tuplas.

# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple

from typing import NamedTuple
from collections import namedtuple


# NamedTuple
class Carta(NamedTuple):
    valor: str = 'X'
    naipe: str = 'Y'
    
as_ouro = Carta('A', 'OURO')

print(as_ouro.naipe)


# namedtuple
C = namedtuple(
    'Carta', ['valor', 'naipe'],
    defaults=['X', 'Y']
)

as_espadas = C('A', 'ESPADA')

print(as_espadas.valor)