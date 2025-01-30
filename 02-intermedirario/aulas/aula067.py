# Métodos úteis dos dicionários em Python

pessoa = {
    'nome': 'Marcos Renê',
    'sobrenome': 'Gomes',
}

pessoa.get('nome', None) # get - obtém uma chave

pessoa.pop('nome') # pop - Apaga um item com a chave especificada (del)
pessoa.popitem() # popitem - Apaga o último item adicionado

pessoa.update({
     'nome': 'novo valor',
     'idade': 30,
 }) # update - Atualiza um dicionário com outro

# pessoa.update(nome='novo valor', idade=30)
# tupla  ou lista = (('nome', 'novo valor'), ('idade', 30))
# pessoa.update(tupla  ou lista)
