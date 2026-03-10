## p079-factorial-numeros.py
## Calcular el factorial de los numeros hasta un numero que ingrese el usuario

print("\033[H\033[J")
print('Calculadora de factoriales')

n = int(input('Hasta que numero?: '))

for i in range(1,n+1):
    f = 1
    m = ''

    for j in range(1,i+1):
        m = m + str(j) 
        m += '*' if i != j else '' ## if de corto circuito
        f = f * j ## Calculo de factorial 

    print(f'{j}!= {m} = {f}')

