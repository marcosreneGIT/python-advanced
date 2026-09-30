"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo

Criar um sistema bancário (extremamente simplificado) que tenha clientes, contas
e um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas correntes tem um limite extra.


Conta(ABC)
    ContaCorrente 
    ContaPoupanca
    
Pessoa
    Cliente 
        Cliente > Conta
        
Banco
    Banco > Cliente 
    Banco > Conta


Dicas:

Criar classes Cliente que herda da classe Pessoa (Herança)

    Pessoa tem NOME e IDADE (com getters) # USO DIDÁTICO
    Cliente TEM CONTA (Agregação da classe ContaCorrente ou ContaPoupanca)


Criar classes ContaCorrente e ContaPoupanca que herdam de Conta

    Contas têm AGÊNCIA, NÚMEROS DA CONTA e SALDO
    Contas devem ter métodos para DEPÓSITOS
    Conta (super classe) deve ter o método SACAR abstrato (Abstração e
    polimorfismo. As subclasses que implementam) 

    ContaCorrente deve ter limite extra 
    

Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será resposável autenticar o cliente e as contas da seguinte maneira:

    Banco tem contas e clientes (Agregação)
        - Checar se a agência é daquela banco
        - Checar se o cliente é daquele banco 
        - Checar se a conta é daquele banco
        
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
        
"""