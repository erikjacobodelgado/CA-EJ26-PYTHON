## p085-rombo-caracter.py
## Generar un rombo en base a un numero impar y un caracter ingresado

print("\033[H\033[J")
print('Generar un rombo en base a un numero impar y un caracter ingresado')

n = int(input('Dame el numero impar para la altura y el ancho del rombo: '))
car = input('Caracter: ')

for i in range(1, n + 1):
    print(' ' * (n - i) + car * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + car * (2 * i - 1))