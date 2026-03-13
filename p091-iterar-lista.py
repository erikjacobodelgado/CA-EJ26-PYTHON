## p091-iterar-lista.py
## Moverse entre los elemetnos de una lista

print("\033[H\033[J")
print('Moverse entre los elementos de una lista')

numeros = [10,20,30,40,50,60,70,10,20,99]

print('\nIteracion por elemento')
for n in numeros:
    print(n, end=' ')

print('\n\nIteracion por indice')
for i in range(len(numeros)):
    print(numeros[i], end=' ')

print('\n\nIterar por elemento y sumar 2')
for n in numeros:
    print(n+2, end=' ')

print('\n\nIterar por indice y sumar 10, se modifica')
print(f'Lista inicial: {numeros}')
for i in range(len(numeros)):
    numeros[i] = numeros[i] + 10
print(f'Lista final: {numeros}')