# context manager com classes 
# criando e usando gerenciadores de contexto

# você pode implementar seus próprios protocolos com (__dunder__).

# isso é chamado de Duck Typing:
# um conceito relacionado com tipagem dinâmica.
# o Python não relaciona o tipo (str, int...), mas sim os métodos em seu objeto (__enter__, __exit__...).
# (se anda como pato, nada como pato e voa como pato...)

# para criar um context manager, deve se aplicar os métodos __enter__ e __exit__.

# o método __exit__ receberá a classe de execeção, a exceção e o traceback.
# se ele retornar True, exceção no with será suprimidas.

# ex:
#    with open('aula142.txt', 'w') as file:

class MyOpen:
    def __init__(self, path_file, mode):
        self._file = None
        self.path_file = path_file
        self.mode = mode
        
    def __enter__(self):
        print('__enter__')
        self._file = open(self.path_file, self.mode, encoding='utf8')
        
        return self._file
    
    def __exit__(self, class_, exception_, traceback_):
        print('__exit__')
        self._file.close()
        
        # raise class_(*exception_.args).with_traceback(traceback_) # representação do erro e do que se pode fazer com ele.
        # exception_.add_note('My note.')...
        
        # return True # se True for retornado siguinifica que o erro foi devidamente tratato.
        
    
with MyOpen('aula142.txt', 'w') as file:
    file.write('Linha 1')
    
    print('with')
        