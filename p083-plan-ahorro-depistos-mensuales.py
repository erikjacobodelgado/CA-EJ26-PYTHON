## p083-plan-ahorro-depistos-mensuales.py
## Simulación de un plan de ahorro

print("\033[H\033[J")
print('Simula tu plan de ahorro\n')

mi = float(input('Monto inicial de ahorro:'))
dm = float(input('Depósito mensual fijo: '))
tim = float(input('Tasa de interés mensual: '))
m = int(input('Número de meses a simular: '))

print('\nPlan de ahorro detallado')
for i in range (1, m+1):
    print(f'Mes {i} || Saldo inicial: {mi:.2f} || Interés: {mi*(tim/100):.2f}')
    mi = (mi + dm) + (mi * (tim/100))
    print(f'Saldo final: {mi:.2f}')

print(f'\nAl final de {m} meses tendrías: {mi:.2f}')