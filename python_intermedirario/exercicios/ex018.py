def perguntas(per, opc, res):
   return {
        'Pergunta': per,
        'Opções': opc,
        'Resposta': res,
    },


jogo = [
    perguntas(
        'Qual a atual capital do Brasil?',
        ['Salvador', 'Brasília', 'São Paulo', 'Rio de Janeiro'],
        'Brasília',
    ),
    perguntas(
        'Qual oceano banha a costa do Brasil?',
        ['Pacífico', 'Atlântico', 'Índico', 'Ártico'],
        'Atlântico',
    ),
    perguntas(
        'Qual é a principal vegetação encontrada na região nordeste do Brasil?',
        ['Floresta Amazônica', 'Mata Atlântica', 'Cerrado', 'Caatinga'],
        'Caatinga'
    )
]

i = 0
contador_acertos = 0

while i < len(jogo):
    print(jogo[i][0]['Pergunta'], '\n')

    for j, opcao in enumerate(jogo[i][0]['Opções']):
        print(f'{j + 1})', opcao)

    resposta_str = input('\nEscolha uma opção: ')

    try:
        resposta_int = int(resposta_str)
        resposta_correta = jogo[i][0]['Opções'][resposta_int - 1] == jogo[i][0]['Resposta']

        if  resposta_correta:
            print('\nAcertou!\n')
            contador_acertos += 1

        else:
            print('\nErrou!\n')

    except:
        print('\nOpção invalida! Tente novamente.\n')
        continue
   
    i += 1

print(f'Total de acertos: {contador_acertos}\n')

