



#Generador de usuarios para plataforma

print("*** Generador de usuarios para plataforma ***")
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
ciudad = input('Ingrese su ciudad: ')
anio = input('Ingrese su anio de nacimiento (YYYY): ')

nombre_final = nombre[0:4].strip().lower()
apellido_final = apellido[0:2].strip().lower()
ciudad_final =  ciudad.strip().lower()
anio_final = anio[2:]

from random import randint
aleatoriedad = randint(1000,9999)

usuario = f'{nombre_final}{apellido_final}{ciudad_final}{anio_final}{aleatoriedad}'

print(f'''Hola, {nombre}. \t\n Tu usuario generado es: \n\t {usuario} \t\n Felicidades!!!''')

