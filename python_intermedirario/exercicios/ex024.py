"""
considerando duas listas de inteiros ou floats (lista A e lista B)

some os valores nas listas retornando uma nova lista com os valores somados:
se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

resultado:
lista_soma = [2, 4, 6, 8]
"""

lista_0 = [1, 2, 3, 4, 5, 6, 7]
lista_1 = [1, 2, 3, 4]


def somador_listas(lista_x=[0], lista_y=[0]):

    listas_somadas = list(zip(lista_x, lista_y))

    def somador_valores():
        nonlocal listas_somadas

        lista_somada = []

        for i in listas_somadas:
            lista_somada.append(i[0] + i[1])

        return lista_somada

    return somador_valores


lista_somada = somador_listas(lista_0, lista_1)
lista_2 = lista_somada()

print(lista_2)



