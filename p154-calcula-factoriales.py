## p154-calcula-factoriales.py
## Calcula el facotorial de cada numero de una lista 

from ast import Tuple
from typing import List

print("\033[H\033[J")

def factorial(n: int) -> int:
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac


def factorial_lista(numeros: List[int]) -> List[int]:
    resultados = []
    for num in numeros:
        resultados.append(factorial(num))
    return resultados

entrada = input('Dame los numeros separados por un espacio: ')
numeros = list(map(int, entrada.split()))
factores = factorial_lista(numeros)
print(f'Lista de numeros originales: {entrada}')
print(f'Lista de facotriales: {factores}')