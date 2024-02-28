primeiro_valor = input('Digite um número: ')
segundo_valor = input('Digite outro número: ')

if primeiro_valor > segundo_valor:
    print(f'O número {primeiro_valor} é maior que o número {segundo_valor}')
elif segundo_valor > primeiro_valor:
    print(f'O número {segundo_valor} é maior que o número {primeiro_valor}')
else:
    print(f'O primeiro número possui o mesmo valor que o segundo número: {primeiro_valor}')