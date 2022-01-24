# 33.	Obtener la suma de la serie de Fibonacci para n términos:

# 1 + 1 + 2 + 3 + 5 + 8 + ………. para n términos

n = int(input('Cuantos terminos de Fibonacci quiere '))
suma_fibo = 0 # Acumulador empiezan en 0
a = 1
b = 0
for i in range(n):
    fibo = a+b
    suma_fibo += fibo # Aumentando el acumulador
    # print(fibo,end=' ')
    a = b
    b = fibo

print('La suma de los terminos es',suma_fibo)