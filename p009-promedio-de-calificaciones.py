## p009-promedio-de-calificaciones
## Calcula el promedio de tres calificaciones ingresadas por el usuario

## Entrada
print('Dame tres calificaciones separadas por espacio: ')
cal1, cal2, cal3 = input().split()
cal1, cal2, cal3 = int(cal1), int(cal2), int(cal3)

## Calcular promedio
promedio = (cal1 + cal2 + cal3) / 3

##Mostrar resultado
print(f'La calificaciones fueron: {cal1}, {cal2}, {cal3}')
print(f'El promedio es: {promedio}')
