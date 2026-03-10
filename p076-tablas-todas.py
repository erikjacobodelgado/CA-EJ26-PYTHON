## p076-tablas-todas.py
## Imprime las tablas de 1 al n hasta el m

print("\033[H\033[J")
print('Imprime las tablas del 1 al n hasta el m')

n = int(input('Hasta que tabla?: '))
m = int(input('Hasta que numero se multiplica?: '))

for i in range(1, n+1):
    print(f'Tabla del {i}')
    for j in range(1, m+1):
        print(f'{i} + {j} = {i*j}')
    print() ## Salto de linea en blanco 