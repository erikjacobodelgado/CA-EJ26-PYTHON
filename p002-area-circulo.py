# p002-area-circulo.py
# Calcular el area de un circulo 

import math

print('Calculando el area de u circulo:\n')

print('Dame el radio: ')

radio = float(input())
area = math.pi * math.pow(radio,2)

print(f'El circulo de raio {radio:.2f} tiene un area de {area:.2f}')
