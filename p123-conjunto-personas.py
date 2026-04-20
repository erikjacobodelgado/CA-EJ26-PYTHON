## p123-conjunto-personas.py
## Practica de conjuntos con elementos de texto 

print("\033[H\033[J")

A = {'Juan', 'Maria', 'Pedro', 'Jose', 'Rocio'}
B = {'Pedro', 'Juan', 'Pablo', 'Mateo', 'Ester'}

print('Conjuntos iniciales')
print(f'A = {A}')
print(f'B = {B}')

C = A | B
print('\nUnión:')
print(C)

D = A & B 
print('\nIntersección:')
print(D)

E = A - B 
print('\nDiferencia:')
print(E)

F = A ^ B
print('\nDiferencia simetrica:')
print(F)

G = {'Pablo', 'Mateo'}
print(f'\nEs (Pablo, Mateo) subconjunto de B?: {G <= B}')

H = {'Reynaldo', 'Angelica'}
print(f'\nEs A un superconjunto de (Reynaldo, Angelica)?: {H >= A}')

print(f'\nEsta "Pedro" en el conjunto A?: {'Pedro' in A}')

print(f'\nNo esta "Lilia" en el conjunto B?: {'Lilia' not in B}')