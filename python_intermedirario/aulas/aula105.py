# filter é um filtro funcional

def print_iter(iter):
    print(*list(iter), sep='\n')
    print()


produtos = [
    {'nome': 'produto 1', 'preco': 10},
    {'nome': 'produto 2', 'preco': 20},
    {'nome': 'produto 3', 'preco': 30},
    {'nome': 'produto 4', 'preco': 40},
    {'nome': 'produto 5', 'preco': 50},
]

# novos_produtos = [
    # produto for produto in produtos
    # if produto['preco'] >= 30]

novos_produtos = list(filter(
    lambda produto : produto['preco'] >= 30, produtos
))

print_iter(produtos)
print_iter(novos_produtos)