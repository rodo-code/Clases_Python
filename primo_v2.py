# Saber si es un numero es primo
import math
num = int(input('Ingrese un numero '))
cont_divisores = 0
limite = math.floor(math.sqrt(num))+1
print('Voy a buscar hasta',limite)
for i in range(1,limite):
    if num % i == 0: #Si i divide a num
        cont_divisores += 1
        pareja = num // i
        if pareja != i:
            cont_divisores += 1

print('Hay',cont_divisores,'divisores')
if cont_divisores == 2: # Si hay 2 divisores
    print('ES PRIMO')
else:
    print('NO ES PRIMO')