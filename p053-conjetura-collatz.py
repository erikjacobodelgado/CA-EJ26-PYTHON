## p053-conjetura-collatz.py
## Resolver la conjetura de Collatz

while True:

    print("\033[H\033[J")

    print('Imprime la conjetura de Collatz')

    while True:
        n = int(input('Dame un numero: '))
        if n > 1 : break

    p = 0
    while n != 1:
        print(n,end='-') ## imprime la variable n y al acabar (end) imprime lo que este entre parentesis
        p+=1
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1

    print(n, end=' ')
    print(f'\nPasos hasta llegar a 1: {p}')

    if input('Deseas continuar (S/N)?: ').upper() == 'N' : break

print('Proceso terminado')