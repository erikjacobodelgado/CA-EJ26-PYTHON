## p043-calculadora-anio-bisiesto.py
## Programa para determinar si un año es bisiesto o no

print("\033[H\033[J")

print('Ingresa un año: ')
a = int(input())

if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print('Es año bisisesto')
else:
    print('No es año bisisesto')

print('\nProceso finalizado')