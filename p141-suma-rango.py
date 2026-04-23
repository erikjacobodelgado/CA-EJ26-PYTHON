## p141-suma-rango.py
## suma un rango de valores

def sumarango(i:int, f:int) -> int:
    s = 0
    for n in range (i, f+1):
        s = s + n
    return s
    
def main() -> None:
    i = int(input('Inicio: '))
    f = int(input('Final: '))
    r = sumarango(i, f)
    print(f'La suma de valores desde {i} hasta {f} es: {r}')

if __name__ == '__main__':
    print("\033[H\033[J")
    main()