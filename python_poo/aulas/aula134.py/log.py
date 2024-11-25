# abstração

class Log:
    def log(self, msg):
        raise NotImplementedError('Implemente o método log.')
    

class LogFileMixin(Log):
    def log(self, msg):
        return msg


if __name__ == '__main__':
    l = LogFileMixin()
    print(l.log('Exemplo de mensagem.'))
    