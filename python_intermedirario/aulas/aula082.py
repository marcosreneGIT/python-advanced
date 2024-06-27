# valores truthy e falsy, tipos mutáveis e imutáveis
# mutáveis [] {} set()
# imutáveis () "" 0 0.0 none false range(0, 10)

# mutáveis
lista = []
dicionario = {}
colecao = set()

# imutáveis
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)


def falsy(valor):
    return 'Falsy' if not valor else 'Truthy'

def test_falsy_truthy(nome, valor):
    return print(f'{nome} is', falsy(valor))
    

test_falsy_truthy('test', 'Teste')
test_falsy_truthy('list', lista)  
test_falsy_truthy('dict', dicionario)
test_falsy_truthy('set', colecao)
test_falsy_truthy('tuple', tupla)
test_falsy_truthy('str', string)
test_falsy_truthy('int', inteiro)
test_falsy_truthy('float', flutuante)
test_falsy_truthy('None', nada)
test_falsy_truthy('False', falso)
test_falsy_truthy('range', intervalo)

