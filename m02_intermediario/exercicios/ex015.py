def multiplicador(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

numeros = (1, 2, 3, 4, 5)

numeros_mult = multiplicador(1, 2, 3, 4, 5)
numeros_mult_tupla = multiplicador(*numeros)

print(numeros_mult)
print(numeros_mult_tupla)