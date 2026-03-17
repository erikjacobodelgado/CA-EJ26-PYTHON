## p093-procesar-calificaciones.py
## Procesar una lista de calificaciones

print("\033[H\033[J")
print('Procesador de calificaciones\n')
print('Introduce calificaciones entre 0 y 10 (99 para terminar)\n')

cals =[]
mp = []
s = 0.0

while True:
    try:
        n = float(input('Calificación: '))
        if n == 99: break 
        if 1 <= n <= 10:
            cals.append(n)
            s += n
        else:
            print('X')
    except:
        print('Calificación no válida')

p = s / len(cals)
print(f'Se capturaron: {len(cals)}:{cals}')
print(f'La suma es: {s}')
print(f'El promedio es: {p}')

for c in cals:
    if c > p: mp.append(c)

print(f'Mayores al promedio: {len[mp]}:{mp}')
print(f'Calificación más alta: {max(cals)}')
print(f'Calificación más baja: {min(cals)}')
