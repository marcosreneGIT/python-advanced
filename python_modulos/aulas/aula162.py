# formatando datas do datetime

# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html

from datetime import datetime


data = datetime.now()
data_fmt = data.strftime('%d/%m/%Y %H:%M:%S')

print(data_fmt) #class str

print(data.strftime('%Y'), data.year)
