## p129-func-param-nombre.py
## Funcion que es invocada con el nombre de los parametros

print("\033[H\033[J")

def saluda(apaterno:str, amaterno:str, nombre:str)->None:
    print(f'Hola {nombre} {apaterno} {amaterno}')

saluda('Jacobo', 'Delgado', 'Erik') ## Normal, en el orden de arriba

saluda(nombre='Erik', apaterno='Jacobo', amaterno='Delgado') ## Llamando por nombre
saluda(amaterno='Delgado', nombre='Erik', apaterno='Jacobo')
