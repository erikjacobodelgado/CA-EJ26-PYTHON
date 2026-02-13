## p026-convertir-temperaturas-v2.py
## Covertir temperatura de Celsius a Fahrenheit o viceversa segun decida el usuario 

print("\033[H\033[J")

print('Coversion de temperatura \n')
print('[ 1 ] Fahrenheit a Celsius\n')
print('[ 2 ] Celcius a Fahrenheit\n')

opc = int(input('Ingresa una opcion: '))

if opc == 1:
    print('Conversion a celsius \n')
    f = float(input('Dame los grados en Fahrenheit: '))
    c = (( f - 32 ) * 5 ) / 9
    print(f'Los {f} grados Fahrenheit equivalen a {c:.2f} grados celsius ')

elif opc == 2:
    print('Conversion a Fahrenheit \n')
    c = float(input('Dame los grados en Celsius: '))
    f = ((c * 5) / 9) + 32
    print(f'Los {c} grados Celsius equivalen a {f:.2f} grados Fahrenheit ')

else:
    print('La opcion seleccionada no es valida ')

print('Programa finalizado')