# from functools import partial


# map, partial e esgotamento de iterators

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


# def aumentar_preco(valor, porcentagem):
    # return round(valor * porcentagem, 2)

# dez_porcento = partial(aumentar_preco, porcentagem = 1.1)


# novos_produtos = [
    # {**produto, 'preco': dez_porcento(produto['preco'])}
    #  for produto in produtos]


# map - para mapear dados

novos_produtos = list(map(
    lambda produto : {**produto, 'preco': round(produto['preco'] * 1.1, 2)}, produtos))

print_iter(produtos)
print_iter(novos_produtos)
