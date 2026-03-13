## p088-modificar-lista.py
## Modificar elementos de una lista

print("\033[H\033[J")
print('Modificar elementos de una lista')

numeros = [10,20,30,40,50,60,70,10,20,99]

print(f'Elementos de la lista: {len(numeros)} - {numeros}')
print('\nModificiar 1er y 7mo elemento por 7 y 7')
numeros [0] = 7
numeros [6] = 7 ## Se comienza a contar desde 0
print(f'Elementos de la lista: {len(numeros)} - {numeros}')

print('\nModificar del 2do al 5to elemetno')
numeros [2:5] = [0,0,0,0]
print(f'Elementos de la lista: {len(numeros)} - {numeros}')
