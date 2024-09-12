
def validacao(nome=None):

    def validar(func):

        def checar_num(x, y):
            if x < 0 or y < 0:
                raise ValueError('X e Y não podem ser negativos.')
            
            res = func(x, y)
            return f'{res} {nome}'
        return checar_num
    
    return validar
            

@validacao('Segundo')
@validacao('Primeiro')
def soma(x, y):
    return x + y


@validacao()
def mult(x, y):
    return x * y

print(soma(2, 3))
print(mult(5, 6))