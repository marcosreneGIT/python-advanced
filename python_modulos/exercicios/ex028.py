# Exercício solucionado: calculando as datas e parcelas de um empréstimo

# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.

# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.

# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta


valor_emprestimo = 1_000_000
periodo_pagamento = relativedelta(years=5, months=6)

data_inicio_emprestimo = datetime(2020, 12, 20)
data_final_emprestimo = data_inicio_emprestimo + periodo_pagamento


diferenca_data = relativedelta(data_final_emprestimo, data_inicio_emprestimo)
quantidade_parcelas_emprestimo = diferenca_data.years * 12 + \
                                 diferenca_data.months

valor_parcela_emprestimo = valor_emprestimo / quantidade_parcelas_emprestimo

data_vencimento_parecela = data_inicio_emprestimo + relativedelta(months=1)

while data_vencimento_parecela <= data_final_emprestimo:
    print(f'DATA DE VENCIMENTO: {data_vencimento_parecela.strftime('%d/%m/%Y')}'
          f'\nVALOR DA PARCELA: R${valor_parcela_emprestimo:,.2f}\n')
    
    data_vencimento_parecela += relativedelta(months=1)    





