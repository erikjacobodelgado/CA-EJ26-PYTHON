## p019-calculo-tiempo.py
## Programa para calcular los equivalentes de horas a dias, minutos y segundos

print("\033[H\033[J")

print('Dame el numero de horas: ')
horas = int(input())

dias = float(horas / 24)
minutos = int(horas * 60)
segundos = int(minutos * 60) 

print(f'Las {horas} horas son equivalentes a: \n {dias:.2f} dias \n {minutos} minutos \n {segundos} \n ')
