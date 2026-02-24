## p052-tabla-conversion.py
## Mostrar una tabla de conversion de peso a dolar en un rango especifico

tc = 19.70

while True:
    print("\033[H\033[J")
    print('Impresion de una tabla de conversion de pesos a dolares')
    while True:
        pi = int(input('Dame valor inicial: '))
        pf = int(input('Dame valor final: '))
        if pi>0 and pf>0 and pi<pf : break 
        print('*')

    c = pi
    print('-'*30)
    print(f'Peso\t\tDolar') ##\t es un tab 
    print('-'*30)
    while c <= pf:
        print(f'{c:>5} - {c/tc:>15.2f}') ## :>5 y :>15 espacios libres
        c = c + 1
    
    if input('Deseas continuar (S/N)?: ').upper() == 'N' : break

print('Proceso terminado')
