## p115-crear-acceder-diccionario.py
## Diccionario de dias 

print("\033[H\033[J")
print('Diccionario inicial:')

dias = {
    1:'Lunes', 2:'Martes', 3:'Miercoles', 4:'Jueves', 5:'Viernes', 6:'Sabado', 7:'Domingo'
}
print(dias)

print('\nAccediendo a elementos:')
l = dias[1]
d = dias[7]
print(f'Llave 1 (con []): {l}')
print(f'Llave 7 (con []): {d}')
print(f'Llave 5 (con get()): {dias.get(5)}')
print(f'Llave 7 (con get()): {dias.get(7)}')

print('\nDiccionario final:')
print(dias)