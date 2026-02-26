## p059-pares-descendente.py
## Imprimir los numeros pares y su suma total en un rango descendente desde 100 hasta un numero n que elija el usuario.

while True:
    print("\033[H\033[J")
    print('Imprimir los numeros pares y su suma total en un rango descendente desde 100 hasta un numero n.')

    lim = int(input('Introduce el numero limite (menor a 100): '))

    suma = 0

    print('Numeros pares:')

    while lim <= 100:
        print(lim, end=' ')
        suma += lim
        lim += 2

    print(f'\nLa suma de los pares es : {suma}')


    if input('\nDeseas continuar (S/N)?: ').upper() == 'N': break

print('Proceso terminado')