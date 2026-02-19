## p047-conteo-descendente.py
## Imprime numeros de n a 1 con ciclo while de manera descendente

print("\033[H\033[J")

print('Numeros de n a 1 con while de manera descedente ')

n = int(input('Desde donde?: '))
m = int(input('A que paso?: '))
r = n

while r >= 1:
    print(r)
    r = r - m

print('\Ciclo terminado')