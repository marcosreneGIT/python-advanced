cpf_inicial_1 = '416.453.870-89'

cpf_str_1 = []
cpf_sep_1 = []

cpf_numeros_1 = 0


cpf_str_1.append(cpf_inicial_1[:11].split('.'))

cpf_numeros_1 = ''.join(cpf_str_1[0])

for i in range(0, 9):
    cpf_sep_1.append(cpf_numeros_1[i])


numero_mult_1 = 10
soma_cpf_1 = 0

for i in range(0, 9):

    cpf_int_1 = int(cpf_sep_1[i])

    soma_cpf_1 += cpf_int_1 * numero_mult_1
    numero_mult_1 -= 1


primeiro_digito = (soma_cpf_1 * 10) % 11

primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

# --------------------------------------------------------------------

cpf_inicial_2 = '416.453.870-89'

cpf_sep_2 = []

cpf_inicial_2 = cpf_inicial_2[:13].replace('.', '', 2)
cpf_inicial_2 = cpf_inicial_2.replace('-', '')

for i in range(0, 10):
    cpf_sep_2.append(cpf_inicial_2[i])

numero_mult_2 = 11
soma_cpf_2 = 0

for i in range(0, 10):

    cpf_int_2 = int(cpf_sep_2[i])

    soma_cpf_2 += cpf_int_2 * numero_mult_2
    numero_mult_2 -= 1


segundo_digito = (soma_cpf_2 * 10) % 11

segundo_digito = segundo_digito if segundo_digito <= 9 else 0

# -------------------------------------------------------------------

validacao_cpf = str(primeiro_digito) + str(segundo_digito)

if validacao_cpf == cpf_inicial_1[-2:]:
    print('cpf validado.')

else: 
    print('cpf não validado.')