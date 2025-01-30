# os.listdir serve para navegar em caminhos e listar diretorios.

import os 


# C:\Users\marco\Documents\Estudos\back-end\python_2\testes\caminho
caminho = os.path.join('/Users', 'marco', 'Documents', 'Estudos', 'back-end', 
                       'python_2', 'testes', 'caminho')

for pastas in os.listdir(caminho):
    caminho_pasta = os.path.join(caminho, pastas)
    print(pastas)
    
    if not os.path.isdir(caminho_pasta):
        continue
    
    for arquivos in os.listdir(caminho_pasta):
        print(' ', arquivos)