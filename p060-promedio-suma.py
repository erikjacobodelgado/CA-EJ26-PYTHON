## p060-promedio-suma.py
## Leer numeros introducidos por el usuario hasta que ingrese un cero.
## Al finalizar, mostrar el conteo total de numeros, la suma y el promedio de la serie

while True:
    print("\033[H\033[J")
    con = 0
    suma = 0
    while True:  
        num = int(input('Introduce numeros (0 para terminar)'))
        suma = suma + num
        con = con + 1
        if num == 0: break

    print(f'Se introdujeron {con-1} numeros')
    print(f'La suma es: {suma}')
    prom = (suma)/(con-1)
    print(f'El promedio es: {prom}')

    if input('\nDeseas continuar (S/N)?: ').upper() == 'N': break

print('Proceso terminado')