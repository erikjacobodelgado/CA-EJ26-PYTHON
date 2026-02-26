## p065-sistema-papeleria.py
## Calcula y registra las ventas de una papeleria

print("\033[H\033[J")
print('-------------------------')
print('PAPELERIA MALENA')
print('Sistema de venta de copias')
print('-------------------------')

ventas = 0 ## conteo de ventas
subtotal = 0 ## cantidad de dinero acumulado
cantidad_c = cantidad_o = cantidad_d = cantidad_p = 0 ## contadores para el tipo de copia
total_c = total_o = total_d = total_p = 0 ## contadores de venta de cada tipo de hoja

while True:
    ventas = ventas + 1 # contador de ventas
    print(f'Ventas: {ventas}')
    tipo = input('Tipo de copia (C)arta $3, (O)ficio $4, (D)oble Of $6, (P)lano $12 ? ').upper()
    
    if tipo not in 'CODP': ## not in para determinar que lo que no esta en las comillas es incorrecto
        print('Error: Tipo de copia no valido, intente de nuevo')
        ventas = ventas - 1 ## resta el valor invalido
        continue 

    cantidad = int(input('Cantidad ? '))

    if tipo == 'C':
        cantidad_c = cantidad_c + cantidad
        total_c += cantidad * 3 ## total de cartas mas cantidad por tres
    elif tipo == 'O':
        cantidad_o = cantidad_o + cantidad
        total_o += cantidad * 4
    elif tipo == 'D':
        cantidad_d = cantidad_d + cantidad
        total_d += cantidad * 6
    elif tipo == 'P':
        cantidad_p = cantidad_p + cantidad
        total_p += cantidad * 12

    if input('Otra venta (S/N)? ').upper() != 'S': break 

total_copias = cantidad_c + cantidad_o + cantidad_d + cantidad_p ##total de copias
total_ventas = total_c + total_o + total_d + total_p ##total de ventas

if total_copias >= 50:
    total_ventas *= 0.90 ##descuento del 10%

print('---------------------------------------')
print('Resumen diario de ventas')
print('---------------------------------------')
print(f'Ventas realizadas: {ventas}')
print('---------------------------------------')
print(f'Carta\t\t: {cantidad_c:2d} - ${total_c:8.2f}')
print(f'Oficio\t\t: {cantidad_o:2d} - ${total_o:8.2f}')
print(f'Doble oficio\t: {cantidad_d:2d} - ${total_d:8.2f}')
print(f'Plano\t\t: {cantidad_p:2d} - ${total_p:8.2f}')

print(f'\nTot. Ventas\t: {total_copias:2d} - ${total_ventas:8.2f}')

mensaje = ''
if total_ventas > 150:
    mensaje = 'VENTA SUPERADA'
elif total_ventas >= 50:
    mensaje = 'VENTA FRECUENTE'
else:
    mensaje = 'VENTA MODERADA'

print(f'Esta venta es una: {mensaje}')