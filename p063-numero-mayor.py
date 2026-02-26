## p063-numero-mayor.py
## Leer una serie de numeros hasta que el usuario ingrese un 0.
## Al terminar, el programa debera costrar cual fue el numero mas grande de todos los introducidos

while True:
    print("\033[H\033[J")

    num = int(input('Introduce numeros (0 para terminar): '))

    if num == 0:
        print('Proceso terminado')

    else:
        nm = num
        while True:
            num = int(input('Introduce numeros (0 para terminar): '))
            if num == 0: break
            
            if num > nm:
                nm = num 
                
        print(f'El numero mayor fue: {nm}')
        
    if input('\nDeseas continuar (S/N)?: ').upper() == 'N': break

print('Proceso terminado')