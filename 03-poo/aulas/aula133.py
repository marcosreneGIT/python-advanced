# herança múltipla - Python Orientado a Objetos

# quer dizer que no Python, uma classe pode estender várias outras classes.

# herança simples:
# Animal -> Mamifero -> Humano -> Cliente
# Cliente(Humano)

# Herança múltipla e mixins:
# Animal -> Mamifero -> Humano -> Cliente
# Log -> FileLog

# Cliente(Humano, FileLog)

# problema do diamante: 

# A, B, C, D
# D(B, C) - C(A) - B(A) - A

#           A
#         /   \
#        B     C
#         \   /
#           D

# python 3 usa C3 superclass linearization para gerar o mro.

# para saber a ordem de chamada dos métodos
# use o método de classe Classe.mro()
# ou o atributo __mro__ (Dunder - Double Underscore)

class A:
    pass

    def informar_classe(self):
        print('A')
    

class B(A):
    pass
    
    # def informar_classe(self):
    #     print('B')


class C(A):
    pass

    def informar_classe(self):
        print('C')

    
class D(B, C):
    pass

    # def informar_classe(self):
    #     print('D')
    

d = D()
d.informar_classe()

print(D.mro())