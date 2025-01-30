# Exercício solucionado: calculando as datas e parcelas de um empréstimo

# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos e 6 meses.

# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.

# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento apos 2 anos e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta


valor = 100_000
periodo_pagamento = relativedelta(years=5, months=6)

data_inicio_emprestimo = datetime(2020, 12, 20)
data_vencimento = data_inicio_emprestimo + relativedelta(years=2)
data_final_emprestimo = data_vencimento + periodo_pagamento

datas_parecelas: list[datetime] = []
while data_vencimento < data_final_emprestimo:
      datas_parecelas.append(data_vencimento)
      
      data_vencimento += relativedelta(months=1)
      
quantidade_parcelas = len(datas_parecelas)
valor_parcela = valor / quantidade_parcelas
      
for i, data in enumerate(datas_parecelas):
      print(f'NÚMERO DA PARECELA: {i+1}\n'
            f'DATA DE VENCIMENTO: {data.strftime('%d/%m/%Y')}\n'
            f'VALOR DA PARECELA: {valor_parcela:,.2f}\n')
