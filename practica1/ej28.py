# 28.	Realice un programa que imprima la secuencia como en el siguiente ejemplo.

# n,n-1,n-1,n-2,n-3,……1

# ENTRADA
n = int(input('Ingrese un numero '))
for i in range(n,0,-1): # For hacia atras
    print(i,end=" ")