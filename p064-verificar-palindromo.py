## p064-verificar-palindromo.py
## Solicitar al usuario que ingrese un numero entero y determinar si es un palindromo.
## Un numero es palindromo si se lee igual de izquiera a derecha que de derecha a izquierda

while True:
    print("\033[H\033[J")

    num = int(input("Introduce un número para verificar si es palindromo: "))
    no = num
    ni = 0

    while num > 0: ##Ejemplo introduce 121
        dig = num % 10 ## obtiene el ultimo numero 121/10=12 residuo 1, 12%10=2, 1%10=1
        ni = ni * 10 + dig ## 121*10+1=1211, 1211*10+2=12112, 12112*10+1=121121
        num = num // 10 ## elimina el ultimo numero 121/10=12, 12/10=1, 1/10=0 aquí termina el ciclo

    if no == ni:
        print(f"El numero {dig} si es palíndromo")
    else:
        print(f"El numero {dig} no es palíndromo")
        
    if input('\nDeseas continuar (S/N)?: ').upper() == 'N': break

print('Proceso terminado')