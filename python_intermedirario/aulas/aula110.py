# modos:

# r (leitura)
# w (escrita) 
# x (para criação)
# a (escreve ao final)
# b (binário)
# t (modo texto) 
# + (leitura e escrita)

# context manager: with (abre e fecha) 

# métodos úteis:

# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)


caminho = 'aula110.txt'

with open(caminho, 'w+', encoding= 'utf-8') as arquivo:
    print('Arquivo aberto.')

    arquivo.write('Atenção\n')
    arquivo.write('Linha A\n')
    arquivo.write('Linha B\n')
    arquivo.write('Linha C\n')

    arquivo.writelines(('Linha D\n', 'Linha F\n'))

    arquivo.seek(0, 0) 

    print(arquivo.read())

    arquivo.seek(0, 0)

    print(arquivo.readline(), end='')
    print(arquivo.readline(), end='')

    arquivo.seek(0, 0)

    for linha in arquivo.readlines():
        print(linha.strip())


print('Arquivo fechado.')


with open(caminho, 'r') as arquivo:
    print(arquivo.read())
