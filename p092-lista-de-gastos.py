## p092-lista-de-gastos.py
## Gestionar una lista de gastos mensuales 

print("\033[H\033[J")
print('Gestionar una lista de gastos mensuales')

gastos = [100, 400, 500, 200, 55]
limite = 200

while True:
    print('Selecciona una opción')
    print('1. Mostrar gastos actuales')
    print('2. Agregar nuevo gasto')
    print('3. Modificar gasto existente')
    print('4. Eliminar gasto')
    print('5. Mostrar total de gastos')
    print('6. Salir')
    opc = int(input('\nIntroduce la opción deseada: '))

    if opc == 1:
        print('Gastos actuales')
        print(gastos)

    elif opc == 2:
        print('Agregar nuevo gasto')
        nuevo = int(input('Introduce el nuevo gasto: '))
        gastos.append(nuevo)
        print('Lista actualizada:')
        print(gastos)
    
    elif opc == 3:
        print('Modificar gasto existente')
        pos = int(input('Ingresa la posicion del gasto a modificar: '))
        nuevo = int(input('Introduce el nuevo gasto: '))
        gastos [pos-1] = nuevo 
        print('Lista actualizada:')
        print(gastos)

    elif opc == 4:
        print('Eliminar gasto')
        pos = int(input('Ingresa la posicion del gasto a eliminar: '))
        gastos.pop(pos-1)
        print('Lista actualizada:')
        print(gastos)

    elif opc == 5:
        total = sum(gastos)
        print(f'Total de gastos: {total}')

    elif opc == 6:
        print('Gracias')

    else:
        print('Opción invalida')

    break