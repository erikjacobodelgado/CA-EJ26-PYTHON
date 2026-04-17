## p120-contar-caracteres.py
## Contador de caracteres de una cadena ingresada por el usuario mediante diccionarios 

print("\033[H\033[J")

cadena = input('Ingrese una cadena: ')

caracteres = {}
for c in cadena:
    if c in caracteres:
        caracteres[c] += 1
    else:
        caracteres[c] = 1

print('Resultado')
print(caracteres)