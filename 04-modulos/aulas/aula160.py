# pip install pytz types-pytz 

from datetime import datetime
from pytz import timezone


data_atual = datetime.now()
print(data_atual)

data_Tokyo = datetime.now(timezone('Asia/Tokyo'))
print(data_Tokyo)

print(data_atual.timestamp()) # número inteiro de segundos. (1970)
print(data_atual.fromtimestamp(1737982327.835883)) # data formatada

