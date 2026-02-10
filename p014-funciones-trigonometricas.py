## p014-funciones-trigonometricas.py
## Demostrar el uso de las funciones trigonometricas 

import math as mt
print("\033[H\033[J")

print('Demostrando el uso de funciones trigonometricas\n')

angulo = 90 ## en grados
radianes = mt.radians(angulo)

seno = mt.sin(radianes)
coseno = mt.cos(radianes)
tangente = mt.tan(radianes)

grados = mt.degrees(radianes) ## regresa a grados 

salida = ('Resumen de funciones \n'
f'Seno: {seno:.4f} \n'
f'Coseno: {coseno:.4f} \n'
f'Tangente: {tangente:.4f} \n'
f'El angulo {angulo:.4f} grados, en radianes equivale a {radianes:.4f}\n'
f'El angulo {radianes:.4f} radianes, en grados equivale a {angulo:.4f}\n'
)
## salida almacena todo el texto 

print(salida)
## imprimimos salida 