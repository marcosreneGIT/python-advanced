# super() e a sobreposição de membros | Python Orientado a Objetos

# class MyStr(str):
#     def upper(self):
#         print('Chamou UPPER.')
#         return super().upper()
    

# variavel = MyStr('Hello, World!')

# print(variavel.upper())

class A:
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, b):
        super().__init__(atributo)
        self.b = b

    def metodo(self):
        super().metodo()
        print('B')

    
class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def metodo(self):
        super(B, self).metodo()
        print('C')


c = C('Atributo', 'B')

print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)

c.metodo()

print(c.atributo, c.b)