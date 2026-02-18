## p040-calculo-notas.py
## Escribe un programa que calcule el promedio de 5 calificaciones ingresadas por el usuario. Basado en el promedio, el programa deberá mostrar uno de los siguientes mensajes:
## • Menor a 6: "Quedas reprobado"
## • Desde 6 hasta menos de 7: "Pasas de panzazo"
## • Desde 7 hasta menos de 8: "Muy bien, puedes mejorar"
## • Desde 8 hasta menos de 9: "Excelente, sigue así"
## • Desde 9 hasta 10: "Perfecto, tu esfuerzo valió la pena"

print("\033[H\033[J")

print('Dame tus cinco calificaciones separadas por espacio')

cal1, cal2, cal3, cal4, cal5 = input().split()
cal1, cal2, cal3, cal4, cal5 = int(cal1), int(cal2), int(cal3), int(cal4), int(cal5)
prom = (cal1+cal2+cal3+cal4+cal5) / 5

if cal1 <= 10 and cal1 >= 0 and cal2 <= 10 and cal2 >= 0 and cal3 <= 10 and cal3 >= 0 and cal4 <= 10 and cal4 >= 0 and cal5 <= 10 and cal5 >= 0:
    if prom < 6:
        print(f'Promedio: {prom:.2f}, Quedas reprobado')
    elif prom >= 6 and prom < 7:
        print(f'Promedio: {prom:.2f}, Pasas de panzaso')
    elif prom >= 7 and prom < 8:
        print(f'Promedio: {prom:.2f}, Muy bien, puedes mejorar')
    elif prom >= 8 and prom < 9:
        print(f'Promedio: {prom:.2f}, Excelente, sigue asi')
    elif prom >= 9 and prom <= 10:
        print(f'Promedio: {prom:.2f}, Perfecto, tu esfuerzo valio la pena')
else: 
    print('Una de las calificaciones no es valida')

print('\nProceso finalizado')