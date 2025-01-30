# módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html


# inteiro - import nome_modulo
# vantagens: você tem o namespace do módulo
# desvantagens: nomes grandes
# exemplo: import sys

# partes - from nome_modulo import objeto_0, objeto_1
# vantagens: nomes pequenos
# desvantagens: sem o namespace do módulo
# exemplo: from sys import exit, platform

# alias 1 - import nome_modulo as apelido
# exemplo: import sys as s

# alias 2 - from nome_modulo import objeto as apelido
# exemplos: 
# from sys import exit as ex
# from sys import platform as pf

# vantagens: você pode reservar nomes para seu código
# desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# vantagens: importa tudo de um módulo
# desvantagens: importa tudo de um módulo
# exemplo: from sys import exit, platform
