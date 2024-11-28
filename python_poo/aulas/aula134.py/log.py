# abstração
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log.')

    def log_error(self, msg):
        return self._log(f'Error! {msg}' )

    def log_succes(self, msg):
        return self._log(f'Succes! {msg}')
    

class LogFileMixin(Log):
    def _log(self, msg):
        formatação = f'Saída: {msg} ({self.__class__.__name__}).'
        print('Salvando arquivo...')
        with open(LOG_FILE, 'a', encoding='utf8') as arquivo:
            arquivo.write(formatação)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'Saída: {msg} ({self.__class__.__name__}).')
    

if __name__ == '__main__':
    log_f = LogFileMixin()
    log_f.log_succes('Exemplo de mensagem.')
    log_f.log_error ('Exemplo de mensagem.')

    log_p = LogPrintMixin()
    log_p.log_error ('Exemplo de mensagem.')