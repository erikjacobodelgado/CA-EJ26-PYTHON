## p094-consolidar-ventas.py
## Consolidar la venta de dos sucursales usando listas 

print("\033[H\033[J")
print('Consolidar ventas de dos sucursales\n')

n = int(input('Ventas diarias por sucursal: '))

vs1 = []
vs2 = []
vtot = []
s = 0

print('\nVENTAS SUCURSAL 1')
for i in range(n):
    venta = int(input(f'Venta del dia {i+1}: '))
    vs1.append(venta)

print('\nVENTAS SUCURSAL 2')
for i in range(n):
    venta = int(input(f'Venta del dia {i+1}: '))
    vs2.append(venta)

for i in range(n):
    sd = vs1[i] + vs2[i]
    vtot.append(sd)
    s += sd

print('\nREPORTE DE VENTAS')
print(f'Sucursal 1: {vs1}')
print(f'Sucursal 1: {vs2}')
print(f'Ventas consolidadas: {vtot} : {s}')
