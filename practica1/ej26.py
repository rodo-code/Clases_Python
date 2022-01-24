# Ejercicio 26
# 26.	Leer n números diferentes entre sí e imprima el número mayor.
n = int(input('¿Cuantos numeros va a ingresar? '))
mayor = 0
for i in range(n):
    x = int(input('Ingrese el numero '+str(i+1)+' '))
    if x > mayor:
        mayor = x
print('El mayor es',mayor)

import math
if 1000000000000 < math.inf: # Infinito
    print(':)')