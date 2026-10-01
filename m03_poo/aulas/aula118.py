class Animal:

    def __init__(self, nome):
        self.nome = nome # self permite a transição de dados entre metodos da classe 

        variavel = 'Escopo local\n' # ja variaveis tem escopo local

    def comendo(self, alimento):

        return f'{self.nome} está se alimentando de {alimento}'
    

macaco = Animal('Macaco')

print(macaco.comendo('banana'))