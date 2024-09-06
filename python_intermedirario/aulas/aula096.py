# variaveis livres + nonlocal (local , global)

def fora(x):
    a = x
    def dentro():
        return a
    return dentro

dentro_0 = fora(10)
dentro_1 = fora(20)

print(dentro_0())
print(dentro_1())


def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_final

        valor_final += valor_a_concatenar
        return valor_final

    
    return interna

string_concatenada = concatenar('a ')

print(string_concatenada('b '))
print(string_concatenada('c '))
print(string_concatenada('d '))