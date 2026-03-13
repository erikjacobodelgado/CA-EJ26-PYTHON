## p087-acceder-lista.py
## Acceder a los elementos de una lista 

print("\033[H\033[J")
print('Acceder a los elementos de una lista')

numeros = [10,20,30,40,50,60,70,10,20,99]

print('\nLongitud y contedio de la lista')
print(f'Cantidad de números: {len(numeros)}')
print(f'Números: {numeros}')

print('\nAcceder por indice positivo')
print(f'Primer y ultimo numero: {numeros[0]} - {numeros[9]}')

print('\nAcceder por indice negativo')
print(f'Primer y ultimo numero: {numeros[-9]} - {numeros[0]}')

print('\nAcceder a un rango de valores en la lista')
print(f'Del segundo al sexto: {numeros[1:6]}') ## Menos uno porque cuenta la posicicon 0

print('\nPor saltos')
print(f'Los primeros tres desde el inicio: {numeros[:3]}') ## :n Desde el inicio 
print(f'Los ultimos tres desde el final: {numeros[7:]}') ## n: Hasta el final