## p125-segundo-examen-parcial.py
## Porcesamiento y registro de vuelos

print("\033[H\033[J")

print('Captura de datos de los vuelos (* para terminar)')

datos = {}
i = 1

while True:
    numero = input('\nNumero de vuelo: ')
    if numero == '*': break
    origen = input('Origen: ')
    destino = input('Destino: ')
    aerolinea = input('Aerolinea: ')
    pasajeros = int(input('Pasajeros: '))
    tarifa = float(input('Tarifa: '))

    datos [i] = {
        'Numero de vuelo': numero,
        'Origen': origen,
        'Destino': destino,
        'Aerolinea': aerolinea,
        'Pasajeros': pasajeros,
        'Tarifa': tarifa

    }

    i = i + 1

print('\nDATOS EN CRUDO')
for k in datos.items():
    print(k)

print('\nTABLA DE DATOS')
print('{:<5} {:<15} {:<15} {:<15} {:<15} {:<15}'.format(
    "#", "Origen", "Destino", "Aerolinea", "Pasajeros", "Tarifa"
))
print('-' * 90)
## Utilice el método .format, ya que apoyándome con la IA al momento de organizar los datos
## encontré que este método permite atribuir un valor dentro de un texto en posiciones específicas
## en este caso son 5 valores para 5 cadenas de texto, se atribuye el 1ro con el 1ro, el 
## 2do con el 2do y asi sucesivamente 

for k, v in datos.items():
    print('{:<5} {:<15} {:<15} {:<15} {:<15} {:<15.2f}'.format(
        v['Numero de vuelo'],
        v['Origen'],
        v['Destino'],
        v['Aerolinea'],
        v['Pasajeros'],
        v['Tarifa']
    ))
## Mismo uso del .format que en la parte anterior, solo que aquí lo utilicé para generar la tabla

print('\nRESUMEN')
print(f'Total de vuelos: {len(datos)}')

print('\nAerolineas')
aerolineas ={}
for x in datos.values():
    aerolinea = x['Aerolinea']
    aerolineas[aerolinea] = aerolineas.get(aerolinea, 0) + 1
for aerolinea, cant in aerolineas.items():
    print(aerolinea, ':', cant)

print('\nDestinos')
destinos = {}
for x in datos.values():
    destino = x['Destino']
    destinos[destino] = destinos.get(destino, 0) + 1

for destino, cant in destinos.items():
    print(destino, ':', cant)

totpasajeros = 0
for x in datos.values():
    totpasajeros += x['Pasajeros']
print(f'\nPasajeros: Suma = {totpasajeros}, Promedio = {totpasajeros/len(datos)}')

tottarifa = 0
for x in datos.values():
    tottarifa += x['Pasajeros'] * x['Tarifa']
print(f'\nTarifa: Suma = {tottarifa}, Promedio = {tottarifa/len(datos)}')

