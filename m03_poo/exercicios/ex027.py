# exercício com classes

# 1 - crie uma classe Carro, Motor e Fabricante

# 2 - faça a ligação entre Carro tem um Motor
# obs.: Um motor pode ser de vários carros

# 3 - faça a ligação entre Carro e um Fabricante
# obs.: Um fabricante pode fabricar vários carros

# exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, modelo, ano, motor, fabricante):
        self.modelo = modelo
        self.ano = ano
        self.motor = motor
        self.fabricante = fabricante

    def __str__(self):
        return f'{self.modelo}, {self.ano}, {self.motor}, {self.fabricante}'
    
class Motor:
    def __init__(self, modelo, potencia):
        self.modelo = modelo
        self.potencia = potencia

    def __str__(self):
        return f'{self.modelo}, {self.potencia}'
    

class Fabricante:
    def __init__(self, nome, CNPJ):
        self.nome = nome 
        self.CNPJ = CNPJ

    def __str__(self):
        return f'{self.nome}, {self.CNPJ}'
    


motor_0 = Motor('Motor 1.0', '65 cv' )
motor_1 = Motor('Motor 2.0', '147 cv')

fabricante_0 = Fabricante('Volkswagen', '59.104.422/0001-50')
fabricante_1 = Fabricante('Honda', '01.192.333/0001-22.')


carro_0 = Carro('Gol' , 2004, motor_0, fabricante_0)
carro_1 = Carro('Polo', 2000, motor_0, fabricante_0)

carro_2 = Carro('Civic', 2024, motor_1, fabricante_1)
carro_3 = Carro('Suv'  , 2024, motor_1, fabricante_1)

carros = [carro_0, carro_1, carro_2, carro_3]

for i in range(0, len(carros)):
    print(carros[i],'\n')