## p101-mes-día-nombre.py
## Asociar un numero del 1 al 12 con su respectivo mes 

print("\033[H\033[J")
print('Asociar un numero del 1 al 12 con su respectivo mes')

mes = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

num = int(input('Introduzca numero del mes: '))
if num <= 12 and num >= 1:
    print(f'Mes: {mes[num-1]}\nDías: {dias[num-1]}')
else: 
    print('Entrada incorrecta')