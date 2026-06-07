

print('PLAYLIST')
#Creamos una lista vacia
playlist = []

numero_canciones = []

#Iteramos cada elemento de la lista para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f'Proporciona la canciones {indice + 1}: ')
    playlist.append(cancion)



# Ordenar lista en orden alfabetico
playlist.sort()

# Mostar lista de canciones
print(f'\n Lista de Reproduccion en orden alfabetico')
print(playlist)

# Mostrar la lista iterando sus elementos 
print('Iteramos la playlist')
for cancion in playlist:
    print(f'\n - {cancion}')