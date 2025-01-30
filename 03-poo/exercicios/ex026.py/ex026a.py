# exercício - Salve sua classe em JSON

# salve os dados da sua classe em JSON e depois crie novamente as instâncias da classe com os dados salvos
# faça em arquivos separados.
import json


PATH = 'C:\\Users\\marco\\Documents\\Estudos\\back-end\\python_2\\python_poo\\exercicios\\ex026\\ex026.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    

pessoa_0 = Pessoa('Marcos', 21)
pessoa_1 = Pessoa('Maria', 33)

data = [vars(pessoa_0), vars(pessoa_1)]

with open(PATH, 'w', encoding='utf8') as file:
    json.dump(data, file, indent=2)