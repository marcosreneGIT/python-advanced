# usando calendar para calendários e datas 

# docs:
# # https://docs.python.org/3/library/calendar.html

# calendar é usado para coisas genéricas de calendários e datas.
# com calendar, você pode saber coisas como:
# - qual o ultimo dia do mês (ex.: monthrange)
# - qual o nome e número do dia de determinada data (ex.: weekday)
# - criar um calendário em si (ex.: monthcalendar)
# - trabalhar com coisas específicas de calendários (ex.: calendar, month)

# por padrão dia da semana começa em 0 ate 6 (0 = segunda | 6 = domingo)

import calendar 


calendario_2025 = calendar.calendar(2025)
print(calendario_2025) # ano completo

janeiro_2025 = calendar.month(2025, 1) 
print(janeiro_2025) # mês completo

primeiro_dia_semana, ultimo_dia = calendar.monthrange(2025, 1)
print(primeiro_dia_semana, ultimo_dia) # dia: 2 = quarta | ultimo dia: 31

print(calendar.day_name[primeiro_dia_semana])
print(calendar.day_name[calendar.weekday(2025, 1, ultimo_dia)])


for week in calendar.monthcalendar(2025, 1):
    print(week) # 0 = dias não correspondentes aquele mês
    for day in week:
        print(day)