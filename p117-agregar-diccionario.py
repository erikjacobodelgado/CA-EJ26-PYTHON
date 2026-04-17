## p117-agregar-diccionario.py
## Agregar datos a un diccionario de ventas

print("\033[H\033[J")

ventas = {
    'Juan':1550, 'Jose':2600, 'Maria':2220 
}
print('Ventas iniciales:')
print(ventas)

ventas['Rocio']=2500
ventas['Mateo']=1567

ventas.update({'Andrea':9567, 'Miguel':1234})

print('\nVentas actualizadas:')
print(ventas)