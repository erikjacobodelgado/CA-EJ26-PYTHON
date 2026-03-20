## p099-procesar-notas.py
## Procesador de notas 

print("\033[H\033[J")
print('PROCESADOR DE NOTAS \n')

notas = []
i = 0
menores = []

while True:
    n = int(input('Ingresa una nota entre 1 y 100\n(0 para terminar): '))
    if n == 0: break 
    if n <= 100 and n > 0:
        notas.append(n)
        i += n
    else:
        print('Nota no válida')

prom = i/len(notas)

for n in notas:
    if n < prom:
        menores.append(n)

print('\nRESULTADOS')
print(f'Total de notas introducidas: {len(notas)}')
print(f'Lista de notas: {notas}')
print(f'Suma de notas: {i}')
print(f'Promedio de notas: {prom:.2f}')
print(f'Nota máxima: {max(notas)}')
print(f'Nota mínima: {min(notas)}')
print(f'Notas menores al promedio: {len(menores)}')
print(f'Lista de notas menores al promedio: {menores}')
