## p100-listas-multiplica.py
## Multiplicación entre listas 

print("\033[H\033[J")
print('MULTIPLICACIÓN DE DOS LISTAS')

uno = []
dos = []
tres = []

for i in range(0,5):
    a = int(input(f'\nIntroduzca {i+1}/5 números para la lista A: '))
    uno.append(a)
    b = int(input(f'Introduzca {i+1}/5 números para la lista B: '))
    dos.append(b)

for i in range(len(uno)):
    mult = uno[i] * dos[i]
    tres.append(mult)


print('RESULTADOS')
print(f'Lista A: {uno}')
print(f'Lista B: {dos}')
print(f'Lista C: {tres}')

