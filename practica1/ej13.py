# Ejercicio 13
# 13.	Indicar si un año es bisiesto. 
# Un año es bisiesto si es divisible por cuatro, 
# excepto cuando es divisible por 100, a no ser que sea divisible por 400. 
# Así, 1900 no fue bisiesto, pero 2000 sí lo fue. 

año = int(input('Ingrese el año ')) 

# Primera forma
if año%4==0: # Si el año es divisible por 4
    if año%100==0:
        if año%400==0:
            print(año,'es un año bisiesto')
        else:
            print(año,'no es un año bisiesto')
    else:
        print(año,'es un año bisiesto')
else:
    print(año,'no es un año bisiesto')

# Segunda forma
if año%4==0 and (año%100!=0 or año%400==0):
    print(año,'es un año bisiesto')
else:
    print(año,'no es un año bisiesto')