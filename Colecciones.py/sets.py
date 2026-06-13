



# SETS O CONJUNTOS
# Son colecciones de datos no ordenados de elementos unicos. Es muy util para identificar que no haya elementos duplicados

# No hay orden de almacenamiento de estos datos.

# En los conjuntos no se aplica el concepto de indice, ya que no se posee un orden. A la hora de remover elementos, solo se ocupa escribir el elemento.


# EJEMPLO DE SETS

set_a = {1, 2, 3, 4, 5, 6}
set_b = {3, 'Juan', True, 6.5}
numeros = {1, 2, 2, 3, 3, 4, 5, 6}

print(f'Conjunto de numeros: {numeros}, conjunto set_b: {set_b}, conjunto set_a: {set_a}')

print('*** Manejo de Sets o conjuntos ***')

# Crear un conjunto
mi_set = {1, 2, 3, 4, 5, 4}

print(f'Mi set: {mi_set}')
mi_set.add(6)
mi_set.add(7)


# Intentando agregar un elemento duplicado
mi_set.add(3)


# Eliminar un elemento del conjunto
mi_set.remove(4)

print(f'Mi set modificado: {mi_set}')


# Iterar los elementos del set
for elemento in mi_set:
    print(elemento, end=' ')


# Comprobar si existe un elemento en el set
print(f'\nExiste el valor de 4 en el set? {1 in mi_set}')

# Obtener la longitud del set
print(f'Longitud del conjunto: {len(mi_set)}')


































