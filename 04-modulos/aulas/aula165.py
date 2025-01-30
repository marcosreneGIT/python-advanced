# o módulo 'os' serve para interações com o sistema

# docs:
# https://docs.python.org/3/library/os.html

# o módulo 'os' fornece funciolidades para interagir com o sistema operacional.

# exemplos:
# os.path (path = módulo) contém funções para trabalhar com caminhos de arquivos.
# os.listdir() (listdir = função) pode ser usada para listar os arquivos.
# os.system() permite execultar comandos do sistema operacional no Python.

# exemplo (os.system):
# Windows 11 (PowerShell), Linux, Mac = os.system('clear')
# sistemas anteriores = os.system('cls')

import os


os.system('echo "Hello World"') # 'echo' é um comando de prompt = print
                                # O Python apenas repassa o comando para o OS