# csv.writer e csv.DictWriter para escrever em CSV

import csv
from pathlib import Path


CAMINHO_CSV = Path(__file__).parent / 'aula179.csv'

clientes = [
    {'Nome': 'Marco', 'Endereco': 'Rua RE'},
    {'Nome': 'Maria', 'Endereco': 'Rua FA'}
]

with open(CAMINHO_CSV, 'w') as arquivo:
    colunas = clientes[0].keys()
    escritor = csv.DictWriter(arquivo, fieldnames=colunas)
    escritor.writeheader()
    
    for cliente in clientes:
        escritor.writerow(cliente)