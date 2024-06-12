import importlib

import aula097

print(aula097.variavel)

for i in range(10):
    importlib.reload(aula097)
    print(i)

print('Fim')