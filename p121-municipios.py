## p121-municipios.py
## Aministrar un padron de municipios mediante conjuntos y sus operaciones

print("\033[H\033[J")

municipios = {'Zacatecas', 'Guadalupe', 'Jerez', 'Fresnillo', 'Fresnillo'}
print(f'Padron original: {municipios} - {len(municipios)}')

print('\nLista de municipios:')
for municipio in municipios:
    print(municipio)

print(f'\nEsta Zacatecas en el padron? : {"Zacatecas" in municipios}')

print('\nAgregar municipio: ')
municipios.add('Teul')
print(f'Padron actualizado: {municipios} - {len(municipios)}')

otros = {'Luis Moya', 'Ojocaliente', 'Tepetongo'}
municipios.update(otros)
print(f'\nPadron actualizado: {municipios} - {len(municipios)}')

print('\nEliminar municipios')
municipios.remove('Zacatecas')
print(f'Padron actualizado: {municipios} - {len(municipios)}')

municipios.discard('Ojocaliente')
print(f'\nPadron actualizado: {municipios} - {len(municipios)}')

municipio = municipios.pop()
print(f'\nPadron actualizado: {municipios} - {len(municipios)}')
print(municipio)

municipios.clear()
print(f'\nPadron actualizado: {municipios} - {len(municipios)}')