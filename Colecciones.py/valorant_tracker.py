

print('*** Tracker de VALORANT ***')

partidas = int(input('Cuantas partidas jugaste? '))

cantidad_eliminaciones = []

for indice in range(partidas):
    eliminaciones = int(input(f'Cuantas kills hiciste en la partida {indice + 1}?: '))
    cantidad_eliminaciones.append(eliminaciones)

total_eliminaciones = sum(cantidad_eliminaciones)

promedio_eliminaciones = total_eliminaciones / partidas

print(f'\nTotal de kills: {total_eliminaciones}')
print(f'Promedio finalo de las eliminaciones: {promedio_eliminaciones:.2f}')

