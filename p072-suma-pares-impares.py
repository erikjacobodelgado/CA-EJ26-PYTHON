## p072-suma-pares-impares.py
## Imprime la suma de pares e impares e un rango determinado 

print("\033[H\033[J")

print('Imprime la suma de pares e impares e un rango determinado ')

n = int(input('Dame el valor final (1...n): '))

cp = ci = ''
sp = si = 0

for i in range(1, n+1):
    if i % 2 == 0:
        cp = cp + ' ' + str(i) ## Convierte los numeros a una cadena de caracteres
        sp = sp + i
    else:
        ci = ci + ' ' + str(i)
        si = si + i 

print('\nResumen')
print(f'Pares: {cp} - {sp}')
print(f'Impares: {ci} - {si}')