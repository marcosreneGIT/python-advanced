# csv.reader e csv.DictReader

# csv.reader lê em formato de lista
# csv.DictReader lê em formato de dicionário

import csv
from pathlib import Path


CAMINHO_CSV = Path(__file__).parent / 'aula177.py' / 'aula177.csv'

with open(CAMINHO_CSV, 'r') as arquivo:
    lista = csv.reader(arquivo) # csv.DictReader faria o mesmo 
                                # so que em formato de dicionário
    
    for linha in lista:
        print(linha)
