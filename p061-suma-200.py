## p061-suma-200.py
## Leer numeros y sumarlos hasta que el total acumulado sea mayor o igual a 200
## Al terminar, mostrar cuantos numeros se introdujeron y la suma final

while True:
    print("\033[H\033[J")
    
    suma = 0
    con = 0

    while True:
        print(f'Suma actual: {suma}')
        num = int(input('Introduce un numero: '))
        suma = suma + num
        con = con + 1
        if suma > 200: break

    print('\nMeta de 200 alcanzada')
    print(f'Suma final: {suma}')
    print(f'Total de numeros introducidos: {con}')

    if input('\nDeseas continuar (S/N)?: ').upper() == 'N': break

print('Proceso terminado')