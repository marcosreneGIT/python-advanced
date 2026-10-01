# método especial __call__

# callable é algo que pode ser executado com parênteses 
# como por exemplo: foo() ou foo('bar')

# em classes normais, __call__ faz a instância de uma classe "callable"

class CallMe:
    def __init__(self, phone):
        self.phone = phone
        
    def __call__(self, name):
        print(f'{name} está chamando {self.phone}')
        
        # return ...
        
        
cell_1 = CallMe('5584999230098')
cell_1('Marcos Renê')