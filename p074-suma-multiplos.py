## p074-suma-multiplos.py
## Imprime multiplos m en el rango de 1 a n


while True:
    print("\033[H\033[J")

    print('Imprime multiplos m en el rango de 1 a n')

    n = int(input('Hasta donde?: '))
    m = int(input('Que multiplos?: '))

    c = s = 0

    for i in range(1, n+1):
        if i % m == 0: ## Se calcula el modulo para saber si es multiplo
            print(i, end=' ')
            c = c + 1
            s = s + i 

    print(f'\nLos multiplos de {m} en el rango de 1 a {n} son: {c}')
    print(f'La suma de los multiplos es: {s}')

    if input('\nDeseas continuar (S/N)?: ').upper()=='N':break