## p142-suma-lista.py
## Funcion que recibe una lista de numeros y regresa la suma 

print("\033[H\033[J")

from typing import List

def suma_lista(lista : List[float]) -> float:
    suma = 0
    for numero in lista:
        suma += numero
    return suma

## Lista 1
lista = [1.5, 2.3, 3.7, 4.0]
resultado = suma_lista(lista)
print('Suma ', resultado)

## Lista 2
print('Suma 2 ', suma_lista([1,5,6.5,7,8]))