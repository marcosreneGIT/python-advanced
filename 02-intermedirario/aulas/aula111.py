import json


# pessoa = {
#    'nome': 'Marcos Renê',
#    'sobrenome': 'Gomes',
#    'enderecos': [
#        {'rua ': 'R1', 'numero': 12},
#        {'rua' : 'R2', 'numero': 34}
#    ],
#    'altura': 1.9,
#    'numeros_da_sorte': (0, 4, 8),
#    'dev': True,
#    'nada': None
# }

# with open('aula111.json', 'w', encoding='utf8') as arquivo:
#    json.dump(pessoa, arquivo, indent=2)


with open('aula111.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)

    print(pessoa)