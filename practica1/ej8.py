# Ejercicio 8
horas_trabajadas = int(input('Horas trabajadas '))
salario_hora = float(input('Salario por hora '))
horas_extra = 0 # En realidad no se cuantas son
horas_extra_normales = 0
horas_extra_especiales = 0

if horas_trabajadas > 40:
    horas_extra = horas_trabajadas-40
    print('Usted trabajo',horas_extra,'horas extra')
    if horas_extra > 8:
        # Horas extras especiales
        horas_extra_especiales = horas_extra-8
        horas_extra_normales = 8
    else:
        # Horas extras normales
        horas_extra_normales = horas_extra
    
    # Decirle cuanto gano por horas extra
    pago_extra = horas_extra_normales*(2*salario_hora)+horas_extra_especiales*(3*salario_hora)
    print('Usted gano por horas extra ',pago_extra)
else:
    print('Usted no tiene horas extra')