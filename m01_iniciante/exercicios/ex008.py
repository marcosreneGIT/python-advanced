"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.

- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.

    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.

Faça a contagem de tentativas do seu usuário.
"""

palavra_secreta = 'python'
tentativas = 0
tentativas_corretas = 0

while True:
    letra_digitada = input('\nDigite apenas uma letra: ').lower()

    if len(letra_digitada) == 0 or len(letra_digitada) > 1 or letra_digitada.isnumeric() == True:

        print('\nPreencha os dados corretamente!')
        continue

    tentativas += 1

    if letra_digitada in palavra_secreta:
        print('\n', letra_digitada)
        tentativas_corretas += 1
    else:
        print('\n*')
    
    if tentativas_corretas == len(palavra_secreta):
        break

print(f'\nPalavra secreta: "{palavra_secreta}"!\nNúmeros de tentativas: {tentativas}')