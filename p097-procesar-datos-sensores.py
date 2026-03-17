## p097-procesar-datos-sensores.py
## Simulación de proceso de datos de sensores 

import random

print("\033[H\033[J")
print('Simulación de proceso de datos de sensores \n')

MAX = 10

sensorA = []
sensorB = []
todos = []

for _ in range(MAX):
    sensorA.append(random.randint(1,10))
    sensorB.append(random.randint(1,10))

print('\nLECTURAS DE LOS SENSORES')
print(f'Sensor A: {sensorA}')
print(f'Sensor B: {sensorB}')

for i in range(MAX):
    sensorA[i] = sensorA[i] ** 2
    sensorB[i] = sensorB[i] ** 2
    todos.append(sensorA[i] + sensorB[i])

print('\nLECTURAS DE LOS SENSORES')
print(f'Sensor A: {sensorA}')
print(f'Sensor B: {sensorB}')
print(f'Todos: {todos}')
