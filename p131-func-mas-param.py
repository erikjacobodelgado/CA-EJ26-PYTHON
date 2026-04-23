## p131-func-mas-param.py
## Funcion con n parametros 

print("\033[H\033[J")

def saluda_todos(*todos:str)->None:
    for nombre in todos:
        print(f'Hola {nombre}')
    print()

saluda_todos('Erik')
saluda_todos('Erik', 'Alberto')
saluda_todos('Erik', 'Alberto', 'Jacobo')