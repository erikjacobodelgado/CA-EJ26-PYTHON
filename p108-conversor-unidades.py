## p108-conversor-unidades.py
## Conversor de unidades de medida 

conversiones = {
'km': 1000,
'm': 1,
'cm': 0.01,
'mm': 0.001
}

print("\033[H\033[J")
print('Conversor de unidades de medida ')

long = int(input('Longitud: '))

while True:
    unidad = input('Unidad (km, m, cm, mm): ').lower()
    if unidad in conversiones: break

res = long * conversiones[unidad]

print(f'Una longitud de {long} equivale a {res:.2f} metros')