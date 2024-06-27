# dir, hasattr e getattr em Python

string = 'Marcos'
metodo = 'lower'

if hasattr(string, metodo):
    print(f'O método {metodo}() é plausível')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)