## p031-2da-ley-newton.py
## Calcula la fuerza, masa o aceleracion segun la segunda ley de Newton

print("\033[H\033[J")

print('Programa para calcular la fuerza, masa o aceleracion mediante la segunda ley de Newton')
print('[ F ] Fuerza      f = m * a')
print('[ M ] Masa        m = f / a')
print('[ A ] Aceleracion a = f * m')
op = input('Que opcion quieres?: ').upper()

if op == 'F':
    print('Calculando la fuerza')
    m = float(input('Dame la masa: '))
    a = float(input('Dame la aceleracion: '))
    f = m * a 
    print(f'La fuerza es igual a {f:.2f}')
elif op == 'M':
    print('Calculando la masa')
    f = float(input('Dame la fuerza: '))
    a = float(input('Dame la aceleracion: '))
    m = f / a 
    print(f'La masa es igual a {m:.2f}')
elif op == 'A':
    print('Calculando la aceleracion')
    m = float(input('Dame la masa: '))
    f = float(input('Dame la fuerza: '))
    a = f * m
    print(f'La aceleracion es igual a {a:.2f}')
else:
    print('\nOpcion invalida')
    
print('\nProceso terminado')