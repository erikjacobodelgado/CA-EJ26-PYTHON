## p147-aleatorios.py
## Genera dos listas con numeros aleatorios y las suma en una tercera

import random
from typing import List

print("\033[H\033[J")

def aleatorios()->List[int]:
    lista = []
    for _ in range (10):
        lista.append(random.randint(1,100))
    return lista

def suma_listas(lista1:List[int],lista2:List[int])->List[int]:
    suma = []
    for i in range(10):
        s = lista1[i] + lista2[i]
        suma.append(s)
    return suma

lista1 = aleatorios()
lista2 = aleatorios()
suma = suma_listas(lista1,lista2)

print(lista1)
print(lista2)
print(suma)