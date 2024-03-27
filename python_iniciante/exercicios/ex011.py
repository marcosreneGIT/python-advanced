"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista_compras = []

while True:

    print('\n[I]nserir | [A]pagar | [L]istar | [S]air')
    opcao = input('\nDigite a opção que deseja ultilizar: ').upper()

    if opcao == 'I':
        item_compras = input('\nAdicione o item a lista: ')
        lista_compras.append(item_compras)
        os.system('cls') 
        print('Item adicionado com sucesso!')
    elif opcao == 'A':
        indice_str = input('\nEscolha um indice para apagar: ')

        try:

            os.system('cls') 
            indice = int(indice_str)

            del lista_compras[indice]
            print('Item apagado com sucesso!')

        except  ValueError:
            os.system('cls') 
            print('\nPor favor digite um número inteiro!')
        except IndexError:
            os.system('cls') 
            print('\nEste valor não esta na lista!')
        except Exception:
            os.system('cls') 
            print('\n[err0]')

    elif opcao == 'L':
         
        os.system('cls')

        if len(lista_compras) == 0:
            print('\nNada para listar.')
        else:

            for i, item in enumerate(lista_compras):
                print(i, item)

    elif opcao == 'S':
        os.system('cls') 
        break 

    else:
        os.system('cls') 
        print('\nEscolha uma opção valida.')
        