## p044-conteo-ascendente.py
## Imprime numeros de 1 a 100 con ciclo while

print("\033[H\033[J")

print('Numeros de 1 a 100 con while')

z = 1

while z <= 100:
    print(z)
    z = z + 1

print('\nCiclo terminado')

x = 1

while x <= 100:
    print(x, end = ' ') ## end = ' ' para que el programa lance los numeros en una sola linea
    x = x + 1

print('\nCiclo terminado')