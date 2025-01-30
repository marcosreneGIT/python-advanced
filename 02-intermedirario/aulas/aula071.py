# Operadores úteis:

# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

set_0 = {1, 2, 3}
set_1 = {2, 3, 4}

set_2 = set_0 | set_1 # união
set_3 = set_0 & set_1 # intersecção
set_4 = set_1 - set_0 # diferença
set_5 = set_0 ^ set_1 # diferença simétrica

print(set_2) # |
print(set_3) # &
print(set_4) # -
print(set_5) # ^