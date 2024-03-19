"""
iterável -> str, range, etc (__iter__)
iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""


texto = 'Marcos'  # iterável

iteratador = iter(texto)  # iterator

while True:
     try:
         letra = next(iteratador)
         print(letra)
     except StopIteration:
         break
     
print( )

for letra in texto:
    print(letra)