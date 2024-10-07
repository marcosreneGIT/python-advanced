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

    return lista


def remover_tarefa(lista_remover, lista_resevar):
    lista = lista_resevar.append(lista_remover[-1])
    lista_remover.pop()
    
    return lista 


def desfazer_remover(lista_desfazer, lista_adicionar):
    lista = lista_adicionar.append(lista_desfazer[-1])
    lista_desfazer.pop()

    return lista


def menu(lista_adicionar, lista_resevar = None, opcao = None):
    
    if   opcao == 1:
        adicao = input('Informe a tarefa: ')
        adicionar_tarefa(lista_adicionar, adicao)

    elif opcao == 2:
        remover_tarefa(lista_adicionar, lista_resevar)

    elif opcao == 3:
        desfazer_remover(lista_resevar, lista_adicionar)



while True:
    print('Comandos: | [1] Adicionar | [2] Remover | [3] Desfazer | [4] Listar | [0] Sair |')
    try:
        opcao = int(input('Escolha uma opção: '))
        
        if   opcao == 1:
            menu(lista_adicionar=lista_tarefas, opcao=1)
        elif opcao == 2:
            menu(lista_adicionar=lista_tarefas, lista_resevar= lista_reseva, opcao=2)
        elif opcao == 3:
            menu(lista_adicionar=lista_tarefas, lista_resevar= lista_reseva, opcao=3)
        elif opcao == 4:
            print(lista_tarefas)
        elif opcao == 0:
            break
        else:
            print('Opção não disponível. Tente novamente!')

    except ValueError:
        print('Opção inválida. Tente novamente!')


