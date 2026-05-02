## p152-suma-pares-impares.py
## Funcion que suma pares o imapres dentro de un rango de numeros 

from ast import Tuple
from typing import List

def pares_impares(numeros:List[int])->Tuple[List:[int],List[int]]:
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares 

def main()->None:
    print('Suma en rango')
    inicio = int(input('Introduce el inicio: '))
    fin = int(input('Introduce el final: '))
    numeros = list(range(inicio, fin+1))
    opc = input('Sumar P:Pares o I:Impares: ')
    pares, impares = pares_impares(numeros)
    if opc == 'P' or opc == 'p':
        suma_pares = sum(pares)
        print(f'La suma de los numeros pares entre {inicio} y {fin} es: {suma_pares}')
    elif opc == 'I' or opc == 'i':
        suma_impares = sum(impares)
        print(f'La suma de los numeros impares entre {inicio} y {fin} es: {suma_impares}')
    else:
        print('Error')

if __name__ == '__main__':
    print("\033[H\033[J")
    main()