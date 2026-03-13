## p090-eliminar-lista.py
## Eliminar elementos de una lista 

print("\033[H\033[J")
print('Eliminar elementos de una lista')

numeros = [10,20,30,40,50,60,70,10,20,99]

print(f'Inicial: {len(numeros)} - {numeros}')

print('\nElimina el 99')
numeros.remove(99)
print(f'Actual: {len(numeros)} - {numeros}')

print('\nElimina el 5to elemento')
numeros.pop(4)
print(f'Actual: {len(numeros)} - {numeros}')

print('\nEliminar el ultimo elemento')
numeros.pop()
print(f'Actual: {len(numeros)} - {numeros}')

print('\nEliminar todos los elementos')
numeros.clear()
print(f'Actual: {len(numeros)} - {numeros}')