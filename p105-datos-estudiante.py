## p105-datos-estudiante.py
## Ejemplifica las operaciones sobre un diccionario 

print("\033[H\033[J")
print('Gestión de estudiantes')

estudiante = {'nombre':'Juan', 'edad':45, 'email':'hola@gmail.com', 'carrera':'diseño'}

print(f'Diccionario: {estudiante} - {len(estudiante)}')

estudiante['calificacion'] = 9.5
estudiante['email'] = 'juan@gmail.com'

print(f'Diccionario: {estudiante} - {len(estudiante)}')
print('\nLlaves del diccionario')
for k in estudiante.keys(): print(k, end=' ')

print('\nValores del diccionario')
for v in estudiante.values(): print(v, end=' ')

print('\nLlaves y valores')
for k, v in estudiante.items(): print(f'{k:<12} - {v}')