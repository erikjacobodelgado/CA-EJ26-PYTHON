## p012-funcion-matematica-ecuacion.py
## Evaluar la funcion
## Usando operadores de exponenciacion y la funcion pow

print("\033[H\033[J")

import math as mt 
## cambiamos de nombre a math por mt 

print('Evaluar la expresion: f(x,y) = 3x2 + √(x2 + y2) + e^(ln(x))')
x = float(input('Dame x: '))
y = float(input('Dame y: '))

fxy = 3 * mt.pow(x,2) + mt.sqrt( mt.pow(x,2) + mt.pow(y,2) ) + mt.exp( mt.log(x) )
## mt.pow para sustituir el ** de esponenciacion 

print(f'El resultado es de f({x}, {y}) = {fxy}')
