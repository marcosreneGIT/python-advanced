import pessoa, conta, banco


marcos = pessoa.Cliente('Marcos', 21)
conta_corrente_0 = conta.ContaCorrente(1, 1, 0, 100)

marcos.conta = conta_corrente_0

maria = pessoa.Cliente('Maria', 59)
conta_poupanca_0 = conta.ContaPoupanca(2, 2, 200)

maria.conta = conta_poupanca_0


nubanco = banco.Banco(
    [1, 2, 3], 
    [marcos, maria], 
    [conta_corrente_0, conta_poupanca_0]
    )

if nubanco.autenticar(marcos, conta_corrente_0):
    marcos.conta.depositar(0)
    marcos.conta.depositar(100)
    
    marcos.conta.sacar(200)
    
if nubanco.autenticar(maria, conta_corrente_0):
    maria.conta.depositar(200)
    