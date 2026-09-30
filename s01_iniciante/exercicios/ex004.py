"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ').strip()
idade = input('Digite sua idade: ')

if len(nome) > 0 and len(idade) > 0:

    idade_numero = int(idade)
    nome_ivertido = nome[::-1]

    print(f'\nSeu nome é {nome}')
    print(f'Seu nome invertido é {nome_ivertido.capitalize()}')
    
    if nome.count(' ') > 0:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome não contem espaços.')
    
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[len(nome) - 1]}')

else: 
    print('\nVocê deixou dados em branco. Tente novamente!')
