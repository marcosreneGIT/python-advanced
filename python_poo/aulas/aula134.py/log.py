# abstração

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log.')

    def log_error(self, msg):
        return self._log(f'Error! {msg}')

    def log_succes(self, msg):
        return self._log(f'Succes! {msg}')
    

class LogFileMixin(Log):
    def _log(self, msg):
        return f'Saída: {msg} ({self.__class__.__name__}).'


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'Saída: {msg} ({self.__class__.__name__}).')
    

if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_error('Exemplo de mensagem.')
    l.log_succes('Exemplo de mensagem.')
    

