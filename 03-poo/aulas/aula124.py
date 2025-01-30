# method vs @classmethod vs @staticmethod

# method : self, método de instância
# @classmethod : cls, método de classe
# @staticmethod : método estático, sem acesso a self e cls
class Connection:
    
    def __init__(self, host='localhost' ):
        self.host = host
        self.user = None
        self.password = None
        

    # method
    def set_user(self, user): # setter
        self.user = user

    # method
    def set_password(self, password):
        self.password = password

    # @classmethod
    @classmethod
    def creat_whit_auth(cls, user, password):
        connection = cls()

        connection.user = user
        connection.password = password
        
        return connection
    
    # @staticmethod
    @staticmethod
    def log(msg):
        return msg

# method

# user = Connection()

# user.set_user('Marcos')
# user.set_password('AMal82nC')


# print(f'Usuário: {user.user}\nSenha: {user.password}')


# @classmeth

# user = Connection.creat_whit_auth('Marcos', 'AMal82nC')

# print(f'Usuário: {user.user}\nSenha: {user.password}')


# @staticmethod

# print(Connection.log('Você está logado.'))