# 36 Leer un número entero y mostrar sus divisores
num = int(input('Ingrese un numero '))

for i in range(1,num+1):
    if num % i == 0: #Si i divide a num
        print(i,end=' ')
