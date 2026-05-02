## p153-suma-digitos.py
## Funcion que suma los digitos de un entero, ejemplo 1971 = 1+9+7+1

from ast import Tuple
from typing import List

print("\033[H\033[J")

def suma(n:int) -> int:
    s = 0
    while n != 0:
        d = n % 10
        s = s + d
        n = n // 10
    return s

def suma_varios(numeros:List[int])->List[int]:
    resultados = []
    for num in numeros:
        resultados.append(suma(num))
    return resultados

entrada = input('Dame los numeros separados por un espacio: ')
numeros = list(map(int, entrada.split()))
resultado = suma_varios(numeros)
print(f'Lista de numeros original: {numeros}')
print(f'Lista con la suma de los digitos de los nuemros: {resultado}')