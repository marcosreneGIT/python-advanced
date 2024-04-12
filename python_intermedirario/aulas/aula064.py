# Manipulando chaves e valores em dicionários
pessoa = {}

chave = 'nome'

pessoa[chave] = 'Marcos Renê'
pessoa['sobrenome'] = 'Gomes'

print(pessoa[chave])

pessoa[chave] = 'Maria'
del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('Não encontrado!')

else:
    print(pessoa['sobrenome'])

