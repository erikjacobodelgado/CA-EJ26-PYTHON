## p058-impares-ascendente.py
## Imprimir los numeros impares y su suma total en un rango ascendente desde 1 hasta un numero n que elija el usuario.

while True:
    print("\033[H\033[J")
    print('Imprimir los numeros impares y su suma total en un rango ascendente desde 1 hasta un numero n.')

    lim = int(input('Introduce el numero limite: '))

    suma = 0
    num = 1

    print('Numeros impares:')

    while num <= lim:
        print(num, end=' ')
        suma += num
        num += 2

    print()
    print(f'La suma de los impares es: {suma}')

    if input('Deseas continuar (S/N)?: ').upper() == 'N': break

print('Proceso terminado')