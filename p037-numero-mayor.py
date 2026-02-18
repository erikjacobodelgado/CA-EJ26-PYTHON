## p037-numero-mayor.py
## Escribe un programa que reciba tres números enteros e identifique y muestre cuál de ellos es el mayor.

print("\033[H\033[J")

print('Programa para encontrar el mayor de tres numeros')
print('Ingresa tres numeros enteros separados por un espacio')

n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if n1 > n2 and n1 > n3:
    print(f'El numero mayor es {n1}')
elif n2 > n1 and n2 > n3:
    print(f'El numero mayor es {n2}')
else:
    print(f'El numero mayor es {n3}')

print('\nProceso finalizado')