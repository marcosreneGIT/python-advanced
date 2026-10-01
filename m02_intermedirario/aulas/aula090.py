# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def zero_divisao_erro(d):
    if d == 0:
        raise ZeroDivisionError ('Você está tentando dividir por zero (0).')
    return True
    
def obrigatoriedade_int_float (n):
    tipo_n = type(n)
    
    if not isinstance(n, (int, float)):
        raise TypeError(
            f'"{n}" deve ser int ou float.'
            f'"{tipo_n.__name__}" enviado.'
        )
    return True

def divide(n, d):
    obrigatoriedade_int_float(n)
    obrigatoriedade_int_float(d)

    zero_divisao_erro(d)

    return n / d

print(divide(8, '0'))
    