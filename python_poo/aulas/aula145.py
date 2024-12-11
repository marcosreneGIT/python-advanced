# fução decoradoras e decoradores com métodos

def quadrado(metodo):
    def par_impar(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)
        resultado *= resultado
        
        print(f'\nSe multiplicarmos seu número por {args[0]}\nE logo após fizermos ele ao quadrador...\n\nEle será:', end=' ')
        
        if resultado % 2 == 0:
            return 'PAR'
        return 'IMPAR.'

    return par_impar


class Numerico:
    def __init__(self, numero = int):
        self.numero =  numero
    
    @quadrado   
    def multiplo(self, mult):
        return self.numero * mult       
   
    
dois = Numerico(2)
tres = Numerico(3)


print(dois.multiplo(3))
print(tres.multiplo(3))
