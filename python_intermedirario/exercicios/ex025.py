# exercício - lista de tarefas com desfazer e refazer

# todo = [] - lista de tarefas

# todo = ['fazer café'] - adicionar fazer café
# todo = ['fazer café', 'caminhar'] - adicionar caminhar

# desfazer = ['fazer café',] - refazer ['caminhar']
# desfazer = [] - refazer ['caminhar', 'fazer café']

# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar'] 

# música para codar: Everybody wants to rule the world - Tears for fears


lista_tarefas = []
lista_reseva  = []

# menu - opçoes: adcionar, desfazer e refazer

def adicionar_tarefa(lista_adicionar, tarefa):
    lista = lista_adicionar.append(tarefa)
    print(f'"{tarefa}" foi adicionado a sua lista de tarefas.')

    return lista


def confirmar_adicao(lista):
     while True:
        adicao = input('\nInforme a tarefa: ').capitalize()
        adicionar_tarefa(lista, adicao)
        while True:
            confirmacao = input('\nDeseja adicionar outra tarefa a sua lista? [S/N]: ').upper()
            if   confirmacao == 'N':
                break
            elif confirmacao == 'S':
                break
            else:
                print('\nOpção invalida. Tente novamente!')

        if confirmacao == 'N':
            break


def remover_tarefa(lista_remover, lista_resevar):
    if len(lista_remover) > 0:
        confirmacao = input(f'\nDeseja mesmo remover "{lista_remover[-1]}" da sua lista de tarefas? [S/N]: ').upper()

        if confirmacao == 'S':
            lista = lista_resevar.append(lista_remover[-1])
            lista_remover.pop()
            return lista

        elif confirmacao == 'N':
            if len(lista_remover) > 1:
                segunda_confiramacao = input('\nDeseja remover alguma outra tarefa da sua lista?  [S/N]: ').upper()

                if segunda_confiramacao == 'S':

                    for i in range(len(lista_remover) -2, -1, -1):
                        terceira_confirmacao = input(f'\nDeseja remover "{lista_remover[i]}" da sua lista de tarefas? [S/N]: ').upper()

                        if terceira_confirmacao == 'S':
                            lista_resevar.append(lista_remover[i])
                            lista_remover.pop(i)
                            continue
                        
                        elif terceira_confirmacao == 'N':
                            continue

                        else:
                            print('Opção invalida. Tente novamente!')
                    print('\nSua lista chegou ao fim.')
    else: 
        print('\nNão há nada a ser removido.')
                        

def desfazer_remover(lista_desfazer, lista_adicionar):
    if len(lista_adicionar) > 0:
        tarefa = lista_desfazer[-1]

        lista = lista_adicionar.append(tarefa)
        lista_desfazer.pop()

        print(f'{tarefa} retornou a sua lista de tarefas.')

        return lista

    else:
        print('\nNão há nenhuma tarefa removida!')

    

def listar_lista(lista):
    print('')
    if len(lista) > 0:
        for item in lista:

            print('-', item)
    else:
        print('Não há nada para se listar.')


def menu(lista_adicionar, lista_resevar, opcao):
    
    if   opcao == 1:
        confirmar_adicao(lista_adicionar)
  
    elif opcao == 2:
        remover_tarefa(lista_adicionar, lista_resevar)

    elif opcao == 3:
        desfazer_remover(lista_resevar, lista_adicionar)
    
    elif opcao == 4:
        listar_lista(lista_adicionar)



while True:
    print('\nComandos: [1] Adicionar | [2] Remover | [3] Desfazer | [4] Listar | [0] Sair')
    try:
        opcao = int(input('Escolha uma opção: '))
        
        if   opcao == 0:
            break
        elif 1 <= opcao <= 4:
            menu(lista_adicionar=lista_tarefas, lista_resevar= lista_reseva, opcao=opcao)
        else:
            print('\nOpção não disponível. Tente novamente!')

    except ValueError:
        print('\nOpção inválida. Tente novamente!')

        