"""
escopo de funções em Python

escopo significa o local onde aquele código pode atingir.
existe o escopo global e local.
o escopo global é o escopo onde todo o código é alcançavel.
o escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
"""

x = 1


def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)