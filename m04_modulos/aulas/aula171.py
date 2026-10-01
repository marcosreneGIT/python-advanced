# os + shutil 
# apagando, copiando, movendo e renomeando pastas com python

# vamos copiar arquivos de uma pasta para outra.

# shutil.copy = copiar
# shutil.copytree = copiar recursivamente 
# shutil.rmtree = apagar recursivamente
# shutil.move = renomear/mover

# os.unlink = apagar
# os.rename = renomear/mover

import os, shutil


HOME  = os.path.expanduser('~')
PASTA = os.path.join(HOME, 'Documents', 'EStudos', 
                    'back-end', 'python_2', 'testes', 'caminho')

NOVA_PASTA =  os.path.join(HOME, 'Documents', 'EStudos',
                        'back-end', 'python_2', 'testes', 'novo-caminho')

shutil.rmtree(NOVA_PASTA, ignore_errors=True) 
shutil.copytree(PASTA, NOVA_PASTA) # = aula 170

