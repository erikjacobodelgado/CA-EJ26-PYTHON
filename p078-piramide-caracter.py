## p078-piramide-caracter.py
## Imprime una piramide de n renglones de un caracter ingresado por el usuario 

print("\033[H\033[J")
print('Imprime una piramide de n renglones de un caracter ingresado por el usuario')

n = int(input('Renglones: '))
c = input('Caracter: ')

for i in range(1,n+1):

    esp = n - i ## Espacios a la izquierda
    cars = 2 * i - 1 ## Caracteres 

    for s in range(esp):
        print(' ', end='')

    for j in range(cars): ## Va aumentando conforme a la variable i que llega hasta n+1 
        print(c, end='')
    print()