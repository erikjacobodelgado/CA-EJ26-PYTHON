## p160-ventas.py
## Simular un sistema de control de ventas 

class Venta:
    def __init__(self, articulo, cantidad, precio):
        self.articulo = articulo
        self.cantidad = cantidad 
        self.precio = precio 
        self.total = self.cantidad * self.precio

    def __str__(self):
        return f'Articulo: {self.articulo:<15} Cantidad: {self.cantidad:<10.2f} Precio: {self.precio:<10.2f} Total: {self.total:<10.2f}'
    

class Cliente:
    def __init__(self, rfc, nombre, domicilio, correo):
        self.rfc = rfc
        self.nombre = nombre
        self.domicilio = domicilio
        self.correo = correo
        self.ventas = list()
    
    def agregarventa(self, venta):
        self.ventas.append(venta)

    def totalventas(self):
        total = 0
        for venta in self.ventas:
            total += venta.total 
        return total 
    
    def __str__(self):
        return f'Cliente: [Nombre:{self.nombre:<15} RFC:{self.rfc:<12} Domicilio:{self.domicilio:<20} Correo:{self.correo:<20}]'
    
class Tienda:
    def __init__(self, nombre, domicilio, propietario):
        self.nombre = nombre 
        self.domicilio = domicilio 
        self.propietario = propietario 
        self.clientes = list()
    
    def agregarcliente(self, cliente):
        self.clientes.append(cliente)

    def totalgeneral(self):
        total = 0
        for cliente in self.clientes:
            total += cliente.totalventas()
        return total
    
    def __str__(self):
        return f'Tienda [Nombre:{self.nombre}, Domicilio:{self.domicilio}, Prpietario:{self.propietario}]'


## Programa principal todo junto 
print("\033[H\033[J")

mitienda = Tienda('Ferreteria Don Pepe','Av Jerez 102','Don Jose')
mitienda.agregarcliente(Cliente('abcd1234','Carlos','Av Mexico 113','abc@gmail.com'))
mitienda.agregarcliente(Cliente('xyz789','Juan','Av España 200','xyz@gmail.com'))
mitienda.clientes[0].agregarventa(Venta('Martillo',10,100))
mitienda.clientes[0].agregarventa(Venta('Pala',12,150))
mitienda.clientes[1].agregarventa(Venta('Clavo',200,2))
mitienda.clientes[1].agregarventa(Venta('Cinta',3,60))

print(f'\nReporte de ventas: {mitienda}\n')
print('\nClientes:')
for cliente in mitienda.clientes:
    print(cliente)

print('\Ventas de cada cliente:')
for cliente in mitienda.clientes:
    print(f'\n{cliente.rfc} - {cliente.nombre} - {cliente.totalventas():,.2f}')
    for venta in cliente.ventas:
        print(f'\n{venta}')
    print(f'\nTotal ventas general: {mitienda.totalgeneral():,.2f}')




"""## Programa principal
print("\033[H\033[J")
v1 = Venta('Martillo',10,100)
v2 = Venta('Pala',5,200)
v3 = Venta('Cinta de medir',1,400)

c1 = Cliente('abcd1234','Carlos','Av Mexico 113','abc@gmail.com')
c1.agregarventa(v1)
c1.agregarventa(v2)
c1.agregarventa(v3)
print(c1)
print(c1.ventas[0])
print(c1.ventas[1])
print(c1.ventas[2])
print(c1.totalventas())"""
