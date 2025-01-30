produtos = [
    {'nome': 'feijão', 'preco': 10, 'tipo': 'alimento', },
    {'nome': 'arroz' , 'preco': 5 , 'tipo': 'alimento', },
    {'nome': 'café'  , 'preco': 8 , 'tipo': 'alimento', },
    {'nome': 'sabão' , 'preco': 3 , 'tipo': 'higiênico', }
]

valor_promoção = 0.1 # %

promoção_produtos = [
    {**produto, 'preco': produto['preco'] - (produto['preco'] * valor_promoção)}
    if produto['preco'] > 5.50 else {**produto}

     for produto in produtos   
]

print(*promoção_produtos, sep='\n')