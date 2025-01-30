while True:

    numero_1 = input('\nDigite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('\nDigite um operador (+-/*): ')

   
    num_1_float = 0
    num_2_float = 0
    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:

        if numeros_validos is None:
            print('\nUm ou ambos os números digitados são invalidos. Tente novamente!')
            continue

    operadores_validos = '+-/*'

    if operador not in operadores_validos:
        print('\nOperador invalido. Tente novamente!')
        continue 

    if len(operador) > 1:
        print('\nDigite apenas um operador. Tente novamente!')
        continue

    if len(operador) == 0:
        print('\nDigite um operador. Tente novamente!')
        continue

    print('\nResultado: ', end='')
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)

    sair = input('\nDeseja sair? [s]im: ').lower().startswith('s')

    if sair:
        break