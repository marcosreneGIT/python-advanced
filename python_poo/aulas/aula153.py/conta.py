from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
        print(f'AGÊNCIA: {self.agencia}\n'
              f'NÚMERO DA CONTA: {self.conta}\n'
              f'SALDO: R$ {self.saldo:.2f}\n')

    @abstractmethod
    def sacar(self, valor): ...
    
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'Deposito de R$ {valor:.2f} concluído.\n')
        
    def detalhes(self, msg=''):
        print(f'{msg}O seu saldo atual é de: R$ {self.saldo:.2f}.\n')
        

class ContaCorrente(Conta):
    LIMITE_EXTRA = 200
    
    def sacar(self, valor):
        self.detalhes(f'Valor que você deseja sacar R$ {valor:.2f}\n'
                      f'Você possui R$ {self.LIMITE_EXTRA:.2f} '
                      'de limite extra.\n')
        
        if valor <= (self.saldo + self.LIMITE_EXTRA):
            saldo_atual = self.saldo
            
            if valor > self.saldo:
                limite_ultizado = valor - self.saldo
                self.saldo = 0
                
                return self.detalhes(f'Você retirou R$ {valor:.2f} de '
                                     f'R$ {saldo_atual:.2f}\n'
                                     'Você utilizou seu limite extra de '
                                     f'{limite_ultizado:.2f}.\n'
                                     'Saque concluido com sucesso.\n')
            else:
                self.saldo -= valor
                return self.detalhes(f'Você retirou R$ {valor:.2f} de ' 
                                     f'R$ {saldo_atual:.2f}\n'
                                     'Saque concluido com sucesso. \n')
        
        print('Não foi possível efetuar o saque.')
                

class ContaPoupanca(Conta):
    def sacar(self, valor):
        self.detalhes(f'\nValor que você deseja sacar R$ {valor:.2f}\n')
         
        if valor <= self.saldo and valor > 0:
            saldo_atual = self.saldo
            self.saldo -= valor 
             
            self.detalhes(f'Você retirou R$ {valor:.2f} '
                          f'de R$ {saldo_atual:.2f}\n'
                          f'Saque concluido com sucesso. \n')
            return self.saldo
        
        print('Não foi possível efetuar o saque.')
        
             