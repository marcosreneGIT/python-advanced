# @staticmethod (métodos estáticos)
# métodos estáticos são métodos que estão dentro da classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua classe.

class Classe:
    def funcao():
        ...

objeto = Classe()

Classe.funcao()
objeto.funcao()