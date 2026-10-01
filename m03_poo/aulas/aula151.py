# Enum -> Enumerações 

# Enumerações na programação, são usadas em ocasiões onde temos um determinado
# número de coisas para escolher.

# Enums têm membros e seus valores são constantes são constantes.
# Enuns em python:
    # - são um conjuto de nomes simbólicos (membros) ligados a valores únicos
    # - podem ser internados para retornar seus membros canônicos na ordem de 
    # definição

# enum.Enum é a superclasse para suas enumerações. Mas támbem pode ser usada 
# diretamente (mesmo assim, Enums não são classes normais em Pyhton)

# Você poderá usar seu Enum com type annotations, com isinstance e outras coisas
# relacionadas com tipo.

# Para obter os dados:
    # - membro = Classe(valor), Classe['chave']
    # - chave  = Classe.chave.name
    # - valor  = Classe.chave.value
    
