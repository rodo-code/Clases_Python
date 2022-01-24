# 36 Leer un número entero y mostrar sus divisores
import math
num = int(input('Ingrese un numero '))

limite = math.floor(math.sqrt(num))+1
print('Voy a buscar hasta',limite)
for i in range(1,limite):
    if num % i == 0: #Si i divide a num
        print(i,end=' ')
        pareja = num // i
        if pareja != i:
            print(pareja)