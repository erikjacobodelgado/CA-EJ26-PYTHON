## p086-triangulo-invertido-numeros.py
## Triangulo invertido de 1 a n 

print("\033[H\033[J")
print('Triangulo invertido de 1 a n')

n = int(input('Qué número?: '))
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end='')
    print()