"""
métodos úteis:
    append - adiciona um item ao final
    insert - adiciona um item no índice escolhido
    pop - remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas

Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Marcos')

nome = lista.pop()
print(nome)

lista.append(00)
del lista[-1]

# lista.clear()

lista.insert(100, 5)
print(lista[4])