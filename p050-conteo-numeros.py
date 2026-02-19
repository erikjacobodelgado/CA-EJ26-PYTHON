## p050-conteo-numeros.py
## Lee y cuenta numeros hasta que el usuario introduzca 999

print("\033[H\033[J")

print('Lee y cuenta numeros hasta que el usuario introduzca 999')

s = c = cp = cn = cz = 0

while True: ## El ciclo se ejecutara mientras la condicion sea verdadera 
    num = int(input('Numero?: '))
    if num == 999: 
        break
    c += 1
    s += num 
    if num > 0 : 
        cp += 1 ## += funciona como contador cp += 1 es lo mismo que cp = cp + 1
    elif num < 0 : 
        cn += 1
    else: 
        cz += 1

print('\nReporte final')
print(f'Fueron {c} numeros que sumados dan {s}')
print(f'Positivos: {cp}')
print(f'Negativos: {cn}')
print(f'Ceros: {cz}')