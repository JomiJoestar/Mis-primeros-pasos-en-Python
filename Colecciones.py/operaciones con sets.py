

# Los sets permiten operaciones de union, interseccion y diferencia de conjuntos

print('... Operaciones con Sets o Conjuntos ...')

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a | b
print(f' Union a | b: {union}')

interseccion = a & b
print(f'Intersecion de a & b: {interseccion}')

diferencia = a - b # le estamos quitando los elementos que se repiten en el segundo conjunto.
print(f'La diferencia de los conjuntos a - b: {diferencia}')

 