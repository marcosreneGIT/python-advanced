# criando datas com módulo datatime

# datatime(ano, mês, dia)
# datatime(ano, mês, dia, horas, minutos, segundos, microsegundos)

# datatime.strptime('DATA', 'FORMATO')

# datatime.now()

# datetime.fromtimestamp(Unix Timestamp)

# https://docs.python.org/3/library/datetime.html
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

# pip install pytz types-pytz

from datetime import datetime


data = datetime(2025, 1, 27) # padrão EUA
print(data)

data_str = '27 01 2025 08 35' 
data_formato = '%d %m %Y %H %M' # seguir o mesmo padrão de 'data_str' 

data_formatada = datetime.strptime(data_str, data_formato)
print(data_formatada)