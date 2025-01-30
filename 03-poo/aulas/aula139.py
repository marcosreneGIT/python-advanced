# teoria: Python Special Methods ou Dunder Methods

# Dunder = Double Underscore = __dunder__
# artigos: https://rszalski.github.io/magicmethods/ 
         # https://docs.python.org/3/reference/datamodel.html#specialnames

# exemplos: 
# __lt__(self, other) : self < other 
# __gt__(self, other) : self > other 

# __str__(self) : str

# existe inumeros metodos, por isso é recomendada a leitura da documentação

class Ponto:
    def __init__(self, x, y, z ='245'):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self): # fornecer uma representação legível e amigável do objeto, voltada para o usuário.
        return f'({self.x}, {self.y}, {self.z})'
    
    def __repr__(self): # fornecer uma representação detalhada e não ambígua do objeto, voltada para desenvolvedores.
        class_name = type(self).__name__ # = self.__class__.__name__
        return f'{class_name}(x = {self.x!r}, y = {self.y!r}, z = {self.z!r})'
    
ponto_0 = Ponto(321, 233)
ponto_1 = Ponto(795, 205)

print(ponto_0)
print(repr(ponto_1))