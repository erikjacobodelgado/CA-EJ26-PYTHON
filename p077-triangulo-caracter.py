## p077-triangulo-caracter.py
## Crear un triangulo rectangulo de n renglones de un caracter ingresado por el usuario 

print("\033[H\033[J")
print('Crear un triangulo rectangulo de n renglones de un caracter ingresado por el usuario ')

n = int(input('Renglones: '))
car = input('Caracter: ')

for i in range(1,n+1):
    for j in range(i): ## Va aumentando conforme a la variable i que llega hasta n+1 
        print(car, end='')
    print()