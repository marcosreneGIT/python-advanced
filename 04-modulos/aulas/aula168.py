# os.walk() para navegar em caminhos de forma recursiva.

# serve para revisar diretorios e seus subdiretorios, juntos com seus arquivos.
# funciona melhor de maneira geral, pórem perde em desempenho em relacção a o listdir.
  
# função que gera um sequência de tuplas, onde cada tupla possui três elementos:

    # root: diretorio atual
    # dirs: lista de subdiretórios
    # files: lista dos arquivos do diretório atual
    
import os
from itertools import count


c = count()
path = os.path.join('/Users', 'marco', 'Documents', 'Estudos', 'back-end', 
                       'python_2', 'testes')

for root, dirs, files in os.walk(path):
    counter = next(c)
    
    print(counter, f'root: {root} dirs: {dirs} files: {files}')

# os.remove/os.unlink = apaga tudo no diretorio (CUIDADO).