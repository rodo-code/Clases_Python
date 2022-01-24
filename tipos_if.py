# Clase 1

# libreria.- Es un conjunto de funciones y objetos
import math

# Operaciones
print(5.2 + 5.7) # Suma
print(4.5 - 7.8) # Resta
print(7.41 * 4.1) # Multiplicacion
print(18 / 5) # Division Exacta ( / )
print(18 // 5) # Division Entera ( // )
print(16 % 5) # Residuo o Resto ( % )
print(6 ** 3) # Exponenciacion 6 elevado a 3

# Funciones Built-in
maximo = max(8,78)
minimo = min(4,6)

print(maximo,minimo)

# Raiz Cuadrada
print(math.sqrt(4))
# Constante e
print(math.e)

# ----------------------------
a = 3
print(a,type(a)) # 3 <class 'int'> int = Entero = {...,-4, -3, -2, -1, 0, 1, 2, 3, 4,...}
a = 'Rodolfo'
print(a,type(a)) # Rodolfo <class 'str'> str = String/Cadena de caracteres
a = 3.1416
print(a,type(a)) # 3.1416 <class 'float'> float = Numero de Punto Flotante / Números Reales/Con Decimales
a = True
print(a,type(a)) # True <class 'bool'> bool = Booleanos True/False

# CONDICIONALES
# if ¿Pregunta/Booleano?:
#   ... Lo que va a pasar si la pregunta es TRUE
# else:
#   ... Lo que va a pasar si la pregunta es FALSE

a = int( input('Ingrese un numero ') )
if a > 5:
    print(a,"es mayor a 5")
else:
    print(a,"es menor a 5")

# Posibles Preguntas
# > Mayor que
# < Menor que
# >= Mayor o igual
# <= Menor o igual
# == Igualdad
# != Diferencia

