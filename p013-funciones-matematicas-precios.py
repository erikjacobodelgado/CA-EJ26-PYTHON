## p013-funciones-matematicas-precios.py
## Demostrar el uso de funciones matematicas para redondeo 

import math as mt

print("\033[H\033[J")
print('Demostrando el uso de funciones de redondeo ')

precio = 15.656
print(f'Precio: {precio}')
print(f'Arriba: {mt.ceil(precio)}')
print(f'Abajo: {mt.floor(precio)}')
print(f'Truncar: {mt.trunc(precio)}')
print(f'Normal: {round(precio)}')
print(f'2 decimales: {round(precio,2)}')  ## cantidad de decimales a conservar

## .5 redondea hacia abajo, .6 redondea hacia arriba 
