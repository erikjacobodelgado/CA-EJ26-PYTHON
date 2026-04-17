## p122-operaciones-conjuntos.py
## Operaciones entre conjuntos numericos 

print("\033[H\033[J")

c1 = {1, 2, 3, 4, 5}
c2 = {5, 6, 7, 8, 9, 10}
c3 = {9, 10, 11, 12, 13}
c4 = {3, 4, 5}

print("Conjuntos Base")
print(f"c1: {c1}\nc2: {c2}\nc3: {c3}\nc4: {c4}")

print('\nUnion ( | )')
print(f'c1 union c2: {c1.union(c2)}')
print(f'c1 union c3: {c1|c3}')

print('\nIntersección ( & )')
print(f'c1 interseccion c2: {c1.intersection(c2)}')
print(f'c2 interseccion c3: {c2&c3}')

print('\nDiferencia ( - )')
print(f'c1 diferencia c4: {c1.difference(c4)}')
print(f'c2 diferencia c3: {c2-c3}')

print('\nDiferencia simetrica ( ^ )')
print(f'c1 dif simetrica c2: {c1.symmetric_difference(c2)}')
print(f'c2 dif simetrica c3: {c2^c3}')

print('\nSuperconjuntos')
print(f'c1 es superconjunto c4: {c1.issuperset(c4)}')
print(f'c2 es superconjunto c3: {c2>=c3}')

print('\nSubconjuntos')
print(f'c3 es subconjunto del c1: {c4.issubset(c1)}')
print(f'c3 es subconjunto del c2: {c3<=c2}')

print('\nPertenencia')
print(f'Esta 2 en c1: {2 in c1}')
print(f'6 no esta en c1: {6 not in c1}')