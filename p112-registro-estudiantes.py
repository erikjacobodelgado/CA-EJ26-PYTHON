## p112-registro-estudiantes.py
## Lista de diciconarios para representar estudiantes 

print("\033[H\033[J")

grupo = [
{'nombre':'Carlos','edad':45,'carrera':'sistemas','promedio':9} ,
{'nombre':'Rocio','edad':35,'carrera':'sistemas','promedio':10}
]

print('\nRegistro de estudiantes')

print(f'\nGrupo: {grupo} - {len(grupo)}')

print('\nCAPTURA DE ESTUDIANTES')
print('-'*50)
while True:
    datos = {}
    print('Datos del estudiante: ')
    nombre = input('Nombre: ')
    if nombre == '':break
    datos ['nombre'] = nombre
    datos ['edad'] = int(input('Edad: '))
    datos ['carrera'] = input('Carrera: ')
    datos ['promedio'] = float(input('Promedio: '))
    grupo.append(datos)

print(f'\nGrupo: {grupo} - {len(grupo)}')

print('\nFORMA DE TABLA')
for k in grupo[0].keys():
    print(f'{k:<13}', end='')
print()
for alumno in grupo:
    for v in alumno.values():
        print(f'{v:<13}',end='')
    print()

print('\nFORMA DE REGISTRO')
s = 0
for estudiante in grupo:
    s = s + estudiante['promedio']
    for k, v in estudiante.items():
        print(f'{k:13} : {v}')
    print()

print('\nCALCULO DE PROMEDIO')
p = s / len(grupo)
print(f'La suma es: {s}, y el promedio es: {p}')