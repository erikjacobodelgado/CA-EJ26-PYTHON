## p017-convertir-temperatura.py
## Programa para convertir una temperatura dada por el usuario de grados Celcius a grados Fahrenheit

print("\033[H\033[J")

print('Dame la temperatura en grados Celcius: ')
cel = float(input())

far = (cel * (9/5)) + 32

print(f'La temperatura en grados Fahrenheit es: {far:.2f}')
