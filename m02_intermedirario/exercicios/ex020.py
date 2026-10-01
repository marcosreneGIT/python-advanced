from copy import deepcopy
# copy, sorted, produtos.sort

# Exercícios

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

def traco():
    print('-'*38)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = deepcopy(produtos)

for produto in novos_produtos:
    produto['preco'] += (produto['preco'] * 0.10)
    
print(*novos_produtos, sep='\n')

traco()


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = deepcopy(sorted(produtos, key=lambda produto : produto['nome'], reverse=True))

print(*produtos_ordenados_por_nome, sep='\n')

traco()

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = deepcopy(sorted(produtos, key=lambda produto : produto['preco']))
print(*produtos_ordenados_por_preco, sep='\n')

traco()