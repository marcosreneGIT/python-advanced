import conta, pessoa


class Banco:
    def __init__(self, 
                 agencias: list[int] | None = None,
                 clientes: list[pessoa.Pessoa] | None = None,
                 contas: list[conta.Conta] | None = None
                 ) -> None:
        
       self.agencias = agencias or []
       self.clientes = clientes or []
       self.contas = contas or []
       
    def _checar_agencia(self, conta: conta.Conta) -> bool:
        
        print(f"{'AGÊNCIA':<15}:", end=' ')
        
        if conta.agencia in self.agencias:
            
            print('CONFIRMADO.')
            return True
        
        print('NEGADO.')
        return False
    
    def _checar_cliente(self, cliente: pessoa.Cliente) -> bool:
        
        print(f"{'CLIENTE':<15}:", end=' ')
        
        if cliente in self.clientes:
            
            print('CONFIRMADO.')
            return True
        
        print('NEGADO.')
        return False  
    
    def _checar_conta(self, conta: conta.Conta) -> bool:
        
        print(f"{'CONTA':15}:", end=' ')
        
        if conta in self.contas:
            
            print('CONFIRMADO.')      
            return True
        
        print('NEGADO.')
        return False
    
    def _checar_conta_cliente(self, 
                              conta: conta.Conta,
                              cliente: pessoa.Cliente)-> bool:
          
        print(f"\n{'CONTA CLIENTE':<15}:", end=' ')
        
        if conta is cliente.conta:
            print('CONFIRMADO.\n')
            return True

        print('NEGADO.\n')
        return False
        
    def autenticar(self, cliente: pessoa.Cliente, conta: conta.Conta) -> bool:
        return self._checar_agencia(conta) and \
            self._checar_cliente(cliente) and \
            self._checar_conta(conta) and \
            self._checar_conta_cliente(conta, cliente)
        
    def __repr__(self):
        return  f'{"AGÊNCIAS":<10}: {self.agencias!r}\n'\
                f'{"CLIENTES":<10}: {self.clientes!r}\n'\
                f'{"CONTAS":<10}: {self.contas!r}'

        
if __name__ == '__main__':
    cliente_0 = pessoa.Cliente('Marcos', 21)
    conta_cliente_0 = conta.ContaCorrente(1, 10, 100, 1000)
    
    cliente_0.conta = conta_cliente_0
    
    banco_0 = Banco([1, 2, 3, 4], [cliente_0], [conta_cliente_0])
    
    banco_0.autenticar(cliente_0, conta_cliente_0)
    
    print()
    print(banco_0)