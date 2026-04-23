## p135-numero-mayor.py
## Funcion que recibe 3 numeros y me dice el mayor

print("\033[H\033[J")

def mayor(n1:int, n2:int, n3:int)->int:
    if n1 > n2 and n1 > n3:
        m = n1
    elif n2 > n1 and n2 > n3:
        m = n2
    elif n3 > n1 and n3 > n2:
        m = n3 
        return m
    
print('Dame los tres valores ')
a,b,c = int(input()), int(input()), int(input())
print(f'El mayor es: {mayor(a,b,c)}')

print(f'\nEl mayor de 100, 200, 300: {mayor(100,200,300)}')
