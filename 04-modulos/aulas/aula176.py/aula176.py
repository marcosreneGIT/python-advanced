from pathlib import Path


caminho_pasta = Path(__file__).parent / 'pasta'
caminho_subpasta = caminho_pasta / 'subpasta'
caminho_subpasta_arquivo = caminho_subpasta / 'arquivo.txt'

caminho_pasta.mkdir(exist_ok=True) # criando um diretorio
caminho_subpasta.mkdir(exist_ok=True) # criando outro diretorio #dentro do anterrior

caminho_subpasta_arquivo.touch(exist_ok=True) # criando um arquivo dentro da subpasta

def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print(f'Dir: {file}')
            rmtree(file, False)
            file.rmdir()
        else:
            print(f'File: {file}')
            file.unlink
        
    if remove_root:
        root.rmdir()
            
rmtree(caminho_pasta)