# 1.	El promedio de prácticas de un curso se calcula en base a cuatro prácticas 
# calificadas de las cuales se elimina la nota menor y se promedian las tres notas 
# más altas. Diseñe un algoritmo que determine la nota eliminada y el promedio de 
# prácticas de un estudiante.

# ENTRADA
nota1 = float(input('Ingrese nota 1: '))
nota2 = float(input('Ingrese nota 2: '))
nota3 = float(input('Ingrese nota 3: '))
nota4 = float(input('Ingrese nota 4: '))

# PROCESO

# Si solo quisieramos saber quien es el menor
"""
notamenor = min(nota1,nota2)
notamenor = min(notamenor,nota3)
notamenor = min(notamenor,nota4)
print('La nota eliminada es',notamenor)
"""
# PASO 1: SACAR LA NOTA MENOR
# Entre nota1 y nota2
if nota1 < nota2:
    notamenor = nota1
else:
    notamenor = nota2
# Entre nota1, nota2 y nota3
if nota3 < notamenor:
    notamenor = nota3
# Entre nota1, nota2, nota3 y nota4
if nota4 < notamenor:
    notamenor = nota4

# PASO 2: SACAR EL PROMEDIO SIN LA NOTA MENOR
promedio = (nota1+nota2+nota3+nota4-notamenor)/3

# SALIDA
print('La nota eliminada es',notamenor)
print('La nota promedio es',promedio)