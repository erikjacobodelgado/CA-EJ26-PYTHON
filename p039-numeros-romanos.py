## p039-numeros-romanos.py
## Escribe un programa que pida al usuario un número entero entre 1 y 10 y muestre su equivalente en números romanos. Si el número está fuera de este rango, debe mostrar un mensaje de error.

print("\033[H\033[J")

print('Dame un numero entero del 1 al 10 y te lo convierto a romano')

num = int(input())

if num == 1:
    print('I')
elif num == 2:
    print('II')
elif num == 3:
    print('III')
elif num == 4:
    print('IV')
elif num == 5:
    print('V')
elif num == 6:
    print('VI')
elif num == 7:
    print('VII')
elif num == 8:
    print('VIII')
elif num == 9:
    print('IX')
elif num == 10:
    print('X')
else:
    print('Error: Nuemero invalido')

print('\nProceso terminado')