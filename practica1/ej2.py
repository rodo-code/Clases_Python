# Ejercicio 2
import math

# ENTRADA
a = float(input('Ingrese lado 1: '))
b = float(input('Ingrese lado 2: '))
c = float(input('Ingrese lado 3: '))

# PROCESO
if a > 0 and b > 0 and c > 0: # PASO 1: Verificar que los lados sean positivos
    if a+b>c and a+c>b and b+c>a: # PASO 2: Verificar que la suma de dos lados cualquiera sea mayor que el otro lado
        # Se a cumplido el paso 1 y el paso 2
        print('El triangulo existe')
        # PASO 3: Como ya sabemos que el triangulo existe, calculamos el area con la formula
        p = (a + b + c) / 2
        area = math.sqrt(p*(p-a)*(p-b)*(p-c))
        print('El area es',area)
    else:
        # Se a cumplido el paso 1 pero NO el paso 2
        print('El triangulo no existe')
else:
    # Si no ha cumplido el paso 1
    print('El triangulo no existe')

# OTRA FORMA CON FLAGS
"""
if a > 0 and b > 0 and c > 0: # PASO 1: Verificar que los lados sean positivos
    paso1 = True
else:
    paso1 = False

if paso1 and (a+b>c and a+c>b and b+c>a):
    print('El triangulo es valido')
else:
    print('El triangulo no es valido')
"""
