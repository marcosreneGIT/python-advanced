# datetime.timedelta e dateutil.relativetimedelta (calculando datas)

# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime, timedelta


data_i = datetime.strptime('2003/09/04 15:45:34', '%Y/%m/%d %H:%M:%S')
data_f = datetime.now()

delta = timedelta(days=data_f.day)

datas = (data_i, data_f,
        (data_i > data_f),
        (data_i < data_f),
        (data_f - data_i),
        (data_i + delta ))

for data in datas:
    print(data)


from dateutil.relativedelta import relativedelta

relativedelta_total = relativedelta(data_f, data_i)

print(relativedelta_total.years)
print(data_i + relativedelta(years=data_f.year))
