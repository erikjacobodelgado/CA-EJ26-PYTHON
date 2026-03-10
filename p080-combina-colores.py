## p080-combina-colores.py
## Genera todas las posibles combinaciones de colores

print("\033[H\033[J")
print('Genera todas las posibles combinaciones de colores')

colores = input('Ingresa colores separados por coma: ').strip().split(',')
## strip quita los espacios en blanco
## separa en base al caracter entre parentesis

print(f'{len(colores)} - {colores}')
for c1 in colores:
    for c2 in colores:
        if c1 != c2:
            print(f'{c1} - {c2}')