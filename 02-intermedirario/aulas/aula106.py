# reduce é uma função que faz a redução de um interavel em um valor.

from functools import reduce


numeros = [1, 2, 3, 4, 5]

total_numeros = reduce(
    lambda x, y: x * y, numeros, 10
)

print(total_numeros)


produtos = [
    {'nome': 'produto 1', 'preco': 10},
    {'nome': 'produto 2', 'preco': 20},
    {'nome': 'produto 3', 'preco': 30},
    {'nome': 'produto 4', 'preco': 40},
    {'nome': 'produto 5', 'preco': 50},
]

total_produtos = reduce(lambda acc, produto: acc + produto['preco'], produtos, 0)

print(total_produtos)


letras = ['B', 'C']

total_letras = reduce(lambda acc, letra: acc + letra, letras, 'A')

print(total_letras)
