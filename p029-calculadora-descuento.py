## p029-calculadora-descuento.py
## Programa para calcular el precio final de una compra aplicando un descuento escalonado 

print("\033[H\033[J")

print('Calculadora de descuentos')

descuento = 0
porcentaje = 0

compra = float(input('Ingresa el total de tu compra: '))

if compra > 2000:
    porcentaje = 0.20
elif compra > 1000:
    porcentaje = 0.10
elif compra > 500:
    porcentaje = 0.05
else:
    porcentaje = 0

descuento = compra * porcentaje 

total = compra - descuento 
print('Resumen:')
print(f'Total de tu compra: {compra:.2f}')
## print(f('Descuento: {porcentaje} %'))
print(f'Ahorraste: {descuento}')
print(f'Total a pagar: {total}')