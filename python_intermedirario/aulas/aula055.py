"""
introdução às funções (def) em Python

funções são trechos de código usados para replicar determinada ação ao longo do seu código.
elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
por padrão, funções Python retornam None (nada).
"""

def imprimir(a, b, c):
     print(a, b, c)


imprimir(1, 2, 3)
imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')


saudacao('Luiz Otávio')
saudacao('Maria')
saudacao('Helena')
saudacao()