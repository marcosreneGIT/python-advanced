from pathlib import Path


HOME = Path.home()
print(HOME) # home do usuário

caminho = Path() # caminho do projeto atual (python_2)
caminho_arquivo = Path(__file__) # caminho do arquivo atual (aula175.py)

print(caminho) # = (.)
print(caminho.absolute()) # = caminho escrito

print(caminho_arquivo.parent.parent) # = diretorio "pai"/"avô"...

arquivo_json = caminho_arquivo.parent / 'aula175.json' 
print(arquivo_json) # caminho com um arquivo json

arquivo_json.touch() # cria o arquivo 
arquivo_json.unlink() # apaga o arquivo

arquivo_json.touch()
arquivo_json.write_text('Olá, Mundo!') # escreve no arquivo
print(arquivo_json.read_text()) # lê o que esta ecrito no arquivo


arquivo_json.unlink()
caminho_arquivo_json = Path(__file__).parent / 'aula175.json'

with caminho_arquivo_json.open('a+') as arquivo: # escrevendo em multiplas linhas
    arquivo.write('A\n')
    arquivo.write('B\n')
    arquivo.write('C\n')
    
print(caminho_arquivo_json.read_text())