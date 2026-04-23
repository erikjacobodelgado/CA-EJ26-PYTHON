## p138-suma-digitos.py
## suma digitos

def sumad(n:int) -> int:
    s = 0
    while n != 0:
        d = n % 10
        s = s + d
        n = n // 10
    return s

def main() -> None:
    n = int(input('Dame un numero: '))
    r = sumad(n) 
    print(f'La suma de los digitos de {n} es: {r}')

if __name__ == '__main__':
    print("\033[H\033[J")
    main()