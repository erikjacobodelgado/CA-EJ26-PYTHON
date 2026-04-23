## p139-factorial.py
## calcula factorial

def factorial(n:int) -> int:
    if n < 0:
        return -1
    r = 1
    for i in range(2, n+1):
        r = r * i
    return r

def main() -> None:
    n = int(input('Dame un numero: '))
    r = factorial(n)
    if r == -1:
        print('El factorial no esta definido en negativos')
    else:
        print(f'El factorial de {n} es: {r}')

if __name__ == '__main__':
    print("\033[H\033[J")
    main()