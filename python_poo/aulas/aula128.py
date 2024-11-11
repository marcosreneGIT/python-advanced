# relações entre classes: associação, agregação e composição

# associação é um tipo de relação onde os objetos estão ligados dentro do sistema.essa é a relação mais comum entre objetos e tem subconjuntos como agregação e composição (que veremos depois).
# geralmente, temos uma associação quando um objeto tem  um atributo que referencia outro objeto. a associação não especifica como um objeto controla o ciclo de vida de outro objeto.

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None
    
    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

    def trabalhar(self):
        return f'{self.nome} está escrenvendo seu livro com um(a) {self.ferramenta}'


class Ferramenta:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo.'
    
    def __str__(self):
        return self.nome  

    
escritora = Escritor('Agatha Christie')
lapis = Ferramenta('Lápis')
maquina_escrever = Ferramenta('Máquina de escrever')

escritora.ferramenta = maquina_escrever
escritora.ferramenta = lapis

print(maquina_escrever.escrever())
print(escritora.ferramenta.escrever())

print(escritora.trabalhar())
