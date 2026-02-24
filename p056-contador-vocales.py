## p056-contador-vocales.py
## Contar el numero de vocales y consonantes en una frase

print("\033[H\033[J")

print('Cuenta de vocales y consonantes')

frase = input('Introduce la frase: ').lower() ## .lower() convierte a minusculas
v = c = o = 0
indice = 0
while indice < len(frase): ##len(variable) cuenta la longitud de la variable 
    print(frase[indice]) ## separa la frase en sus componentes 
    caracter = frase[indice]
    if 'a' <= caracter <= 'z':
        if caracter in 'aeiou':
            v = v + 1
        else:
            c = c + 1
    else:
        o = o + 1 

    indice += 1 ## += es contador

print(f'\nAnalisis de la frase: {len(frase)} - {frase}')
print(f'Vocales: {v}')
print(f'Consonantes: {c}')
print(f'Otros: {o}')