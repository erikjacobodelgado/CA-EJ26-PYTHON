## p062-conversion-temperaturas.py
## El usuario debe introducir una temperatura inicial y una final en grados Celcius.
## El programa mostrará la conversión a grados Fahrenheit para cada grado en ese rango, incrementando de uno en uno

while True:
    print("\033[H\033[J")
    
    ci = int(input('Introduce la temperatura inicial: '))
    cf = int(input('Introduce la temperatura final: '))
    c = ci

    while c <= cf:
        f = (c * 1.8) + 32
        print(f'{c}°C = {f}°F')
        c = c + 1 

    if input('\nDeseas continuar (S/N)?: ').upper() == 'N': break

print('Proceso terminado')