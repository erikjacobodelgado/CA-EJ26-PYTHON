## p073-suma-promedio-numeros.py
## Suma de n numeros introducidos por el usuario usando for

while True:

    print("\033[H\033[J")

    print('Suma de n numeros introducidos por el usuario usando for')

    cuantos = int(input('Cuantos numeros deseas procesar?: '))
    suma = 0
    cadnum = ''

    for i in range(1, cuantos+1):
        n = float(input(f'Numero {i}/{cuantos}: '))
        suma = suma + n
        cadnum = cadnum + ' ' + str(n)

    print(f'\nLos numeros son: {cadnum}')
    print(f'La suma es: {suma:.2f}')
    print(f'El promedio es: {suma/cuantos:.2f}')

    if input('\nDeseas continuar (S/N)?: ').upper()=='N':break
