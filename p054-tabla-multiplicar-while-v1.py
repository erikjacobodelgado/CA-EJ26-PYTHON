## p054-tabla-multiplicar-while-v1.py
## Imprime una tabla t desde 1 hasta n

while True:
    print("\033[H\033[J")
    print('Imprime una tabla t desde 1 hasta n')

    while True:
        t = int(input('Tabla: '))
        n = int(input('Hasta donde: '))
        if t>0 and n>0: break

    z = 1
    while z <= n:
        print(f'{z:>5} x {t:>5} = {z*t:>10}')
        z = z + 1

    if input('Deseas continuar (S/N)?: ').upper() == 'N' : break

print('Proceso terminado')