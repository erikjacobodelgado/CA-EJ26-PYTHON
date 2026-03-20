## p102-listas-aleatorios-suma.py
## Dos listas de numeros aleatorios suman sus elementos solaente si estos son impares

import random 

print("\033[H\033[J")
print('Dos listas de numeros aleatorios suman sus elementos solaente si estos son impares')

uno = []
dos = []
tres = []
MAX = 10

for i in range(MAX):
    uno.append(random.randint(1,10))
    dos.append(random.randint(1,10))
    if uno[i] % 2 != 0 and dos[i] % 2 != 0:
        suma = uno[i] + dos[i]
        tres.append(suma)

print('\nListas generadas')
print(uno)
print(dos)
print('\nResultados de sumas de los impares')
print(tres)