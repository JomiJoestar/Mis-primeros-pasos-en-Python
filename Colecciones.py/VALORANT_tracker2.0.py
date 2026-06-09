


print('*** Tracker de VALORANT 2.0 ***')

cantidad_partidas = int(input('Cuantas partidas jugaste: '))
eliminaciones = [] # Lista vacia para almacenar los valores

for indice in range(cantidad_partidas): #por cada indice en rango de cantidad partida, recorre la lista...
    cantidad_kills = int(
        input(f'Cuantas kills te hiciste en la partida {indice + 1}: ')) #input con la cantidad de kills realizadas, tambien usamos el +1 para que no parta de 0 en el indice

    eliminaciones.append(cantidad_kills) #usamos el .append para agregar los datos a la lista.

print(f'Kills registradas {eliminaciones}')
# Promedio de kills
promedio = sum(eliminaciones) / cantidad_partidas

print(f'Promedio: {promedio:.2f|}')

top_kills = max(eliminaciones)

print(f'Mayor cantidad de kills {top_kills}')

bot_kills = min(eliminaciones)

print(f'Menor cantidad de kills {bot_kills}')


partidas_destacadas = 0

for kills in eliminaciones:
    if kills >= 15:
        partidas_destacadas += 1

print(f'Partidas con 15 kills o mas: {partidas_destacadas}')








