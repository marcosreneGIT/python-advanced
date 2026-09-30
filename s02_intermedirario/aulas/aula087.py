# parte1 - try e except para tratar exceções

# a = 18
# b = 0
# c = a / 

try:
    a = 18
    b = 0

    c = a / b

except ZeroDivisionError:
    print('Não é possivel se dividir por 0 (zero).')

except NameError:
    print('Variável não está definada.')

except (TypeError, IndexError, SyntaxError):
    print('Tipo de dado invalido.')

except Exception:
    print('Um erro desconhecido ocorreu.')

else:
    print(f'O resultado da divisião é: {c}')
