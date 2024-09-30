# criando arquivos com Python + Context Manager with

# usamos a função open para abrir um arquivo em Python (ele pode ou não existir)

# modos:
# r (leitura)
# w (escrita) 
# x (para criação)
# a (escreve ao final)
# b (binário)
# t (modo texto) 
# + (leitura e escrita)
# context manager: with (abre e fecha) 

# métodos úteis;
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)

# módulo os:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo

# módulo json:
# json.dump - gera um arquivo json
# json.load - carrega um arquivo json

caminho = 'C:\\Users\\marco\\Documents\Estudos\python_2\\caminho\\' # utilizar sempre duas barras (\\) para evitar erros.
caminho += 'aula109.py'

# arquivo = open(caminho, 'w')
# arquivo.close

# with: ja garante o fechamento do arquivo

with open(caminho, 'w') as arquivo:
    print('Arquivo aberto.')
    
print('Arquivo fechado.')