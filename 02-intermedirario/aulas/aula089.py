# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
try:
    print('Open File')
    a = 8
    b = 8
    c = a / b
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('Não é possivel dividir por zero (0).')
except IndexError as e:
    print(e.__class__.__name__)
    print('Indice indisponível.')
except (NameError, ImportError) as e:
    print(e.__class__.__name__)
    
    if e.__class__.__name__ == 'NameError':
        print('Nome errado.')

    elif e.__class__.__name__ == 'ImportError':
        print('Importe mal sucedido.')
else:
    print('Nenhum erro encontrado.')
finally:
    print('Close File')