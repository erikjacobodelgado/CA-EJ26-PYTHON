## p127-funcion-parametro.py
## Funcion que recibe un parametro 

print("\033[H\033[J")

def saluda(nombre: str) -> None: 
    print(f'Hola {nombre}, bienvenido tu nombre tiene {len(nombre)} caracteres\n')

saluda('Erik')
saluda('Alberto')
saluda('Jacobo')