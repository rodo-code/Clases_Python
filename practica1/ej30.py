# 30.	Leer las temperaturas de varias regiones del país y determine el porcentaje 
# temperaturas por debajo de cero grados y cual la temperatura más alta. 
# Emplear un valor centinela para detener la entrada de datos.

# Valor Centinela de los datos: -100
centinela = -100
temperatura = float(input('Ingrese Temperatura '))
cant_datos = 0 # Contador
cant_menor_cero = 0 # Contador
mas_alto = temperatura # En mas_alto voy a guardar la temperatura mas alta
while temperatura != centinela:
    # PROCESO
    cant_datos += 1 # Contando la cantidad de datos
    if temperatura < 0: # Vemos si la temperatura esta por debajo de cero grados
        cant_menor_cero += 1 # Contando la cantidad de temperaturas menores a cero
    if temperatura > mas_alto: # Obteniendo la temperatura mas alta
        mas_alto = temperatura
    # RE-PETICION    
    temperatura = float(input('Ingrese Temperatura '))

# RESULTADOS
print('La cantidad de temperaturas menores a 0 es: ',cant_menor_cero)
print('La cantidad de datos ingresados es:',cant_datos)

porcentaje = (cant_menor_cero/cant_datos)*100
print('El porcentaje de temperaturas por debajo de cero grados es: ',porcentaje)
print('La temperatura mas alta es:',mas_alto)