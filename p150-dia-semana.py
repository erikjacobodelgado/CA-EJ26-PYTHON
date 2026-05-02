## p150-dia-semana.py
## p150-dia-semana.py

print("\033[H\033[J")

from typing import List

def dia_semana(n:int)->str:
    if n == 1:
        n = 'El dia de la semana es: Lunes'
    elif n == 2:
        n = 'El dia de la semana es: Martes'
    elif n == 3:
        n = 'El dia de la semana es: Miercoles'
    elif n == 4:
        n = 'El dia de la semana es: Jueves'
    elif n == 5:
        n = 'El dia de la semana es: Viernes'
    elif n == 6:
        n = 'El dia de la semana es: Sabado'
    elif n == 7:
        n = 'El dia de la semana es: Domingo'
    else:
        n = 'Error: El numero debe estar entre 1 y 7'
    return n 

a = int(input('Introduce un numero del 1 al 7: '))
print(dia_semana(a))