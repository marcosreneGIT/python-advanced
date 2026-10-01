import importlib

import python_intermedirario.aulas.aula094.modulo094 as modulo094

print(modulo094.variavel)

for i in range(10):
    importlib.reload(modulo094)
    print(i)

print('Fim')