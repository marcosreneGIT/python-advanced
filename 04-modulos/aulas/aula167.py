# os.listdir serve para navegar em caminhos e listar diretorios.
# deve ser ultilizado focando em apenas um unico diretorio expecifico.
# foco em desempenho e precisão.

import os 


# C:\Users\marco\Documents\Estudos\back-end\python_2\testes\caminho
caminho = os.path.join('/Users', 'marco', 'Documents', 'Estudos', 'back-end', 
                       'python_2', 'testes', 'caminho')

print(os.listdir(caminho),'\n') # arquivos no diretorio 'caminho'

for pastas in os.listdir(caminho): 
    caminho_pasta = os.path.join(caminho, pastas)
    print(pastas)
    
    if not os.path.isdir(caminho_pasta):
        continue
    
    for arquivos in os.listdir(caminho_pasta):
        print(' ', arquivos) # para percorrer camadas de diretorios a melhor 
                             # opção é o os.walk. 
                             