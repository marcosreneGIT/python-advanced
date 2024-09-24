# reduce é uma função que faz a redução de um interavel em um valor.

from functools import reduce


numeros = [1, 2, 3, 4, 5]

total_numeros = reduce(
    lambda x, y: x * y, numeros, 0
)

print(total_numeros)