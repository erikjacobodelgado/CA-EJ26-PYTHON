## p025-verificar-suma.py
## Dados tres numeros verifica si la suma de los dos primeros es igual al tercero

print("\033[H\033[J")

print('Verificador de suma: Es la suma de los dos primeros igual al tercero? ')

n1 = int(input('Dame el primer numero: '))
n2 = int(input('Dame el segundo numero: '))
n3 = int(input('Dame el tercer numero: '))

suma = n1 + n2 

if suma == n3:
    print(f'✅ La suma de {n1} + {n2} = {n3}')
else:
    print(f'❌ La suma de {n1} + {n2} != {n3} ')

print('-' * 60)
print('\nPrograma terminado')