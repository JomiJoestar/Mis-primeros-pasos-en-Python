print('*** Aplicacion de Salud y Fitness ***')

# Constantes 

META_PASOS_DIARIOS = 1000
CALORIAS_POR_PASO = 0.4 #Valor aproximado en kilocalorias

# Pedir los valores al usuario 
nombre_usuario = input('Cual es tu nombre? ')
pasos_diarios = int(input('Cuantos pasos has caminado hoy? '))

# Verificar si el usuario alcanzo la meta.
meta_alcanzada = pasos_diarios >= META_PASOS_DIARIOS
meta_alcanzada_txt = 'Si' if meta_alcanzada else 'No'

# Calculamos las calorias quemadas
calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

# Mostramos la informacion
print(f'\nUsuario: {nombre_usuario}')
print(f'Pasos dados hoy {pasos_diarios}')
print(f'Calorias quemadas: {calorias_quemadas}kcal')
print(f'Meta de pasos diarios alcanzada? {meta_alcanzada_txt}')
print(f'La meta de pasos diarios es de: {META_PASOS_DIARIOS} pasos')

