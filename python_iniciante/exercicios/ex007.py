frase = 'Olá Mundo!'.lower()

i = 0
quantidade_mais_repetida = 0
letra_mais_repetida = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    quantidade_mais_repetida_atual = frase.count(letra_atual)

    if quantidade_mais_repetida_atual > quantidade_mais_repetida:
        quantidade_mais_repetida = quantidade_mais_repetida_atual
        letra_mais_repetida = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_mais_repetida}". Que apareceu '
    f'{quantidade_mais_repetida}x'
)