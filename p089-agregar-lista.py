## p089-agregar-lista.py
## Agregar elemetnos a una lista

print("\033[H\033[J")
print('Agregar elementos a una lista')

numeros = [10,20,30,40]
print(f'Datos iniciales: {len(numeros)} - {numeros}') ## len cuenta los elementos 

print(f'\nAgregar con append 90 y 100')
numeros.append(90) ## append agrega de uno por uno
numeros.append(100)
print(f'Datos: {len(numeros)} - {numeros}')

print(f'\Insertar 80 en 4ta posicion')
numeros.insert(3,80) ## insert inserta en una posicion especifica, n-1 por el 0
print(f'Datos: {len(numeros)} - {numeros}')

print('\Extender la lista con 110, 120, 130')
numeros.extend([110,120,130]) ## extend agrega de varios 
print(f'Datos: {len(numeros)} - {numeros}')