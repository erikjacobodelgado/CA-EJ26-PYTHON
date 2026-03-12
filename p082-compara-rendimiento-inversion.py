## p082-compara-rendimiento-inversion.py
## Comparador de dos fondos de iversión 

print("\033[H\033[J")
print('Comparador de dos fondos de inversión')

print('\nFondo de inversión A')
mia = float(input('Monto inicial: '))
tia = float(input('Tasa de interes anual (%): '))

print('\nFondo de inversión B')
mib = float(input('Monto inicial: '))
tib = float(input('Tasa de interes anual (%): '))

anio = int(input('\nAños a proyectar: '))

print('\nComparación de rendimientos anuales')
print('Año ||   Fondo A   ||   Fondo B  ')
print('----------------------------------')
for i in range (1, anio+1):
    mia = (mia * (tia / 100)) + mia 
    mib = (mib * (tib / 100)) + mib
    print(f'  {i} ||  {mia:.2f}    ||  {mib:.2f}')
    
if mia > mib:
    print(f'\nEl fondo A {mia:.2f} superó al fondo B {mib:.2f}')
else:
    print(f'\nEl fondo B {mib:.2f} superó al fondo A {mia:.2f}')