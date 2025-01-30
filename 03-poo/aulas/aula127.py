# encapsulamento (modificadores de acesso: public, protected, private), python NÃO TEM modificadores de acesso.
# mas podemos seguir as seguintes convenções:
#   (sem underline) = public
#       pode ser usado em qualquer lugar

# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.

# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

class Test:
    def __init__(self):
        self.public = '  = public'
        self._protected = '_ = protected'
        self.__private = '__ = private'

    
    def public_method(self):
        print('  = public method')

    
    def _protected_method(self):
        print('_ = _protected')

    
    def __private_method(self):
        print('__ = __private')

    


t = Test()

print(t.public)
t.public_method()

print(t._protected)
t._protected_method()

print(t.__private) # sem acesso (name mangling)
t._Test__private_method() # _Test no inicio é uma maneira de se ter acesso (o que não é aconselhado).
