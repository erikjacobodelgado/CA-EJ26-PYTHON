## p015-hipotenusa-triangulo.py
## Programa para calcular la hipotenusa de un triangulo en base a los catetos dados por el usuario 

import math as mt
print("\033[H\033[J")

print('Dame el cateto opuesto: ')
cop = float(input())
print('Dame el cateto adyacente: ')
cad = float(input())

hipo = mt.sqrt((cop**2)+(cad**2))
print(f'El valor de la hipotenusa del triangulo es: {hipo:.2f}')
