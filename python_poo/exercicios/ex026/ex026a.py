# exercício - Salve sua classe em JSON

# salve os dados da sua classe em JSON e depois crie novamente as instâncias da classe com os dados salvos
# faça em arquivos separados.
import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    

pessoa_0 = Pessoa('Marcos', 21)
dados_pessoais = vars(pessoa_0)

path = 'C:\\Users\\marco\\Documents\\Estudos\\back-end\\python_2\\python_poo\\exercicios\\ex026\\ex026.json'

with open(path, 'w', encoding='utf8') as file:
    json.dump(dados_pessoais, file, indent=2)