from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None: 
        
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
        print(f'AGÊNCIA: {self.agencia}\n'
              f'NÚMERO DA CONTA: {self.conta}\n'
              f'SALDO: R$ {self.saldo:.2f}\n')

    @abstractmethod
    def sacar(self, valor: float) -> float: ...
    
    def depositar(self, valor: float) -> float | None:
        if valor > 0:
            self.saldo += valor
            self.detalhes(f'Deposito de R$ {valor:.2f} concluído.\n')
            return self.saldo
        print('Não é possível depositar valores nulos.\n')
        
    def detalhes(self, msg: str ='') -> None:
        print(f'{msg}O seu saldo atual é de: R$ {self.saldo:.2f}.\n')
        

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite_extra: float = 0):
        super().__init__(agencia, conta, saldo)
        
        self.limite_extra = limite_extra
            
    def sacar(self, valor: float) -> float | None:
        self.detalhes(f'Valor que você deseja sacar R$ {valor:.2f}\n'
                      f'Você possui R$ {self.limite_extra:.2f} '
                      'de limite extra.\n')
        
        if valor <= (self.saldo + self.limite_extra) and valor > 0:
            saldo_atual = self.saldo
            
            if valor > self.saldo:
                limite_ultizado = valor - self.saldo
                self.saldo = 0
                
                self.detalhes(f'Você retirou R$ {valor:.2f} de '
                              f'R$ {saldo_atual:.2f}\n'
                              'Você utilizou seu limite extra de '
                              f'{limite_ultizado:.2f}.\n'
                              'Saque concluido com sucesso.\n')
                return self.saldo
            
            self.saldo -= valor
            self.detalhes(f'Você retirou R$ {valor:.2f} de ' 
                          f'R$ {saldo_atual:.2f}\n'
                           'Saque concluido com sucesso. \n')
            return self.saldo
        
        print('Não foi possível efetuar o saque.\n')
                

class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float | None:
        self.detalhes(f'Valor que você deseja sacar R$ {valor:.2f}\n')
         
        if valor <= self.saldo and valor > 0:
            saldo_atual = self.saldo
            self.saldo -= valor 
             
            self.detalhes(f'Você retirou R$ {valor:.2f} '
                          f'de R$ {saldo_atual:.2f}\n'
                          f'Saque concluido com sucesso. \n')
            return self.saldo
        
        print('Não foi possível efetuar o saque.\n')
        

if __name__ == '__main__':
    conta_corrente = ContaCorrente(1, 10, 1000, 100)
    
    conta_corrente.depositar(100)
    conta_corrente.sacar(600)
    
    
    conta_poupanca = ContaPoupanca(2, 20, 2000) 
    
    conta_poupanca.depositar(200)
    conta_poupanca.sacar(700)
       