"""Este é um módulo de exemplo 
Este módulo contém funções e exemplos de documentação de funções."""

variavel_1 = 1

# def soma(
# x: int | float,
# y: int | float) -> int | float: ==

def soma(x, y):
    """Soma x e y
    A função soma você ja conhece bem.
    
    :param x: Número 1
    :type x: int ou float
    
    :param y: Número 2
    :type y: int ou float
    
    :return: A soma entre x e y
    :rtype: int or float"""
    
    return x + y


def multiplicar(
    x: int | float,
    y: int | float,
    z: int | float | None = None 
    
) -> int | float: # == def multiplicar(x, y, z=None):
    """Multiplica x, y e/ou z
    Multiplica x e y. Se z for enviado, multiplica x, y z.
    """
    
    if z is not None:
        return x * y * z
    
    return x * y


variavel_2 = 2
variavel_3 = 3
variavel_4 = 4



