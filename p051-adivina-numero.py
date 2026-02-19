## p051-adivina-numero.py
## Permite al usuario adivinar un numero generado al azar

import random  ## Genera numeros random

print("\033[H\033[J")

print('Permite al usuario adivinar un numero generado al azar entre 1 y 50')

n = random.randint(1,50)

ci = 0

while True:
    i = int(input('Numero: '))
    ci += 1
    if i < n:
        print('Estas abajo')
    elif i > n:
        print('Estas arriba')
    else:
        print(f'Adivinaste que era {n}')
        print(f'Usaste {ci} intentos')
        break 

print('\nFin del juego')
