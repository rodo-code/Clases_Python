# Ejercicio 9
# 9.	Escriba un algoritmo para leer 3 números enteros distintos 
# entre si e imprimirlos en orden ascendente.

# ENTRADA
a = int(input('Ingrese numero 1: '))
b = int(input('Ingrese numero 2: '))
c = int(input('Ingrese numero 3: '))

# VALIDAR SI SON DIFERENTES
if a!=b and a!=c and b!=c:
    # Esta bien
    # Imprimir en orden ascendente
    if a < b and b < c:
        print(a,b,c)
    elif a < c and c < b:
        print(a,c,b)
    elif b < a and a < c:
        print(b,a,c)
    elif b < c and c < a:
        print(b,c,a)
    elif c < a and a < b:
        print(c,a,b)
    elif c < b and b < a:
        print(c,b,a)
else:
    print('Tus numeros deben ser diferentes')