# classes decoradoras (Decorator classes)

class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador
        
    def __call__(self, func):
        def interna(*args, **kwargs):
            result = func(*args, **kwargs)
            
            return result * self._multiplicador
        return interna
    
@Multiplicar(2)
def soma(x, y):
    return x + y

somar = soma(2, 4)
print(somar)

