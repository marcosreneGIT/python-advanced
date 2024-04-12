# Métodos úteis dos dicionários em Python


import copy

dicionario = {
    'chave': 1,
    'lista': [0, 1, 2],
}

dicionario_copia = dicionario.copy() # copy - retorna uma cópia rasa (shallow copy)
dicionario_copia = copy.deepcopy(dicionario) # deepcopy - retorna uma copia completa

dicionario_copia['chave'] = 2
dicionario_copia['lista'][1] = 2

print(dicionario)
print(dicionario_copia)