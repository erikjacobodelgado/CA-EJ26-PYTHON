## p149–numero-menor.py
## Funcion para enviar el menor de tres numeros ingresados por el usuario

print("\033[H\033[J")

def menor(n1:int, n2:int, n3:int)->int:
    if n1 < n2 and n1 < n3:
        m = n1
    elif n2 < n1 and n2 < n3:
        m = n2
    elif n3 < n1 and n3 < n2:
        m = n3 
    return m
    
a = int(input('Introduce el primer numero: '))
b = int(input('Introduce el segundo numero: '))
c = int(input('Introduce el tercer numero: '))
print(f'El numeor menor es: {menor(a,b,c)}')