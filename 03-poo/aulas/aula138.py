# criando Exceptions em Python Orientado a Objetos 

# para criar uma Exception em Python, você só precisa herdar de alguma exceção da linguagem.
# a recomendação da doc é herdar de Exception (https://docs.python.org/3/library/exceptions.html).

# criando exeções (comum colocar Error ao final).
# levantando (raise) e lançando (throw)
# relançando exceções 

# adicionando notas em exceções (3.11.0)

class FooError(Exception): pass


class BarError(Exception): pass 


def raise_(): 
    exception_ = FooError('ErrorX', 'ErrorY')
    exception_.add_note('Note')
    
    raise exception_


try:
    raise_()

except (FooError, BarError, ZeroDivisionError) as error:
    print(f'Name: {error.__class__.__name__}\nError: {error}\n')
    
    exception_ = BarError('New Error')
    exception_.add_note  ('New Note' )
    
    raise exception_ from error
