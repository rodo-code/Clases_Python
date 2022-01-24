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
    menor = min(a,min(b,c))
    mayor = max(a,max(b,c))
    medio = a+b+c-menor-mayor
    print(menor,medio,mayor)
else:
    print('Tus numeros deben ser diferentes')