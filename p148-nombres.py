## p148-nombres.py
## Funcion que toma dos listas y las procesa

from typing import List

print("\033[H\033[J")

def une(lista1:List[str],lista2:List[str])->List[str]:
    todo = lista1 + lista2
    inv = todo[::-1]
    res = []
    for nombre in inv:
        res.append(nombre.upper())
        res.sort()
    return res

nombres1 = ['Ana','Luis','Carlos','Martha','Sofia']
nombres2 = ['Jose','Juan']
nombres3 = une(nombres1,nombres2)

print(nombres1)
print(nombres2)
print(nombres3)