

# Mostramos el título del programa
print('*** Promedio de Calificaciones ***')

# Pedimos cuántas calificaciones se van a evaluar.
total_calificaciones = int(input('Proporciona el número de calificaciones a evaluar: '))

# Creamos una lista vacía para guardar las calificaciones.
calificaciones = []

# El ciclo se repite según la cantidad indicada.
# Por ejemplo, range(3) genera los índices 0, 1 y 2.
for indice in range(total_calificaciones):

    # Pedimos una calificación.
    calificacion = float(input(f'Calificación [{indice + 1}]: '))

    # Agregamos la calificación a la lista.
    calificaciones.append(calificacion)

# Mostramos la lista completa.
# \n crea un salto de línea.
print(f'\nCalificaciones ingresadas: {calificaciones}')

# sum() suma todos los números guardados en la lista.
suma_calificaciones = sum(calificaciones)

# Calculamos el promedio:
# suma de calificaciones / cantidad de calificaciones.
promedio = suma_calificaciones / total_calificaciones

# :.2f muestra el resultado con dos decimales.
print(f'Promedio de las calificaciones: {promedio:.2f}') 