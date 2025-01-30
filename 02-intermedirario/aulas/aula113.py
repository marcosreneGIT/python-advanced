# guard clause - evite o uso exagerado de condicioanis (if, elif, else)

lista = []


def adicionar(item, lista):

    if not item:
        print('\nNão há item para se adicionar.')
        return
    
    lista.append(item)
    print()
    for i in lista:
        print(f'- {i}')

    return lista


def remover(lista):

    if len(lista) <= 0:
        print('\nNão há nada para remover.')
        return
    
    lista.pop()
     
    for i in lista:
        print(f'- {i}')

    return lista


while True:
    print('\nOpções: [A]dicionar | [R]emover')
    opcao = input('Escolha uma opção: ').upper().strip()[0]


    if opcao != 'A' and opcao != 'R':
        print('\nOpção invalida. Tente novamente!')
        continue

    if opcao == 'A':
        item = input('\nDigite algo: ')


    opcoes = {
        'A': lambda: adicionar(item, lista),
        'R': lambda: remover(lista)
    }

    executar = opcoes.get(opcao)()
