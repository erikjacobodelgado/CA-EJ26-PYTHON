## p057-interes-simple.py
## Calcula los años necesarios para alcanzar una meta de ahorro

print("\033[H\033[J")
print('Calcula los años necesarios para alcanzar una meta de ahorro')

ci = float(input('Capital inicial: '))
ti = float(input('Tasa de interes anual en porcentaje: '))
ma = float(input('Meta de ahorro: '))

ca = ci 
anio = 0
iaf = ci * (ti/100)

while ca <= ma:
    print(f'{anio} {ca} - {iaf}')
    ca = ca + iaf 
    anio = anio + 1

print(f'Para alcanzar {ma:,.2f}, necesitas {anio} años')
print(f'Monto final: ${ca:,.2f}')