## p038-dia-semana.py
## Escribe un programa que solicite un número entero del 1 al 7 y muestre el día de la semana correspondiente, considerando que 1 es domingo y 7 es sábado. Si el número ingresado está fuera de ese rango, debe mostrar un mensaje de error.

print("\033[H\033[J")

print('Te digo a que dia corresponde en base al numero que ingresaste')
print('Dame un numero del 1 al 7')

dia = int(input())

if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Lunes')
elif dia == 3:
    print('Martes')
elif dia == 4:
    print('Miercoles')
elif dia == 5:
    print('Jueves')
elif dia == 6:
    print('Viernes')
elif dia == 7:
    print('Sabado')
else:
    print('Error: Dia invalido')

print('\nProceso finalizado')