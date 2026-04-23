## p134-cuadro-caracter.py
## Funcion que recibe 3 parametros y dibuja un cuadro

print("\033[H\033[J")

print('\nCONVENCIONAL')
ren = 10
col = 2
car = '$'

for r in range(ren):
    for c in range(col):
        print(car,end=(''))
    print()

print('\nUSANDO UNA FUNCION')
def cuadro(ren:int, col:int, car:str)->None:
    for r in range(ren):
        for c in range(col):
            print(car,end=(''))
        print()
cuadro(5, 10, '%')

print('\nPIDIENDO LOS VALORES')
ren = int(input('Renglones: '))
col = int(input('Columnas: '))
car = input('Caracter: ')
cuadro(ren, col, car)