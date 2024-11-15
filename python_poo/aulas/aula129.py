# relações entre classes: associação, agregação e composição
# agregação é uma forma mais especializada de associação entre dois ou mais objetos. 
# cada objeto terá seu ciclo de vida independente.
# geralmente é uma relação de um para muitos, onde um objeto tem um ou muitos objetos.
# os objetos podem viver separadamente, mas pode se tratar de uma relação onde um objeto precisa de outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

class Carrinho:
    def __init__(self):
        self._produtos = []

    def inserir_produto(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)
    
    def listar_produtos(self):
        for produto in self._produtos:
            print(f'Nome: {produto.nome} | Preço: R${produto.preco}')

    def total(self):
        return sum([produto.preco for produto in self._produtos])

    
class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, value):
        self._preco = value

carrinho = Carrinho()
produto_0, produto_1 = Produto('Caneta', 1.20), Produto('Camisa', 20)

carrinho.inserir_produto(produto_0, produto_1)
carrinho.listar_produtos()

print(f'Total: R${carrinho.total()}')