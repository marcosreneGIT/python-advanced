# isinstace - para saber se objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (0, 1),
    {0, 1}, {'nome' : 'Marcos'}
]

for item in lista:
    if isinstance(item, set):
        item.add(2)
        print('set:', item, isinstance(item, set))

    elif isinstance(item, str):
        print('str:', item.upper(), isinstance(item, str))

    elif isinstance(item, (int, float)):
        print('num:', item, item * 2, isinstance(item, (int, float)))

    else: 
        print('outro:', item, isinstance(item, (list, tuple)))

    
