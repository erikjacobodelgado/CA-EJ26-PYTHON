## p109-conversion-divisas.py
## Convresor de divisas 

conversiones = {
'USD': 20.50,
'EUR': 22.30,
'GBP': 25.80,
'JPY': 0.19,
'CAD': 16.20
}

print("\033[H\033[J")
print('\nConversor de divisas ')

print('\nOpciones de monedas')
for m in conversiones.keys():
    print(f'{m}', end=' ')

while True:
    mon = input('\nMoneda: ').upper()
    if mon in conversiones: break 
    else: print('Moneda no valida')

cantidad = float(input('Cantidad: '))

res = cantidad * conversiones[mon]

print(f'\nPara {cantidad:.2f} {mon} equivalen a {res} pesos')