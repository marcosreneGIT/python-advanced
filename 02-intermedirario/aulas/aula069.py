# Sets são eficientes para remover valores duplicados de iteráveis.

# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)


lista_0 = [1, 2, 3, 3, 3, 3, 3, 1]

set_0 = set(lista_0)

lista_1 = list(set_0)

print(lista_1)


print(3 in set_0)

for numero in set_0:
    print(numero)

