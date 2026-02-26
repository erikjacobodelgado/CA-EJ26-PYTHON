## p064-verificar-palindromo.py
## Solicitar al usuario que ingrese un numero entero y determinar si es un palindromo.
## Un numero es palindromo si se lee igual de izquiera a derecha que de derecha a izquierda

while True:
    print("\033[H\033[J")

    num = int(input("Introduce un número para verificar si es palindromo: "))
    no = num
    ni = 0

    while num > 0: 
        dig = num % 10 
        ni = ni * 10 + dig 
        num = num // 10 

    if no == ni:
        print("Si es palíndromo")
    else:
        print("No es palíndromo")
        
    if input('\nDeseas continuar (S/N)?: ').upper() == 'N': break

print('Proceso terminado')