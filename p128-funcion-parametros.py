## p128-funcion-parametros.py
## Funcion que recibe multiples parametros

print("\033[H\033[J")

def saluda(apaterno:str, nombre:str)->None:
    print(f'Hola {nombre} {apaterno}')

saluda('Jacobo','Erik')
saluda('Delgado','Alberto')