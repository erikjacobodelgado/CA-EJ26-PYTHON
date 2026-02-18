## p041-aceptar-estudiante.py
## Programa para administrar el ingreso de nuevos estudiantes a una universidad en base a su sexo, edad y promedio

print("\033[H\033[J")

print('UNIVERSIDAD KITTY KAT SA\n')
print('Ingresa tus datos')
nombre = input('Nombre: ')
sexo = input('Sexo (H/M): ').upper()
edad= int(input('Edad: '))
cal1, cal2, cal3 = input('Ingresa tus calificaciones separadas por espacio:  ').split()
cal1, cal2, cal3 = int(cal1), int(cal2), int(cal3)
prom = (cal1 + cal2 + cal3)/3

if sexo == 'M':
    if edad >= 21:
        if prom >= 8 and prom <= 9.5:
            print(f'Felicidades {nombre}, has sido acepada. Cumples con la edad y tu promedio de {prom:.2f} esta dentro del rngo permitido')
        else:
            print(f'Lo sentimos {nombre}, tu promedio {prom:.2f} no entra dentro del rango permitido (8 - 9.5)')
    else:
        print(f'Lo sentimos {nombre}, no cumples con la edad requerida (mayores de 21)')
else:
    print(f'Lo sentimos {nombre}, la universidad es solo para mujeres') 

print('\nProceso finalizado')       