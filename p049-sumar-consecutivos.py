## p049-sumar-consecutivos.py
## Suma numeros hasta un total de 5000, pero cuenta hasta 200

print("\033[H\033[J")

print('Cuantos boletos tengo que vender para juntar una cantidad de dinero? ')
n = int(input('Cuanto quieres recaudar?: '))

boleto = 0
dinero = 0

while boleto < 200:
    boleto = boleto + 1 
    dinero = dinero + boleto 
    print(boleto, end = ' ')

    if dinero >= n:
        print('\nDinero completado')
        break ## detiene el ciclo una vez que la condicion fue cumplida

if dinero < n:
    print(f'\n200 boletos no fueron suficientes para juntar {n} pesos')
else:
    print(f'\nUse {boleto} boletos para llegar a {dinero} pesos')