# Funções decoradoras e decoradores com classes:

def add_repr(cls):
    
   def repr(self):
       class_name = self.__class__.__name__
       class_dict = self.__dict__
       return f'{class_name}({class_dict})'
   
   cls.__repr__ = repr
   return cls


@add_repr
class Alfabeto:
    def __init__(self, letra):
        self.letra = letra
        

@add_repr
class Numerico:
    def __init__(self, numero):
        self.numero = numero
        

a = Alfabeto('A')
b = Alfabeto('B')

um = Numerico(1)
dois = Numerico(2)

print(f'{a}\n{b}\n')
print(f'{um}\n{dois}')