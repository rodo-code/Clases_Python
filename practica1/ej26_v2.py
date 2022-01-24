# Ejercicio 26
# 26.	Leer n números diferentes entre sí e imprima el número menor.
n = int(input('¿Cuantos numeros va a ingresar? '))
menor = 1e9 # 10 elevado a 9
for i in range(n): # Ciclo que va a hacer n vueltas
    x = int(input('Ingrese el numero '+str(i+1)+' '))
    # El proceso
    if x < menor:
        menor = x
print('El menor es',menor)

