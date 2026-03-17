## p096-registro-estudiantes.py
## Registro de estudiante para evento 

print("\033[H\033[J")
print('Registro de estudiante para evento \n')

nombres = []
edades = []

while True:
    nombre = input('Nombre: ')
    if nombre == '*': break
    try:
        edad = int(input('Edad: '))
        nombres.append(nombre)
        edades.append(edad)
    except ValueError:
        print('X')

print(f'Nombres: {nombres}')
print(f'Edades: {edades}')

print('Mayores de edad: ')
for i in range(len(nombres)):
    if edades[i] >= 18:
        print(f'{nombres[i]} - {edades[i]}')

edadmax = max(edades)
posmax = edades.index(edadmax)

print(f'El reconociemiento es para: {nombres[posmax]} - {edadmax}')