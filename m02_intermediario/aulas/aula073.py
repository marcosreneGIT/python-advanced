# introdução à função lambda (função anônima de uma linha)

# a função lambda é uma função como qualquer outra em Python
# porém, são funções anônimas, que contém apenas uma linha. 
# ou seja, tudo deve ser contido dentro de uma única expressão.

lista_0 = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


def exibir(lista):
    for item in lista:
        print(item)
    print()


lista_1 = sorted(lista_0, key=lambda item : item['nome'])
lista_2 = sorted(lista_0, key=lambda item : item['sobrenome'])

exibir(lista_1)
exibir(lista_2)