## p159-rectangulo.py
## Modela un rectangulo 

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    def obtenerarea(self):
        return self.largo * self.ancho
    def obtenerperimetro(self):
        return 2 * self.largo * self.ancho 
    def __str__(self):
        return f'Rectangulo: \nLargo {self.largo}\nAncho: {self.ancho}\nArea: {self.obtenerarea():.2f}\nPerimetro: {self.obtenerperimetro():.2f}'
    
print("\033[H\033[J")

r1 = Rectangulo(12,3.4)
print()
print(r1)

r2 = Rectangulo(5.6,7.8)
print()
print(r2)

r3 = Rectangulo(10,20)
print()
print(r3)

print(f'\nPromedio de areas: {(r1.obtenerarea() + r2.obtenerarea() + r3.obtenerarea()) / 3:.2f}')