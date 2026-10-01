# os.path trabalha com caminhos em Windowns, Linux e Mac

# docs:
# https://docs.python.org/3/library/os.path.html#module-os.path

# os.path é o módulo para se trabalhar com caminhos de arquivos.
# ideal para todos os sistemas, sem se preocupar com suas diferenças.

# exemplo do os.path: 
# os.path.join() = junta strings em um único caminho.
    # - os.path.join('pasta-1', 'pasta-2', 'arquivo.txt') 
    
    # linux e mac = pasta-1/pasta-2/arquivo.txt
    # windows = pasta-1\pasta-2\arquivo.txt
    

# os.path.split(): divide um caminho em uma tupla(diretório, arquivo)
    # - os.path.split('home/user/arquivo.txt') = ('home/user', 'arquivo.txt'). 


# os.path.exists(): verifica se um caminho especificado existe.
    # - os.path.exists('home/user/arquivo.txt') = False
    

# os.path só trabalha com caminhos de arquivos e não faz nenhuma operação 
# entrada/saída (I/O) com os arquivos em si.

import os 

caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
print(f'Caminho: {caminho}\n')

diretorio, arquirvo = os.path.split(caminho)
print(f'Diretorio: {diretorio}\nArquivo: {arquirvo}\n')

nome_arquivo, extensao_arquivo = os.path.splitext(arquirvo)
print(f'Nome: {nome_arquivo}\nExtensão: {extensao_arquivo}\n')

caminho_absoluto = os.path.abspath('.') # . = caminho atual.
print(caminho_absoluto, '\n')

caminho_existente = os.path.exists(caminho_absoluto) # = True

if caminho_existente:
    print('Encotrei o caminho.')
    
else:
    print('Não encotrei o caminho.')
    
print()


# os.path.basename() aponta por ultimo "nome" listado.
# os.path.dirname informa o diretorio listado.

print(f'Caminho: {caminho}\n{os.path.basename(caminho)}\n')          
print(f'Diretorio: {os.path.dirname(caminho)}\n{os.path.basename(diretorio)}\n')
