# @property - um getter no modo Pythônico

# getter - um método para obter um atributo
# modo pythônico - modo do Python de fazer coisas

# @property é uma propriedade do objeto, ela é um método que se comporta como um atributo 
# geralmente é usada nas seguintes situações:
# - como getter
# - evitar quebrar código cliente
# - habilitar setter
# - executar ações ao obter um atributo

# código cliente - é o código que usa seu código

# ------------------------------------------ 

# seu codigo

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade 


    @property
    def nome(self):
        print('@property')
        return self._nome
    

    @property
    def idade(self):
        print('@property')
        return self._idade
    
    
# ------------------------------------------ 

# codigo do cliente

pessoa = Pessoa('Marcos', 21)

print(pessoa.nome)
print(pessoa.idade)
