## p156-empleado1
## Modelamos un empleado usando una clase

class Empleado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}'
    
## Porgrama principal
print("\033[H\033[J")
## Instanciamos la clase 
empleado1 = Empleado('Jose Diaz',35)
print(f'Nombre: {empleado1.nombre}')
print(f'Edad: {empleado1.edad}')
print(empleado1)

empleado2 = Empleado('Rocio Soto',34)
print(empleado2)