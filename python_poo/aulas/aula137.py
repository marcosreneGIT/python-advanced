# polimorfismo em Python Orientado a Objetos 

# polimorfismo é o princípio que permite que classes derivadas de uma mesma superclasse
# tenham métodos iguais (com a mesma assinatura) mas comportamentos diferentes.


# assinatura do método = mesmo nome e quantidade de parâmetros (retorno não faz parte da assinatura).

# opinião + princípios que contam:
# assimatura do método = nome, parâmetros e retorno iguais     


# SO "L" ID
# Liskov Substitution Principle (princípio da substituição de Liskov)
# objetos de uma superclasse devem ser substituíveis por objetos de uma subclasse sem quebrar a aplicação.

# sobrecaga de métodos = overload (python não suporta)
# sobreposição de métodos = override (python suporta)

from abc import ABC, abstractmethod


class Notificacao(ABC):

    def __init__(self, msg) -> None:
        self.msg = msg

    @abstractmethod
    def enviar(self) -> bool: pass


class NotificacaoEmail(Notificacao):

    def enviar(self) -> bool:
        print(f'E-mail enviando: {self.msg}')

        return True 
    

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print(f'SMS enviando: {self.msg}')

        return True 
    

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        return 'Notificação foi enviada com sucesso!'
    
    return 'ERROR! Notificação não enviada.'


notificacao_email = NotificacaoEmail('Exemplo EMAIL')
notificacao_sms = NotificacaoSMS('Exemplo SMS')

print(notificar(notificacao_email))
print(notificar(notificacao_sms))
