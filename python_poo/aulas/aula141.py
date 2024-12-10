# __new__ e __init__ em classes Python ('contrutores')

# __new__ é o método responsável por criar e retornar o novo objeto.
# __new__ recebe (cls) e não (self), pois é ele o que cria.
# __new__ DEVE retornar o novo objeto!

# __init__ é o método responsável por inicializar a instância.
# __init__ por isso, init recebe (self).
# __init__ NÃO DEVE retornar None!

# Object é a super classe de um classe.

class A:
    def __new__(cls, *args, **kwargs):
        print('Antes da criação.')
        inst = super().__new__(cls)
        print('Depois da crição.')
        
        return inst
    
    def __init__(self, x):
        self.x = x
        print('__init__')
        

a = A(123)
print(a.x)