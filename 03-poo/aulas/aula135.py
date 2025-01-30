# classes abstratas - Abstract Base Class (ABC)

# ABCs são usadas como contratos para a definição de novas classes,
# elas podem forçar outras classes a criarem métodos concretos.

# também podem ter métodos concretos por elas mesmas,
# e (@abstractmethods) que são métodos que não têm corpo.

# as regras para classes abstratas com métodos abstratos é que elas NÃO PODEM ser instânciadas diretamente,
# métodos abstratos DEVEM ser implementados nas subclasses (@abstractmethods)

# uma classe abstrata em Python tem sua metaclasse sendo ABCMeta.

# é possivel criar @property @setter @classmethod @staticmethod e @method como abstratos,
# para isso use @abstractmethod como decorartor mais interno.

from abc import ABC, abstractmethod


class Log(ABC):
    @abstractmethod
    def _log(self, msg): pass

    def login_sucess(self, msg):
        return self._log(f'Succes! {msg}')
    
    def login_error(self, msg):
        return self._log(f'Error! {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        return f'{msg} ({self.__class__.__name__})'
    

ex = LogFileMixin()

print(ex.login_error('Exemplo de mensagem.'))
