
def multiplicando(multiplicador):
    def resultado(numero):
        return numero * multiplicador
    return resultado

duplicar = multiplicando(2)
triplicar = multiplicando(3)
quadruplicar = multiplicando(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
