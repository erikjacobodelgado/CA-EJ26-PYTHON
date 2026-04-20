## p124-conjunt-numeros.py
## Practica de conjuntos con elementos numericos 

print("\033[H\033[J")

A = {50, 60, 70, 80, 90, 100, 200}
B = {60, 90, 100, 300, 400, 500}
C = {10, 20, 60, 90, 70, 100, 600, 700}

print('Conjuntos iniciales')
print(f'A = {A}')
print(f'B = {B}')
print(f'C = {C}')

print('\nUnion A | B')
print(A | B)

print('\nUnion B | C')
print(B | C)

print('\nDiferencia A - C')
print(A - C)

print('\nDiferencia simetrica B ^ C')
print(B ^ C)

print('\nIntersection B & C')
print(B & C)

print(f'\nEs A subconjunto de B? {A <= B}')
print(f'Es C subconjunto de A? {C <= A}')
print(f'Esta el numero 100 en A? {100 in A}')
D = A | B | C
print(f'Esta el numero 60 en A, B y C? {60 in D}')
print(f'No esta el numero 900 en C? {900 not in C}')