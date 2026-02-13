## p028-retira-cuenta.py
## Simular el retiro de dinero de una cuenta 

print("\033[H\033[J")

print('Validando el retiro de dinero de una cuenta')
saldo_actual = 1500
print(f'Saldo actual = {saldo_actual}')

cantidad_retiro = float(input('Cantidad a retirar: '))

if cantidad_retiro > 0:
    if cantidad_retiro <= saldo_actual:
        nuevo_saldo = saldo_actual - cantidad_retiro
        print('Retiro exitoso')
        print(f'Nuevo saldo = {nuevo_saldo}')
    else:
        print(f'No tienes saldo suficiente, te falta = {cantidad_retiro - saldo_actual}')
else:
    print('La cantidad debe ser mayor a 0')

print('Programa finalizado')