## p098-producto-punto.py
## Calculo del producto punto de dos vectores

vector_a = [1,3,-5]
vector_b = [4,-2,-1]
pro_pun = 0

print("\033[H\033[J")
print('Calculo del producto punto de dos vectores de la misma longitud\n')

print(f'Vector A: {vector_a}')
print(f'Vector B: {vector_b}')

if len(vector_a) == len(vector_b):
    for i in range(len(vector_a)):
        pro_pun += vector_a[i] * vector_b[i]
    print(f'Producto punto: {pro_pun}')
else:
    print('Error: Los vectores deben tener la misma longitud')