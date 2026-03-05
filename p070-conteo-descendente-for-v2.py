## p070-conteo-descendente-for-v2.py
## Imprime numeros de 1 a n en intervalos de m usando for en descedente

print("\033[H\033[J")

print('Imprimiendo numeros de 1 a n en intervalos de m usando un ciclo for en descendente')

p = int(input('Desde donde?: '))
n = int(input('Hasta donde?: '))
m = int(input('De cuanto en cuanto?: '))

for h in range(p, n-1, -m): ## No olvidar poner el '-' para el decremento
    print(h, end=' ')   