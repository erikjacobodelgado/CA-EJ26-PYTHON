## p018-area-volumen-cilindro.py
## Programa para calcular el area y el volumen de un cilindro 

import math as mt
print("\033[H\033[J")

print('Ingresa el radio y la altura del cilindro separados por enter: ')
rad, alt = float(input()), float(input())

area = mt.pi * rad * (rad + alt)
vol = mt.pi * (rad**2) * alt

print(f'El area del cilindro es {area:.2f} y el volumen es {vol:.2f}')
