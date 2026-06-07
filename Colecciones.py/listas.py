


# Listas en Python: Las listas son colecciones ordenadas y mutables de elementos que pueden ser diferentes... Las listas son dinamicas, las podemos cambiar de tamaño, añadir, modificar o eliminar elementos.

mi_lista = [1,2,3,4,5,6]

# Su estructura es con corchetes.

numeros = ['Manzana', 'Banana', 'Cereza']

# Tambien puede ser mixta

mixta = ['Mapa: Bind', 1, [0, 5], 2.5]

print('Manejo de Listas')
mi_lista = [1, 2, 3, 4, 5, 6]

# Probando con la lista
print(f'Largo de la lista con len {len(mi_lista)}')

# Acceder a los elementos por indica
print(f'Accedemos al valor almacenado en el indice 4: {mi_lista[4]}')
print(f'Accedemos al ultimo valor almacenado en el indice de la lista, usando un indice negativo: {mi_lista[-1]}')

# Para modificar los elementos de una lista
mi_lista[1] = 10
print(f'Modificamos el valor del indice 1: {mi_lista[1]}')

# Agregar unnuevo elemento al final de la lista
mi_lista.append(7)
print(f'{mi_lista} -> se agrego el elemento 7')

# Añadir un nuevo elemento en un indice especifico con insert, su funcion es INSERTAR, los demas elementos se corren una casilla para que este entre
mi_lista.insert(2, 15)
print(f'{mi_lista} -> Se añadio el elemento 15 en el indice 2')

# Eliminar elementos de una lista por su nombre
# Usando el metodo remove

mi_lista.remove(6)
print(f'{mi_lista} -> Se removio el elemento 6')

# Removemos por indice por el metodo pop, la diferencia es que, con el metodo pop se eliminan los elementos por indice

mi_lista.pop(0) # Remueve el elemento del indice 0 
print(f'{mi_lista} -> Se elimino el indice 0, es decir el 1') #Al eliminar un elemento las casillas vuelven, es decir recorren una casilla a la izquierda

del mi_lista(2)
print(f'{mi_lista} -> se elimino el indice 2')

# Obtener sublistas
sublista = mi_lista[1:3] #genera una sublista del indice 1 y 2 (3 no se incluye)
print(f'{sublista}') #toma los indices como el rango y genera la sublista






