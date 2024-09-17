# combinations, permutations e product - itertools

# combinação - ordem não importa - iterável + tamanho do grupo

# permutação - ordem importa

# produto - ordem importa e repete valores únicos

from itertools import combinations, permutations, product


def print_iter(iterator):

    print(*list(iterator), sep='\n')
    print()



lista = ['a', 'b', 'c', 'd']

print_iter(combinations(lista, 2))
print_iter(permutations(lista, 2))

roupas = [
    ['Blusas', 'Calças', 'Camisas', 'Camisetas', 'Saias', 'Vestidos' ],
    ['Algodão', 'Poliéster', 'Jeans'],
    ['Amarela', 'Azul', 'Branca', 'Laranja', 'Preta', 'Verde', 'Vermelho'],
    ['P', 'M', 'G', 'XG', 'XGG'],
    ['Masculino', 'Feminino', 'Unisex']
]

print_iter(product(*roupas))
