class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        class_name = type(self).__name__
        
        return f'{class_name}(x = {self.x!r}, y = {self.y!r})'
    
    def __add__(self, other):
        soma_x = self.x + other.x
        soma_y = self.y + other.y
        
        return Ponto(soma_x, soma_y)
    
    def __gt__(self, other):
        soma_self = self.x + self.y
        soma_other = other.x + other.y
        
        resultado = soma_self - soma_other
        
        return resultado > 0
    

if __name__ == '__main__':
    ponto_0 = Ponto(1, 2)
    ponto_1 = Ponto(3, 4)
    
    ponto_2 = ponto_0 + ponto_1 
     
    print(ponto_2)
    
    print(f'P0 é maior que P1: {ponto_0 > ponto_1}')
    print(f'P1 é maior que P0: {ponto_1 > ponto_0}')
    