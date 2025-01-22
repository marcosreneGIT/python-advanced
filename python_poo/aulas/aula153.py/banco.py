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
        print('Checar Agência:', end=' ')
        if conta.agencia in self.agencias:
            print('Confirmado.')
            return True
        
        print('Negado.')
        return False
    
    
if __name__ == '__main__':
    cliente_0 = pessoa.Cliente('Marcos', 21)
    conta_cliente_0 = conta.ContaCorrente(10, 10, 100, 1000)
    
    cliente_0.conta = conta_cliente_0
    
    banco_0 = Banco([1, 2, 3, 4])
    banco_0._checar_agencia(conta_cliente_0)