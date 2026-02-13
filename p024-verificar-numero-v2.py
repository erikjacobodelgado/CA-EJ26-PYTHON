## p023-verificar-numero-v2.py
## Programa para verificar si un numero entero es positivo, negativo o cero (if else)

print("\033[H\033[J")

print('Verificando si un numero entero es positivo, negativo o cero \n')

num = int(input('Dame un numero entero: '))

if num > 0:
    print('Numero positivo 👍')
elif num < 0:                           ## elif = else if
    print('Numero negativo 👎')
else:
    print('Numero cero 👌')

print('\nPrograma terminado \n')
