# 29.	Escriba un programa que lea una contraseña hasta que esta sea válida. 
# Por cada intento de contraseña incorrecta leída, escriba el mensaje "Invalido". 
# Cuando la contraseña se escriba correctamente, imprima el mensaje "Acesso Permitido" 
# y finalice el programa. La contraseña correcta es el número 2020.

# Cuando no sepamoas cuantas veces hay que repetir es una señal para
# usar un WHILE
contrasena = input('Ingrese Contraseña ')
while contrasena!='2020':
    print('Invalido')
    contrasena = input('Ingrese de nuevo su contraseña ')

# Fuera del ciclo
print('Acceso Permitido')