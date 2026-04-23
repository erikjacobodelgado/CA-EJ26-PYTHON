## p140-promedio-letra.py
## recibe un promedio y regresa una letra y un mensaje 

def caletra(p:float) -> tuple[str, str]:
    l = '';m=''
    if 90 <= p <= 100: l='A';m='Excelente'
    elif 80 <= p < 90: l='B';m='Bien'
    elif 70 <= p < 80: l='C';m='Suficiente'
    elif 60 <= p < 70: l='D';m='Deficiente'
    elif 0 <= p < 60: l='E';m='Malo'
    else: l='X';m='Calificacion invalida'
    return l, m 

def main() -> None:
    p = float(input('Promedio: '))
    l, m = caletra(p)
    if m:
        print(f'Promedio {p}: {l} - {m}')
    else:
        print(l)
if __name__ == '__main__':
    print("\033[H\033[J")
    main()