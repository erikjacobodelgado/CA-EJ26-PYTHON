## p095-precio-acciones.py
## Análisis básico de portafolio de acciones 

print("\033[H\033[J")
print('Análisis básico de portafolio de acciones \n')

dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']
precios = [10.25, 152.50, 149.75, 155.00, 1153.20, 200.00]

pmax = max(precios)
pmin = min(precios)

posmax = precios.index(pmax)
posmin = precios.index(pmin)

print(f'Precios de las acciones más altas en la semana: {precios}')
print(f'Precio mas alto ${pmax} el dia {dias[posmax]}')
print(f'Precio mas bajo ${pmin} el dia {dias[posmin]}')