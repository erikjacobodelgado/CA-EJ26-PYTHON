## p027-calcular-paga-extra-v2.py
## Calcula la paga de un trabajador considerando horas extras 

print("\033[H\033[J")

print('Calculando la paga de un trabajador considerando las horas extras (se pagan al doble) \n')

print('Dame los datos del trabajador')
nom = input('Nombre: ')
horas = int(input('Horas trabajadas: '))
paga_hora = float(input('Paga por hora: '))

if horas < 40:
    horas_normales = horas 
else: 
    horas_normales = 40 
    
pago_normal = horas_normales * paga_hora 

horas_extra = paga_extra = 0
if horas > 40:
    horas_extra = horas - 40 
    paga_extra = horas_extra * (paga_hora * 2)
    pago_total = pago_normal + paga_extra 
else:
    pago_total = pago_normal

print('Calculo completado')
print(f'El trabajador {nom} trabajo {horas} horas con una paga de {paga_hora} por hora')
print(f'Trabajo {horas_extra} horas extras y recibio un pago de {paga_extra} por esas horas')
print(f'Paga normal = {pago_normal:.2f}')
print(f'Paga extra = {paga_extra:.2f}')
print(f'Pago total = {pago_total:.2f}')