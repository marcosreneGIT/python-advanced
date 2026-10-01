# metaclasses são o tipo das classes

# em python, tudo é um objeto (incluindo classes)
# então, qual é o tipo de uma classe? (type)


# seu objeto é uma instância da sua classe
# sua classe é uma instância de type (type é uma metaclasse)
# type('Name', (Bases,), __dict__)


# ao criar uma classe, coisas ocorrem por padrão nesssa ordem:

# __new__ da metaclasse é chamado e cria a nova classe (class Foo:)

# __call__ da metaclasse é chamado com os argumentos e chama (f = Foo(x)): 
    # __new__ da classe com os argumentos (cria a instância)
    # __init__ da classe com os argumentos
# __call__ da metaclasse termina a execução


# métodos importantes da metaclasse 
# __new__(mcs, name, bases, dct) - cria a classe 
# __call__(cls, *args, **kwargs) - cria e inicializa a instância

# "Metaclasses são magias mais profundas do que 99% dos usuários
# deveriam se preocupar. Se você quer saber se precisa delas, 
# não precisa (as pessoas que realmente precisam sabem
# com certeza que precisam delas e não precisam de uma explicação
# sobre o porquê)."
# — Tim Peters (CPython Core Developer)

Foo = type('Foo', (object,), {})
f = Foo()

print(type(Foo))
print(type(f))
