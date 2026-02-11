## p022-resistencia-equivalente-paralelo.py
## Porgrama  para calcular la resitencia total o equivalente de un circuito con cuatro resistencias en paralelo

print("\033[H\033[J")

print('Dame el valor de las cuatro resistencias separadas por espacio')
r1, r2, r3, r4 = input().split()
r1, r2, r3, r4 = float(r1), float(r2), float(r3), float(r4)

rt = float(1 / ((1/r1) + (1/r2) + (1/r3) + (1/r4)))
print(f'El valor de la resistencia total es: {rt:.2f}')
