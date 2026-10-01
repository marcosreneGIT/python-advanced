# relações entre classes: associação, agregação e composição
# composição é uma especialização da agregação.
# mas nela, quando o objeto "pai" for apagado, todas as referências dos objetos filhos também são apagadas.

class Cliente:
    def __init__(self, nome):
        self._nome = nome
        self._enderecos = []

    def inserir_enderecos(self, rua, numero):
        self._enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self._enderecos:
            print(f'Rua: {endereco.rua} | Número: {endereco.numero}')

    
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua 
        self.numero = numero


client_0 = Cliente('Marcos')
client_0.inserir_enderecos('A', 12)
client_0.inserir_enderecos('B', 13)

client_0.listar_enderecos()

del client_0

