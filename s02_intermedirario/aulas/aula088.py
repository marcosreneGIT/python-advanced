# parte 2 - try e except para tratar exceções
# a = 18
# b = 0
#

try:
    a = 18
    b = 0
    c = a / b

except ZeroDivisionError as e:
    # print(e.__class__.__name__)
    # print(e)
    print('divisão por zero')

except NameError:
    print('variavel não definida')

except(TypeError, IndexError) as e:
    if e.__class__.__name__ == 'TypeError':
        print('tipo invalido')

    elif e.__class__.__name__ == 'IndexError':
        print('indice invalido')
        
except Exception:
    print('Um erro desconhecido ocorreu.')

else:
    print(f'O resultado da divisião é: {c}')
