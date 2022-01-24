# Serie Rara
# 28.-  Mediante un programa genere la serie:
	
#	4 , 6 , 9 , 13 , 19 , 28 , ……. Para n términos

# Entrada
n = int(input('Ingrese el numero de terminos '))
a = 1
b = 2
s = a + b -1
term = 4
for i in range(n): #Solo va a ser para controlar la cantidad de terminos impresos
    print(term)
    term = term + s
    a = b
    b = s
    s = a + b - 1

