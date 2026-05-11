

print("*** Generador de ID unico ***")

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
anio = input("En que anio naciste (yyyy): ")

nombre_id = nombre[0:2].upper()
apellido_id = apellido[0:2].upper()
anio_id = anio[2:]

from random import randint
valor_aleatorio = randint(1000,9999)


print("Hola, {nombre}")
print("\t Tu nuevo numero de identificacion (ID) generado por el sistema es: ")
print(f"\t {nombre_id}{apellido_id}{anio_id}{valor_aleatorio}")
print("\t Felicidades!")
