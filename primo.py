# Programa para saber si un numero es primo
num = int(input('Ingrese un numero '))
cont_divisores = 0
for i in range(1,num+1):
    if num % i == 0: #Si i divide a num
        cont_divisores += 1

print('Hay',cont_divisores,'divisores')
if cont_divisores == 2: # Si hay 2 divisores
    print('ES PRIMO')
else:
    print('NO ES PRIMO')