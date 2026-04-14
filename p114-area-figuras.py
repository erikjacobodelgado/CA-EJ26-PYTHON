## p114-area-figuras.py
## Calculadora geometrica dinamica en base a diccionario de diccionarios

import math

figuras = {
"Circulo": {"radio": 0, "formula": "math.pi * r ** 2"},
"Triangulo": {"base": 0, "altura": 0, "formula": "0.5 * b * a"},
"Rectangulo": {"largo": 0, "ancho": 0, "formula": "l * a"}
}

print("\033[H\033[J")
print('Área de figuras geométricas\n')

for k, v in figuras.items():
    print(f'{k:<10} - Fórmula: {v['formula']}')

while True:
    fig = input('Figura: ').title()
    if fig in figuras: break
    print('Error')

if fig == 'Circulo':
    r = float(input('Radio: '))
    area = eval(figuras[fig]['formula'].replace('f',str(r)))

elif fig=='Triangulo':
    b = int(input('Base : '))
    a = int(input('Altura : '))
    area = eval(figuras[fig]['formula'].replace('b', str(b)).replace('a',str(a)))

elif fig=='Rectangulo':
    l = int(input('Largo : '))
    a = int(input('Ancho : '))
    area = eval(figuras[fig]['formula'].replace('l', str(l)).replace('a',str(a)))

print('Area: ',area)