## p084-cuadro-hueco-caracter.py
## Crea un cuadro hueco en base a un lado y un caracter ingresado

print("\033[H\033[J")
print('Crea un cuadro hueco en base a un lado y un caracter ingresado')

lado = int(input('De qué tamaño será el lado del cuadrado?: '))
car = input('Qué carácter quieres usar?: ')

for i in range(lado):
    for j in range(lado):
        if i == 0 or i == lado-1 or j == 0 or j == lado-1:
            print(car, end='')
        else:
            print(' ', end='')
    print()