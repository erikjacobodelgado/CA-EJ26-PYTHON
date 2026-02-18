## p036-numeros-consecutivos.py
## Escribe un programa que reciba tres números enteros y determine si son consecutivos. Si lo son, muestra un mensaje de confirmación; de lo contrario, informa que no lo son.

print("\033[H\033[J")

print('Programa para determinar si los numeros ingresados son consecutivos o no')
print('Dame tres numeros enteros separados por espacio')
n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if n3 - n2 == 1 and n2 - n1 == 1 or n2 - n1 == -1:
    print('Los numeros son consecutivos')
else:
    print('Los numeros no son consecutivos')

print('\nProceso finalizado')