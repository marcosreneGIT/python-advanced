
"""
interpolação básica de strings

s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Marcos'
preco = 100.329555

variavel = '%s, o preço é %.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %i é igual a %x' % (2300, 2300))