"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número inteiro: ') 

try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('Seu número é par.')
    else:
        print('Seu número é impar.')
except:
    print('Você não dogitou um número inteiro. Tente novamente!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Informe a hora atual: ')

try:
    hora_int = int(hora)

    if 0 <= hora_int <= 11:
        print('Bom dia!')
    elif 12 <= hora_int <= 17:
        print('Boa tarde!')
    else:
        print('Boa noite!')
except:
    print('Você não digitou o horario corretamente. Tente novamente!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Informe seu nome: ')

try: 

    nome_int = int(nome)
    nome_float = float(nome)
    
    print('Este não é o seu verdadeiro nome. Tente novamente!')

except:
    
    if len(nome) <= 4:
        print('Seu nome é curto.')
    elif 5 <= len(nome) <= 6:
        print('Seu nome é normal.')
    else:
        print('Seu nome é muito grande.')