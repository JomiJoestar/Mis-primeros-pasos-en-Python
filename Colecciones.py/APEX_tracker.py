



print('*** APEX LEGENDS TRACKER')

cantidad_partidas = 0
cantidad_partidas = int(input('Cuantas partidas jugaste? '))

if cantidad_partidas > 0 :

    cantidad_kills = []
    danio_realizado = []
    posicion_final = []


    for indice in range(cantidad_partidas):
        print(f'\nPartida {indice + 1}')

        kills = int(input('Kills: '))
        danio = int(input('Daño: '))
        posicion = int(input('Posición: '))

        cantidad_kills.append(kills)
        danio_realizado.append(danio)
        posicion_final.append(posicion)

# print(f'kills {cantidad_kills}, damage {danio_realizado}, position {posicion_final}')

# Total de kills
    total_kills = sum(cantidad_kills)
    print(f'Total de kills realizadas: {total_kills}')

# Promedio de danio

    total_danio = sum(danio_realizado) / cantidad_partidas
    print(f'Promedio del damage realizado: {total_danio:.2f}')

# Mayor danio realizado
    mayor_damage = max(danio_realizado)
    print(f'Mayor damage: {mayor_damage}')

# Posicion en el top 5

    top_5 = 0
    for posicion in posicion_final:
        if posicion >= 1 and posicion <= 5:
            top_5 += 1
    print(f'Partidas en el top 5: {top_5}')


# Victorias
    victorias = 0
    for win in posicion_final:
        if win == 1:
            victorias += 1
    print(f'Victorias: {victorias}')

else:
    print('Número no válido')
