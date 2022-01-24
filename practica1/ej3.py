# Ejercicio 3
# 3.	Leer tres números enteros y determinar si forman un triángulo isósceles, 
# equilátero o escaleno. Un triángulo equilátero es aquel que tiene   los 3 lados 
# iguales, el triángulo escaleno tiene los 3 lados diferentes, y un triángulo isósceles 
# (dos lados iguales y uno desigual analice en este tipo los 3 casos posibles).

# ENTRADA
a = float(input('Ingrese lado 1: '))
b = float(input('Ingrese lado 2: '))
c = float(input('Ingrese lado 3: '))

# PROCESO
# If anidado
if a==b and b==c:
    print('Triangulo Equilatero')
elif a!=b and a!=c and b!=c:
    print('Triangulo Escaleno')
elif (a==b and a!=c and b!=c) or (a==c and a!=b and c!=b) or (b==c and b!=a and c!=a):
    print('Triangulo Isosceles')


