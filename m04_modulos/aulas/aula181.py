# secrets gera números aleatórios seguros

import secrets

import string as s
from secrets import SystemRandom as Sr

print(''.join(Sr().choices(s.ascii_letters + s.digits, k=8)))

# Funções:

random = secrets.SystemRandom()

# seed
# NÃO FAZ NADA
random.seed(10)

# random.randrange(início, fim, passo)
# Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 20, 2)

# random.randint(início, fim)
# Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)

# random.uniform(início, fim)
# Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)

# random.shuffle(SequenciaMutável)
# Embaralha a lista original
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
random.shuffle(nomes)

# random.sample(Iterável, k=N)
# Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=3)

# random.choices(Iterável, k=N)
# Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=3)

# random.choice(Iterável) 
# Escolhe um elemento do iterável
print(random.choice(nomes))
