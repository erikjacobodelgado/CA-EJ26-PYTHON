## p069-conteo-descendente-for.py
## Imprime numeros de 100 a 1 con for

print("\033[H\033[J")

print('Imprime numeros de 100 a 1 con for')

for x in range(100, 0, -1): ## -1 porque va de forma descendente 
    print(x, end=' ')