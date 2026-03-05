## p068-conteo-ascendente-for-v2.py
## Imprime numeros de 1 a n en intervalos de m usando for

print("\033[H\033[J")

print('Imprimiendo numeros de 1 a n en intervalos de m usando un ciclo for')

p = int(input('Desde donde?: '))
n = int(input('Hasta donde?: '))
m = int(input('De cuanto en cuanto?: '))

for h in range(p, n+1, m): ## El for siempre cuenta uno menos que el indicado por eso el 101
    print(h, end=' ')   ## range(inicio, fin+1, incremento)