## p111-lote-autos.py
## Conrol de un lote de autos mediante diccionarios 

print("\033[H\033[J")

autos = [
    {'marca':'Ford','modelo':'Mustang','año':1964},
    {'marca':'VW','modelo':'Jetta','año':2005},
]

autos.append({'marca':'Ford','modelo':'Focus','año':2000})

print('='*50)
print('Listado de autos')
print('='*50)

print(f'\nTodos los autos: {autos} - {len(autos)}')

print('\nCada auto dentro de los autos')
for auto in autos:
    print(auto)

print('-'*50)
print('\nDATOS EN FORMATO DE TABLA')
print()
for k in autos[0].keys():
    print(f'{k}\t',end='')
print('')
print()

for auto in autos:
    for v in auto.values():
        print(f'{v}\t',end='')
    print()
print('-'*50)

print('\nDATOS EN FORMATO DE REGISTRO')
print()
for auto in autos:
    for k, v in auto.items():
        print(f'{k:<12} : {v}')
    print()
print('-'*50)