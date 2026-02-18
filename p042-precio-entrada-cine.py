## p042-precio-entrada-cine.py
## Programa para calcular el precio de los boletos de un cine en base a la edad del usuario 

print("\033[H\033[J")

print('Dame tu edad: ')
edad = int(input())

if edad < 5:
    print('Tu entrada es gratis')
elif edad >= 5 and edad <= 12:
    print('El costo de tu entrada es de $5')
elif edad >= 13 and edad <= 64:
    print('El costo de tu entrada es de $10')
else:
    print('El costo de tu entrada es de 7')

print('\nProceso finalizado')