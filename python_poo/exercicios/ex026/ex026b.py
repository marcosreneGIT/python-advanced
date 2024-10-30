import json 
from ex026a import PATH, Pessoa

with open(PATH, 'r', encoding='utf8') as file:
    data = json.load(file)

print(data, '\n')

pessoa_0 = Pessoa(**data[0])
pessoa_1 = Pessoa(**data[1])

print(pessoa_0.nome)