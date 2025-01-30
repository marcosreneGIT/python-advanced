def par_impar(n):
    resultado = n % 2 == 0

    if resultado is True:
        return 'Par'
    else: 
        return 'Impar'
    
numero = par_impar(2)

print(numero)