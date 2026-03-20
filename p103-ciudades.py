## p103-ciudades.py
## Lista de ciudades 

print("\033[H\033[J")
print('Lista de ciudades\n')

ciudades = []
consonantes = []
i = 0
vocales = 'aeiou'

while True:
    ciudad = input('Ingresa una ciudad ($ para terminar de ingresar): ')
    if ciudad == "$": break
    ciudades.append(ciudad) 

print('\nResultados')
print(f'Total de ciudades introducidas: {len(ciudades)}')
print(f'Lista original: {ciudades}')

ciudades.sort(reverse=True) ## Ordenar alfabeticamente de Z a A
print(f'\nLista ordenada descendente: {ciudades}')

for ciudad in ciudades:
    if ciudad[0].lower() not in vocales:
        consonantes.append(ciudad)
print(f'\nCiuades que inician con consonante: {len(consonantes)}')
print(f'Lista d ciudades que inician con consonante: {consonantes}')
