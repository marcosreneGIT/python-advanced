"""
iterando strings com while
"""
#       012345678910
nome = 'Marcos Renê'  # iteráveis
#      1110987654321

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

nova_string = ''
nova_string += 'M-a-r-c-o-s- -R-e-n-ê'
print(nova_string)


indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]

    novo_nome += letra
    indice += 1

    if indice < len(nome):
        novo_nome += '-'

print(novo_nome)