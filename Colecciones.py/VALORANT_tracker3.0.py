

print('*** VALORANT tracker 3.0 ***')

cantidad_partidas = int(
    input('Cuantas partidas jugaste? '))

puntos = []

for indice in range(cantidad_partidas):
    puntos_partida = int(
        input(f'Cuanto de RR te dieron en la partida {indice + 1} ? ')
    )

    puntos.append(puntos_partida)

print(f'Puntos por partida {puntos}')

cambio_total = sum(puntos)
print(f'Cambio total de RR: {cambio_total}RR')

victorias = []
derrotas = []

for RR in puntos:
    if RR > 0:
        victorias.append(RR)

    elif RR < 0:
        derrotas.append(RR)

cantidad_victorias = len(victorias)
cantidad_derrotas = len(derrotas)

print(f'Partidas ganadas: {cantidad_victorias}')
print(f'Partidas perdidas: {cantidad_derrotas}')

if victorias:
    mvp = max(victorias)
    print(f'Mejor partida: {mvp} RR')
else:
    print('No hubo victorias')

if derrotas:
    mlp = min(derrotas)
    print(f'Peor partida: {mlp} RR')
else:
    print('No hubo derrotas')



