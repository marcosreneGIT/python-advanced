def validar(func):

    def valida(*args, **kwargs):

        for arg in args:
            e_string(arg)

        result = func(*args, **kwargs)

        print(f'Resultado: {result}')
        return result

    return valida

def e_string(string):
    if not isinstance(string, str):
        raise TypeError('Você deve digitar apenas letras.')
    
def inverter_str(string):
    return string[::-1]


inverter_str_checagem = validar(inverter_str)
invertida = inverter_str_checagem('123')

print(invertida)