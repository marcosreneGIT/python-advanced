import abc


class Conta(abc.ABC):
    def __init__(self, agencia, num_conta, saldo):
        
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo
        
        print(f'AGÊNCIA: {self.agencia}\n'
              f'NÚMERO DA CONTA: {self.num_conta}\n'
              f'SALDO: R$ {self.saldo:.2f}\n')

        
    def detalhes(self, msg=''):
        print(f'{msg}O seu saldo atual é de: R$ {self.saldo:.2f}.\n')
        
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'Deposito de R$ {valor:.2f} concluído.\n')

    @abc.abstractmethod
    def sacar(self, valor): ...
    

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
        
        return f'Você não possui saldo suficiente.'
                

class ContaPoupanca(Conta):
    def sacar(self, valor):
        saldo_atual = self.saldo
        self.detalhes(f'\nValor que você deseja sacar R$ {valor:.2f}\n')
         
        if valor <= self.saldo:
            self.saldo -= valor
             
            return self.detalhes(f'Você retirou R$ {valor:.2f} '
                                  f'de R$ {saldo_atual:.2f}\n'
                                  f'Saque concluido com sucesso. \n')
        
        return f'Você não possui saldo suficiente.'
             

pessoa_0 = ContaCorrente(1, 10, 500)
pessoa_1 = ContaPoupanca(2, 20, 200)

pessoa_0.depositar(500)
pessoa_1.depositar(200)

print(pessoa_0.sacar(1000))
print(pessoa_1.sacar(400))


