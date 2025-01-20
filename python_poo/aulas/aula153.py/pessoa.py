import conta

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self._nome  = nome
        self._idade = idade
        
    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome
        
    @property
    def idade(self) -> int:
        return self._idade
    
    @idade.setter
    def idade(self, idade: int) -> None:
        self._idade = idade
        
    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}: ({self.nome!r}, {self.idade!r})'
    
    
class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: conta.Conta | None = None
        
        
if __name__ == '__main__':
    cliente_0 = Cliente('Marcos', 21)
    
    cliente_0.conta = conta.ContaCorrente(1, 10, 100, 1000)
    
    print(cliente_0, '\n')
    cliente_0.conta.sacar(100)