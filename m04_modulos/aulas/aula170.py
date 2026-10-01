# os + shutil
# copiando arquivos com python

# vamos copiar arquivos de uma pasta para outra.
# shutil.copy = copiar 

import os, shutil

HOME  = os.path.expanduser('~')
PASTA = os.path.join(HOME, 'Documents', 'EStudos', 
                    'back-end', 'python_2', 'testes', 'caminho')

NOVA_PASTA =  os.path.join(HOME, 'Documents', 'EStudos',
                        'back-end', 'python_2', 'testes', 'novo-caminho')

os.makedirs(NOVA_PASTA, exist_ok=True) # criando uma nova pasta.


for root, dirs, files in os.walk(PASTA):
    for dir in dirs:
        novo_dir = os.path.join(root.replace(PASTA, NOVA_PASTA), dir)
        os.makedirs(novo_dir, exist_ok=True)
        
    for file in files:
        caminho_arquivo = os.path.join(root, file)
        novo_caminho_arquivo = os.path.join(root.replace(PASTA, NOVA_PASTA), file)

        shutil.copy(caminho_arquivo, novo_caminho_arquivo)
        