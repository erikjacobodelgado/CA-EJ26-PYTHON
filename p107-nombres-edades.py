## p107-nombres-edades.py
## Gestionar nombres y edades usando un diccionario 

print("\033[H\033[J")
print('Gestionar nombres y edades usando un diccionario')

datos = {}
while True:
    nombre = input('Nombre: ')
    if nombre == '' : break
    datos[nombre] = int(input('Edad: '))

print(f'Nombres y edades: {datos} - {len(datos)}')

suma = 0
for n, e in datos.items():
    print(f'{n:<20} - {e:3}')
    suma += e

print(f'Suma edades: {suma}, Promedio edades: {suma/len(datos)}')