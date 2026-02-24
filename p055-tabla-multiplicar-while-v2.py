## p055-tabla-multiplicar-while-v2.py
## Imprime todas las tablas de 1 a 10 desde 1 hasta 10

while True:
    print("\033[H\033[J")
    print('Tablas de multiplicar')
    while True:
        n = int(input('Hasta que tabla: '))
        m = int(input('Hasta que numero: '))
        if n>0 and m>0: break 

    t = 1
    while t <= n:

        z = 1
        print(f'\nTabla del {t}')

        while z <= m:
            print(f'{t} x {z} = {z*t}')
            z = z + 1

        t = t + 1

    if input('Deseas continuar (S/N)?: ').upper() == 'N' : break

print('Proceso terminado')