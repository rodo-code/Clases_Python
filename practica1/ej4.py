# Ejercicio 4
# 4.	Escribir un algoritmo para leer un número y determinar si el mismo 
# es un entero positivo par, positivo impar, negativo par o negativo impar o es cero.

# ENTRADA
num = int(input('Ingrese numero: '))

# PROCESO
if num>0:
    # Positivo
    if num%2==0:
        # Par
        print('Es un entero positivo par')
    else:
        # Impar
        print('Es un entero positivo impar')
elif num == 0:
    # Cero
    print('Es cero')
else:
    # Negativo
    num = num*(-1) # Para asegurarnos de que el modulo trabaje bien
    if num%2==0:
        # Par
        print('Es un entero negativo par')
    else:
        # Impar
        print('Es un entero negativo impar')