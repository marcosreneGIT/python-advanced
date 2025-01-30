# Métodos úteis:
# add, update, clear, discard

set_0 = set()
set_1 = set()

set_0.add('Marcos') # uma unica entrada 
set_0.add(1) # uma unica entrada 

set_0.update(('Olá mundo', 1, 2, 3, 4)) # mais de uma entrada # atenção na ultilização de um interravel

set_1.clear() # limpa

set_0.discard('Olá mundo') # descarta um dado

print(set_0)