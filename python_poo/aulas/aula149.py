def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__})'


class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('Meta.__new__')
        
        cls = super().__new__(mcs, name, bases, dct)
        cls.__repr__ = meu_repr 
        return cls
    
    def __call__(cls, *args, **kwargs):
        inst = super().__call__(*args, **kwargs)
        return inst
    
    
class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('Pessoa.__new__')

        inst =  super().__new__(cls)
        return inst
    
    def __init__(self, nome):
        print('Pessoa.__init__')
        
        self.nome = nome


pessoa_1 = Pessoa('Marcos')