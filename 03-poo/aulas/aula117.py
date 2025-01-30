# métodos em instâncias de classes Python

class Carros:
    def __init__(self, nome):
        # self.nome = 'Gol' - Hard coded
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


gol = Carros('Gol')
print(gol.nome)
gol.acelerar()

celta = Carros('Celta')
print(celta.nome)
celta.acelerar()