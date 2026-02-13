## p023-verificar-numero.py
## Programa para verificar si un numero entero es positivo, negativo o cero

print("\033[H\033[J")

print('Verificando si un numero entero es positivo, negativo o cero \n')

num = int(input('Dame un numero entero: '))

if num > 0:
    print('Numero positivo 👍')

if num < 0:
    print('Numero negativo 👎')

if num == 0:
    print('Numero cero 👌')

print('\nPrograma terminado \n')
