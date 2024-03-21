"""
listas em python

tipo list - mutável
suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - índices e fatiamento
métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'João',  1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))