## p151–medidas-longitud.py
## Conversor de longitud mediante dos funciones diferentes 

def pul_a_cm(pul:float)->float:
    return pul*2.54

def m_a_ft(m:float)->float:
    return m*3.28

def main()->None:
    print('Conversor de unidades')
    print('1. Pulgadas a centimetros')
    print('2. Metros a pies')
    print('3. Salir')
    opc = int(input('Elige una opcion: '))

    if opc == 1:
        print('Introduce la cantidad en pulgadas: ')
        pul = float(input())
        cm = pul_a_cm(pul)
        print(f'{pul} pulgadas equivalen a {cm} centimetros')

    elif opc == 2:
        print('Introduce la cantidad en metros: ')
        m = float(input())
        ft = m * 3.28
        print(f'{m} metros es equivalente a {ft} pies')

    else:
        print('Fin del proceso')

if __name__ == '__main__':
    print("\033[H\033[J")
    main()