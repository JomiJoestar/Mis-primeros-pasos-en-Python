


#CON INPUT
nombre = input("Introduce tu nombre: ")
empresa = input("Introduce el nombre de tu empresa: ")
dominio = input("Introduce el dominio (ejemplo.com): ")

email = f"{nombre}.{empresa}@{dominio}".lower() #Convertimos el email a minusculas para evitar problemas de mayusculas y minusculas
print(f"Tu email generado es: {email}")

#SIN INPUT
nombre = "Jomi"
empresa = "Joestar"
dominio = "ejemplo.com"

email = f"{nombre}.{empresa}@{dominio}".lower() #Convertimos el email a minusculas para evitar problemas de mayusculas y minusculas
print(f"Tu email generado es: {email}")

#NOTA, PUEDES AGREGAR . , @ EN LOS F STRINGS
# EJEMPLO  f"{nombre}.{empresa}@{dominio}"



#GENERADOR DE EMAIL 
nombre = 'Jomi Toxic Blackwood'
empresa = 'Joestar Industries'
dominio = '.com.co' 

email = f"{nombre}@{empresa}{dominio}".lower().replace(" ", ".") 
#Convertimos el email a minusculas para evitar problemas de mayusculas y minusculas, y reemplazamos los espacios por puntos