


#INPUT
#Estructura Base: 
#Variable = input("Ingrese su nombre")

#nombre = input("Ingresa tu nombre: ")
#print("Hola " + nombre)

#LA FUNCION INPUT SOLO DEVUELVE CADENAS, ES DECIR STRINGS AUNQUE PROPORCIONEMOS NUMEROS, SOLO DEVUELVE TIPO CADENA

#edad = input("Ingresa tu edad: ")

#print(edad + 26) #Esto devuelve error, no se pueden concatenar cadenas con enteros


#SOLUCION 

#Entrada datos a python

nombre = input("Ingrese se nombre: ")
print(f"Tu nombre es: {nombre}")

#CUIDADO CON LA CONVERSION DE TIPOS AL TRA(BAJAR CON VALORES NUMERICOS
#FORMA CORRECTA: ENVOLVER CON int() o float()

edad = int(input("Ingresa tu edad: "))
print(f"Tu edad es: {edad}")
print(edad + 20) #FUNCIONA

#lA CONVERSION TAMBIEN SE PUEDE REALIZAR EN PRINT SI NO SE HA HECHO ANTES
#print(int(edad + 4)) #Tambien funciona

#Para decimales (precio y altura)
altura = float(input("Ingrese su altura: "))
print(f"Su altura es: {altura}")

