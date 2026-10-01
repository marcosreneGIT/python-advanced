# os.stat (dados) e os.getsize (tamanho)  
# o retorno dos dados relacionados a tamanho são em bytes

# https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

import os, math
from itertools import count


def formatar_bytes(tamanho_bytes: int, base = 1024) -> str:
    """
    Formata um tamanho, de bytes para o tamanho apropriado.
    """

    # se o tamanho for menor ou igual a zero = 0B.
    if tamanho_bytes <= 0:
        return '0B'
    
    # tupla com os tamanhos referentes.
    abreviacoes = ('B', 'KB', 'MB', 'GB', 'TB', 'PB')
                #   0    1     2     3     4     5 
                
    # logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    
    # math.log vai retornar o logaritmo do tamanho_bytes
    # com a base = 1024 (padrão), deve bater com os índices acima
    
    tamanho_referente = int(math.log(tamanho_bytes, base))
    
    # por quanto nosso tamanho deve ser dividido para gerar o tamanho exato.
    divisor_variavel = base ** tamanho_referente
    
    # tamanho final
    valor_formatado = tamanho_bytes / divisor_variavel
    
    abreviacao = abreviacoes[tamanho_referente]
    
    return f'{valor_formatado:.2f}{abreviacao}'


c = count()
caminho = os.path.join('/Users', 'marco', 'Documents', 'Estudos', 'back-end', 
                       'python_2', '03-poo')

for root, dirs, files in os.walk(caminho):
    contador = next(c)
    print(f'\n{contador} path: {root}\n')
    
    for dir_ in dirs:
        print(f'  {contador} folder: {dir_}') 
    print()
    
    for file_ in files:
        caminho_arquivo = os.path.join(root, file_)
        
        stats = os.stat(caminho_arquivo)
        arquivo_tamanho = stats.st_size # = os.path.getsize(caminho_arquivo)
        
        print(f'  {contador} file: {file_} {formatar_bytes(arquivo_tamanho)}')
        
        
