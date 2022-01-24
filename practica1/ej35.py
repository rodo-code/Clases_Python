# 35 Leer un número entero y contar cuantos dígitos pares e impares tiene

num = int(input('Ingrese un numero '))
cont_pares = 0
cont_impares = 0

while num>0:
    dig = num % 10
    num = num // 10
    if dig%2 == 0: # Si el digito es par
        cont_pares += 1
    else: # Si el digito es impar
        cont_impares += 1

print('Hay',cont_pares,'digitos pares')
print('Hay',cont_impares,'digitos impares')
