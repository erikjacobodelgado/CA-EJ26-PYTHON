## p106-calificaciones-estudiante.py
## Gestion de calificaciones en dos listas y un diccionario

print("\033[H\033[J")
materias = ['fisica','quimica','matematicas','geografia','fisica']
califs = [10,9,8,7.5,6]

print(f'Materias: {materias} - {len(materias)}')
print(f'Calificaciones: {califs} - {len(califs)}')

notas = dict(zip(materias,califs))

print(f'\nNotas: {notas} - {len(notas)}')

notas.update({'Ingles':10})
notas.update({'Programacion':7})
print(f'\nNotas: {notas}- {len(notas)}')

notas.pop('fisica')
notas.popitem()
print(f'\nNotas: {notas} - {len(notas)}')

notas.update({'quimica':10, 'matematicas':10})
print(f'\nNotas: {notas} - {len(notas)}')

suma = 0
print('\nResumen')
for m, c in notas.items():
    print(f'{m:<12} - {c:5}')
    suma += c
print(f'\nSuma: {suma}, Promedio: {suma/len(notas)}')

notas.clear()
print(f'\nNotas: {notas} - {len(notas)}')