# dictionary comprehension e set comprehension

produto = {
    'nome' : 'Caneta Azul',
    'preco' : 2.5,
    'cartegoria' : 'Escritório'
}

dicionario_0 = {
    chave : valor.upper() if isinstance(valor, str)
    else valor
    for chave, valor in produto.items()
    if chave != 'cartegoria'
}

print(dicionario_0, sep='\n')

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

dicionario_1 = {
    chave : valor
    for chave, valor in lista
}

print(dicionario_1, sep='\n')

set_0 = {
    2 ** i for i in range(10)
    if 2 ** i < 100
}

print(set_0)