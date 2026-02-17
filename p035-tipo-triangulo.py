## p035-tipo-triangulo.py
## Programa para identificar el tipo de triangulo mediante sus lados

print("\033[H\033[J")

print('Clasificador de triangulos')

l1 = float(input('Dame el lado 1: '))
l2 = float(input('Dame el lado 2: '))
l3 = float(input('Dame el lado 3: '))

if l1 == l2 == l3:
    print('Triangulo equilatero')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('Triangulo isoceles')
else:
    print('Triangulo escaleno')

print('\nProceso finalizado')