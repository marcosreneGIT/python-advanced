import abc


class Conta(abc.ABC):
    def __init__(self, agencia, num_conta, saldo):
        
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo
        
    def detalhes(self, msg=''):
        print(f'{msg}O seu saldo atual é de: R${self.saldo:.2f}.\n')
        
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'Deposito de R${valor:.2f} concluído.\n')

    @abc.abstractmethod
    def sacar(self, valor): ...
    

class ContaCorrente(Conta):
    limite_extra = 200
    
    def sacar(self, valor):
        print(f'Valor que você deseja sacar R$:{valor:.2f}')
        
        if valor <= (self.saldo + self.limite_extra):
            print(f'Você sacou R${valor:.2f}'
                  f' do seu saldo de R${self.saldo:.2f}')
            
            if valor >= self.saldo:
                print('Você utilizou seu limite extra.\nSeu saldo atual é de '
                      f'{(self.saldo + self.limite_extra) - valor:.2f}')
                return
            else:
                print(f'Seu saldo atual é de R${self.saldo - valor:.2f}')
                return
                
        return 'Você não possui saldo suficiente.'
                

# class ContaPoupanca(Conta):
#     def sacar(self, valor):
#         ...

pessoa = ContaCorrente(1, 10, 500)

pessoa.depositar(500)
print(pessoa.sacar(1200))
