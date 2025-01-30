# empacotamento e desempacotamento de dicionários
# exemplo: 

a, b = 1, 2
a, b = b, a

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

# exemplo: 

pessoas_completa = {**pessoa, **dados_pessoa}


# args e kwargs
# kwargs - keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)
    print()


mostro_argumentos_nomeados(1, 2, nome='Joana', idade=19)
mostro_argumentos_nomeados(1, 2, **pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)