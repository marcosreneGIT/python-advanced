
def validacao(a=None, b=None):

    def validar(func):

        def checar_num(x, y):
            if x < 0 or y < 0:
                raise ValueError('X e Y não podem ser negativos.')
            
            return func(x, y)
            
        return checar_num
    
    return validar
            

@validacao()
def soma(x, y):
    return x + y


@validacao()
def mult(x, y):
    return x * y

print(soma(2, 3))
print(mult(5, 6))