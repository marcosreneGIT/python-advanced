from log import LogPrintMixin


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def delisgar(self):
        if self._ligado:
            self._ligado = False
            

class Smartphone(Eletronico, LogPrintMixin):
    def ligar(self):
        super().ligar()
        
        if self._ligado:
            self.log_succes(f'O {self._nome} está ligado.')

    def delisgar(self):
        super().delisgar()

        if not self._ligado:
            self.log_error(f'Não foi possivel ligar o {self._nome}.')