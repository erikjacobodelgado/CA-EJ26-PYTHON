## p032-aceptar-estudiante.py
## Programa para administrar el sistema de ingreso de una universidad en base a dos condiciones

print("\033[H\033[J")

print('Programa para administrar el sistema de ingreso de alumnos de una universidad')

nom = input('Nombre: ')
edad = int(input('Edad: '))

if edad < 18:
    print(f'No aceptamos niños, {nom}')
else:
    print('Ingresa dos calificaciones separadas por enter:')
    cal1 = float(input())
    cal2 = float(input())
    if cal1 < 8 or cal2 < 8:
        print(f'No aceptamos tontos, {nom}')
    else:
        print(f'Fuiste aceptado {nom}')


print('Proceso finalizado')