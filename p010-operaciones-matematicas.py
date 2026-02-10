## p010-operaciones-matematicas
## Demuestra el uso de los diferentes operadores aritmeticos

print("\033[H\033[J") ## Imprime una secuencia ansi que borra la pantalla

print('=' * 50)
print('Calculadora de operaciones matematicas')
print('=' * 50)

x = float(input('Dame el valor de x: '))
y = float(input('Dame el valor de y: '))

print(f'Los valores de x y y son: {x} y {y}')
print('-' * 40)

## Mostrar las operaciones directamente con datos alineados 
print(f'Suma:            {x:>6} + {y:>6} = {x+y:>6.2f}') ## >6 recorre 6 posiciones a la derecha, .2f muestra dos decimales unicamente
print(f'Resta:           {x} - {y} = {x-y}')
print(f'Multiplicacion:  {x} * {y} = {x*y}')
print(f'Division:        {x} / {y} = {x/y}')
print(f'Modulo:          {x} % {y} = {x%y}')
print(f'Exponenciacion:  {x} ^ {y} = {x**y}')
print(f'Division entera: {x} // {y} = {x//y}')