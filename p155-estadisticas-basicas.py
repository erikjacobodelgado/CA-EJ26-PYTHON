## p155-estadisticas-basicas.py
## Calculo de estadisticas basicas poblaciones 

from ast import Tuple
from typing import List
import math

print("\033[H\033[J")

def mayor (lista:List[float])->float:
    m = lista[0]
    for n in lista:
        if n > m: 
            m = n
    return m

def menor (lista:List[float])->float:
    m = lista[0]
    for n in lista:
        if n < m: 
            m = n
    return m

def media(lista: List[float])->float:
    return sum(lista)/len(lista)

def varianza(lista: List[float]) -> float:
    m = media(lista)
    suma = 0
    for x in lista:
        suma += (x - m) ** 2
    return suma / len(lista)

def desviacion_estandar(lista: List[float]) -> float:
    return math.sqrt(varianza(lista))

def main()->None:
    entrada = input('Dame los numeros separados por espacio: ')
    lista = list(map(float,entrada.split()))
    print('Estadisticas')
    print(f'Lista de numeros: {lista}')
    print(f'Mayor: {mayor(lista)}')
    print(f'Menor: {menor(lista)}')
    print(f'Media: {media(lista):.3f}')
    print(f'Varianza: {varianza(lista):.3f}')
    print(f'Desviacion estandar: {desviacion_estandar(lista):.3f}')

if __name__ == "__main__":
    main()