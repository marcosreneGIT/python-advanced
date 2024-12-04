# criando Exceptions em Python Orientado a Objetos 

# para criar uma Exception em Python, você só precisa herdar de alguma exceção da linguagem.
# a recomendação da doc é herdar de Exception (https://docs.python.org/3/library/exceptions.html).

# criando exeções (comum colocar Error ao final).
# levantando (raise) e lançando (throw)
# relançando exceções 

# adicionando notas em exceções (3.11.0)

class MyError(Exception): pass