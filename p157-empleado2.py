## p157-empleado2.py
## Modelamos un empleado usando una clase, agregamos mas atributos

class Empleado:
    def __init__(self, nombre, edad, sexo, casado):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.casado = casado

    def __str__(self):
        return f'Nombre: {self.nombre}\nEdad: {self.edad}\nSexo: {'Mujer' if self.sexo == 'M' else 'Hombre'}\nCasado: {'Casado' if self.casado else 'Soltero'} \n'
    
##  Programa principal 
print("\033[H\033[J")
## Instanciamos la clase 
empleado1 = Empleado('Juan Diaz', 35, 'H', True)
print(empleado1)

print(f'\nNombre: {empleado1.nombre}')    
print(f'Edad: {empleado1.edad}')    
print(f'Sexo: {empleado1.sexo}')    
print(f'Casado: {empleado1.casado}')

empleado2 = Empleado('Rocio Soto', 45, 'M', False)
print(f'\nNombre: {empleado2.nombre}')    
print(f'Edad: {empleado2.edad}')    
print(f'Sexo: {empleado2.sexo}')    
print(f'Casado: {empleado2.casado}')

empleado3 = Empleado('Pedro Torres', 45, 'H', False)
print(f'\nNombre: {empleado3.nombre}')    
print(f'Edad: {empleado3.edad}')    
print(f'Sexo: {empleado3.sexo}')    
print(f'Casado: {empleado3.casado}')

suma_edades = empleado1.edad + empleado2.edad + empleado3.edad
promedio_edades = suma_edades / 3 
print(f'\nPromedio edad: {promedio_edades:.2f}')