## p033-aceptar-estudiante-v2.py
## Programa para administrar el sistema de ingreso de una universidad en base a dos condiciones version 2

print("\033[H\033[J")

print('Programa para administrar el sistema de ingreso de alumnos de una universidad')

nom = input('Nombre: ')
edad = int(input('Edad: '))

if edad >= 18:
    print('Ingresa dos calificaciones separadas por enter:')
    cal1 = float(input())
    cal2 = float(input())
    if cal1 >= 8 and cal2 >= 8:
        print(f'Fuiste aceptado {nom}')
    else:
        print(f'No aceptamos tontos, {nom}')
else:
    print(f'No aceptamos niños, {nom}')


print('\nProceso finalizado')