## p044-conteo-ascendente-v2.py
## Imprime numeros de 1 a n con ciclo while

print("\033[H\033[J")

print('Numeros de 1 a n con while')

n = int(input('Hasta donde?: '))
m = int(input('A que paso?: '))

z = 0

while z <= n:
    print(z)
    z = z + m

print('\nCiclo terminado')