## p048-multiplos-continue.py
## Imrpime solo los multiplos de 10 hasta 200

print("\033[H\033[J")

print('Imprime los multiplos de 10 desde el 0 al 200')

n = int(input('Que multiplos quieres hasta 200?: '))

c = 0

while c < 200:
    c = c + 1
    if c % n != 0:
        continue ## continua haciendo el ciclo hasta que se cumpla la condición 
    print(c, end = ' ')