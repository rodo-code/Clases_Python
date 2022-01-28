# Ejercicio 48

n = int(input('Ingrese un numero '))

# range(inicio,<final,paso)
for fila in range(0,n,1): # 6 vueltas
    for col in range(0,n,1): # 6 vueltas
        if (fila+col)%2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()