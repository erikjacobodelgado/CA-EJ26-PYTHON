## p137-temperatura.py
## Dos funciones para calcular temperatura 

## c a f
def caf(c:float)->float:
    return (c*9/5)+32

## de f a c
def fac(f:float)->float:
    return (f-32)*5/9

def main()->None:
    print('Conversion de temperatura')
    print('1 de c a f')
    print('2 de f a c')
    op = int(input('Elige: '))
    if op == 1:
        print('Dame la temperatura en c')
        c = float(input())
        f = caf(c)
        print(f'{c} C = {f} F')

    elif op == 2:
        print('Dame la temperatura en F')
        f = float(input())
        c = fac(f)
        print(f'{f} F = {c} C')

if __name__ == '__main__':
    print("\033[H\033[J")
    main()