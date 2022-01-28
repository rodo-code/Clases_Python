n = int(input('Ingrese un numero '))

for lim in range(n,0,-1):
    for i in range(1,lim+1,1):
        print(i,end=" ")
    print()
