## p133-tabla-multiplicar.py
## Funcion que recibe dos parametros y crea un atabla de multiplicar 

print("\033[H\033[J")

tabla = 5
limite = 8

print(f'Tabla de multiplicar del {tabla}, del 1 al {limite}')
for i in range(1,limite+1):
    res = tabla * i
    print(f'{tabla} * {i} = {res}')

print('\nUSANDO UNA FUNCION')
def tabla_multiplicar(tabla:int, limite:int)->None:
    print(f'Tabla de multiplicar del {tabla}, del 1 al {limite}')
    for i in range(1,limite+1):
        res = tabla * i
        print(f'{tabla} * {i} = {res}')

print('\nCON VALORES YA PUESTOS')
tabla_multiplicar(6,10)

print('\nPIDIENDO LOS VALORES')
print('Dame la tabla y el límite')
tabla = int(input('Tabla: '))
limite = int(input('Limite: '))
tabla_multiplicar(tabla, limite)