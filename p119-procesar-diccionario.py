## p119-procesar-diccionario.py
## Administracion de una nomina de trabajo mediante diccionarios

from optparse import Values


print("\033[H\033[J")

nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

nomina = dict(zip(nombres,sueldos))
print('Diccionario de nóomina:')
print(nomina)

print('\nIterando llaves (keys)')
for n in nomina.keys():
    print(n)

print('\nIterando valores (values)')
for s in nomina.values():
    print(s)

print('\nIterando llave y valor (accediendo por llave)')
for k in nomina.keys():
    print(k,nomina[k])

print('\nIterando llave y valor (items)')
for k,v in nomina.items():
    print(k,v)

print('\nCalculos')
suma = 0
for s in nomina:
    suma += nomina[s]
promedio = suma / len(nomina)
print(f'Suma total de los sueldos: {suma}')
print(f'Promedio de sueldos: {promedio:.2f}')