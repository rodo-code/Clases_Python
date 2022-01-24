# 31.	Simular el lanzamiento de un dado múltiples veces y determinar 
# la cantidad de caras pares e impares que se han producido.
import random

lanzamientos = int(input('¿Cuantas veces quiere lanzar el dado? '))

cont_pares = 0 # Contador de pares
cont_impares = 0 # Contador de impares

for i in range(lanzamientos): # Dar la cantidad de lanzamientos necesarios
    cara = random.randint(1,6) # Lanzar dado
    if cara==2 or cara==4 or cara==6:
        # es par
        cont_pares += 1 # Contando los pares
    else:
        # es impar
        cont_impares += 1 # Contando los impares

print('Hay',cont_pares,'caras pares')
print('Hay',cont_impares,'caras impares')   
