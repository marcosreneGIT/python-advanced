# problemas dos parametros mutaveis em funçao pyhton


# def lista_compras(item, lista = []): # evitar usar valores padroes para paramentros mutaveis
def lista_compras(item, lista = None):
    if lista == None:
        lista = [] # assim sempre que chamada a funçao criarar uma nova lista

    lista.append(item)
    return lista

lista_0 = lista_compras('Maça')
lista_1 = lista_compras('Banana')
lista_compras('Mamão', lista_1)

print(lista_0)
print(lista_1)