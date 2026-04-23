## p132-funcion-retorno.py
## Funcion que recibe parametros y regresa un valor

print("\033[H\033[J")

def suma(n1:float, n2:float)->float:
    s = n1 + n2
    return s

print('Suma de dos numeros constantes')
resultado = suma(10, 20)
print(f'La suma es: {resultado}')

print('\nDame dos valores separados por enter: ')
a, b = int(input()), int(input())
print(f'La suma es: {suma(a,b)}')