import abc


class Conta(abc.ABC):
    def __init__(self, agencia, num_conta, saldo):
        
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo
        
    def detalhes(self, msg=''):
        print(f'{msg}O seu saldo atual é de: R${self.saldo:.2f}.')
        
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'Deposito de R${valor:.2f} concluído.\n')

    # @abc.abstractmethod
    # def sacar(self, valor): ...
    
pessoa = Conta(1, 10, 0)

pessoa.depositar(50)
        