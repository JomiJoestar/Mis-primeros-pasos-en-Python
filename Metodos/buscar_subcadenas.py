
#PROGRAMA BUSCAR SUBCADENAS

#ESTO VA A DEVOLVER EL INDICE DE UNA SUBCADENA. Un solo valor
#SOLAMENTE TOMA EN CUENTA LA PRIMERA OCURRENCIA

cadena = "Hola, mundo"
indice = cadena.find("mundo")
print(f"el indice de la subcadena mundo es: {indice}")
#Salida: el indice de la subcadena mundo es: 6

# OBTENER EL INDICE DE LA SUBCADENA HOLA
indice = cadena.find("Hola")
print(f"el indice de la subcadena Hola es: {indice}")
#Salida: el indice de la subcadena Hola es: 0


