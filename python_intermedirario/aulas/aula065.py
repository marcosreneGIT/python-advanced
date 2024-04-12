# Métodos úteis dos dicionários em Python

pessoa = {
    'nome': 'Marcos Renê',
    'sobrenome': 'Gomes',
    # 'idade': 20,
}


print(len(pessoa)) # len - quantidade de chaves


print(list(pessoa.keys())) # keys - iterável com as chaves
print(list(pessoa.values())) # values - iterável com os valores
print(list(pessoa.items())) # items - iterável com chaves e valores

for chave, valor in pessoa.items():
     print(chave, valor)


pessoa.setdefault('idade', None) # setdefault - adiciona valor se a chave não existe
print(pessoa['idade'])
