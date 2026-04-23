## p136-estacion-año.py
## Funcion que recibe un numero y regresa la estacion del año

## print("\033[H\033[J")

def estacion(mes: int)->str:
    e = ''
    if mes in [12,1,2]:
        e = 'invierno'
    elif mes in [3,4,5]:
        e = 'Primavera'
    elif mes in [6,7,8]:
        e = 'verano'
    elif mes in [9,10,11]:
        e = 'otoño'
    else:
        e = 'mes invalido'

    print('Dame un mes del año entre 1 y 12')
    mes  = int(input())
    print(f'La estacion del año de {mes} es: {estacion(mes)}')