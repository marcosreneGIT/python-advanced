# introdução à List comprehension em Python
# list comprehension é uma forma rápida para criar listas a partir de iteráveis.

lista = []

for numero in range(10):
    lista.append(numero)


lista = [numero for numero in range(10)]

print(lista)

multiplo_dois = [numero * 2 for numero in range(10)]

print(multiplo_dois)