## p081-suma-potencias.py
## Calcula el resultado de la potencia ingresada de un numero ingresado 

print("\033[H\033[J")
print('Calcula el resultado de la potencia (n) ingresada de un numero ingresado (X)')

x = int(input('X: '))
n = int(input('n: '))

print(f'\nCalculando el resultado de {x}^{n}:')
suma = 0

for i in range(1,n+1):
    ta = 1 ## primer potencia a la que se eleva
    for j in range(i): ## este for multiplica el numero por las veces que la potencia indica 
        ta = ta * x
    print(f' {x}^{i} ', end='')
    print('+' if i!=n else '', end='')

    suma = suma + ta

print(f'= {suma}')
