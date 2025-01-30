def validar(func):
    def checar_num(x, y):
        if x < 0 or y < 0:
            raise ValueError('X e Y não podem ser negativos.')
        
        return func(x, y)
        
    return checar_num
        

@validar
def soma(x, y):
    return x + y

print(soma(2, 3))
