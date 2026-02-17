## p034-tipo-angulo.py
## Programa para identificar que tipo de angulo es un angulo dado por el usuario

print("\033[H\033[J")

print('Aqui te decimos el tipo de angulo')

angulo = int(input('Dame el angulo en grados: '))

if angulo >= 0 and angulo <= 360:
    if angulo < 90:
        print('Angulo agudo')
    elif angulo == 90:
        print('Angulo recto')
    elif angulo < 180:
        print('Angulo obtuso')
    elif angulo == 180:
        print('Angulo llano')
    elif angulo < 360:
        print('Angulo concavo')
    else:
        print('Angulo completo')
else:
    print('Los angulos en grados se miden de 0 a 360 grados tonto')    

print('\nProceso finalizado ')