## p021-distancia-entre-puntos.py
## Programa para meidr la distancia entre dos puntos en un plano cartesiano mediante la siguiente formula d = √((ax-bx)²+(ay-by)²)

print("\033[H\033[J")
import math as mt
print("\033[H\033[J")

print('Dame las coordenadas del punto X separados por una coma: ')
xa, ya = input().split(',')
xa, ya = int(xa), int(ya)
print('Dame las coordenadas del punto Y separados por una coma: ')
xb, yb = input().split(',')
xb, yb = int(xb), int(yb)

dis = float(mt.sqrt(((xa-xb)**2) + ((ya-yb)**2)))

print(f'La distancia entre los puntos es: {dis:.2f}')
