# exercício - unir listas

# crie uma função zipper (como o zipper de roupas)
# o trabalho dessa função será unir duas listas na ordem.
# use todos os valores da menor lista.

# ex.:

# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']

# resultado: 

# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

estados = ['BA', 'SP', 'MG', 'RJ']
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']


def zipper(cidade, estado):
    estado_cidade = []

    for i in range(len(cidades)):
        estado_cidade.append((cidade[i], estado[i]))
    
    return estado_cidade

print(zipper(cidades, estados))




  
