## p071-arriba-abajo.py
## Imprime los numeros de 1 a n o de n a 1

print("\033[H\033[J")

while True:
    print('\n1 Imprimir los numeros de 1 a n (arriba)')
    print('2 Imprimir los numeros de n a 1 (abajo)')

    op = int(input('Elige opcion: '))

    if op == 1:
        print('Numeros de 1 a n')
        n = int(input('Hasta donde?: '))
        for x in range(1, n+1):
            print(x, end=' ')

    elif op == 2:
        print('Numeros de n a 1')
        n = int(input('Hasta donde?: '))
        for x in range(n, 0, -1):
            print(x, end=' ')

    else:
        print('Opcion invalida')

    if input('\nDeseas continuar (S/N)?: ').upper()=='N':break

print('\nProceso terminado')