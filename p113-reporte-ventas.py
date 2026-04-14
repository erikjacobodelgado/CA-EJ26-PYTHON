## p113-reporte-ventas.py
## Reporte de ventas mediante un diccionario dentro de otro diccionario 

print("\033[H\033[J")

compras = []

print('\nREGISTRO DE TRANSACCIONES')
n = int(input('Cuantas compras vas a registrar?: '))

for i in range(1, n+1):
    print(f'\nCompra {i}')
    compra = {
        'cliente' : input('Nombre cliente: '),
        'producto' : input('Producto: '),
        'cantidad' : int(input('Cantidad: ')),
        'precio' : float(input('Precio: '))
    }
    compras.append(compra)

print(f'\nLista de compras registradas: {compras}')

clientes = {}
for compra in compras:
    cliente = compra['cliente']
    if cliente not in clientes:
        clientes[cliente] = {'cantidad':0, 'subtotal':0}
    clientes[cliente]['cantidad'] += compra['cantidad']
    clientes[cliente]['subtotal'] += compra['cantidad'] * compra['precio']

print('\nREPORTE TOTAL POR CLIENTE')
for cliente, datos in clientes.items():
    print('Cliente: ', cliente)
    print('Total productos: ', datos['cantidad'])
    print('Total a pagar: ', datos['subtotal'])
    print()

print(f'\nDICCIONARIO CONSOLIDADO', clientes)