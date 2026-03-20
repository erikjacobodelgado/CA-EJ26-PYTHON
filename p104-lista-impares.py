## p104-lista-impares.py
## Leer un entero n, despues imprimir los impares desde 1 hasta n

print("\033[H\033[J")
print('Leer un entero n, despues imprimir los impares desde 1 hasta n')

impares = []
entre3 = []
suma = 0
suma3 = 0

n = int(input('Introduzca la cantidad de numeros impares (n): '))

for i in range(1, n+1):
    if i % 2 != 0:
        impares.append(i)
        suma += i
        if i % 3 == 0:
            entre3.append(i)
            suma3 += i

print('\nGeneracion de lista')
print(f'Lista de los primeros {n} numeros impares: {impares}')

print('\nCalculos')
print(f'Suma de los numeros: {suma}')
print(f'Promedio de los numeros: {suma/len(impares)}')

print('\nDivisibles entre 3')
print(f'Numeros divisibles entre tres: {entre3}')
print(f'Suma de los numeros divisibles entre tres: {suma3}')

print('\nBusqueda')
bus = int(input('Introduzca elelemento a buscar: '))
if bus in impares:
    pos = impares.index(bus)
    print(f'El elemento {bus} esta en la posicion {pos+1} de la lista')
else:
    print('No existe el elemento en la lista')