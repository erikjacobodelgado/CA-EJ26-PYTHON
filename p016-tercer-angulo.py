## p016-tercer-angulo.py
## Programa para determinar el tercer angulo de un triangulo en base a los otros dos dados por el usuario 

print("\033[H\033[J")

print('Dame el primer angulo: ')
ang1 = float(input())
print('Dame el segundo angulo: ')
ang2 = float(input())

ang3 = 180 - (ang1 + ang2)

print(f'El valor del tercer angulo es: {ang3:.2f}')
